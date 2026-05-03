#!/usr/bin/env python3
"""generate-dashboard.py — 방법론 대시보드 단일 파일 빌더.

하는 일:
  1) docs/methodology-graph.json 을 읽어 방법론 그래프 + 라이프사이클을 시각화
  2) TODO.md 의 5개 섹션(Backlog/Ready/InProgress/Blocked/Done)을 칸반으로 파싱
  3) SPRINTS.md 의 ### S-NNN 블록을 타임라인(주/월/연 토글)으로 파싱
  4) CLAUDE.md, HANDOFF.md, docs/archive/planning-guides/README.md 일부를 가이드 탭에 인라인

산출물: dashboard.html (자기완결, CDN: d3.v7)

사용:
  python generate-dashboard.py                 # dashboard.html 생성
  python generate-dashboard.py --serve         # 파일 생성 후 8765 포트로 서빙
  python generate-dashboard.py --out PATH      # 출력 경로 지정
  python generate-dashboard.py --root PATH     # 다른 프로젝트에 대해 실행
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent

KANBAN_SECTIONS = ["Backlog", "Ready", "InProgress", "Blocked", "Done"]


# ─────────────────────────────────────── parsers ───────────────────────────────────────

@dataclass
class Card:
    id: str
    section: str
    fields: dict[str, str] = field(default_factory=dict)
    criteria: list[tuple[bool, str]] = field(default_factory=list)


def parse_todo(path: Path) -> dict[str, list[Card]]:
    """TODO.md 를 섹션별 카드 리스트로 파싱."""
    out = {s: [] for s in KANBAN_SECTIONS}
    if not path.exists():
        return out

    text = path.read_text(encoding="utf-8")
    # 현재 섹션 추적
    current_section: str | None = None
    current_card: Card | None = None
    current_field_key: str | None = None

    for raw in text.splitlines():
        line = raw.rstrip()

        # 섹션 헤더 ## Ready
        m = re.match(r"^##\s+(Backlog|Ready|InProgress|Blocked|Done)\s*$", line)
        if m:
            if current_card and current_section:
                out[current_section].append(current_card)
                current_card = None
            current_section = m.group(1)
            continue

        # 카드 헤더 ### ID-001
        m = re.match(r"^###\s+(.+?)\s*$", line)
        if m and current_section:
            if current_card:
                out[current_section].append(current_card)
            current_card = Card(id=m.group(1).strip(), section=current_section)
            current_field_key = None
            continue

        if current_card is None:
            continue

        # 필드 - **key**: value
        m = re.match(r"^-\s+\*\*([^*]+)\*\*\s*:\s*(.*)$", line)
        if m:
            key, val = m.group(1).strip().lower(), m.group(2).strip()
            current_card.fields[key] = val
            current_field_key = key
            continue

        # 체크박스   - [ ] criterion / - [x] criterion (들여쓰기 또는 일반)
        m = re.match(r"^\s*-\s+\[( |x|X)\]\s+(.+)$", line)
        if m:
            current_card.criteria.append((m.group(1).lower() == "x", m.group(2).strip()))
            continue

    if current_card and current_section:
        out[current_section].append(current_card)

    return out


@dataclass
class Sprint:
    id: str
    fields: dict[str, str] = field(default_factory=dict)
    goals: list[tuple[bool, str]] = field(default_factory=list)


def parse_sprints(path: Path) -> list[Sprint]:
    """SPRINTS.md 를 ### S-NNN 블록 단위로 파싱."""
    out: list[Sprint] = []
    if not path.exists():
        return out

    text = path.read_text(encoding="utf-8")
    current: Sprint | None = None
    in_goals = False

    for raw in text.splitlines():
        line = raw.rstrip()

        m = re.match(r"^###\s+(S-\d+|s-\d+)\s*$", line)
        if m:
            if current:
                out.append(current)
            current = Sprint(id=m.group(1).upper())
            in_goals = False
            continue

        if current is None:
            continue

        m = re.match(r"^-\s+\*\*([^*]+)\*\*\s*:\s*(.*)$", line)
        if m:
            key, val = m.group(1).strip().lower(), m.group(2).strip()
            current.fields[key] = val
            in_goals = key == "goals"
            continue

        if in_goals:
            m = re.match(r"^\s*-\s+\[( |x|X)\]\s+(.+)$", line)
            if m:
                current.goals.append((m.group(1).lower() == "x", m.group(2).strip()))
                continue

    if current:
        out.append(current)
    return out


def read_text_safe(path: Path, max_chars: int = 8000) -> str:
    if not path.exists():
        return ""
    s = path.read_text(encoding="utf-8")
    return s if len(s) <= max_chars else s[:max_chars] + "\n\n…(truncated)"


# ──────────────────────────────────── data assembly ────────────────────────────────────


def assemble(root: Path) -> dict[str, Any]:
    # graph: root에 있고, 없으면 docs/ 하위 fallback (이전 구조 호환)
    graph_path = root / "methodology-graph.json"
    if not graph_path.exists():
        graph_path = root / "docs" / "methodology-graph.json"

    # TODO: 루트 → 40_resources/templates → docs/templates
    todo_path = root / "TODO.md"
    for cand in [root / "40_resources" / "templates" / "TODO.md", root / "docs" / "templates" / "TODO.md"]:
        if not todo_path.exists():
            todo_path = cand

    # SPRINTS: 30_dev → 루트 → 40_resources/templates → docs/templates
    sprints_path = root / "30_dev" / "SPRINTS.md"
    for cand in [root / "SPRINTS.md", root / "40_resources" / "templates" / "SPRINTS.md", root / "docs" / "templates" / "SPRINTS.md"]:
        if not sprints_path.exists():
            sprints_path = cand

    handoff_path = root / "HANDOFF.md"
    for cand in [root / "40_resources" / "templates" / "HANDOFF.md", root / "docs" / "templates" / "HANDOFF.md"]:
        if not handoff_path.exists():
            handoff_path = cand

    # MASTER_PLAN: 30_dev → root → 40_resources/templates
    master_plan_path = root / "30_dev" / "MASTER_PLAN.md"
    for cand in [root / "MASTER_PLAN.md", root / "40_resources" / "templates" / "MASTER_PLAN.md"]:
        if not master_plan_path.exists():
            master_plan_path = cand

    claude_path = root / "CLAUDE.md"
    # README: 새 구조 → 구 구조 fallback
    readme_path = root / "10_guides" / "README.md"
    if not readme_path.exists():
        readme_path = root / "docs" / "archive" / "planning-guides" / "README.md"

    graph = json.loads(graph_path.read_text(encoding="utf-8")) if graph_path.exists() else {
        "nodes": [], "edges": [], "lifecycle": {"stages": []}, "kinds": {}
    }
    kanban_raw = parse_todo(todo_path)
    sprints = parse_sprints(sprints_path)

    kanban = {
        section: [
            {"id": c.id, "fields": c.fields, "criteria": c.criteria}
            for c in cards
        ]
        for section, cards in kanban_raw.items()
    }
    sprints_json = [
        {"id": s.id, "fields": s.fields, "goals": s.goals} for s in sprints
    ]

    # 그래프 노드의 path를 따라 실제 파일 내용 로드 (클릭 시 하단 패널에 표시)
    node_contents = {}
    for n in graph.get("nodes", []):
        rel = n.get("path")
        if not rel:
            continue
        p = root / rel
        if p.is_file():
            try:
                txt = p.read_text(encoding="utf-8")
                node_contents[n["id"]] = {"kind": "file", "text": txt, "size": len(txt)}
            except Exception as e:
                node_contents[n["id"]] = {"kind": "error", "text": f"(읽기 실패: {e})"}
        elif p.is_dir():
            entries = []
            for child in sorted(p.iterdir()):
                entries.append({
                    "name": child.name,
                    "is_dir": child.is_dir(),
                    "size": child.stat().st_size if child.is_file() else None,
                })
            node_contents[n["id"]] = {"kind": "dir", "entries": entries, "rel": rel}
        else:
            node_contents[n["id"]] = {"kind": "missing", "text": f"(경로 없음: {rel})"}

    return {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "root": str(root),
        "graph": graph,
        "kanban": kanban,
        "sprints": sprints_json,
        "node_contents": node_contents,
        "master_plan_text": read_text_safe(master_plan_path, 50000),
        "master_plan_path": str(master_plan_path.relative_to(root)) if master_plan_path.exists() else "",
        "guide_excerpts": {
            "claude_md": read_text_safe(claude_path, 4000),
            "handoff_md": read_text_safe(handoff_path, 3000),
            "guides_readme": read_text_safe(readme_path, 8000),
        },
    }


# ──────────────────────────────────── HTML rendering ───────────────────────────────────


HTML_TEMPLATE = r"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<title>방법론 대시보드</title>
<script src="https://d3js.org/d3.v7.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/marked@12/marked.min.js"></script>
<style>
:root{
  --bg:#0B0F1A; --panel:#111827; --panel2:#0F172A; --line:#1F2937;
  --text:#E5E7EB; --muted:#9CA3AF; --accent:#60A5FA; --accent2:#34D399;
  --warn:#F59E0B; --danger:#EF4444; --violet:#A78BFA; --cyan:#22D3EE;
}
*{box-sizing:border-box}
html,body{margin:0;padding:0;background:var(--bg);color:var(--text);
  font-family:-apple-system,BlinkMacSystemFont,"SF Pro Text","Segoe UI","Pretendard","Noto Sans KR",sans-serif;
  font-size:14px;line-height:1.55}
header{display:flex;align-items:baseline;gap:16px;padding:16px 24px;border-bottom:1px solid var(--line);
  position:sticky;top:0;background:rgba(11,15,26,.85);backdrop-filter:blur(8px);z-index:10}
h1{font-size:18px;margin:0;font-weight:600;letter-spacing:-.01em}
.muted{color:var(--muted)}
.tabs{display:flex;gap:4px;padding:8px 24px;border-bottom:1px solid var(--line);background:var(--panel2);
  position:sticky;top:53px;z-index:9}
.tab{padding:8px 14px;border-radius:8px;cursor:pointer;color:var(--muted);user-select:none;font-weight:500}
.tab:hover{background:var(--panel);color:var(--text)}
.tab.active{background:var(--accent);color:#0B1220}
.page{display:none;padding:24px}
.page.active{display:block}
.card{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:14px;margin-bottom:12px}
.card h3{margin:0 0 6px;font-size:14px}
.row{display:flex;gap:8px;flex-wrap:wrap;font-size:12px;color:var(--muted)}
.pill{padding:2px 8px;border-radius:999px;border:1px solid var(--line);background:var(--panel2)}
.pill.A{color:#86EFAC;border-color:#14532D} .pill.B{color:#FCD34D;border-color:#78350F}
.pill.C{color:#FCA5A5;border-color:#7F1D1D}
.kanban{display:grid;grid-template-columns:repeat(5,1fr);gap:12px}
.col{background:var(--panel2);border:1px solid var(--line);border-radius:10px;padding:10px;min-height:200px}
.col h2{font-size:13px;margin:0 0 10px;color:var(--muted);text-transform:uppercase;letter-spacing:.05em;
  display:flex;justify-content:space-between;align-items:center}
.col h2 .count{background:var(--panel);padding:1px 8px;border-radius:999px;font-size:11px;color:var(--text)}
.timeline-controls{display:flex;gap:8px;margin-bottom:16px}
.btn{padding:6px 12px;border-radius:6px;background:var(--panel);border:1px solid var(--line);
  color:var(--text);cursor:pointer;font-size:12px}
.btn.active{background:var(--accent);color:#0B1220;border-color:var(--accent)}
.timeline{position:relative;background:var(--panel2);border:1px solid var(--line);border-radius:10px;padding:16px;overflow-x:auto}
.timeline-grid{display:grid;gap:2px;min-width:max-content}
.tcell{padding:6px 8px;font-size:11px;color:var(--muted);border-right:1px solid var(--line);min-width:80px;text-align:center}
.tbar{height:28px;background:var(--accent);border-radius:6px;display:flex;align-items:center;padding:0 10px;
  color:#0B1220;font-size:12px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.tbar.done{background:var(--accent2);opacity:.7}
.tbar.planned{background:var(--violet)} .tbar.cancelled{background:var(--danger);opacity:.5}
.tbar.active{background:var(--warn);color:#0B1220}
.graph-layout{display:grid;grid-template-columns:1fr 320px;gap:12px}
@media(max-width:900px){ .graph-layout{grid-template-columns:1fr} }
#graph{width:100%;height:640px;background:var(--panel2);border:1px solid var(--line);border-radius:10px}
.graph-detail{background:var(--panel2);border:1px solid var(--line);border-radius:10px;padding:14px;
  max-height:640px;overflow-y:auto;font-size:13px}
.graph-detail h4{margin:0 0 4px;font-size:15px;color:var(--text)}
.graph-detail .kind-tag{display:inline-block;padding:2px 8px;border-radius:999px;font-size:11px;
  font-weight:600;color:#0B1220;margin-bottom:8px}
.graph-detail code{background:var(--panel);padding:2px 6px;border-radius:4px;font-size:11px;color:#CBD5E1}
.graph-detail .role{margin:8px 0;color:var(--text);line-height:1.6}
.graph-detail .conn{margin-top:12px;padding-top:10px;border-top:1px solid var(--line)}
.graph-detail .conn h5{margin:0 0 6px;font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.05em}
.graph-detail .conn ul{margin:0;padding-left:16px}
.graph-detail .conn li{margin-bottom:3px;color:var(--text)}
.graph-detail .conn li .edge-kind{color:var(--muted);font-size:11px}
.role-table{width:100%;border-collapse:collapse;font-size:12px}
.role-table th,.role-table td{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top}
.role-table th{color:var(--muted);font-weight:500;font-size:11px;text-transform:uppercase;letter-spacing:.05em;background:var(--panel2)}
.role-table tr:hover td{background:var(--panel2)}
.role-table .label{font-weight:600;color:var(--text);white-space:nowrap}
.role-table .path{font-family:ui-monospace,Menlo,monospace;font-size:11px;color:#94A3B8}
.role-table .role-cell{color:var(--text);max-width:520px}
.node-circle{cursor:pointer;transition:stroke-width .15s}
.node-circle:hover{stroke-width:4}
.node-circle.selected{stroke:#FBBF24;stroke-width:4}
.content-body{background:var(--panel2);border:1px solid var(--line);border-radius:8px;
  padding:18px 22px;max-height:560px;overflow-y:auto;font-size:13px;line-height:1.7;color:#CBD5E1}
.content-body h1{font-size:20px;color:#F1F5F9;margin:8px 0 12px;padding-bottom:8px;border-bottom:1px solid var(--line)}
.content-body h2{font-size:16px;color:#E2E8F0;margin:18px 0 8px}
.content-body h3{font-size:14px;color:#CBD5E1;margin:14px 0 6px}
.content-body h4,.content-body h5{font-size:13px;color:#94A3B8;margin:10px 0 4px}
.content-body p{margin:6px 0}
.content-body ul,.content-body ol{margin:6px 0;padding-left:22px}
.content-body li{margin:2px 0}
.content-body code{background:#1E293B;color:#FCD34D;padding:1px 5px;border-radius:3px;font-size:12px}
.content-body pre{background:#0B1220;border:1px solid var(--line);border-radius:6px;padding:10px;
  overflow-x:auto;margin:8px 0}
.content-body pre code{background:transparent;color:#CBD5E1;padding:0}
.content-body table{border-collapse:collapse;margin:8px 0;font-size:12px;width:100%}
.content-body th,.content-body td{border:1px solid var(--line);padding:5px 9px;text-align:left}
.content-body th{background:var(--panel);color:#E5E7EB;font-weight:600}
.content-body blockquote{border-left:3px solid var(--accent);padding:2px 12px;margin:8px 0;
  color:#94A3B8;background:rgba(96,165,250,.06)}
.content-body hr{border:none;border-top:1px solid var(--line);margin:14px 0}
.content-body a{color:var(--accent);text-decoration:none}
.content-body a:hover{text-decoration:underline}
.content-dir-list{list-style:none;padding:0;margin:0}
.content-dir-list li{padding:4px 8px;border-bottom:1px solid var(--line);font-family:ui-monospace,Menlo,monospace;font-size:12px}
.content-dir-list li:last-child{border-bottom:none}
.content-dir-list .dir-icon{color:#F59E0B;margin-right:6px}
.content-dir-list .file-icon{color:#94A3B8;margin-right:6px}
.content-dir-list .file-size{color:#64748B;font-size:11px;float:right}
.mp-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(360px,1fr));gap:12px;margin-top:12px}
.mp-card{background:var(--panel2);border:1px solid var(--line);border-radius:8px;padding:14px;
  max-height:340px;overflow-y:auto}
.mp-card h4{margin:0 0 10px;font-size:13px;color:var(--accent);font-weight:600;
  padding-bottom:6px;border-bottom:1px solid var(--line)}
.mp-card .mp-content{font-size:12px;line-height:1.65;color:#CBD5E1}
.mp-card .mp-content p{margin:4px 0}
.mp-card .mp-content ul,.mp-card .mp-content ol{padding-left:18px;margin:4px 0}
.mp-card .mp-content table{border-collapse:collapse;font-size:11px;width:100%;margin:6px 0}
.mp-card .mp-content th,.mp-card .mp-content td{border:1px solid var(--line);padding:3px 6px;text-align:left}
.mp-card .mp-content th{background:var(--panel);color:#E5E7EB}
.mp-card .mp-content code{background:var(--panel);color:#FCD34D;padding:1px 4px;border-radius:3px;font-size:11px}
.mp-card .mp-content h2,.mp-card .mp-content h3{font-size:13px;color:#E5E7EB;margin:8px 0 4px}
.mp-card.empty{opacity:.5}
.mp-card.empty .mp-content::after{content:"(아직 내용 없음 — TODO)";color:#64748B;font-style:italic}
.sprint-table{width:100%;border-collapse:collapse;font-size:12px;margin-top:8px}
.sprint-table th,.sprint-table td{border:1px solid var(--line);padding:7px 9px;text-align:left;vertical-align:top}
.sprint-table th{background:var(--panel2);color:#94A3B8;font-weight:500;text-transform:uppercase;
  letter-spacing:.04em;font-size:11px;white-space:nowrap}
.sprint-table tr:hover td{background:var(--panel2)}
.sprint-table .s-id{font-weight:600;color:var(--text);white-space:nowrap}
.sprint-table .s-status{padding:2px 8px;border-radius:999px;font-size:10px;font-weight:600;
  display:inline-block;text-transform:uppercase}
.sprint-table .s-status.planned{background:#A78BFA;color:#0B1220}
.sprint-table .s-status.active{background:#F59E0B;color:#0B1220}
.sprint-table .s-status.done{background:#34D399;color:#0B1220}
.sprint-table .s-status.cancelled{background:#EF4444;color:#FFF}
.sprint-table .s-goals{margin:0;padding:0;list-style:none}
.sprint-table .s-goals li{font-size:11px;color:#CBD5E1;line-height:1.5}
.sprint-table .s-goals li.done{color:#64748B;text-decoration:line-through}
.sprint-table .s-goals li::before{content:"☐ ";color:#64748B}
.sprint-table .s-goals li.done::before{content:"☑ ";color:#34D399}
#flow{width:100%;background:var(--panel2);border:1px solid var(--line);border-radius:10px;padding:20px}
.guide-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.guide-grid pre{background:var(--panel2);border:1px solid var(--line);border-radius:8px;padding:12px;
  overflow:auto;max-height:520px;font-size:12px;color:#CBD5E1;white-space:pre-wrap;word-break:break-word}
.legend{display:flex;gap:12px;flex-wrap:wrap;margin-top:8px;font-size:12px;color:var(--muted)}
.legend .dot{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:4px;vertical-align:middle}
@media(max-width:1100px){ .kanban{grid-template-columns:1fr 1fr} .guide-grid{grid-template-columns:1fr} }
@media(max-width:700px){ .kanban{grid-template-columns:1fr} }
</style>
</head>
<body>
<header>
  <h1>방법론 대시보드</h1>
  <span class="muted" id="meta"></span>
</header>
<nav class="tabs" id="tabs">
  <div class="tab active" data-page="guide">가이드 &amp; 플로우</div>
  <div class="tab" data-page="graph">관계 그래프</div>
  <div class="tab" data-page="timeline">타임라인</div>
  <div class="tab" data-page="kanban">칸반보드</div>
  <div class="tab" data-page="exec">통합 뷰</div>
</nav>

<section class="page active" id="page-guide">
  <div class="card">
    <h3>기획-개발 라이프사이클</h3>
    <div id="flow"></div>
    <div class="legend" id="flow-legend"></div>
  </div>
  <div class="guide-grid">
    <div class="card"><h3>CLAUDE.md (요약)</h3><pre id="g-claude"></pre></div>
    <div class="card"><h3>HANDOFF.md (현재 상태)</h3><pre id="g-handoff"></pre></div>
    <div class="card" style="grid-column:1/-1"><h3>기획 지침서 카탈로그</h3><pre id="g-readme"></pre></div>
  </div>
</section>

<section class="page" id="page-graph">
  <div class="card">
    <h3>방법론 폴더·문서 관계 그래프</h3>
    <div style="display:flex;gap:8px;margin-bottom:10px;align-items:center;flex-wrap:wrap">
      <button class="btn active" data-layout="hierarchy">계층 (상하위)</button>
      <button class="btn" data-layout="force">자유 (force)</button>
      <span class="muted" style="margin-left:8px">노드 클릭 → 오른쪽 패널에 역할 표시</span>
    </div>
    <div class="graph-layout">
      <svg id="graph"></svg>
      <aside id="graph-detail" class="graph-detail">
        <div class="muted">노드를 클릭하면 여기에 역할·경로·연결이 표시됩니다.</div>
      </aside>
    </div>
    <div class="legend" id="graph-legend"></div>
  </div>
  <div class="card" id="content-card" style="margin-top:12px">
    <div style="display:flex;justify-content:space-between;align-items:baseline;gap:12px;margin-bottom:8px">
      <h3 id="content-title" style="margin:0">파일 내용</h3>
      <span id="content-meta" class="muted" style="font-size:12px"></span>
    </div>
    <div id="content-body" class="content-body">
      <div class="muted">노드를 클릭하면 여기에 파일 내용이 표시됩니다.</div>
    </div>
  </div>
  <div class="card" style="margin-top:12px">
    <h3>전체 문서·폴더 역할 목록</h3>
    <div id="role-table"></div>
  </div>
</section>

<section class="page" id="page-timeline">
  <div class="card">
    <h3>스프린트 타임라인</h3>
    <div class="timeline-controls">
      <button class="btn active" data-view="week">주간</button>
      <button class="btn" data-view="month">월간</button>
      <button class="btn" data-view="year">연간</button>
    </div>
    <div class="timeline"><div id="timeline-grid" class="timeline-grid"></div></div>
    <div class="legend" style="margin-top:12px">
      <span><span class="dot" style="background:#A78BFA"></span>planned</span>
      <span><span class="dot" style="background:#F59E0B"></span>active</span>
      <span><span class="dot" style="background:#34D399"></span>done</span>
      <span><span class="dot" style="background:#EF4444"></span>cancelled</span>
    </div>
  </div>
</section>

<section class="page" id="page-kanban">
  <div class="kanban" id="kanban"></div>
</section>

<section class="page" id="page-exec">
  <div class="card">
    <div style="display:flex;justify-content:space-between;align-items:baseline;flex-wrap:wrap;gap:8px">
      <h3 style="margin:0">마스터플랜</h3>
      <span class="muted" id="mp-meta" style="font-size:12px"></span>
    </div>
    <div id="mp-sections" class="mp-grid"></div>
  </div>

  <div class="card" style="margin-top:12px">
    <h3>스프린트 (전체)</h3>
    <div style="overflow-x:auto"><table class="sprint-table" id="sprint-table"></table></div>
  </div>

  <div class="card" style="margin-top:12px">
    <h3>칸반보드</h3>
    <div class="kanban" id="kanban-exec"></div>
  </div>
</section>

<script id="data" type="application/json">__DATA__</script>
<script>
const DATA = JSON.parse(document.getElementById('data').textContent);
document.getElementById('meta').textContent =
  `생성: ${DATA.generated_at} · ${DATA.root}`;

// ── 탭
document.querySelectorAll('.tab').forEach(t => t.addEventListener('click', () => {
  document.querySelectorAll('.tab').forEach(x => x.classList.remove('active'));
  document.querySelectorAll('.page').forEach(x => x.classList.remove('active'));
  t.classList.add('active');
  document.getElementById('page-' + t.dataset.page).classList.add('active');
  if(t.dataset.page === 'graph') renderGraph();
}));

// ── 가이드 인라인
document.getElementById('g-claude').textContent = DATA.guide_excerpts.claude_md || '(CLAUDE.md 없음)';
document.getElementById('g-handoff').textContent = DATA.guide_excerpts.handoff_md || '(HANDOFF.md 없음 — 템플릿 미리보기)';
document.getElementById('g-readme').textContent = DATA.guide_excerpts.guides_readme || '(planning-guides/README.md 없음)';

// ── 라이프사이클 플로우 (SVG)
function renderFlow(){
  const stages = DATA.graph.lifecycle?.stages || [];
  if(!stages.length){ document.getElementById('flow').textContent = '(라이프사이클 데이터 없음)'; return; }
  const W = 1080, BOX_W = 130, BOX_H = 64, GAP_X = 22, ROW_GAP = 48;
  const perRow = Math.floor((W + GAP_X) / (BOX_W + GAP_X));
  const rows = Math.ceil(stages.length / perRow);
  const H = rows * (BOX_H + ROW_GAP) + 40;
  const svg = d3.select('#flow').append('svg')
    .attr('viewBox',`0 0 ${W} ${H}`).attr('width','100%').attr('height',H);

  const defs = svg.append('defs');
  defs.append('marker').attr('id','arr').attr('viewBox','0 -5 10 10')
    .attr('refX',9).attr('refY',0).attr('markerWidth',7).attr('markerHeight',7).attr('orient','auto')
    .append('path').attr('d','M0,-5L10,0L0,5').attr('fill','#60A5FA');

  const pos = {};
  stages.forEach((s, i) => {
    const r = Math.floor(i / perRow), c = (r % 2 === 0) ? (i % perRow) : (perRow - 1 - (i % perRow));
    pos[s.id] = { x: 20 + c*(BOX_W+GAP_X), y: 20 + r*(BOX_H+ROW_GAP), row: r, col: c };
  });

  // 박스
  const g = svg.selectAll('.stage').data(stages).enter().append('g')
    .attr('transform', d => `translate(${pos[d.id].x},${pos[d.id].y})`);
  g.append('rect').attr('width',BOX_W).attr('height',BOX_H).attr('rx',8)
    .attr('fill', d => d.human_gate ? '#1E293B' : '#0F172A')
    .attr('stroke', d => d.human_gate ? '#F59E0B' : '#334155').attr('stroke-width',1.5);
  g.append('text').attr('x',8).attr('y',16).attr('fill','#94A3B8').attr('font-size',10).text(d => d.id);
  g.append('text').attr('x',8).attr('y',34).attr('fill','#E5E7EB').attr('font-size',12).attr('font-weight',600).text(d => d.label);
  g.append('text').attr('x',8).attr('y',54).attr('fill','#F59E0B').attr('font-size',10)
    .text(d => d.human_gate ? '⚑ ' + d.human_gate : '');

  // 화살표
  function path(a, b, isLoop){
    const ax = pos[a].x + BOX_W/2, ay = pos[a].y + BOX_H/2;
    const bx = pos[b].x + BOX_W/2, by = pos[b].y + BOX_H/2;
    if(isLoop){
      // 큰 곡선
      return `M${pos[a].x + BOX_W},${ay} C${W-10},${ay} ${W-10},${by} ${pos[b].x + BOX_W},${by}`;
    }
    return `M${pos[a].x + BOX_W},${ay} L${pos[b].x},${by}`;
  }
  stages.forEach(s => {
    if(s.next){
      svg.append('path').attr('d', path(s.id, s.next, false))
        .attr('stroke','#60A5FA').attr('stroke-width',1.5).attr('fill','none').attr('marker-end','url(#arr)');
    }
    if(s.loops_to){
      svg.append('path').attr('d', path(s.id, s.loops_to, true))
        .attr('stroke','#A78BFA').attr('stroke-width',1.5).attr('fill','none')
        .attr('stroke-dasharray','4 4').attr('marker-end','url(#arr)');
    }
  });

  document.getElementById('flow-legend').innerHTML =
    `<span><span class="dot" style="background:#0F172A;border:1px solid #334155"></span>일반 단계</span>
     <span><span class="dot" style="background:#1E293B;border:1px solid #F59E0B"></span>휴먼 게이트</span>
     <span><span class="dot" style="background:#A78BFA"></span>루프 (재기획→개발)</span>`;
}
renderFlow();

// ── 관계 그래프 (계층 / 자유 토글)
let graphState = { rendered:false, layout:'hierarchy', selectedId:null };

function renderGraph(layout){
  layout = layout || graphState.layout || 'hierarchy';
  graphState.layout = layout;

  const nodes = (DATA.graph.nodes||[]).map(n => ({...n}));
  const links = (DATA.graph.edges||[]).map(e => ({source:e.from, target:e.to, kind:e.kind, label:e.label}));
  const kinds = DATA.graph.kinds || {};
  const tiers = DATA.graph.tiers || [];

  const svg = d3.select('#graph');
  const w = svg.node().clientWidth, h = 640;
  svg.selectAll('*').remove();

  svg.append('defs').append('marker').attr('id','garr').attr('viewBox','0 -5 10 10')
    .attr('refX',18).attr('refY',0).attr('markerWidth',6).attr('markerHeight',6).attr('orient','auto')
    .append('path').attr('d','M0,-5L10,0L0,5').attr('fill','#475569');

  let sim = null;

  if(layout === 'hierarchy'){
    // 2D 계층 배치: 가로축=category(5개), 세로축=tier(category 내부 순서)
    const categories = DATA.graph.categories || [];
    const catOrder = categories.length ? categories.map(c => c.id) : [...new Set(nodes.map(n=>n.category||'misc'))];
    const catLabel = Object.fromEntries((categories||[]).map(c => [c.id, c.label]));
    const catColor = Object.fromEntries((categories||[]).map(c => [c.id, c.color]));

    // 노드를 카테고리별로 분류 → 카테고리 안에서 tier 정렬
    const byCat = {};
    nodes.forEach(n => {
      const c = n.category || 'misc';
      (byCat[c] = byCat[c] || []).push(n);
    });
    Object.values(byCat).forEach(arr => arr.sort((a,b) => (a.tier||99) - (b.tier||99)));

    // 가로: 카테고리별 컬럼 (균등)
    const colW = w / Math.max(1, catOrder.length);
    const padTop = 60, padBot = 30;

    // 카테고리 배경 밴드 + 헤더
    catOrder.forEach((cid, ci) => {
      const x0 = ci * colW;
      svg.append('rect').attr('class','cat-band')
        .attr('x', x0+2).attr('y', padTop-4).attr('width', colW-4).attr('height', h-padTop-padBot+10)
        .attr('rx', 8).attr('fill', catColor[cid]||'#1E293B').attr('opacity', 0.18);
      svg.append('text').attr('class','cat-header')
        .attr('x', x0 + colW/2).attr('y', 22).attr('text-anchor','middle')
        .attr('fill','#E5E7EB').attr('font-size',13).attr('font-weight',700)
        .text(catLabel[cid] || cid);
      svg.append('text').attr('class','cat-folder')
        .attr('x', x0 + colW/2).attr('y', 40).attr('text-anchor','middle')
        .attr('fill','#94A3B8').attr('font-size',10).attr('font-family','ui-monospace,Menlo,monospace')
        .text((categories.find(c => c.id===cid)||{}).folder || '');
    });

    // 노드 좌표: 컬럼 안에서 tier 순서대로 배치
    catOrder.forEach((cid, ci) => {
      const arr = byCat[cid] || [];
      const x0 = ci * colW;
      const innerH = h - padTop - padBot;
      const stepY = arr.length > 1 ? innerH / (arr.length) : 0;
      arr.forEach((n, i) => {
        n.x = x0 + colW/2;
        n.y = padTop + stepY * (i + 0.5);
        n.fx = n.x; n.fy = n.y;
      });
    });
  } else {
    // 자유 force 시뮬레이션
    sim = d3.forceSimulation(nodes)
      .force('link', d3.forceLink(links).id(d=>d.id).distance(110).strength(0.6))
      .force('charge', d3.forceManyBody().strength(-360))
      .force('center', d3.forceCenter(w/2, h/2))
      .force('collide', d3.forceCollide(38));
  }

  // 엣지: 계층 모드에서는 곡선(베지어), 자유 모드에서는 직선
  const link = svg.append('g').selectAll('path').data(links).enter().append('path')
    .attr('stroke','#475569').attr('stroke-opacity',.55).attr('stroke-width',1.2).attr('fill','none')
    .attr('marker-end','url(#garr)');

  function tickLinks(){
    link.attr('d', d => {
      const sx = d.source.x, sy = d.source.y, tx = d.target.x, ty = d.target.y;
      if(layout === 'hierarchy'){
        const my = (sy + ty) / 2;
        return `M${sx},${sy} C${sx},${my} ${tx},${my} ${tx},${ty}`;
      }
      return `M${sx},${sy} L${tx},${ty}`;
    });
  }

  // 자유 모드는 source/target이 객체로 치환되는 시점 차이가 있어서 별도 처리
  if(layout !== 'hierarchy'){
    // links의 source/target 문자열을 객체 참조로 교체 (force가 알아서 해줌)
  } else {
    // 계층 모드는 source/target이 여전히 문자열이므로 노드 매핑
    const nodeById = Object.fromEntries(nodes.map(n => [n.id, n]));
    links.forEach(l => { l.source = nodeById[l.source] || l.source; l.target = nodeById[l.target] || l.target; });
    tickLinks();
  }

  const node = svg.append('g').selectAll('g').data(nodes).enter().append('g')
    .call(d3.drag()
      .on('start', (e,d) => { if(sim){ if(!e.active) sim.alphaTarget(.3).restart(); } d.fx=d.x; d.fy=d.y; })
      .on('drag',  (e,d) => { d.fx=e.x; d.fy=e.y; if(layout==='hierarchy'){ d.x=e.x; d.y=e.y; node.attr('transform', n=>`translate(${n.x},${n.y})`); tickLinks(); } })
      .on('end',   (e,d) => { if(sim && !e.active) sim.alphaTarget(0); /* keep fx,fy in hierarchy mode */ }));

  node.append('circle').attr('class','node-circle').attr('r',18)
    .attr('fill', d => kinds[d.kind]?.color || '#64748B')
    .attr('stroke','#0B0F1A').attr('stroke-width',2)
    .on('click', (e, d) => { e.stopPropagation(); selectNode(d); });
  node.append('text').attr('dy',34).attr('text-anchor','middle').attr('fill','#E5E7EB')
    .attr('font-size',11).text(d => d.label).style('pointer-events','none');
  node.append('title').text(d => `${d.label}\n${d.path||''}\n\n${d.role||''}`);

  if(sim){
    sim.on('tick', () => { tickLinks(); node.attr('transform', d=>`translate(${d.x},${d.y})`); });
  } else {
    node.attr('transform', d=>`translate(${d.x},${d.y})`);
  }

  const categories = DATA.graph.categories || [];
  document.getElementById('graph-legend').innerHTML =
    '<strong style="color:#94A3B8;margin-right:6px">카테고리:</strong>' +
    categories.map(c => `<span><span class="dot" style="background:${c.color}"></span>${c.label} <code style="font-size:10px;color:#64748B">${c.folder}</code></span>`).join(' ') +
    ' <span style="margin:0 8px;color:#475569">|</span> <strong style="color:#94A3B8;margin-right:6px">유형:</strong>' +
    Object.entries(kinds).map(([k,v]) => `<span><span class="dot" style="background:${v.color}"></span>${k}</span>`).join('');

  function selectNode(d){
    graphState.selectedId = d.id;
    svg.selectAll('.node-circle').classed('selected', n => n.id === d.id);
    const incoming = (DATA.graph.edges||[]).filter(e => e.to === d.id);
    const outgoing = (DATA.graph.edges||[]).filter(e => e.from === d.id);
    const labelOf = id => (DATA.graph.nodes.find(n => n.id===id)||{}).label || id;
    const kindMeta = kinds[d.kind] || {};
    const tierLabel = tiers.find(t => t.id === d.tier)?.label;
    const catMeta = (DATA.graph.categories||[]).find(c => c.id === d.category);
    const html = `
      ${catMeta ? `<span class="kind-tag" style="background:${catMeta.color};color:#E5E7EB">${escapeHtml(catMeta.label)}</span>` : ''}
      <span class="kind-tag" style="background:${kindMeta.color||'#64748B'};margin-left:4px">${d.kind}</span>
      ${tierLabel ? `<span class="kind-tag" style="background:#334155;color:#E5E7EB;margin-left:4px">T${d.tier}</span>` : ''}
      <h4>${escapeHtml(d.label)}</h4>
      ${d.path ? `<code>${escapeHtml(d.path)}</code>` : ''}
      <div class="role">${escapeHtml(d.role||'(역할 미정)')}</div>
      ${outgoing.length ? `<div class="conn"><h5>→ 연결 (out)</h5><ul>${
        outgoing.map(e => `<li>${escapeHtml(labelOf(e.to))} <span class="edge-kind">· ${e.kind}${e.label?' · '+escapeHtml(e.label):''}</span></li>`).join('')
      }</ul></div>` : ''}
      ${incoming.length ? `<div class="conn"><h5>← 연결 (in)</h5><ul>${
        incoming.map(e => `<li>${escapeHtml(labelOf(e.from))} <span class="edge-kind">· ${e.kind}${e.label?' · '+escapeHtml(e.label):''}</span></li>`).join('')
      }</ul></div>` : ''}
    `;
    document.getElementById('graph-detail').innerHTML = html;
    renderNodeContent(d);
  }

  const initId = graphState.selectedId || (nodes[0] && nodes[0].id);
  const initNode = nodes.find(n => n.id === initId);
  if(initNode) selectNode(initNode);
  graphState.rendered = true;
}

document.querySelectorAll('[data-layout]').forEach(btn => btn.addEventListener('click', () => {
  document.querySelectorAll('[data-layout]').forEach(x => x.classList.remove('active'));
  btn.classList.add('active');
  renderGraph(btn.dataset.layout);
}));

// ── 노드 클릭 시 파일 내용 렌더
function renderNodeContent(node){
  const titleEl = document.getElementById('content-title');
  const metaEl  = document.getElementById('content-meta');
  const bodyEl  = document.getElementById('content-body');
  titleEl.textContent = node.label;
  metaEl.innerHTML = node.path
    ? `<code style="background:var(--panel);padding:2px 6px;border-radius:4px;color:#94A3B8">${escapeHtml(node.path)}</code>`
    : '';

  const data = (DATA.node_contents || {})[node.id];
  if(!data){ bodyEl.innerHTML = '<div class="muted">(이 노드는 연결된 파일이 없습니다)</div>'; return; }

  if(data.kind === 'file'){
    const isMarkdown = node.path && node.path.toLowerCase().endsWith('.md');
    const isJson     = node.path && node.path.toLowerCase().endsWith('.json');
    metaEl.innerHTML += ` <span style="margin-left:6px;color:#64748B">${data.size.toLocaleString()} bytes</span>`;
    if(isMarkdown && window.marked){
      try {
        marked.setOptions({ breaks:true, gfm:true });
        bodyEl.innerHTML = marked.parse(data.text);
      } catch(e){
        bodyEl.innerHTML = `<pre>${escapeHtml(data.text)}</pre>`;
      }
    } else if(isJson){
      let pretty = data.text;
      try { pretty = JSON.stringify(JSON.parse(data.text), null, 2); } catch(e){}
      bodyEl.innerHTML = `<pre><code>${escapeHtml(pretty)}</code></pre>`;
    } else {
      bodyEl.innerHTML = `<pre>${escapeHtml(data.text)}</pre>`;
    }
  } else if(data.kind === 'dir'){
    const items = data.entries.map(e =>
      `<li>
        <span class="${e.is_dir ? 'dir-icon' : 'file-icon'}">${e.is_dir ? '▸' : '·'}</span>
        ${escapeHtml(e.name)}${e.is_dir ? '/' : ''}
        ${e.size != null ? `<span class="file-size">${e.size.toLocaleString()} B</span>` : ''}
      </li>`
    ).join('');
    bodyEl.innerHTML = `<div class="muted" style="margin-bottom:8px">디렉터리 — ${data.entries.length}개 항목</div><ul class="content-dir-list">${items || '<li class="muted">(비어있음)</li>'}</ul>`;
  } else {
    bodyEl.innerHTML = `<div class="muted">${escapeHtml(data.text || '(없음)')}</div>`;
  }
}

// ── 역할 테이블 (그래프 탭 하단)
function renderRoleTable(){
  const nodes = DATA.graph.nodes || [];
  const kinds = DATA.graph.kinds || {};
  const groupOrder = ['root-doc','live-state','live-state-optional','decisions','snapshots','templates','prompts','guide','guide-ai'];
  const groupLabels = {
    'root-doc':'루트 문서','live-state':'라이브 상태','live-state-optional':'선택적 라이브 상태',
    'decisions':'결정 기록','snapshots':'스냅샷','templates':'템플릿','prompts':'프롬프트',
    'guide':'기획 지침서','guide-ai':'AI 보조 지침서'
  };
  const grouped = {};
  nodes.forEach(n => { (grouped[n.kind] = grouped[n.kind]||[]).push(n); });
  let html = '<table class="role-table"><thead><tr><th style="width:80px">유형</th><th style="width:160px">문서/폴더</th><th style="width:280px">경로</th><th>역할</th></tr></thead><tbody>';
  groupOrder.forEach(k => {
    if(!grouped[k]) return;
    const color = kinds[k]?.color || '#64748B';
    grouped[k].forEach((n, i) => {
      html += `<tr>
        ${i===0 ? `<td rowspan="${grouped[k].length}"><span class="kind-tag" style="background:${color}">${groupLabels[k]||k}</span></td>` : ''}
        <td class="label">${escapeHtml(n.label)}</td>
        <td class="path">${escapeHtml(n.path||'—')}</td>
        <td class="role-cell">${escapeHtml(n.role||'')}</td>
      </tr>`;
    });
  });
  html += '</tbody></table>';
  document.getElementById('role-table').innerHTML = html;
}
renderRoleTable();

// ── 타임라인
function parseDate(s){ if(!s) return null; const m = s.match(/(\d{4})-(\d{2})-(\d{2})/); return m ? new Date(+m[1], +m[2]-1, +m[3]) : null; }
function fmtMD(d){ return `${(d.getMonth()+1).toString().padStart(2,'0')}-${d.getDate().toString().padStart(2,'0')}`; }
function isoWeek(d){
  const target = new Date(d.valueOf()); const dayNr = (d.getDay()+6) % 7;
  target.setDate(target.getDate() - dayNr + 3);
  const firstThu = new Date(target.getFullYear(),0,4);
  return 1 + Math.round(((target - firstThu)/86400000 - 3 + (firstThu.getDay()+6)%7) / 7);
}

function renderTimeline(view){
  const grid = document.getElementById('timeline-grid');
  grid.innerHTML = '';
  const sprints = DATA.sprints.map(s => ({
    id:s.id, title:s.fields.title || s.id, start:parseDate(s.fields.start), end:parseDate(s.fields.end),
    status:(s.fields.status||'planned').toLowerCase()
  })).filter(s => s.start && s.end);
  if(!sprints.length){ grid.textContent = '(SPRINTS.md 데이터 없음)'; return; }

  const minD = new Date(Math.min(...sprints.map(s=>s.start)));
  const maxD = new Date(Math.max(...sprints.map(s=>s.end)));

  let cells = [], cellOf = (d) => null;
  if(view === 'week'){
    const start = new Date(minD); start.setDate(start.getDate() - ((start.getDay()+6)%7));
    for(let d = new Date(start); d <= maxD; d.setDate(d.getDate()+7)){
      cells.push({ start:new Date(d), label:`W${isoWeek(d)} (${fmtMD(d)})` });
    }
    cellOf = (d) => cells.findIndex((c,i) => d >= c.start && (i===cells.length-1 || d < cells[i+1].start));
  } else if(view === 'month'){
    const start = new Date(minD.getFullYear(), minD.getMonth(), 1);
    for(let d = new Date(start); d <= maxD; d.setMonth(d.getMonth()+1)){
      cells.push({ start:new Date(d), label:`${d.getFullYear()}-${(d.getMonth()+1).toString().padStart(2,'0')}` });
    }
    cellOf = (d) => cells.findIndex((c,i) => d >= c.start && (i===cells.length-1 || d < cells[i+1].start));
  } else { // year
    const start = new Date(minD.getFullYear(),0,1);
    for(let y = start.getFullYear(); y <= maxD.getFullYear(); y++){
      cells.push({ start:new Date(y,0,1), label:`${y}` });
    }
    cellOf = (d) => d.getFullYear() - cells[0].start.getFullYear();
  }

  grid.style.gridTemplateColumns = `120px repeat(${cells.length}, minmax(80px,1fr))`;

  // 헤더 row
  const head = document.createElement('div'); head.className='tcell'; head.textContent='Sprint';
  grid.appendChild(head);
  cells.forEach(c => {
    const el = document.createElement('div'); el.className='tcell'; el.textContent = c.label; grid.appendChild(el);
  });

  // 각 스프린트 row
  sprints.forEach(s => {
    const lab = document.createElement('div'); lab.className='tcell';
    lab.style.textAlign='left'; lab.style.color='#E5E7EB'; lab.textContent = `${s.id} · ${s.title}`;
    grid.appendChild(lab);
    const si = Math.max(0, cellOf(s.start));
    const ei = Math.max(si, cellOf(s.end));
    for(let i=0; i<cells.length; i++){
      const cell = document.createElement('div'); cell.className='tcell'; cell.style.padding='4px 2px';
      if(i === si){
        const span = ei - si + 1;
        cell.style.gridColumn = `span ${span}`;
        const bar = document.createElement('div'); bar.className = 'tbar ' + s.status;
        bar.textContent = `${s.id} · ${s.title}`; cell.appendChild(bar);
        grid.appendChild(cell); i = ei;
      } else if(i < si || i > ei){
        grid.appendChild(cell);
      }
    }
  });
}
renderTimeline('week');
document.querySelectorAll('.timeline-controls .btn').forEach(b => b.addEventListener('click', () => {
  document.querySelectorAll('.timeline-controls .btn').forEach(x => x.classList.remove('active'));
  b.classList.add('active'); renderTimeline(b.dataset.view);
}));

// ── 칸반
function renderKanban(){
  const order = ['Backlog','Ready','InProgress','Blocked','Done'];
  const labels = {Backlog:'백로그', Ready:'대기 (Ready)', InProgress:'진행 중', Blocked:'차단됨', Done:'완료'};
  const root = document.getElementById('kanban');
  order.forEach(sec => {
    const cards = DATA.kanban[sec] || [];
    const col = document.createElement('div'); col.className='col';
    col.innerHTML = `<h2>${labels[sec]} <span class="count">${cards.length}</span></h2>`;
    cards.forEach(c => {
      const div = document.createElement('div'); div.className='card';
      const cls = (c.fields['change-class']||'').replace(/\s/g,'').toUpperCase();
      const done = c.criteria.filter(x=>x[0]).length, total = c.criteria.length;
      div.innerHTML = `
        <h3>${c.id}${c.fields.title ? ' · '+escapeHtml(c.fields.title) : ''}</h3>
        <div class="row">
          ${cls ? `<span class="pill ${cls}">Class ${cls}</span>` : ''}
          ${c.fields.mode ? `<span class="pill">${escapeHtml(c.fields.mode)}</span>` : ''}
          ${c.fields.owner ? `<span class="pill">${escapeHtml(c.fields.owner)}</span>` : ''}
          ${c.fields.sprint ? `<span class="pill">${escapeHtml(c.fields.sprint)}</span>` : ''}
          ${total ? `<span class="pill">${done}/${total}</span>` : ''}
        </div>
        ${c.fields.notes ? `<div class="muted" style="margin-top:6px;font-size:12px">${escapeHtml(c.fields.notes)}</div>` : ''}
      `;
      col.appendChild(div);
    });
    root.appendChild(col);
  });
}
function escapeHtml(s){ return String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'})[c]); }
renderKanban();

// ── 통합 뷰: 마스터플랜 섹션 카드 + 스프린트 표 + 칸반
function renderExec(){
  // 1) 마스터플랜
  const text = DATA.master_plan_text || '';
  const meta = document.getElementById('mp-meta');
  meta.innerHTML = DATA.master_plan_path
    ? `<code style="background:var(--panel);padding:2px 6px;border-radius:4px">${escapeHtml(DATA.master_plan_path)}</code>`
    : '<span class="muted">(MASTER_PLAN.md 없음 — 템플릿 사용 중)</span>';

  const sectionsRoot = document.getElementById('mp-sections');
  sectionsRoot.innerHTML = '';
  if(!text){
    sectionsRoot.innerHTML = '<div class="muted">마스터플랜 내용 없음</div>';
  } else {
    // ## N 헤더로 분할
    const lines = text.split('\n');
    let buf = [], header = '(머리말)', sections = [];
    function flush(){ if(buf.length || sections.length===0) sections.push({title:header, body:buf.join('\n').trim()}); }
    for(const line of lines){
      const m = /^##\s+(.+?)\s*$/.exec(line);
      if(m){ flush(); header = m[1]; buf = []; }
      else { buf.push(line); }
    }
    flush();

    sections.forEach(s => {
      // 머리말은 frontmatter라 스킵
      if(s.title === '(머리말)' && s.body.startsWith('---')) return;
      const isEmpty = !s.body.replace(/<!--[\s\S]*?-->/g, '').replace(/\s/g, '');
      const card = document.createElement('div');
      card.className = 'mp-card' + (isEmpty ? ' empty' : '');
      let rendered = '';
      if(window.marked && s.body){
        try { rendered = marked.parse(s.body); } catch(e){ rendered = `<pre>${escapeHtml(s.body)}</pre>`; }
      }
      card.innerHTML = `<h4>${escapeHtml(s.title)}</h4><div class="mp-content">${rendered}</div>`;
      sectionsRoot.appendChild(card);
    });
  }

  // 2) 스프린트 표
  const tbl = document.getElementById('sprint-table');
  const sprints = DATA.sprints || [];
  const headers = ['ID', '제목', '기간', 'cadence', '상태', 'owner', '게이트', '목표 (done/total)', 'TODO IDs', '메모'];
  let html = '<thead><tr>' + headers.map(h => `<th>${h}</th>`).join('') + '</tr></thead><tbody>';
  if(!sprints.length){
    html += `<tr><td colspan="${headers.length}" class="muted" style="text-align:center;padding:18px">스프린트 없음</td></tr>`;
  } else {
    sprints.forEach(s => {
      const f = s.fields || {};
      const status = (f.status || 'planned').toLowerCase();
      const done = (s.goals || []).filter(g => g[0]).length;
      const total = (s.goals || []).length;
      const goalsHtml = (s.goals || []).map(g =>
        `<li class="${g[0] ? 'done' : ''}">${escapeHtml(g[1])}</li>`
      ).join('');
      html += `<tr>
        <td class="s-id">${escapeHtml(s.id)}</td>
        <td>${escapeHtml(f.title || '—')}</td>
        <td style="white-space:nowrap;font-size:11px">${escapeHtml(f.start || '?')} ~ ${escapeHtml(f.end || '?')}</td>
        <td>${escapeHtml(f.cadence || '—')}</td>
        <td><span class="s-status ${status}">${escapeHtml(status)}</span></td>
        <td>${escapeHtml(f.owner || '—')}</td>
        <td>${escapeHtml(f.gate || '—')}</td>
        <td>${goalsHtml ? `<ul class="s-goals">${goalsHtml}</ul><div style="font-size:10px;color:#64748B;margin-top:4px">${done}/${total}</div>` : '—'}</td>
        <td style="font-family:ui-monospace,Menlo,monospace;font-size:11px">${escapeHtml(f['todo-ids'] || '—')}</td>
        <td style="font-size:11px;color:#94A3B8">${escapeHtml(f.notes || '—')}</td>
      </tr>`;
    });
  }
  html += '</tbody>';
  tbl.innerHTML = html;

  // 3) 칸반 (기존 renderKanban과 같은 로직, exec 컨테이너에 다시 그림)
  const kbExec = document.getElementById('kanban-exec');
  kbExec.innerHTML = '';
  const order = ['Backlog','Ready','InProgress','Blocked','Done'];
  const labels = {Backlog:'백로그', Ready:'대기', InProgress:'진행 중', Blocked:'차단됨', Done:'완료'};
  order.forEach(sec => {
    const cards = (DATA.kanban[sec] || []);
    const col = document.createElement('div'); col.className='col';
    col.innerHTML = `<h2>${labels[sec]} <span class="count">${cards.length}</span></h2>`;
    cards.forEach(c => {
      const div = document.createElement('div'); div.className='card';
      const cls = (c.fields['change-class']||'').replace(/\s/g,'').toUpperCase();
      const done = c.criteria.filter(x=>x[0]).length, total = c.criteria.length;
      div.innerHTML = `
        <h3 style="font-size:13px">${c.id}${c.fields.title ? ' · '+escapeHtml(c.fields.title) : ''}</h3>
        <div class="row">
          ${cls ? `<span class="pill ${cls}">Class ${cls}</span>` : ''}
          ${c.fields.sprint ? `<span class="pill">${escapeHtml(c.fields.sprint)}</span>` : ''}
          ${total ? `<span class="pill">${done}/${total}</span>` : ''}
        </div>`;
      col.appendChild(div);
    });
    kbExec.appendChild(col);
  });
}

// 탭 전환 시 그래프와 동일하게 lazy-render
const _origTabHandler = document.querySelectorAll('.tab');
_origTabHandler.forEach(t => t.addEventListener('click', () => {
  if(t.dataset.page === 'exec') renderExec();
}));
</script>
</body>
</html>
"""


def render_html(data: dict[str, Any]) -> str:
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    return HTML_TEMPLATE.replace("__DATA__", payload)


# ──────────────────────────────────────── main ────────────────────────────────────────


def main() -> int:
    parser = argparse.ArgumentParser(description="방법론 대시보드 빌더")
    parser.add_argument("--root", default=str(ROOT), help="프로젝트 루트 (기본: 스크립트 위치)")
    parser.add_argument("--out", default=None, help="출력 HTML 경로 (기본: <root>/dashboard.html)")
    parser.add_argument("--serve", action="store_true", help="생성 후 8765 포트로 서빙")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()

    root = Path(args.root).resolve()
    out = Path(args.out) if args.out else root / "dashboard.html"

    data = assemble(root)
    out.write_text(render_html(data), encoding="utf-8")
    print(f"[ok] {out}  (kanban={sum(len(v) for v in data['kanban'].values())} cards, "
          f"sprints={len(data['sprints'])}, nodes={len(data['graph'].get('nodes',[]))})", file=sys.stderr)

    if args.serve:
        import http.server
        import socketserver
        os.chdir(out.parent)
        handler = http.server.SimpleHTTPRequestHandler

        class Server(socketserver.TCPServer):
            allow_reuse_address = True

        port = args.port
        for attempt in range(20):
            try:
                with Server(("", port), handler) as httpd:
                    print(f"[serve] http://localhost:{port}/{out.name}", file=sys.stderr)
                    try:
                        httpd.serve_forever()
                    except KeyboardInterrupt:
                        print("\n[stop]", file=sys.stderr)
                    break
            except OSError as e:
                if e.errno == 48:  # Address already in use
                    print(f"[warn] port {port} busy, trying {port+1}", file=sys.stderr)
                    port += 1
                    continue
                raise

    return 0


if __name__ == "__main__":
    sys.exit(main())
