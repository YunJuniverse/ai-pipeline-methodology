#!/usr/bin/env python3
"""generate-dashboard.py — 방법론 대시보드 단일 파일 빌더.

하는 일:
  1) docs/methodology-graph.json 을 읽어 방법론 그래프 + 라이프사이클을 시각화
  2) TODO.md 의 5개 섹션(Backlog/Ready/InProgress/Blocked/Done)을 칸반으로 파싱
  3) SPRINTS.md 의 ### S-NNN 블록을 타임라인(주/월/연 토글)으로 파싱
  4) CLAUDE.md, HANDOFF.md, docs/archive/planning-guides/README.md 일부를 가이드 탭에 인라인

산출물: dashboard.html (자기완결, CDN: d3.v7)

사용 (저장소 루트에서 실행):
  python 60_tools/generate-dashboard.py                 # dashboard.html 생성
  python 60_tools/generate-dashboard.py --serve         # 파일 생성 후 8765 포트로 서빙
  python 60_tools/generate-dashboard.py --out PATH      # 출력 경로 지정
  python 60_tools/generate-dashboard.py --root PATH     # 다른 프로젝트에 대해 실행
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent

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


def parse_project_meta(claude_path: Path) -> dict:
    """CLAUDE.md §1 Project Settings의 `**Key**: value` 줄을 파싱."""
    out = {}
    if not claude_path.exists():
        return out
    in_section = False
    for line in claude_path.read_text(encoding="utf-8").splitlines():
        if re.match(r"^##\s+1\.", line):
            in_section = True
            continue
        if in_section and re.match(r"^##\s+", line):
            break
        if not in_section:
            continue
        m = re.match(r"^-\s+\*\*([^*]+)\*\*\s*:\s*(.+?)\s*$", line)
        if m:
            out[m.group(1).strip()] = m.group(2).strip()
    return out


def detect_dev_url(root: Path) -> str | None:
    """package.json scripts에서 dev URL을 추정."""
    pkg = root / "package.json"
    if not pkg.exists():
        return None
    try:
        data = json.loads(pkg.read_text(encoding="utf-8"))
        scripts = " ".join(data.get("scripts", {}).values()) if isinstance(data.get("scripts"), dict) else ""
        deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
        # 명시적 PORT
        m = re.search(r"PORT[=:](\d+)", scripts)
        if m:
            return f"http://localhost:{m.group(1)}"
        m = re.search(r"-p\s+(\d+)", scripts) or re.search(r"--port[=\s](\d+)", scripts)
        if m:
            return f"http://localhost:{m.group(1)}"
        # 프레임워크 기본 포트
        if "next" in deps:
            return "http://localhost:3000"
        if "vite" in deps:
            return "http://localhost:5173"
        if "@remix-run/dev" in deps:
            return "http://localhost:3000"
        if "nuxt" in deps:
            return "http://localhost:3000"
        if "fastify" in deps:
            return "http://localhost:3000"
    except Exception:
        return None
    return None


def read_package_info(root: Path) -> dict:
    pkg = root / "package.json"
    if not pkg.exists():
        return {}
    try:
        data = json.loads(pkg.read_text(encoding="utf-8"))
        return {
            "name": data.get("name", ""),
            "version": data.get("version", ""),
            "scripts": data.get("scripts", {}),
            "dependencies_count": len(data.get("dependencies", {})),
            "dev_dependencies_count": len(data.get("devDependencies", {})),
            "main_deps": list((data.get("dependencies") or {}).keys())[:8],
        }
    except Exception:
        return {}


def read_project_config(root: Path) -> dict:
    """선택: 40_dev/project-config.json (사용자가 직접 채우는 추가 메타)."""
    p = root / "40_dev" / "project-config.json"
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return {}


def parse_master_plan_meta(master_plan_path: Path) -> dict:
    """MASTER_PLAN.md frontmatter의 master_plan 블록 추출 (간이 YAML 파서)."""
    if not master_plan_path.exists():
        return {}
    text = master_plan_path.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        kv = re.match(r"^(\w+):\s*(.+)\s*$", line)
        if kv:
            out[kv.group(1)] = kv.group(2).strip()
        nested = re.match(r"^\s+(\w+):\s*(.+)\s*$", line)
        if nested:
            out[nested.group(1)] = nested.group(2).strip()
    return out


def count_files(p: Path, suffix: str = "") -> int:
    if not p.exists() or not p.is_dir():
        return 0
    return sum(1 for x in p.glob(f"*{suffix}") if x.is_file() and not x.name.startswith("."))


def count_files_recursive(p: Path, suffix: str = "") -> int:
    if not p.exists() or not p.is_dir():
        return 0
    return sum(1 for x in p.rglob(f"*{suffix}") if x.is_file() and not x.name.startswith("."))


def read_json_safe(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _count_observations(root: Path) -> int:
    """관찰 로그 카운트 — 50_resources/ai_observations + 70_meta/observations 모두 포함.
    적용 프로젝트는 50_resources 만 가짐 (70_meta 는 source 전용). source 저장소는 양쪽 합산.
    v3.2 fallback (40_resources / 60_meta) 도 추가 검사.
    """
    total = 0
    for rel in ("50_resources/ai_observations", "70_meta/observations",
                "40_resources/ai_observations", "60_meta/observations"):
        d = root / rel
        if not d.is_dir():
            continue
        # _README.md / README.md 제외
        for f in d.glob("*.md"):
            if f.name.startswith("_") or f.name.lower() == "readme.md":
                continue
            total += 1
    return total


def read_methodology_assets(root: Path) -> dict:
    catalog = root / "50_resources" / "catalog"
    skeletons = root / "50_resources" / "skeletons"
    insights = root / "40_dev" / "snapshots" / "insights"
    context = read_json_safe(root / ".ai" / "context.json")
    return {
        "context": context,
        "observations": _count_observations(root),
        "catalog_pending": count_files(catalog / "_pending", ".md"),
        "catalog_active": len([p for p in catalog.glob("C-*.md") if p.is_file()]),
        "catalog_archived": count_files(catalog / "archived", ".md"),
        "skeleton_domains": len([p for p in skeletons.iterdir() if p.is_dir()]) if skeletons.exists() else 0,
        "skeleton_locks": count_files_recursive(skeletons, "skeleton.lock.json"),
        "insight_reports": count_files(insights, ".md"),
        "adapters": context.get("adapters_present", []),
        "active_todos": context.get("active_todos", []),
    }


# ──────────────────────────────────── data assembly ────────────────────────────────────


def assemble(root: Path) -> dict[str, Any]:
    # graph: 60_tools/ 우선, 루트 fallback, docs/ fallback (이전 구조 호환)
    graph_path = root / "60_tools" / "methodology-graph.json"
    for cand in [root / "methodology-graph.json", root / "docs" / "methodology-graph.json"]:
        if not graph_path.exists():
            graph_path = cand

    # TODO: 루트 → 50_resources/templates → docs/templates
    todo_path = root / "TODO.md"
    for cand in [root / "50_resources" / "templates" / "TODO.md", root / "docs" / "templates" / "TODO.md"]:
        if not todo_path.exists():
            todo_path = cand

    # SPRINTS: 40_dev → 루트 → 50_resources/templates → docs/templates
    sprints_path = root / "40_dev" / "SPRINTS.md"
    for cand in [root / "SPRINTS.md", root / "50_resources" / "templates" / "SPRINTS.md", root / "docs" / "templates" / "SPRINTS.md"]:
        if not sprints_path.exists():
            sprints_path = cand

    handoff_path = root / "HANDOFF.md"
    for cand in [root / "50_resources" / "templates" / "HANDOFF.md", root / "docs" / "templates" / "HANDOFF.md"]:
        if not handoff_path.exists():
            handoff_path = cand

    # MASTER_PLAN: 40_dev → root → 50_resources/templates
    master_plan_path = root / "40_dev" / "MASTER_PLAN.md"
    for cand in [root / "MASTER_PLAN.md", root / "50_resources" / "templates" / "MASTER_PLAN.md"]:
        if not master_plan_path.exists():
            master_plan_path = cand

    claude_path = root / "CLAUDE.md"
    # README: 새 구조 → 구 구조 fallback
    readme_path = root / "20_guides" / "README.md"
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

    # 현재 git 브랜치·HEAD short SHA — dashboard가 *어느 브랜치/시점*의 상태인지 명시
    git_branch = "unknown"
    git_commit = "unknown"
    try:
        git_branch = subprocess.check_output(
            ["git", "-C", str(root), "branch", "--show-current"],
            text=True, stderr=subprocess.DEVNULL,
        ).strip() or "DETACHED"
        git_commit = subprocess.check_output(
            ["git", "-C", str(root), "rev-parse", "--short", "HEAD"],
            text=True, stderr=subprocess.DEVNULL,
        ).strip()
    except Exception:
        pass

    # 자주 사용 명령 메타데이터 (Commands 카드용)
    commands_data: dict = {}
    cmds_path = root / "60_tools" / "commands.json"
    if cmds_path.exists():
        try:
            commands_data = json.loads(cmds_path.read_text(encoding="utf-8"))
        except Exception:
            commands_data = {}

    # 기술 스택 메타데이터 (Stack bento 카드용)
    stack_data: dict = {}
    stack_path = root / "60_tools" / "stack.json"
    if stack_path.exists():
        try:
            stack_data = json.loads(stack_path.read_text(encoding="utf-8"))
        except Exception:
            stack_data = {}

    return {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "root": str(root),
        "git_branch": git_branch,
        "git_commit": git_commit,
        "commands": commands_data,
        "stack": stack_data,
        "graph": graph,
        "kanban": kanban,
        "sprints": sprints_json,
        "node_contents": node_contents,
        "master_plan_text": read_text_safe(master_plan_path, 50000),
        "master_plan_path": str(master_plan_path.relative_to(root)) if master_plan_path.exists() else "",
        "project_overview": {
            "meta":            parse_project_meta(claude_path),
            "config":          read_project_config(root),
            "dev_url":         detect_dev_url(root),
            "package":         read_package_info(root),
            "claude_md":       read_text_safe(claude_path, 50000),
            "claude_md_path":  str(claude_path.relative_to(root)) if claude_path.exists() else "",
            "agents_md":       read_text_safe(root / "AGENTS.md", 50000),
            "handoff_md":      read_text_safe(handoff_path, 50000),
            "handoff_md_path": str(handoff_path.relative_to(root)) if handoff_path.exists() else "",
            "todo_md":         read_text_safe(todo_path, 50000),
            "todo_md_path":    str(todo_path.relative_to(root)) if todo_path.exists() else "",
            "master_plan_meta": parse_master_plan_meta(master_plan_path),
            "kanban_summary": {sec: len(cards) for sec, cards in kanban.items()},
            "adr_count":     count_files(root / "40_dev" / "adr", ".md"),
            "snapshot_count": count_files(root / "40_dev" / "snapshots", ".md"),
            "sprint_total":   len(sprints_json),
            "sprint_active":  sum(1 for s in sprints_json if s["fields"].get("status", "").lower() == "active"),
            "methodology_assets": read_methodology_assets(root),
        },
        "guides_readme": read_text_safe(readme_path, 50000),
    }


# ──────────────────────────────────── HTML rendering ───────────────────────────────────


HTML_TEMPLATE = r"""
<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>in-spire · 방법론 대시보드</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@300;400;500;600;700;800&family=Noto+Sans+KR:wght@300;400;500;600;700;800&family=Noto+Sans+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<script src="https://d3js.org/d3.v7.min.js"></script>
<style>
:root{
  --bg:        oklch(0.165 0.006 70);
  --surface:   oklch(0.205 0.006 70);
  --surface-2: oklch(0.235 0.006 70);
  --hairline:  oklch(0.32  0.008 70);
  --hairline-soft: oklch(0.27 0.006 70);
  --text:      oklch(0.95  0.012 80);
  --text-dim:  oklch(0.78  0.010 75);
  --muted:     oklch(0.58  0.010 75);
  --faint:     oklch(0.42  0.008 75);
  --accent:    oklch(0.80  0.15  75);
  --accent-ink:oklch(0.20  0.04  75);
  --ok:        oklch(0.78  0.13  155);
  --warn:      oklch(0.80  0.14  60);
  --danger:    oklch(0.68  0.18  25);
  --info:      oklch(0.75  0.11  240);
  --violet:    oklch(0.72  0.13  300);
  --font-display:"Noto Sans","Noto Sans KR",-apple-system,BlinkMacSystemFont,sans-serif;
  --font-ui:"Noto Sans","Noto Sans KR",-apple-system,BlinkMacSystemFont,sans-serif;
  --font-mono:"Noto Sans Mono",ui-monospace,Menlo,monospace;
  --pad-section:56px; --pad-card:24px; --gap-card:16px;
}
[data-theme="paper"]{
  --bg:oklch(0.96 0.008 85);--surface:oklch(0.99 0.006 85);--surface-2:oklch(0.93 0.008 85);
  --hairline:oklch(0.80 0.010 80);--hairline-soft:oklch(0.88 0.008 80);
  --text:oklch(0.20 0.012 70);--text-dim:oklch(0.35 0.010 70);
  --muted:oklch(0.50 0.010 75);--faint:oklch(0.65 0.008 75);--accent-ink:oklch(0.98 0.01 85);
}
[data-theme="cool"]{
  --bg:oklch(0.17 0.012 250);--surface:oklch(0.21 0.012 250);--surface-2:oklch(0.24 0.012 250);
  --hairline:oklch(0.33 0.014 250);--hairline-soft:oklch(0.27 0.012 250);
  --text:oklch(0.95 0.015 230);--text-dim:oklch(0.78 0.013 230);
  --muted:oklch(0.58 0.012 230);--faint:oklch(0.42 0.012 230);
}
[data-accent="cyan"]{--accent:oklch(0.82 0.12 200);--accent-ink:oklch(0.20 0.04 200);}
[data-accent="lime"]{--accent:oklch(0.86 0.18 130);--accent-ink:oklch(0.20 0.04 130);}
[data-accent="rose"]{--accent:oklch(0.74 0.17 15);--accent-ink:oklch(0.98 0.02 15);}
[data-density="compact"]{--pad-section:36px;--pad-card:16px;--gap-card:10px;}

*{box-sizing:border-box}
html,body{margin:0;padding:0;background:var(--bg);color:var(--text);font-family:var(--font-ui);font-size:14px;line-height:1.55;-webkit-font-smoothing:antialiased;}
a{color:inherit;text-decoration:none}
button{font:inherit;color:inherit;background:none;border:none;cursor:pointer;padding:0}

.app{max-width:1480px;margin:0 auto;padding:0 40px 80px;}

/* Masthead */
.masthead{display:grid;grid-template-columns:1fr auto;gap:40px;align-items:end;padding:48px 0 28px;border-bottom:1px solid var(--hairline);position:relative;}
.mast-eyebrow{font-family:var(--font-mono);font-size:10.5px;letter-spacing:0.18em;text-transform:uppercase;color:var(--muted);display:flex;gap:14px;flex-wrap:wrap;align-items:center;margin-bottom:14px;}
.mast-eyebrow .dot{width:6px;height:6px;background:var(--accent);display:inline-block;}
.mast-eyebrow .sep{color:var(--faint)}
.mast-title{font-family:var(--font-display);font-weight:800;font-size:64px;line-height:0.98;letter-spacing:-0.035em;margin:0;color:var(--text);}
.mast-title em{color:var(--accent);font-weight:800;font-style:normal;}
.mast-right{display:flex;flex-direction:column;align-items:flex-end;gap:10px;font-family:var(--font-mono);font-size:11px;color:var(--muted);}
.mast-right .branch{color:var(--text);display:flex;align-items:center;gap:8px;border:1px solid var(--hairline);padding:6px 10px;}
.mast-right .branch::before{content:"";width:6px;height:6px;border-radius:50%;background:var(--ok);box-shadow:0 0 0 4px color-mix(in oklch,var(--ok) 18%,transparent);}
.mast-right .commit{letter-spacing:0.02em}
.mast-right .generated{color:var(--faint)}

/* Tabs */
.tabs{display:flex;gap:0;border-bottom:1px solid var(--hairline);position:sticky;top:0;background:color-mix(in oklch,var(--bg) 92%,transparent);backdrop-filter:blur(12px);z-index:50;}
.tab{font-family:var(--font-ui);font-size:13px;font-weight:500;padding:18px 0 16px;margin-right:32px;color:var(--muted);letter-spacing:-0.005em;position:relative;display:flex;align-items:center;gap:8px;cursor:pointer;}
.tab .num{font-family:var(--font-mono);font-size:10px;color:var(--faint);font-weight:400;}
.tab:hover{color:var(--text-dim)}
.tab.active{color:var(--text)}
.tab.active::after{content:"";position:absolute;left:0;right:0;bottom:-1px;height:2px;background:var(--accent);}

/* Pages */
.page{display:none;padding:36px 0;}
.page.active{display:block}

/* Cards */
.card{background:var(--surface);border:1px solid var(--hairline-soft);padding:var(--pad-card);}
.card+.card{margin-top:var(--gap-card)}
.card-head{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:16px;padding-bottom:14px;border-bottom:1px solid var(--hairline-soft);}
.card-head h3{margin:0;font-family:var(--font-display);font-weight:700;font-size:18px;letter-spacing:-0.015em;color:var(--text);}
.card-head h3 em{color:var(--accent);font-style:normal;font-weight:700;}
.card-head .meta{font-family:var(--font-mono);font-size:10.5px;letter-spacing:0.14em;text-transform:uppercase;color:var(--muted);}
.eyebrow{font-family:var(--font-mono);font-size:10.5px;letter-spacing:0.18em;text-transform:uppercase;color:var(--muted);margin-bottom:8px;display:block;}

/* Hero */
.hero{display:grid;grid-template-columns:1.4fr 1fr;gap:0;border-bottom:1px solid var(--hairline);padding:36px 0 40px;}
.hero-left{padding-right:48px;border-right:1px solid var(--hairline-soft);}
.hero-right{padding-left:48px;display:flex;flex-direction:column;justify-content:center;gap:18px;}
.hero h2{font-family:var(--font-display);font-weight:800;font-size:42px;line-height:1.04;letter-spacing:-0.03em;margin:8px 0 14px;}
.hero h2 .ital{color:var(--accent);font-weight:800;}
.hero-desc{color:var(--text-dim);font-weight:300;font-size:15px;line-height:1.6;max-width:54ch;}
.badge-row{display:flex;flex-wrap:wrap;gap:8px;margin-top:18px;}
.badge{font-family:var(--font-mono);font-size:10.5px;letter-spacing:0.12em;text-transform:uppercase;border:1px solid var(--hairline);padding:5px 9px;color:var(--text-dim);}
.badge.accent{border-color:var(--accent);color:var(--accent);}
.badge.solid{background:var(--accent);color:var(--accent-ink);border-color:var(--accent);}

/* Readout / stat row */
.stat-row{display:grid;grid-template-columns:repeat(5,1fr);gap:0;border:1px solid var(--hairline-soft);margin-top:28px;}
.stat{padding:20px 22px;border-right:1px solid var(--hairline-soft);display:flex;flex-direction:column;gap:6px;}
.stat:last-child{border-right:none;}
.stat .l{font-family:var(--font-mono);font-size:10px;letter-spacing:0.15em;text-transform:uppercase;color:var(--muted);}
.stat .n{font-family:var(--font-display);font-weight:700;font-size:36px;line-height:1;color:var(--text);letter-spacing:-0.035em;}
.stat .s{font-family:var(--font-mono);font-size:11px;color:var(--text-dim);}

/* Two-col rows */
.row2{display:grid;grid-template-columns:1fr 1fr;gap:var(--gap-card);margin-top:var(--gap-card);}
@media(max-width:1100px){.row2{grid-template-columns:1fr}}

/* Key/value list */
.kv{list-style:none;margin:0;padding:0;}
.kv li{display:grid;grid-template-columns:160px 1fr;gap:18px;padding:11px 0;border-bottom:1px dashed var(--hairline-soft);font-size:13.5px;}
.kv li:last-child{border-bottom:none;}
.kv .k{font-family:var(--font-mono);font-size:10.5px;letter-spacing:0.12em;text-transform:uppercase;color:var(--muted);align-self:center;}
.kv .v{color:var(--text);font-weight:400;}
.kv .v code,.kv .v .mono{font-family:var(--font-mono);font-size:12.5px;color:var(--accent);background:transparent;padding:0;}

/* Progress bar */
.progress-wrap{margin-top:8px;}
.progress-bar{display:flex;height:8px;background:var(--surface-2);border:1px solid var(--hairline-soft);}
.progress-bar>div{height:100%;}
.pb-done{background:var(--ok);}.pb-now{background:var(--accent);}.pb-next{background:var(--info);}.pb-block{background:var(--danger);}.pb-rest{background:var(--surface-2);}
.progress-legend{display:flex;flex-wrap:wrap;gap:18px;margin-top:14px;font-family:var(--font-mono);font-size:10.5px;letter-spacing:0.06em;text-transform:uppercase;color:var(--text-dim);}
.progress-legend span{display:flex;align-items:center;gap:6px;}
.progress-legend span::before{content:"";width:8px;height:8px;display:inline-block;background:var(--muted);}
.progress-legend .pl-done::before{background:var(--ok);}.pl-now::before{background:var(--accent);}.pl-next::before{background:var(--info);}.pl-block::before{background:var(--danger);}.pl-back::before{background:var(--faint);}

/* Mini bar */
.mini-bar{height:6px;background:var(--surface-2);border:1px solid var(--hairline-soft);overflow:hidden;}
.mini-bar>div{height:100%;background:var(--accent);}
.mini-bar.done>div{background:var(--ok);}

/* File viewer */
.file-tabs{display:flex;flex-wrap:wrap;gap:0;border-bottom:1px solid var(--hairline-soft);margin-bottom:18px;}
.file-tab{font-family:var(--font-mono);font-size:11.5px;padding:10px 16px;border-right:1px solid var(--hairline-soft);color:var(--muted);cursor:pointer;letter-spacing:0.02em;}
.file-tab:hover{color:var(--text-dim);background:color-mix(in oklch,var(--surface-2) 60%,transparent);}
.file-tab.active{color:var(--text);background:var(--surface-2);}
.file-tab .icon{color:var(--accent);margin-right:6px;}
.file-body{font-family:var(--font-mono);font-size:12.5px;line-height:1.7;color:var(--text-dim);background:var(--surface-2);border:1px solid var(--hairline-soft);padding:24px 28px;max-height:520px;overflow:auto;font-weight:300;}
.file-body .md-h1{display:block;font-family:var(--font-display);font-size:22px;color:var(--text);font-weight:800;margin:4px 0 16px;letter-spacing:-0.025em;padding-bottom:10px;border-bottom:1px solid var(--hairline-soft);}
.file-body .md-h2{display:block;font-family:var(--font-display);font-size:16px;color:var(--text);font-weight:600;margin:20px 0 8px;letter-spacing:-0.01em;}
.file-body .md-h3{display:block;color:var(--text);font-family:var(--font-ui);font-weight:600;font-size:12px;margin:16px 0 4px;letter-spacing:0.02em;text-transform:uppercase;}
.file-body .md-li{display:list-item;margin-left:24px;}
.file-body .md-code{color:var(--accent);}
.file-body .md-hr{display:block;border-top:1px dashed var(--hairline);margin:18px 0;}
.file-body .md-quote{display:block;padding:6px 14px;border-left:2px solid var(--accent);color:var(--text-dim);margin:6px 0;}

/* Commands */
.cmd-tabs{display:flex;gap:0;border-bottom:1px solid var(--hairline-soft);margin-bottom:14px;flex-wrap:wrap;}
.cmd-cat{font-family:var(--font-mono);font-size:10.5px;letter-spacing:0.15em;text-transform:uppercase;padding:9px 14px;color:var(--muted);cursor:pointer;border-right:1px solid var(--hairline-soft);}
.cmd-cat.active{color:var(--text);background:var(--surface-2);}
.cmd-cat:hover{color:var(--text-dim);}
.cmd-list{display:flex;flex-direction:column;}
.cmd-item{display:grid;grid-template-columns:260px 1fr auto;gap:24px;align-items:center;padding:14px 0;border-bottom:1px dashed var(--hairline-soft);}
.cmd-item:last-child{border-bottom:none;}
.cmd-item .lbl{font-size:13.5px;color:var(--text);font-weight:500;}
.cmd-item .desc{font-size:12.5px;color:var(--muted);font-weight:300;}
.cmd-item .run{font-family:var(--font-mono);font-size:11.5px;color:var(--text-dim);background:var(--surface-2);padding:6px 10px;border:1px solid var(--hairline-soft);white-space:nowrap;cursor:pointer;transition:all .15s;}
.cmd-item .run:hover{color:var(--accent-ink);background:var(--accent);border-color:var(--accent);}
.cmd-item .run::before{content:"$ ";color:var(--accent);}
.cmd-item .run:hover::before{color:var(--accent-ink);}

/* Table */
.tbl{width:100%;border-collapse:collapse;font-size:13px;}
.tbl thead th{text-align:left;font-family:var(--font-mono);font-size:10px;letter-spacing:0.15em;text-transform:uppercase;color:var(--muted);font-weight:500;padding:10px 16px 10px 0;border-bottom:1px solid var(--hairline);}
.tbl tbody td{padding:14px 16px 14px 0;border-bottom:1px dashed var(--hairline-soft);vertical-align:middle;color:var(--text);}
.tbl tbody tr:last-child td{border-bottom:none;}
.tbl tbody tr:hover td{background:color-mix(in oklch,var(--surface-2) 50%,transparent);}
.tbl .mono{font-family:var(--font-mono);font-size:12px;color:var(--text-dim);}
.tbl .port{color:var(--accent);font-family:var(--font-mono);font-weight:500;}
.btn-row{display:flex;gap:6px;align-items:center;}
.btn{font-family:var(--font-mono);font-size:11px;letter-spacing:0.08em;text-transform:uppercase;padding:6px 12px;border:1px solid var(--hairline);background:transparent;color:var(--text);cursor:pointer;transition:all .15s;}
.btn:hover{border-color:var(--accent);color:var(--accent);}
.btn-primary{background:var(--accent);border-color:var(--accent);color:var(--accent-ink);}
.btn-primary:hover{filter:brightness(1.08);color:var(--accent-ink);}
.btn-danger{border-color:var(--hairline);color:var(--text-dim);}
.btn-danger:hover{border-color:var(--danger);color:var(--danger);}

/* Status dot */
.dot{width:7px;height:7px;border-radius:50%;display:inline-block;}
.dot.ok{background:var(--ok);box-shadow:0 0 0 3px color-mix(in oklch,var(--ok) 20%,transparent);}
.dot.warn{background:var(--warn);}
.dot.dim{background:var(--faint);}

/* Kanban */
.kanban{display:grid;grid-template-columns:repeat(5,1fr);gap:1px;background:var(--hairline-soft);border:1px solid var(--hairline-soft);}
.k-col{background:var(--surface);padding:18px 16px;min-height:520px;}
.k-col-head{display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;padding-bottom:10px;border-bottom:1px solid var(--hairline-soft);}
.k-col-head .title{font-family:var(--font-mono);font-size:10.5px;letter-spacing:0.18em;text-transform:uppercase;color:var(--text);}
.k-col-head .count{font-family:var(--font-display);font-weight:700;font-size:22px;color:var(--accent);line-height:1;letter-spacing:-0.04em;}
.k-col[data-col="now"] .count{color:var(--accent);}
.k-col[data-col="next"] .count{color:var(--info);}
.k-col[data-col="library"] .count{color:var(--ok);}
.k-col[data-col="thinktank"] .count{color:var(--violet);}
.k-col[data-col="blocked"] .count{color:var(--danger);}
.k-card{background:var(--surface-2);border:1px solid var(--hairline-soft);padding:14px 14px 12px;margin-bottom:10px;cursor:pointer;}
.k-card:hover{border-color:var(--accent);}
.k-card .tag{font-family:var(--font-mono);font-size:9.5px;letter-spacing:0.16em;text-transform:uppercase;color:var(--muted);display:flex;justify-content:space-between;margin-bottom:6px;}
.k-card .tag .id{color:var(--accent);}
.k-card .title{font-size:13.5px;color:var(--text);line-height:1.4;margin-bottom:8px;font-weight:400;}
.k-card .meta{font-family:var(--font-mono);font-size:10.5px;color:var(--text-dim);display:flex;gap:10px;align-items:center;}
.k-card .meta .sep{color:var(--faint);}
.k-card .pri.a{color:var(--ok);}.k-card .pri.b{color:var(--warn);}.k-card .pri.c{color:var(--danger);}
.k-col-head .collapse{font-family:var(--font-mono);font-size:14px;color:var(--muted);width:22px;height:22px;display:flex;align-items:center;justify-content:center;border:1px solid var(--hairline-soft);cursor:pointer;line-height:1;}
.k-col-head .collapse:hover{color:var(--accent);border-color:var(--accent);}
.k-col.collapsed{min-height:auto;padding-bottom:12px;}
.k-col.collapsed .k-card{display:none;}
.k-col.collapsed .k-col-head{margin-bottom:0;padding-bottom:0;border-bottom:none;}
.k-col-summary{display:none;margin-top:8px;font-family:var(--font-mono);font-size:10.5px;color:var(--text-dim);letter-spacing:0.05em;line-height:1.6;}
.k-col.collapsed .k-col-summary{display:block;}

/* Timeline / Gantt */
.timeline-toolbar{display:flex;align-items:center;gap:10px;margin-bottom:20px;}
.timeline-toolbar .seg{display:flex;border:1px solid var(--hairline);}
.timeline-toolbar .seg button{font-family:var(--font-mono);font-size:10.5px;letter-spacing:0.14em;text-transform:uppercase;padding:7px 14px;color:var(--muted);border-right:1px solid var(--hairline);}
.timeline-toolbar .seg button:last-child{border-right:none;}
.timeline-toolbar .seg button.active{background:var(--accent);color:var(--accent-ink);}
.gantt{display:grid;grid-template-columns:200px 1fr;gap:0;border:1px solid var(--hairline-soft);}
.hcell{font-family:var(--font-mono);font-size:10px;letter-spacing:0.14em;text-transform:uppercase;color:var(--muted);padding:12px 14px;border-bottom:1px solid var(--hairline);background:var(--surface-2);}
.gantt-track{display:grid;position:relative;border-bottom:1px solid var(--hairline);background:var(--surface-2);}
.tick{font-family:var(--font-mono);font-size:10px;color:var(--muted);padding:12px 0 12px 8px;border-right:1px dashed var(--hairline-soft);}
.tick:last-child{border-right:none;}
.label{padding:18px 14px;border-bottom:1px dashed var(--hairline-soft);display:flex;flex-direction:column;gap:4px;cursor:pointer;}
.label:hover,.lane:hover{background:color-mix(in oklch,var(--surface-2) 70%,transparent);}
.label .id{font-family:var(--font-mono);font-size:10px;letter-spacing:0.14em;text-transform:uppercase;color:var(--accent);}
.label .ttl{font-size:13px;color:var(--text);}
.label .dt{font-family:var(--font-mono);font-size:10.5px;color:var(--muted);}
.lane{position:relative;border-bottom:1px dashed var(--hairline-soft);background:repeating-linear-gradient(to right,transparent 0,transparent calc(100%/12 - 1px),var(--hairline-soft) calc(100%/12 - 1px),var(--hairline-soft) calc(100%/12));cursor:pointer;min-height:66px;}
.gantt-bar{position:absolute;top:50%;transform:translateY(-50%);height:30px;background:var(--accent);color:var(--accent-ink);display:flex;align-items:center;gap:8px;padding:0 12px;font-size:12px;font-weight:500;border:1px solid color-mix(in oklch,var(--accent) 70%,black);overflow:hidden;min-width:0;}
.gantt-bar>span:first-child{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}
.gantt-bar.done{background:var(--ok);border-color:color-mix(in oklch,var(--ok) 70%,black);color:oklch(0.18 0.03 155);}
.gantt-bar.planned{background:transparent;border:1px dashed var(--info);color:var(--info);}
.gantt-bar.active{background:var(--accent);}
.gantt-bar.cancelled{background:color-mix(in oklch,var(--danger) 40%,var(--surface-2));border-color:var(--danger);color:var(--text-dim);text-decoration:line-through;}
.gantt-bar .perc{margin-left:auto;font-family:var(--font-mono);font-size:11px;opacity:.85;flex-shrink:0;}
.now-line{position:absolute;top:0;bottom:0;width:1px;background:var(--accent);box-shadow:0 0 0 1px color-mix(in oklch,var(--accent) 30%,transparent);z-index:2;}
.now-line::after{content:"NOW";position:absolute;top:-18px;left:-16px;font-family:var(--font-mono);font-size:9.5px;letter-spacing:0.18em;color:var(--accent);}

/* Graph */
.graph-grid{display:grid;grid-template-columns:1fr 320px;gap:1px;background:var(--hairline-soft);border:1px solid var(--hairline-soft);}
.graph-canvas{background:var(--surface);padding:24px;min-height:560px;position:relative;overflow:hidden;}
.graph-detail{background:var(--surface);padding:24px;}
.graph-detail .eyebrow{margin-bottom:8px;}
.graph-detail h4{font-family:var(--font-display);font-weight:800;font-size:22px;letter-spacing:-0.025em;margin:0 0 6px;color:var(--text);}
.graph-detail .path{font-family:var(--font-mono);font-size:11px;color:var(--text-dim);margin-bottom:18px;}
.graph-detail p{color:var(--text-dim);font-weight:300;font-size:13.5px;line-height:1.65;}
.graph-detail .conn-block{margin-top:24px;padding-top:18px;border-top:1px solid var(--hairline-soft);}
.graph-detail .conn-block .eyebrow{margin-bottom:10px;}
.graph-detail .conn-block ul{list-style:none;padding:0;margin:0;}
.graph-detail .conn-block li{display:grid;grid-template-columns:auto 1fr;gap:10px;align-items:baseline;padding:6px 0;border-bottom:1px dashed var(--hairline-soft);font-size:12.5px;}
.graph-detail .conn-block li:last-child{border-bottom:none;}
.graph-detail .conn-block li .ek{font-family:var(--font-mono);font-size:10px;letter-spacing:0.14em;text-transform:uppercase;color:var(--muted);}
.legend{display:flex;flex-wrap:wrap;gap:18px;font-family:var(--font-mono);font-size:10.5px;letter-spacing:0.1em;color:var(--text-dim);}
.legend span{display:flex;align-items:center;gap:6px;text-transform:uppercase;}
.legend .lg-dot{width:9px;height:9px;display:inline-block;border-radius:50%;}

/* Stack — 카테고리별 그룹, 정렬된 카드 그리드 (size = 강조 등급, 레이아웃 X) */
.stack-wrap{display:flex;flex-direction:column;gap:0;border:1px solid var(--hairline-soft);background:var(--surface);}
.stack-cat{border-bottom:1px solid var(--hairline-soft);}
.stack-cat:last-child{border-bottom:none;}
.stack-cat-head{display:grid;grid-template-columns:auto 1fr auto;align-items:center;gap:20px;padding:16px 24px;background:var(--surface);border-bottom:1px solid var(--hairline-soft);}
.stack-cat-head .num{font-family:var(--font-mono);font-size:10.5px;letter-spacing:0.16em;color:var(--muted);}
.stack-cat-head .lbl{font-family:var(--font-display);font-weight:700;font-size:18px;letter-spacing:-0.02em;color:var(--text);display:flex;align-items:baseline;gap:12px;}
.stack-cat-head .lbl .primary-note{font-family:var(--font-mono);font-weight:500;font-size:10.5px;color:var(--accent);letter-spacing:0.14em;text-transform:uppercase;}
.stack-cat-head .count{font-family:var(--font-mono);font-size:10.5px;letter-spacing:0.14em;text-transform:uppercase;color:var(--muted);}
.stack-cat-head .count b{color:var(--accent);font-weight:600;font-size:13px;letter-spacing:0;margin-right:4px;}
.stack-cat-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:1px;background:var(--hairline-soft);}
.stack-card{background:var(--surface);padding:18px 22px;display:flex;flex-direction:column;gap:6px;cursor:pointer;position:relative;transition:background .12s;min-height:148px;}
.stack-card:hover{background:var(--surface-2);}
.stack-card .role{font-family:var(--font-mono);font-size:11px;letter-spacing:0.02em;color:var(--muted);font-weight:400;}
.stack-card .name{font-family:var(--font-display);font-weight:700;font-size:17px;letter-spacing:-0.015em;color:var(--text);line-height:1.25;margin:2px 0 0;}
.stack-card .tag{font-family:var(--font-mono);font-size:11px;color:var(--accent);letter-spacing:0.02em;margin-top:2px;}
.stack-card .reason{font-size:12.5px;color:var(--text-dim);font-weight:300;line-height:1.55;margin-top:auto;padding-top:10px;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden;}
.stack-card .chev{position:absolute;bottom:16px;right:20px;color:var(--muted);font-size:13px;opacity:0;transition:opacity .12s,transform .12s;}
.stack-card:hover .chev{opacity:1;transform:translateX(2px);color:var(--accent);}
.stack-card.hero{background:color-mix(in oklch,var(--surface) 82%, var(--accent) 4%);}
.stack-card.hero::before{content:"";position:absolute;left:0;top:0;bottom:0;width:2px;background:var(--accent);}
.stack-card.hero .star{position:absolute;top:16px;right:20px;font-family:var(--font-mono);font-size:10px;letter-spacing:0.18em;color:var(--accent);font-weight:500;}
.stack-card.hero .name{font-size:20px;letter-spacing:-0.02em;}
.stack-card.hero:hover{background:color-mix(in oklch,var(--surface) 68%, var(--accent) 6%);}
@media (max-width:680px){
  .stack-cat-head{grid-template-columns:1fr auto;gap:12px;}
  .stack-cat-head .num{display:none;}
  .stack-cat-grid{grid-template-columns:repeat(auto-fill,minmax(180px,1fr));}
}

/* Section head */
.section-head{margin-top:48px;display:flex;justify-content:space-between;align-items:end;margin-bottom:24px;}
.section-head h2{font-family:var(--font-display);font-weight:800;font-size:32px;letter-spacing:-0.03em;margin:0;line-height:1;}
.section-head h2 em{color:var(--accent);font-weight:800;font-style:normal;}
.row{display:flex;gap:8px;flex-wrap:wrap;align-items:center;}
.divider{height:1px;background:var(--hairline);margin:48px 0 24px;position:relative;}
.divider::after{content:"";position:absolute;left:0;top:-3px;width:32px;height:7px;background:var(--accent);}

/* Modal */
.modal-overlay{position:fixed;inset:0;z-index:2000;background:color-mix(in oklch,black 55%,transparent);backdrop-filter:blur(3px);display:flex;animation:mo-fade .15s ease-out;}
@keyframes mo-fade{from{opacity:0;}to{opacity:1;}}
@keyframes mo-slide{from{transform:translateX(24px);opacity:0;}to{transform:translateX(0);opacity:1;}}
.modal-overlay.side{justify-content:flex-end;}
.modal{background:var(--surface);border:1px solid var(--hairline);display:flex;flex-direction:column;max-height:100vh;overflow:hidden;}
.modal.side{width:560px;max-width:92vw;height:100vh;border-right:none;border-top:none;border-bottom:none;animation:mo-slide .22s ease-out;}
.modal-head{padding:24px 28px 18px;border-bottom:1px solid var(--hairline-soft);display:flex;justify-content:space-between;align-items:flex-start;gap:24px;flex-shrink:0;}
.modal-head .eyebrow{margin-bottom:8px;}
.modal-head h3{margin:0;font-family:var(--font-display);font-weight:800;font-size:22px;letter-spacing:-0.025em;color:var(--text);line-height:1.2;}
.modal-close{width:32px;height:32px;border:1px solid var(--hairline);color:var(--text-dim);display:flex;align-items:center;justify-content:center;cursor:pointer;flex-shrink:0;font-size:18px;line-height:1;}
.modal-close:hover{border-color:var(--accent);color:var(--accent);}
.modal-body{padding:24px 28px 28px;overflow:auto;flex:1;}
.modal-body .section{margin-bottom:24px;}
.modal-body .section:last-child{margin-bottom:0;}
.modal-body .section .eyebrow{margin-bottom:10px;}
.modal-foot{padding:16px 28px;border-top:1px solid var(--hairline-soft);display:flex;justify-content:space-between;align-items:center;gap:10px;flex-shrink:0;background:var(--surface-2);}
.meta-grid{display:grid;grid-template-columns:1fr 1fr;gap:0;border:1px solid var(--hairline-soft);}
.meta-grid .cell{padding:14px 18px;border-right:1px solid var(--hairline-soft);border-bottom:1px solid var(--hairline-soft);}
.meta-grid .cell:nth-child(2n){border-right:none;}
.meta-grid .cell:nth-last-child(-n+2){border-bottom:none;}
.meta-grid .l{font-family:var(--font-mono);font-size:9.5px;letter-spacing:0.16em;text-transform:uppercase;color:var(--muted);}
.meta-grid .v{font-size:13.5px;color:var(--text);margin-top:4px;font-family:var(--font-mono);}
.checklist{list-style:none;padding:0;margin:0;}
.checklist li{display:grid;grid-template-columns:18px 1fr;gap:10px;align-items:start;padding:9px 0;border-bottom:1px dashed var(--hairline-soft);font-size:13.5px;}
.checklist li:last-child{border-bottom:none;}
.checklist li .box{display:inline-flex;align-items:center;justify-content:center;width:16px;height:16px;border:1.5px solid var(--hairline);margin-top:3px;color:var(--accent-ink);font-size:10px;}
.checklist li.done .box{background:var(--ok);border-color:var(--ok);color:oklch(0.15 0.04 155);}
.checklist li.done .t{color:var(--muted);text-decoration:line-through;}
.checklist li .t{color:var(--text);line-height:1.5;}
.rel-list{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;}
.rel-list li{display:grid;grid-template-columns:80px 1fr auto;gap:14px;align-items:center;padding:10px 0;border-bottom:1px dashed var(--hairline-soft);font-size:13px;}
.rel-list li:last-child{border-bottom:none;}
.rel-list .rid{font-family:var(--font-mono);font-size:11px;color:var(--accent);}
.rel-list .rttl{color:var(--text);}
.rel-list .rpri{font-family:var(--font-mono);font-size:10px;letter-spacing:0.14em;color:var(--muted);}
.tag-row{display:flex;flex-wrap:wrap;gap:6px;}
.tag-row .tg{font-family:var(--font-mono);font-size:10px;letter-spacing:0.12em;text-transform:uppercase;border:1px solid var(--hairline);padding:4px 8px;color:var(--text-dim);}
.tag-row .tg.accent{border-color:var(--accent);color:var(--accent);}
.tag-row .tg.ok{border-color:color-mix(in oklch,var(--ok) 60%,var(--hairline));color:var(--ok);}
.tag-row .tg.warn{border-color:color-mix(in oklch,var(--warn) 60%,var(--hairline));color:var(--warn);}
.tag-row .tg.danger{border-color:color-mix(in oklch,var(--danger) 60%,var(--hairline));color:var(--danger);}
.modal-prose{color:var(--text-dim);font-weight:300;font-size:14px;line-height:1.6;}
.modal-prose strong{color:var(--text);font-weight:600;}
.modal-prose code{font-family:var(--font-mono);color:var(--accent);font-size:12.5px;}

/* Responsive */
@media(max-width:1100px){
  .hero{grid-template-columns:1fr;}
  .hero-left{padding-right:0;border-right:none;padding-bottom:32px;border-bottom:1px solid var(--hairline-soft);}
  .hero-right{padding-left:0;padding-top:32px;}
  .stat-row{grid-template-columns:repeat(2,1fr);}
  .kanban{grid-template-columns:repeat(2,1fr);}
  .graph-grid{grid-template-columns:1fr;}
}
@media(max-width:680px){
  .app{padding:0 20px 60px;}
  .mast-title{font-size:44px;}
  .tabs{overflow-x:auto;flex-wrap:nowrap;}
  .tab{flex-shrink:0;}
  .kanban{grid-template-columns:1fr;}
  .stat-row{grid-template-columns:1fr;}
}
</style>
</head>
<body data-theme="warm" data-accent="amber" data-density="cozy">
<div class="app">

  <!-- Masthead -->
  <header class="masthead">
    <div>
      <div class="mast-eyebrow">
        <span class="dot"></span>
        <span id="mast-project-name">METHODOLOGY</span>
        <span class="sep">·</span>
        <span id="mast-phase">v3</span>
        <span class="sep">·</span>
        <span>EVIDENCE-DRIVEN AI DEVELOPMENT</span>
      </div>
      <h1 class="mast-title">in<em>-</em>spire</h1>
    </div>
    <div class="mast-right">
      <div class="branch" id="mast-branch"></div>
      <div class="commit" id="mast-commit"></div>
      <div class="generated" id="mast-generated"></div>
    </div>
  </header>

  <!-- Tabs -->
  <nav class="tabs">
    <div class="tab active" data-page="overview"><span class="num">01</span><span>프로젝트 개요</span></div>
    <div class="tab" data-page="guide"><span class="num">02</span><span>가이드 · 백서</span></div>
    <div class="tab" data-page="graph"><span class="num">03</span><span>관계 그래프</span></div>
    <div class="tab" data-page="timeline"><span class="num">04</span><span>타임라인</span></div>
    <div class="tab" data-page="kanban"><span class="num">05</span><span>칸반 보드</span></div>
    <div class="tab" data-page="exec"><span class="num">06</span><span>통합 뷰</span></div>
  </nav>

  <!-- Page 01: Overview -->
  <section class="page active" id="page-overview">
    <section class="hero">
      <div class="hero-left">
        <span class="eyebrow">Project / <span id="hero-project-name">methodology</span></span>
        <h2>Evidence-driven<br/><span class="ital">AI development</span></h2>
        <p class="hero-desc" id="hero-objective"></p>
        <div class="badge-row" id="hero-badges"></div>
      </div>
      <div class="hero-right">
        <span class="eyebrow">Current sprint</span>
        <div id="hero-sprint-content"><span style="color:var(--muted)">—</span></div>
      </div>
    </section>
    <section class="stat-row" id="stat-row"></section>
    <div class="row2" id="stack-progress-row"></div>
    <div class="card" style="margin-top:var(--gap-card)">
      <div class="card-head">
        <h3>파일 <em>뷰어</em></h3>
        <span class="meta">live state · meta files</span>
      </div>
      <div class="file-tabs" id="file-tabs"></div>
      <div class="file-body" id="file-body"></div>
    </div>
    <div class="card" style="margin-top:var(--gap-card)">
      <div class="card-head">
        <h3>커맨드 <em>팔레트</em></h3>
        <span class="meta">click to copy</span>
      </div>
      <div class="cmd-tabs" id="commands-tabs"></div>
      <div class="cmd-list" id="commands-list"></div>
      <div id="commands-toast" style="min-height:18px;margin-top:12px;font-family:var(--font-mono);font-size:11px;letter-spacing:.1em;color:var(--accent)"></div>
    </div>
    <div class="card" style="margin-top:var(--gap-card)">
      <div class="card-head">
        <h3>로컬 <em>대시보드</em></h3>
        <span class="meta">~/.methodology-dashboards.json</span>
      </div>
      <table class="tbl" id="dashboards-table">
        <thead><tr><th>Port</th><th>Project</th><th>Branch</th><th>Commit</th><th>Started</th><th></th></tr></thead>
        <tbody><tr><td colspan="6" style="padding:14px;color:var(--muted)">Loading…</td></tr></tbody>
      </table>
      <div style="margin-top:12px;display:flex;gap:8px;align-items:center">
        <button class="btn" id="dashboards-refresh">↺ Refresh</button>
        <span id="dashboards-status" style="font-family:var(--font-mono);font-size:11px;color:var(--muted)"></span>
      </div>
    </div>
    <div class="card" style="margin-top:var(--gap-card)">
      <div class="card-head">
        <h3>브랜치 · <em>worktree</em></h3>
        <span class="meta">spawn isolated dashboard</span>
      </div>
      <p style="color:var(--text-dim);font-weight:300;font-size:13px;margin:0 0 14px;max-width:68ch">라디오 선택 → <strong>Open →</strong> 누르면 그 브랜치의 dashboard가 별도 포트에 spawn됩니다.</p>
      <div id="branches-list"></div>
      <div style="margin-top:12px;display:flex;gap:8px;align-items:center">
        <button class="btn btn-primary" id="branches-spawn">Open →</button>
        <button class="btn" id="branches-refresh">↺ Refresh</button>
        <span id="branches-status" style="font-family:var(--font-mono);font-size:11px;color:var(--muted)"></span>
      </div>
    </div>
    <div class="card" style="margin-top:var(--gap-card)">
      <div class="card-head">
        <h3>Dev <em>servers</em></h3>
        <span class="meta">auto-port 3000-3099</span>
      </div>
      <div style="display:flex;gap:8px;margin-bottom:14px;flex-wrap:wrap">
        <input id="dev-cwd" placeholder="cwd" style="flex:1;min-width:240px;background:var(--surface-2);border:1px solid var(--hairline);padding:9px 12px;color:var(--text);font-family:var(--font-mono);font-size:12px"/>
        <input id="dev-cmd" value="pnpm dev" style="width:140px;background:var(--surface-2);border:1px solid var(--hairline);padding:9px 12px;color:var(--text);font-family:var(--font-mono);font-size:12px"/>
        <button class="btn btn-primary" id="dev-start">Start ↗</button>
        <button class="btn btn-danger" id="dev-kill-all">Kill 3000–3099</button>
        <button class="btn" id="dev-refresh">↺</button>
      </div>
      <table class="tbl" id="dev-servers-table">
        <thead><tr><th>Port</th><th>PID</th><th>CWD</th><th>Cmd</th><th>Started</th><th></th></tr></thead>
        <tbody></tbody>
      </table>
      <div id="dev-servers-status" style="margin-top:8px;font-family:var(--font-mono);font-size:11px;color:var(--muted)"></div>
    </div>

    <!-- Stack bento -->
    <div id="stack-section" style="margin-top:var(--gap-card)">
      <div class="section-head" style="margin-top:0;margin-bottom:18px">
        <h2>기술 <em>스택</em>.</h2>
        <span style="font-family:var(--font-mono);font-size:11px;color:var(--muted);letter-spacing:.14em;text-transform:uppercase" id="stack-meta">카드 클릭 → 선택 이유</span>
      </div>
      <div class="stack-wrap" id="stack-grid"></div>
    </div>
  </section>

  <!-- Page 02: Guide -->
  <section class="page" id="page-guide">
    <div id="guide-content"></div>
  </section>

  <!-- Page 03: Graph -->
  <section class="page" id="page-graph">
    <div class="section-head" style="margin-top:0">
      <h2>관계 <em>그래프</em>.</h2>
      <div class="row">
        <div class="timeline-toolbar" style="margin:0"><div class="seg"><button class="active">계층</button></div></div>
      </div>
    </div>
    <div class="graph-grid">
      <div class="graph-canvas">
        <svg id="graph-svg" viewBox="0 0 720 540" width="100%" height="560" style="display:block"></svg>
        <div class="legend" id="graph-legend" style="position:absolute;left:24px;bottom:18px"></div>
      </div>
      <aside class="graph-detail" id="graph-detail">
        <span class="eyebrow">노드를 클릭하세요</span>
        <h4 style="margin:8px 0 6px">—</h4>
        <p style="color:var(--muted)">그래프 노드를 선택하면 상세 정보가 여기 표시됩니다.</p>
      </aside>
    </div>
    <div class="legend" style="margin-top:14px" id="graph-legend-bottom"></div>
  </section>

  <!-- Page 04: Timeline -->
  <section class="page" id="page-timeline">
    <div class="section-head" style="margin-top:0">
      <h2>스프린트 <em>타임라인</em>.</h2>
      <div class="timeline-toolbar" style="margin:0">
        <div class="seg">
          <button class="active" id="view-btn-month" data-view="month">Month</button>
          <button id="view-btn-year" data-view="year">Year</button>
        </div>
      </div>
    </div>
    <div class="card" style="padding:0;overflow:hidden">
      <div class="gantt" id="gantt"></div>
    </div>
    <div class="legend" style="margin-top:18px">
      <span><span class="lg-dot" style="background:var(--ok)"></span>done</span>
      <span><span class="lg-dot" style="background:var(--accent)"></span>active</span>
      <span><span class="lg-dot" style="background:transparent;border:1px dashed var(--info)"></span>planned</span>
      <span><span class="lg-dot" style="background:var(--danger);opacity:.4"></span>cancelled</span>
    </div>
  </section>

  <!-- Page 05: Kanban -->
  <section class="page" id="page-kanban">
    <div class="section-head" style="margin-top:0">
      <h2>칸반 <em>보드</em>.</h2>
      <div class="row">
        <span id="kanban-count" style="font-family:var(--font-mono);font-size:11px;color:var(--muted);letter-spacing:.14em;text-transform:uppercase"></span>
        <button class="btn" id="kanban-collapse-all">Collapse all</button>
        <button class="btn" id="kanban-expand-all">Expand all</button>
      </div>
    </div>
    <div class="kanban" id="kanban-board"></div>
  </section>

  <!-- Page 06: Exec -->
  <section class="page" id="page-exec">
    <div class="section-head" style="margin-top:0">
      <h2>통합 <em>뷰</em>.</h2>
      <span style="font-family:var(--font-mono);font-size:11px;color:var(--muted);letter-spacing:.14em;text-transform:uppercase">quick scan · all surfaces</span>
    </div>
    <section class="stat-row" id="exec-stat-row"></section>
    <div class="row2" style="margin-top:var(--gap-card)" id="exec-row"></div>
    <div id="exec-dashboards" style="margin-top:var(--gap-card)"></div>
    <div id="exec-branches" style="margin-top:var(--gap-card)"></div>
  </section>

</div><!-- .app -->

<!-- Side-sheet modal -->
<div id="modal-overlay" class="modal-overlay side" style="display:none" onclick="if(event.target===this)closeModal()">
  <div class="modal side">
    <div class="modal-head">
      <div>
        <span class="eyebrow" id="modal-eyebrow"></span>
        <h3 id="modal-title"></h3>
      </div>
      <button class="modal-close" onclick="closeModal()">&#x2715;</button>
    </div>
    <div class="modal-body" id="modal-body"></div>
    <div class="modal-foot">
      <span style="font-family:var(--font-mono);font-size:10.5px;color:var(--muted);letter-spacing:.14em;text-transform:uppercase">Esc / click outside to close</span>
      <div class="btn-row">
        <button class="btn" onclick="closeModal()">Close</button>
      </div>
    </div>
  </div>
</div>

<script>
const DATA = __DATA__;

// ── Utilities ────────────────────────────────────────────────
function esc(s){ return String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'})[c]); }
function renderInline(text){
  return String(text)
    .replace(/`([^`]+)`/g,'<span class="md-code">$1</span>')
    .replace(/\b([A-Z]+-\d{3,}|S-\d{3}|T-\d{3}|M\d|METH-\d+)\b/g,'<span class="md-code">$&</span>')
    .replace(/\[A\]/g,'<span style="color:var(--ok);font-weight:600">[A]</span>')
    .replace(/\[B\]/g,'<span style="color:var(--warn);font-weight:600">[B]</span>')
    .replace(/\[C\]/g,'<span style="color:var(--danger);font-weight:600">[C]</span>');
}
function renderMd(text){
  if(!text) return '<span style="color:var(--muted)">(없음)</span>';
  return esc(text)
    .replace(/^# (.+)$/mg,'<span class="md-h1">$1</span>')
    .replace(/^## (.+)$/mg,'<span class="md-h2">$1</span>')
    .replace(/^### (.+)$/mg,'<span class="md-h3">$1</span>')
    .replace(/^&gt; (.+)$/mg,'<span class="md-quote">$1</span>')
    .replace(/^---$/mg,'<span class="md-hr"></span>')
    .replace(/^[-*] (.+)$/mg,'<span class="md-li">$1</span>')
    .replace(/`([^`]+)`/g,'<span class="md-code">$1</span>');
}

// ── Tab switching ─────────────────────────────────────────────
document.querySelectorAll('.tab').forEach(t=>{
  t.onclick=()=>{
    document.querySelectorAll('.tab').forEach(x=>x.classList.remove('active'));
    document.querySelectorAll('.page').forEach(x=>x.classList.remove('active'));
    t.classList.add('active');
    document.getElementById('page-'+t.dataset.page).classList.add('active');
    if(t.dataset.page==='graph') initGraph();
    if(t.dataset.page==='exec') renderExec();
  };
});

// ── Masthead ─────────────────────────────────────────────────
(function(){
  const meta = (DATA.project_overview||{}).meta||{};
  document.getElementById('mast-branch').textContent = DATA.git_branch||'unknown';
  document.getElementById('mast-commit').textContent = 'commit '+(DATA.git_commit||'unknown');
  document.getElementById('mast-generated').textContent = 'generated '+(DATA.generated_at||'').replace('T',' ');
  const name = meta['Project Name']||'methodology';
  document.getElementById('mast-project-name').textContent = name.toUpperCase();
  document.getElementById('hero-project-name').textContent = name;
  document.getElementById('hero-objective').textContent = meta['Objective']||'';
  const badges = document.getElementById('hero-badges');
  badges.innerHTML = [
    meta['Mode']&&`<span class="badge solid">${esc(meta['Mode'])}</span>`,
    meta['Stack']&&`<span class="badge accent">${esc(meta['Stack'])}</span>`,
    meta['Release Policy']&&`<span class="badge">${esc(meta['Release Policy'])}</span>`,
    meta['Primary Approver']&&`<span class="badge">approver · ${esc(meta['Primary Approver'])}</span>`,
    meta['Started On']&&`<span class="badge">started · ${esc(meta['Started On'])}</span>`,
  ].filter(Boolean).join('');
})();

// ── Hero sprint card ──────────────────────────────────────────
(function(){
  const cur = (DATA.sprints||[]).find(s=>(s.fields.status||'').toLowerCase()==='active');
  const el = document.getElementById('hero-sprint-content');
  if(!cur){el.innerHTML='<span style="color:var(--muted)">진행 중 스프린트 없음</span>';return;}
  const goals=cur.goals||[], done=goals.filter(g=>g[0]).length;
  const perc=goals.length?Math.round(done/goals.length*100):(cur.fields.status==='done'?100:0);
  el.innerHTML=`
    <div style="display:flex;align-items:baseline;gap:14px;margin-top:4px">
      <div style="font-family:var(--font-display);font-weight:800;font-size:42px;line-height:1;letter-spacing:-0.035em;color:var(--accent)">${esc(cur.id)}</div>
      <div style="font-family:var(--font-display);font-weight:700;font-size:36px;line-height:1;letter-spacing:-0.04em">${perc}<span style="font-family:var(--font-mono);font-size:13px;color:var(--muted);letter-spacing:.08em;margin-left:4px">%</span></div>
    </div>
    <div style="font-size:15px;color:var(--text);font-weight:500;margin-top:8px;line-height:1.4">${esc(cur.fields.title||'')}</div>
    <div class="mini-bar" style="margin-top:12px"><div style="width:${perc}%"></div></div>
    <ul class="kv" style="margin-top:14px">
      <li><span class="k">window</span><span class="v"><span class="mono">${esc(cur.fields.start||'—')} → ${esc(cur.fields.end||'—')}</span></span></li>
      <li><span class="k">cadence</span><span class="v">${esc(cur.fields.cadence||'—')}</span></li>
      <li><span class="k">gate</span><span class="v" style="font-size:12.5px">${esc(cur.fields.gate||'—')}</span></li>
    </ul>`;
})();

// ── Stat row ──────────────────────────────────────────────────
function buildStatHtml(){
  const ov=DATA.project_overview||{}, ks=ov.kanban_summary||{};
  const total=Object.values(ks).reduce((a,b)=>a+b,0);
  const now=ks.InProgress||0,next=ks.Ready||0,blocked=ks.Blocked||0;
  return [
    {label:'Sprints',value:ov.sprint_total||0,sub:`${ov.sprint_active||0} active`},
    {label:'TODO',value:total,sub:`${now} NOW · ${next} NEXT · ${blocked} blocked`},
    {label:'ADR',value:ov.adr_count||0,sub:'40_dev/adr/'},
    {label:'Snapshots',value:ov.snapshot_count||0,sub:'40_dev/snapshots/'},
    {label:'Guides',value:(ov.methodology_assets||{}).observations||0,sub:'L1 관찰 로그'},
  ].map(s=>`<div class="stat"><span class="l">${s.label}</span><span class="n">${s.value}</span><span class="s">${s.sub}</span></div>`).join('');
}
document.getElementById('stat-row').innerHTML = buildStatHtml();

// ── Stack + Progress row ──────────────────────────────────────
(function(){
  const ov=DATA.project_overview||{}, meta=ov.meta||{}, ks=ov.kanban_summary||{};
  const total=Object.values(ks).reduce((a,b)=>a+b,0)||1;
  const now=ks.InProgress||0,next=ks.Ready||0,blocked=ks.Blocked||0,done=ks.Done||0,backlog=ks.Backlog||0;
  const pct=n=>(n/total*100).toFixed(1);
  const rows=[
    meta['Stack']&&`<li><span class="k">stack</span><span class="v"><span class="mono">${esc(meta['Stack'])}</span></span></li>`,
    '<li><span class="k">cli</span><span class="v"><span class="mono">60_tools/methodology.py</span></span></li>',
    ov.dev_url&&`<li><span class="k">dev url</span><span class="v"><a class="mono" style="color:var(--accent)" href="${esc(ov.dev_url)}">${esc(ov.dev_url)}</a></span></li>`,
    meta['Mode']&&`<li><span class="k">mode</span><span class="v">${esc(meta['Mode'])}</span></li>`,
    meta['Release Policy']&&`<li><span class="k">release</span><span class="v">${esc(meta['Release Policy'])}</span></li>`,
  ].filter(Boolean).join('');
  document.getElementById('stack-progress-row').innerHTML=`
    <div class="card">
      <div class="card-head"><h3>스택 · <em>개발 정보</em></h3><span class="meta">project / stack</span></div>
      <ul class="kv">${rows}</ul>
    </div>
    <div class="card">
      <div class="card-head"><h3>진행 <em>현황</em></h3><span class="meta">${total} todos</span></div>
      <div style="display:flex;align-items:baseline;gap:14px;margin-bottom:10px">
        <div style="font-family:var(--font-display);font-weight:700;font-size:60px;line-height:1;letter-spacing:-0.04em">${Math.round(done/total*100)}<span style="font-family:var(--font-mono);font-size:14px;color:var(--muted);letter-spacing:.1em;margin-left:4px">%</span></div>
        <div style="font-family:var(--font-mono);font-size:11px;color:var(--text-dim);letter-spacing:.1em;text-transform:uppercase">done /<br>${total} todos</div>
      </div>
      <div class="progress-wrap">
        <div class="progress-bar">
          <div class="pb-done" style="width:${pct(done)}%"></div>
          <div class="pb-now" style="width:${pct(now)}%"></div>
          <div class="pb-next" style="width:${pct(next)}%"></div>
          <div class="pb-block" style="width:${pct(blocked)}%"></div>
          <div class="pb-rest" style="width:${pct(backlog)}%"></div>
        </div>
        <div class="progress-legend">
          <span class="pl-done">done · ${done}</span>
          <span class="pl-now">now · ${now}</span>
          <span class="pl-next">next · ${next}</span>
          <span class="pl-block">blocked · ${blocked}</span>
          <span class="pl-back">backlog · ${backlog}</span>
        </div>
      </div>
    </div>`;
})();

// ── File viewer ───────────────────────────────────────────────
(function(){
  const ov=DATA.project_overview||{};
  const files=[
    {id:'claude',  label:'CLAUDE.md',     icon:'›', text:ov.claude_md},
    {id:'handoff', label:'HANDOFF.md',    icon:'›', text:ov.handoff_md},
    {id:'todo',    label:'TODO.md',       icon:'›', text:ov.todo_md},
    {id:'plan',    label:'MASTER_PLAN.md',icon:'›', text:DATA.master_plan_text},
    {id:'agents',  label:'AGENTS.md',     icon:'›', text:ov.agents_md},
  ];
  const tabsEl=document.getElementById('file-tabs');
  const bodyEl=document.getElementById('file-body');
  function show(id){
    tabsEl.querySelectorAll('.file-tab').forEach(t=>t.classList.toggle('active',t.dataset.fid===id));
    const f=files.find(x=>x.id===id);
    bodyEl.innerHTML=f&&f.text?renderMd(f.text.slice(0,15000))+(f.text.length>15000?'<span class="md-hr"></span><span style="color:var(--muted)">(truncated)</span>':''):'<span style="color:var(--muted)">(파일 없음)</span>';
  }
  tabsEl.innerHTML=files.map(f=>`<div class="file-tab" data-fid="${f.id}"><span class="icon">${f.icon}</span>${f.label}</div>`).join('');
  tabsEl.querySelectorAll('.file-tab').forEach(t=>t.onclick=()=>show(t.dataset.fid));
  show('claude');
})();

// ── Commands ──────────────────────────────────────────────────
(function(){
  const cmdData=DATA.commands;
  const tabsEl=document.getElementById('commands-tabs');
  const listEl=document.getElementById('commands-list');
  const toastEl=document.getElementById('commands-toast');
  const fallback={categories:[
    {id:'dashboard',label:'Dashboard',commands:[
      {label:'Dashboard 빌드+서빙',command:'python3 60_tools/generate-dashboard.py --serve',description:'현재 브랜치·commit 반영'},
      {label:'세션 wrap (4/4 ✓)',command:'methodology wrap',description:'TODO/HANDOFF/checkpoint/observation 갱신 확인'},
    ]},
  ]};
  const data=(cmdData&&cmdData.categories&&cmdData.categories.length)?cmdData:fallback;
  function render(catId){
    tabsEl.innerHTML=data.categories.map(c=>`<div class="cmd-cat ${c.id===catId?'active':''}" data-cat="${esc(c.id)}">${esc(c.label)}</div>`).join('');
    tabsEl.querySelectorAll('.cmd-cat').forEach(b=>b.onclick=()=>render(b.dataset.cat));
    const cat=data.categories.find(c=>c.id===catId)||data.categories[0];
    listEl.innerHTML=(cat&&cat.commands||[]).map(c=>`
      <div class="cmd-item">
        <div><div class="lbl">${esc(c.label||c.command)}</div></div>
        <div class="desc">${esc(c.description||c.desc||'')}</div>
        <div class="run" data-cmd="${esc(c.command)}" title="copy">${esc(c.command)}</div>
      </div>`).join('');
    listEl.querySelectorAll('.run').forEach(el=>{
      el.onclick=()=>{
        const cmd=el.dataset.cmd;
        if(navigator.clipboard)navigator.clipboard.writeText(cmd).catch(()=>{});
        toastEl.textContent='copied — '+cmd;
        setTimeout(()=>toastEl.textContent='',1800);
      };
    });
  }
  if(data.categories.length)render(data.categories[0].id);
})();

// ── Stack — 카테고리별 그룹, 정렬된 카드 그리드 ────────────────
// 디자인 변경 이력 (PR #12, stack-cleanup):
//   - hero 의 grid row-span 으로 자동 배치가 깨지던 문제 → size 는 *강조 등급* 으로 의미 전환.
//   - hero = 좌측 액센트 + ★ PRIMARY 배지 + 살짝 다른 톤 (layout 변경 X).
//   - 카테고리 라벨 매 카드 반복 → 카테고리 그룹 헤더 1회.
//   - role 라벨 uppercase 제거 (한글 줄바꿈 회피).
//   - 모든 카드에 reason 3-line clamp 노출.
(function(){
  const stackData=DATA.stack||{};
  const wrap=document.getElementById('stack-grid');
  const metaEl=document.getElementById('stack-meta');
  const section=document.getElementById('stack-section');
  if(!wrap)return;
  const items=stackData.items||[];
  const cats=stackData.categories||[];
  if(!items.length){section.style.display='none';return;}
  const sizeRank={hero:0,mid:1,sm:2};
  wrap.innerHTML=cats.map((cat,i)=>{
    const list=items.filter(x=>x.category===cat.id)
      .sort((a,b)=>(sizeRank[a.size]??9)-(sizeRank[b.size]??9));
    if(!list.length)return '';
    const heroCount=list.filter(x=>x.size==='hero').length;
    return `
      <div class="stack-cat">
        <div class="stack-cat-head">
          <div class="num">${String(i+1).padStart(2,'0')} / ${esc(cat.short||cat.id.toUpperCase())}</div>
          <div class="lbl">${esc(cat.label)}${heroCount?`<span class="primary-note">★ ${heroCount} primary</span>`:''}</div>
          <div class="count"><b>${list.length}</b> items</div>
        </div>
        <div class="stack-cat-grid">
          ${list.map(it=>{
            const hero=it.size==='hero';
            return `
              <div class="stack-card ${hero?'hero':''}" data-id="${esc(it.id)}">
                ${hero?'<span class="star">★ PRIMARY</span>':''}
                <div class="role">${esc(it.role||'')}</div>
                <div class="name">${esc(it.name)}</div>
                ${it.tag?`<div class="tag">${esc(it.tag)}</div>`:''}
                ${it.reason?`<div class="reason">${esc(it.reason)}</div>`:''}
                <div class="chev">→</div>
              </div>`;
          }).join('')}
        </div>
      </div>`;
  }).join('');
  // 카드 클릭 → 모달
  wrap.querySelectorAll('.stack-card').forEach(el=>{
    el.onclick=()=>{
      const it=items.find(x=>x.id===el.dataset.id);
      if(it)openStackModal(it);
    };
  });
  metaEl.textContent=`${items.length} items · ${cats.length} categories`;
})();

function openStackModal(it){
  const stackData=DATA.stack||{};
  const cats=stackData.categories||[];
  const cat=cats.find(c=>c.id===it.category);
  const body=`
    <div class="section">
      <div class="tag-row" style="margin-bottom:14px">
        <span class="tg accent">${esc(cat?cat.label:it.category)}</span>
        ${it.tag?`<span class="tg">${esc(it.tag)}</span>`:''}
        ${it.role?`<span class="tg">${esc(it.role)}</span>`:''}
        ${it.size==='hero'?`<span class="tg">hero</span>`:''}
      </div>
      <p class="modal-prose">${esc(it.reason||'(이유 미작성)')}</p>
    </div>
    <div class="section">
      <span class="eyebrow">Meta</span>
      <div class="meta-grid">
        <div class="cell"><div class="l">id</div><div class="v">${esc(it.id)}</div></div>
        <div class="cell"><div class="l">category</div><div class="v">${esc(it.category)}</div></div>
        <div class="cell"><div class="l">role</div><div class="v">${esc(it.role||'—')}</div></div>
        <div class="cell"><div class="l">size</div><div class="v">${esc(it.size||'sm')}</div></div>
      </div>
    </div>
    ${it.url?`<div class="section"><span class="eyebrow">Docs</span><p class="modal-prose"><a href="${esc(it.url)}" target="_blank" rel="noopener" style="color:var(--accent);text-decoration:none">${esc(it.url)} →</a></p></div>`:''}`;
  openModal(`Stack · ${cat?cat.label:it.category}`,it.name,body);
}

// ── Kanban ────────────────────────────────────────────────────
const KANBAN_MAP=[
  {sec:'InProgress',id:'now',      title:'NOW',       hint:'이번 sprint에서 진행 중인 작업'},
  {sec:'Ready',     id:'next',     title:'NEXT',      hint:'다음 sprint 후보'},
  {sec:'Done',      id:'library',  title:'LIBRARY',   hint:'완료된 작업 아카이브'},
  {sec:'Backlog',   id:'thinktank',title:'THINKTANK', hint:'아이디어 인큐베이터'},
  {sec:'Blocked',   id:'blocked',  title:'BLOCKED',   hint:'외부 의존으로 보류 중'},
];
const collapseState={};
function renderKanban(){
  const kb=DATA.kanban||{};
  const board=document.getElementById('kanban-board');
  board.innerHTML='';
  let total=0;
  KANBAN_MAP.forEach(col=>{
    const items=kb[col.sec]||[];
    total+=items.length;
    const collapsed=!!collapseState[col.id];
    const colEl=document.createElement('div');
    colEl.className='k-col'+(collapsed?' collapsed':'');
    colEl.dataset.col=col.id;
    colEl.innerHTML=`
      <div class="k-col-head">
        <span class="title">${col.title}</span>
        <div style="display:flex;align-items:center;gap:10px">
          <span class="count">${String(items.length).padStart(2,'0')}</span>
          <button class="collapse" data-col="${col.id}">${collapsed?'+':'−'}</button>
        </div>
      </div>
      <div class="k-col-summary">${col.hint}</div>
      ${items.map(c=>{
        const cls=(c.fields['change-class']||'').replace(/\s/g,'').toUpperCase();
        const priCss=cls==='A'?'a':cls==='B'?'b':cls==='C'?'c':'';
        return `<div class="k-card" data-card-id="${esc(c.id)}" data-col-id="${col.id}">
          <div class="tag">
            <span class="id">${esc(c.id)}</span>
            <span class="pri ${priCss}">${cls?`[${esc(cls)}]`:''}</span>
          </div>
          <div class="title">${esc(c.fields.title||c.id)}</div>
          <div class="meta">
            <span>${esc(c.fields.sprint||'—')}</span>
            <span class="sep">·</span>
            <span>${esc(c.fields.owner||'—')}</span>
            ${c.fields['blocked-on']?`<span class="sep">·</span><span style="color:var(--danger)">${esc(c.fields['blocked-on'])}</span>`:''}
          </div>
        </div>`;
      }).join('')}`;
    board.appendChild(colEl);
  });
  document.getElementById('kanban-count').textContent=`${total} todos`;
  board.querySelectorAll('.collapse').forEach(btn=>{
    btn.onclick=e=>{e.stopPropagation();const col=btn.dataset.col;collapseState[col]=!collapseState[col];renderKanban();};
  });
  board.querySelectorAll('.k-card').forEach(card=>{
    card.onclick=()=>{
      const colData=KANBAN_MAP.find(c=>c.id===card.dataset.colId);
      const cardData=(DATA.kanban[colData&&colData.sec]||[]).find(c=>c.id===card.dataset.cardId);
      if(cardData)openTodoModal(cardData,colData);
    };
  });
}
document.getElementById('kanban-collapse-all').onclick=()=>{KANBAN_MAP.forEach(c=>collapseState[c.id]=true);renderKanban();};
document.getElementById('kanban-expand-all').onclick=()=>{KANBAN_MAP.forEach(c=>delete collapseState[c.id]);renderKanban();};
renderKanban();

// ── Timeline / Gantt ──────────────────────────────────────────
(function(){
  const sprints=DATA.sprints||[];
  const ganttEl=document.getElementById('gantt');
  if(!sprints.length){ganttEl.innerHTML='<div style="padding:24px;color:var(--muted)">스프린트 없음</div>';return;}
  function parseDate(s){if(!s||s.includes('YYYY')||s==='—')return null;try{return new Date(s);}catch{return null;}}
  const dates=sprints.flatMap(s=>[parseDate(s.fields.start),parseDate(s.fields.end)]).filter(Boolean);
  const minDate=dates.length?new Date(Math.min(...dates.map(d=>d.getTime()))):new Date(new Date().getFullYear(),0,1);
  const maxDate=dates.length?new Date(Math.max(...dates.map(d=>d.getTime()))):new Date(new Date().getFullYear(),11,31);
  const span=Math.max(maxDate-minDate,1);
  const now=new Date();
  const nowPct=((now-minDate)/span*100).toFixed(2);
  const MN=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'];
  const months=[];
  let d=new Date(minDate.getFullYear(),minDate.getMonth(),1);
  while(d<=maxDate){months.push(new Date(d));d=new Date(d.getFullYear(),d.getMonth()+1,1);}
  const nc=Math.max(months.length,1);
  ganttEl.style.gridTemplateColumns='200px 1fr';
  // Header
  const hdrLabel=document.createElement('div');hdrLabel.className='hcell';hdrLabel.textContent='Sprint';
  const hdrTrack=document.createElement('div');
  hdrTrack.style.cssText=`display:grid;grid-template-columns:repeat(${nc},1fr);border-bottom:1px solid var(--hairline);background:var(--surface-2)`;
  months.forEach(m=>{const tick=document.createElement('div');tick.className='tick';tick.textContent=MN[m.getMonth()]+" '"+String(m.getFullYear()).slice(2);hdrTrack.appendChild(tick);});
  ganttEl.appendChild(hdrLabel);ganttEl.appendChild(hdrTrack);
  // Rows
  sprints.forEach(s=>{
    const start=parseDate(s.fields.start),end=parseDate(s.fields.end);
    const status=(s.fields.status||'planned').toLowerCase();
    const goals=s.goals||[],done=goals.filter(g=>g[0]).length;
    const perc=goals.length?Math.round(done/goals.length*100):(status==='done'?100:0);
    const lft=start?Math.max(0,((start-minDate)/span*100)).toFixed(2):0;
    const wid=(start&&end)?Math.max(1,((end-start)/span*100)).toFixed(2):20;
    const lbl=document.createElement('div');lbl.className='label';
    lbl.innerHTML=`<span class="id">${esc(s.id)}</span><span class="ttl">${esc(s.fields.title||'')}</span><span class="dt">${esc(s.fields.start||'?')} → ${esc(s.fields.end||'?')}</span>`;
    lbl.onclick=()=>openSprintModal(s);
    const lane=document.createElement('div');lane.className='lane';
    lane.onclick=()=>openSprintModal(s);
    const bar=document.createElement('div');bar.className='gantt-bar '+status;
    bar.style.left=lft+'%';bar.style.width=wid+'%';
    const barTitle=(s.fields.title||'').split('·')[0].split('—')[0].trim();
    bar.innerHTML=`<span>${esc(status==='cancelled'?'cancelled':barTitle)}</span>`;
    if(status!=='planned'&&status!=='cancelled'){const pEl=document.createElement('span');pEl.className='perc';pEl.textContent=perc+'%';bar.appendChild(pEl);}
    lane.appendChild(bar);
    if(now>=minDate&&now<=maxDate){const nl=document.createElement('div');nl.className='now-line';nl.style.left=nowPct+'%';lane.appendChild(nl);}
    ganttEl.appendChild(lbl);ganttEl.appendChild(lane);
  });
  // View toggle (cosmetic — same data, just label)
  document.querySelectorAll('[data-view]').forEach(btn=>{
    btn.onclick=()=>{document.querySelectorAll('[data-view]').forEach(b=>b.classList.toggle('active',b===btn));};
  });
})();

// ── Graph ─────────────────────────────────────────────────────
let graphInited=false;
function initGraph(){
  if(graphInited)return;graphInited=true;
  const graph=DATA.graph||{},nodes=graph.nodes||[],edges=graph.edges||[];
  const W=720,H=540,svg=document.getElementById('graph-svg');
  if(!nodes.length){svg.innerHTML='<text x="360" y="280" text-anchor="middle" fill="var(--muted)" font-family="var(--font-mono)" font-size="13">그래프 데이터 없음</text>';return;}
  const KIND_COLOR={meta:'oklch(0.78 0.05 75)',guides:'oklch(0.78 0.13 155)',planning:'oklch(0.74 0.17 25)',dev:'oklch(0.78 0.14 60)',resources:'oklch(0.75 0.11 240)',tools:'oklch(0.72 0.13 300)','root-doc':'oklch(0.78 0.05 75)','live-state':'oklch(0.78 0.10 75)',guide:'oklch(0.78 0.13 155)'};
  const catColors={};(graph.categories||[]).forEach(c=>catColors[c.id]=c.color||'#888');
  function nodeColor(n){return KIND_COLOR[n.kind]||KIND_COLOR[n.category]||catColors[n.category]||'oklch(0.60 0.02 75)';}
  // Force-directed layout: repulsion + edge springs + categorical anchor gravity
  const CATS=['meta','guides','planning','dev','resources'];
  const posMap=new Map();
  const bucketSizeMap=new Map(); // nodeId → same-anchor-bucket size (for label toggle)
  (function(){
    const nodeById=new Map(nodes.map(n=>[n.id,n]));
    const edgePairs=edges.map(e=>[nodeById.get(e.from||e.source),nodeById.get(e.to||e.target)]).filter(([a,b])=>a&&b);
    // Anchor: categorical home position (category→x column, tier→y row)
    const anchors=new Map();
    nodes.forEach(n=>{
      const ci=CATS.indexOf(n.category);
      anchors.set(n.id,{
        x:ci>=0?(ci+0.5)/CATS.length*(W-60)+30:W/2,
        y:n.tier!=null?(n.tier+0.5)/7*(H-60)+30:H/2
      });
    });
    // Track bucket size (same anchor) for label visibility
    const bmap=new Map();
    nodes.forEach(n=>{
      const a=anchors.get(n.id);
      const k=`${Math.round(a.x)},${Math.round(a.y)}`;
      bmap.set(k,(bmap.get(k)||0)+1);
    });
    nodes.forEach(n=>{
      const a=anchors.get(n.id);
      const k=`${Math.round(a.x)},${Math.round(a.y)}`;
      bucketSizeMap.set(n.id,bmap.get(k)||1);
    });
    // Initial positions: anchor + small deterministic offset to break symmetry
    const vels=new Map();
    nodes.forEach((n,i)=>{
      const a=anchors.get(n.id);
      posMap.set(n.id,{x:a.x+(i%7-3)*12,y:a.y+(Math.floor(i/7)%5-2)*10});
      vels.set(n.id,{x:0,y:0});
    });
    // Simulation constants
    const REPULSE=4800,SPRING_K=0.055,REST=95,ANCHOR_K=0.038,DAMP=0.78,PAD=32;
    for(let iter=0;iter<280;iter++){
      const cool=Math.max(0.18,1-iter/320);
      // Node-node repulsion
      for(let i=0;i<nodes.length;i++){
        for(let j=i+1;j<nodes.length;j++){
          const pi=posMap.get(nodes[i].id),pj=posMap.get(nodes[j].id);
          const dx=pj.x-pi.x,dy=pj.y-pi.y;
          const d2=(dx*dx+dy*dy)||0.01,d=Math.sqrt(d2);
          const f=REPULSE*cool/d2,nx=dx/d,ny=dy/d;
          const vi=vels.get(nodes[i].id),vj=vels.get(nodes[j].id);
          vi.x-=nx*f;vi.y-=ny*f;vj.x+=nx*f;vj.y+=ny*f;
        }
      }
      // Edge spring attraction
      edgePairs.forEach(([na,nb])=>{
        const pa=posMap.get(na.id),pb=posMap.get(nb.id);
        const dx=pb.x-pa.x,dy=pb.y-pa.y;
        const d=Math.sqrt(dx*dx+dy*dy)||0.1;
        const f=SPRING_K*(d-REST),nx=dx/d,ny=dy/d;
        vels.get(na.id).x+=nx*f;vels.get(na.id).y+=ny*f;
        vels.get(nb.id).x-=nx*f;vels.get(nb.id).y-=ny*f;
      });
      // Anchor gravity (keeps nodes near their categorical home)
      nodes.forEach(n=>{
        const p=posMap.get(n.id),a=anchors.get(n.id),v=vels.get(n.id);
        v.x+=(a.x-p.x)*ANCHOR_K;v.y+=(a.y-p.y)*ANCHOR_K;
      });
      // Integrate + dampen + boundary clamp
      nodes.forEach(n=>{
        const p=posMap.get(n.id),v=vels.get(n.id);
        v.x*=DAMP;v.y*=DAMP;
        p.x=Math.max(PAD,Math.min(W-PAD,p.x+v.x));
        p.y=Math.max(PAD,Math.min(H-PAD,p.y+v.y));
      });
    }
  })();
  function nodePos(n){return posMap.get(n.id)||{x:W/2,y:H/2};}
  let selId=nodes[0].id;
  function render(){
    svg.innerHTML=`<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="var(--text-dim)"/></marker><marker id="arr-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="var(--accent)"/></marker></defs>`;
    edges.forEach(e=>{
      const na=nodes.find(n=>n.id===(e.from||e.source)),nb=nodes.find(n=>n.id===(e.to||e.target));
      if(!na||!nb)return;
      const pa=nodePos(na),pb=nodePos(nb),active=na.id===selId||nb.id===selId;
      const line=document.createElementNS('http://www.w3.org/2000/svg','line');
      line.setAttribute('x1',pa.x);line.setAttribute('y1',pa.y);line.setAttribute('x2',pb.x);line.setAttribute('y2',pb.y);
      line.setAttribute('stroke',active?'var(--accent)':'var(--text-dim)');
      line.setAttribute('stroke-width',active?1.8:1.2);
      if(!active)line.setAttribute('stroke-dasharray','2 5');
      line.setAttribute('stroke-linecap','round');
      line.setAttribute('marker-end',active?'url(#arr-a)':'url(#arr)');
      line.setAttribute('opacity',active?1:0.55);
      svg.appendChild(line);
    });
    nodes.forEach(n=>{
      const p=nodePos(n),active=n.id===selId,color=nodeColor(n);
      const g=document.createElementNS('http://www.w3.org/2000/svg','g');
      g.style.cursor='pointer';
      const c=document.createElementNS('http://www.w3.org/2000/svg','circle');
      c.setAttribute('cx',p.x);c.setAttribute('cy',p.y);c.setAttribute('r',active?16:11);
      c.setAttribute('fill',active?color:'var(--surface-2)');c.setAttribute('stroke',color);c.setAttribute('stroke-width',active?3:1.5);
      // Show label only for selected node or singleton buckets (avoids text-collision in dense clusters)
      const showLabel=active||(bucketSizeMap.get(n.id)||1)===1;
      if(showLabel){
        const label=n.label||n.id;
        const tx=document.createElementNS('http://www.w3.org/2000/svg','text');
        tx.setAttribute('x',p.x);tx.setAttribute('y',p.y+(active?28:24));tx.setAttribute('text-anchor','middle');
        tx.setAttribute('font-family','var(--font-mono)');tx.setAttribute('font-size','9');
        tx.setAttribute('fill',active?'var(--text)':'var(--text-dim)');
        tx.textContent=label.length>16?label.slice(0,15)+'…':label;
        g.appendChild(tx);
      }
      g.appendChild(c);
      g.onclick=()=>{selId=n.id;render();updateDetail(n);};
      svg.appendChild(g);
    });
  }
  function updateDetail(n){
    const detail=document.getElementById('graph-detail');
    const connEdges=edges.filter(e=>(e.from||e.source)===n.id||(e.to||e.target)===n.id).map(e=>({other:(e.from||e.source)===n.id?(e.to||e.target):(e.from||e.source),kind:e.kind||e.relationship||'',dir:(e.from||e.source)===n.id?'→':'←'}));
    const nc=DATA.node_contents&&DATA.node_contents[n.id];
    detail.innerHTML=`<span class="eyebrow">${esc(n.category||n.kind||'')} / selected</span>
      <h4 style="margin:8px 0 6px">${esc(n.label||n.id)}</h4>
      <div class="path">${esc(n.path||'')}</div>
      <p>${esc(n.role||n.description||'')}</p>
      ${connEdges.length?`<div class="conn-block"><span class="eyebrow">Connections · ${connEdges.length}</span><ul>${connEdges.map(e=>`<li><span class="ek">${esc(e.dir)} ${esc(e.kind)}</span><span class="mono" style="color:var(--text)">${esc(e.other)}</span></li>`).join('')}</ul></div>`:''}
      ${nc&&nc.kind==='file'?`<div class="conn-block"><span class="eyebrow">File · ${nc.size} chars</span><div class="file-body" style="margin-top:8px;max-height:200px;font-size:11px">${esc((nc.text||'').slice(0,600))}${nc.size>600?'…':''}</div></div>`:''}`;
  }
  // Legend
  const cats=[...new Set(nodes.map(n=>n.category||n.kind).filter(Boolean))];
  const lg=document.getElementById('graph-legend-bottom');
  if(lg)lg.innerHTML=cats.slice(0,8).map(c=>`<span><span class="lg-dot" style="background:${KIND_COLOR[c]||catColors[c]||'#888'}"></span>${c}</span>`).join('');
  render();updateDetail(nodes[0]);
}

// ── Guide / Whitepaper ────────────────────────────────────────
(function(){
  document.getElementById('guide-content').innerHTML=`
    <div class="section-head" style="margin-top:0">
      <h2>방법론 <em>백서</em>.</h2>
      <span style="font-family:var(--font-mono);font-size:11px;color:var(--muted);letter-spacing:.14em;text-transform:uppercase">v3.2 · Evidence-Driven AI Development</span>
    </div>
    <div class="row2">
      <div class="card">
        <div class="card-head"><h3><em>5</em> 영역 설계</h3><span class="meta">zones</span></div>
        <ul class="kv">
          <li><span class="k">메타</span><span class="v"><span class="mono">(root)</span> · CLAUDE / AGENTS / HANDOFF / TODO</span></li>
          <li><span class="k">지침서</span><span class="v"><span class="mono">20_guides/</span> · 어떻게 쓰는가 (00–18)</span></li>
          <li><span class="k">기획 산출물</span><span class="v"><span class="mono">30_planning/</span> · 무엇을 만드는가</span></li>
          <li><span class="k">개발 산출물</span><span class="v"><span class="mono">40_dev/</span> · MASTER_PLAN / SPRINTS / ADR</span></li>
          <li><span class="k">재사용 자원</span><span class="v"><span class="mono">50_resources/</span> · templates / prompts</span></li>
        </ul>
      </div>
      <div class="card">
        <div class="card-head"><h3>핵심 <em>원칙</em></h3><span class="meta">principles</span></div>
        <ul class="kv">
          <li><span class="k">Eval-First</span><span class="v">작성보다 평가 정의를 먼저</span></li>
          <li><span class="k">Harness 분리</span><span class="v">Plan / Generate / Evaluate 를 같은 세션에 묶지 않음</span></li>
          <li><span class="k">Guardrails</span><span class="v">프롬프트가 아닌 시스템 컴포넌트로 강제</span></li>
          <li><span class="k">사람-AI 공용</span><span class="v">자연어 + 기계 판독</span></li>
          <li><span class="k">단일 출처</span><span class="v">모든 정보는 정확히 한 군데에서만 산다</span></li>
        </ul>
      </div>
    </div>
    <div class="row2">
      <div class="card">
        <div class="card-head"><h3>변경 <em>등급</em></h3><span class="meta">change class</span></div>
        <ul class="kv">
          <li><span class="k" style="color:var(--ok)">Class A</span><span class="v">일반 기능 · UI 카피 · 내부 리팩토링 — 게이트: 머지된 PR</span></li>
          <li><span class="k" style="color:var(--warn)">Class B</span><span class="v">스키마 · auth · 외부 계약 · destructive — 영향·롤백 명시 의무</span></li>
          <li><span class="k" style="color:var(--danger)">Class C</span><span class="v">가격 · 법무 · 브랜드 · 공개 출시 — 명시적 휴먼 승인 + ADR</span></li>
        </ul>
      </div>
      <div class="card">
        <div class="card-head"><h3>Sync <em>정책</em></h3><span class="meta">file class</span></div>
        <ul class="kv">
          <li><span class="k">shared</span><span class="v"><span class="mono">20_guides/</span>, <span class="mono">50_resources/</span> — sync가 항상 덮어씀</span></li>
          <li><span class="k">managed</span><span class="v">CLAUDE / AGENTS — 마커 사이만 머지</span></li>
          <li><span class="k">scaffolds</span><span class="v"><span class="mono">30_planning/</span>, <span class="mono">40_dev/</span> — init 1회, sync 무시</span></li>
          <li><span class="k">local</span><span class="v">HANDOFF · TODO · MASTER_PLAN · ADR — 절대 안 건드림</span></li>
        </ul>
      </div>
    </div>`;
})();

// ── Modal ─────────────────────────────────────────────────────
function openModal(eyebrow,title,bodyHtml){
  document.getElementById('modal-eyebrow').textContent=eyebrow;
  document.getElementById('modal-title').textContent=title;
  document.getElementById('modal-body').innerHTML=bodyHtml;
  const overlay=document.getElementById('modal-overlay');
  overlay.style.display='';
  document.body.style.overflow='hidden';
  const onEsc=e=>{if(e.key==='Escape')closeModal();};
  window.addEventListener('keydown',onEsc);
  overlay._removeEsc=()=>window.removeEventListener('keydown',onEsc);
}
function closeModal(){
  const overlay=document.getElementById('modal-overlay');
  overlay.style.display='none';
  document.body.style.overflow='';
  if(overlay._removeEsc){overlay._removeEsc();overlay._removeEsc=null;}
}

function openSprintModal(s){
  const goals=s.goals||[],done=goals.filter(g=>g[0]).length;
  const status=(s.fields.status||'planned').toLowerCase();
  const stCls={done:'ok',active:'accent',planned:'warn',cancelled:'danger'}[status]||'';
  const perc=goals.length?Math.round(done/goals.length*100):(status==='done'?100:0);
  const todoIds=(s.fields['todo-ids']||'').replace(/[\[\]]/g,'').split(/[,\s]+/).filter(x=>x&&x!=='—');
  const allCards=Object.entries(DATA.kanban||{}).flatMap(([sec,cards])=>cards.map(c=>({...c,_sec:sec})));
  const relTodos=todoIds.map(tid=>allCards.find(c=>c.id===tid)).filter(Boolean);
  const body=`
    <div class="section">
      <div class="tag-row" style="margin-bottom:14px">
        <span class="tg ${stCls}">${status}</span>
        ${s.fields.cadence?`<span class="tg">${esc(s.fields.cadence)}</span>`:''}
        ${s.fields.owner?`<span class="tg">${esc(s.fields.owner)}</span>`:''}
        ${perc>0&&perc<100?`<span class="tg accent">${perc}% complete</span>`:''}
      </div>
      <p class="modal-prose">${esc(s.fields.notes||s.fields.title||'')}</p>
    </div>
    <div class="section">
      <span class="eyebrow">Meta</span>
      <div class="meta-grid">
        <div class="cell"><div class="l">Start</div><div class="v">${esc(s.fields.start||'—')}</div></div>
        <div class="cell"><div class="l">End</div><div class="v">${esc(s.fields.end||'—')}</div></div>
        <div class="cell"><div class="l">Cadence</div><div class="v">${esc(s.fields.cadence||'—')}</div></div>
        <div class="cell"><div class="l">Owner</div><div class="v">${esc(s.fields.owner||'—')}</div></div>
      </div>
    </div>
    ${goals.length?`<div class="section"><span class="eyebrow">Goals · ${done}/${goals.length}</span><ul class="checklist">${goals.map(g=>`<li class="${g[0]?'done':''}"><span class="box">${g[0]?'&#x2713;':''}</span><span class="t">${esc(g[1])}</span></li>`).join('')}</ul></div>`:''}
    <div class="section"><span class="eyebrow">Gate</span><p class="modal-prose">${esc(s.fields.gate||'—')}</p></div>
    ${relTodos.length?`<div class="section"><span class="eyebrow">Related TODOs · ${relTodos.length}</span><ul class="rel-list">${relTodos.map(c=>{const col=KANBAN_MAP.find(k=>k.sec===c._sec);return `<li onclick="openTodoModal(window._findCard('${esc(c.id)}'),KANBAN_MAP.find(k=>k.sec==='${c._sec}'))" style="cursor:pointer"><span class="rid">${esc(c.id)}</span><span class="rttl">${esc(c.fields.title||c.id)}</span><span class="rpri">[${esc(c.fields['change-class']||'—')}]</span></li>`;}).join('')}</ul></div>`:''}`;
  openModal(`Sprint · ${s.id}`,s.fields.title||s.id,body);
}
window._findCard=function(id){const all=Object.entries(DATA.kanban||{}).flatMap(([sec,cards])=>cards.map(c=>({...c,_sec:sec})));return all.find(c=>c.id===id)||{id,fields:{},criteria:[],_sec:'Backlog'};};

function openTodoModal(card,colData){
  if(!card)return;
  const acc=card.criteria||[],doneAcc=acc.filter(a=>a[0]).length;
  const cls=(card.fields['change-class']||'').replace(/\s/g,'').toUpperCase();
  const priCss={A:'ok',B:'warn',C:'danger'}[cls]||'';
  const colId=colData&&colData.id||'';const colTitle=colData&&colData.title||'';
  const sprintId=card.fields.sprint||'';
  const sprint=(DATA.sprints||[]).find(s=>s.id===sprintId);
  const body=`
    <div class="section">
      <div class="tag-row" style="margin-bottom:14px">
        ${cls?`<span class="tg ${priCss}">Priority [${esc(cls)}]</span>`:''}
        ${colTitle?`<span class="tg ${colId==='now'?'accent':''}">${esc(colTitle)}</span>`:''}
        ${sprintId?`<span class="tg">${esc(sprintId)}</span>`:''}
        ${card.fields.owner?`<span class="tg">${esc(card.fields.owner)}</span>`:''}
      </div>
      <p class="modal-prose">${esc(card.fields.notes||card.fields.title||card.id)}</p>
    </div>
    <div class="section">
      <span class="eyebrow">Meta</span>
      <div class="meta-grid">
        <div class="cell"><div class="l">ID</div><div class="v">${esc(card.id)}</div></div>
        <div class="cell"><div class="l">Mode</div><div class="v">${esc(card.fields.mode||'—')}</div></div>
        <div class="cell"><div class="l">Sprint</div><div class="v">${esc(sprintId||'—')}</div></div>
        <div class="cell"><div class="l">Owner</div><div class="v">${esc(card.fields.owner||'—')}</div></div>
      </div>
    </div>
    ${acc.length?`<div class="section"><span class="eyebrow">Acceptance criteria · ${doneAcc}/${acc.length}</span><div class="mini-bar ${doneAcc===acc.length?'done':''}" style="margin-bottom:14px"><div style="width:${acc.length?doneAcc/acc.length*100:0}%"></div></div><ul class="checklist">${acc.map(a=>`<li class="${a[0]?'done':''}"><span class="box">${a[0]?'&#x2713;':''}</span><span class="t">${esc(a[1])}</span></li>`).join('')}</ul></div>`:''}
    ${sprint?`<div class="section"><span class="eyebrow">Sprint</span><ul class="rel-list"><li onclick="openSprintModal(window._findSprint('${esc(sprint.id)}'))" style="cursor:pointer"><span class="rid">${esc(sprint.id)}</span><span class="rttl">${esc(sprint.fields.title||sprint.id)}</span><span class="rpri">${esc(sprint.fields.status||'—')}</span></li></ul></div>`:''}`;
  openModal(`TODO · ${card.id}`,card.fields.title||card.id,body);
}
window._findSprint=function(id){return(DATA.sprints||[]).find(s=>s.id===id)||{id,fields:{},goals:[]};};

// ── Exec view ─────────────────────────────────────────────────
function renderExec(){
  if(window._execRendered)return;window._execRendered=true;
  document.getElementById('exec-stat-row').innerHTML=buildStatHtml();
  const ov=DATA.project_overview||{};
  const handoff=ov.handoff_md||'';
  const recentLines=handoff.split('\n').filter(l=>/^\d{4}-\d{2}-\d{2}/.test(l)).slice(0,5);
  document.getElementById('exec-row').innerHTML=`
    <div class="card">
      <div class="card-head"><h3>최근 <em>활동</em></h3><span class="meta">HANDOFF.md</span></div>
      <ul class="kv">${recentLines.map(l=>{const m=l.match(/^(\d{4}-\d{2}-\d{2})[\s—\-]*(.*)$/);return m?`<li><span class="k">${esc(m[1])}</span><span class="v">${renderInline(esc(m[2]))}</span></li>`:''}).join('')||'<li><span class="k" style="color:var(--muted)">없음</span><span class="v"></span></li>'}</ul>
    </div>
    <div class="card">
      <div class="card-head"><h3>칸반 <em>요약</em></h3><span class="meta">kanban · all columns</span></div>
      <ul class="kv">${KANBAN_MAP.map(col=>`<li><span class="k">${col.title}</span><span class="v"><strong>${(DATA.kanban[col.sec]||[]).length}</strong> · ${col.hint}</span></li>`).join('')}</ul>
    </div>`;
  document.getElementById('exec-dashboards').innerHTML=`
    <div class="card">
      <div class="card-head"><h3>로컬 <em>대시보드</em></h3><span class="meta">~/.methodology-dashboards.json</span></div>
      <table class="tbl" id="exec-dashboards-table"><thead><tr><th>Port</th><th>Project</th><th>Branch</th><th>Commit</th><th>Started</th><th></th></tr></thead><tbody><tr><td colspan="6" style="padding:14px;color:var(--muted)">Loading…</td></tr></tbody></table>
    </div>`;
  document.getElementById('exec-branches').innerHTML=`
    <div class="card">
      <div class="card-head"><h3>브랜치 · <em>worktree</em></h3><span class="meta">git branches</span></div>
      <div id="exec-branches-list" style="color:var(--muted);font-size:13px;padding:8px 0">Loading…</div>
    </div>`;
  dashboardsRefresh();branchesRefresh();
}

// ── Dev Servers API ───────────────────────────────────────────
const devApi={
  list:async()=>(await fetch('/api/servers')).json(),
  start:async(cwd,cmd)=>{const r=await fetch('/api/servers/start',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({cwd,cmd})});return{ok:r.ok,body:await r.json()};},
  stop:async(pid)=>{const r=await fetch(`/api/servers/${pid}/stop`,{method:'POST'});return{ok:r.ok,body:await r.json()};},
  killRange:async(from,to)=>{const r=await fetch('/api/servers/kill-range',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({from,to})});return{ok:r.ok,body:await r.json()};},
};
const devStatus=document.getElementById('dev-servers-status');
const devTbody=document.querySelector('#dev-servers-table tbody');
const devCwdInput=document.getElementById('dev-cwd');
if(devCwdInput&&DATA.root)devCwdInput.placeholder=`cwd (기본: ${DATA.root})`;
async function devRefresh(){
  try{
    const{servers}=await devApi.list();
    devTbody.innerHTML='';
    if(!servers||!servers.length){devTbody.innerHTML='<tr><td colspan="6" style="padding:14px;color:var(--muted)">추적 중인 서버 없음</td></tr>';}
    else{
      for(const s of servers){
        const tr=document.createElement('tr');
        tr.innerHTML=`<td><a href="http://localhost:${s.port}" target="_blank" class="port">${s.port} ↗</a></td><td class="mono">${s.pid}</td><td class="mono" style="font-size:11px">${esc(s.cwd||'')}</td><td class="mono" style="font-size:11px">${esc((s.cmd||[]).join(' '))}</td><td class="mono">${s.started_at||''}</td><td><button data-pid="${s.pid}" class="dev-stop-btn btn btn-danger">Stop</button></td>`;
        devTbody.appendChild(tr);
      }
      devTbody.querySelectorAll('.dev-stop-btn').forEach(b=>{b.onclick=async e=>{const pid=e.target.dataset.pid;e.target.disabled=true;e.target.textContent='Stopping…';const{ok,body}=await devApi.stop(pid);if(!ok)alert(`stop 실패: ${body.error||'unknown'}`);devRefresh();};});
    }
    devStatus.textContent=`${(servers||[]).length}개 추적 중 · ${new Date().toLocaleTimeString()}`;
  }catch(e){devStatus.textContent=`갱신 실패: ${e.message}`;}
}
document.getElementById('dev-start').onclick=async()=>{
  const cwd=devCwdInput.value.trim()||DATA.root;
  const cmd=document.getElementById('dev-cmd').value.trim()||'pnpm dev';
  devStatus.textContent=`Starting ${cmd} in ${cwd} ...`;
  const{ok,body}=await devApi.start(cwd,cmd);
  if(!ok){devStatus.textContent=`start 실패: ${body.error||'unknown'}`;alert(`start 실패: ${body.error||'unknown'}`);return;}
  devStatus.textContent=`Started PID ${body.pid} on port ${body.port}`;devRefresh();
};
document.getElementById('dev-kill-all').onclick=async()=>{
  if(!confirm('포트 3000-3099 의 모든 LISTEN 프로세스를 종료합니다. 진행할까요?'))return;
  devStatus.textContent='Killing 3000-3099 ...';
  const{ok,body}=await devApi.killRange(3000,3099);
  if(!ok){alert(`kill 실패: ${body.error}`);return;}
  devStatus.textContent=`${(body.killed||[]).length}개 프로세스 종료`;devRefresh();
};
document.getElementById('dev-refresh').onclick=devRefresh;
devRefresh();setInterval(devRefresh,5000);

// ── Dashboards API ────────────────────────────────────────────
const dashApi={
  list:async()=>(await fetch('/api/dashboards')).json(),
  stop:async(port)=>{const r=await fetch('/api/dashboard/stop',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({port})});return{ok:r.ok,body:await r.json()};},
};
async function dashboardsRefresh(){
  try{
    const{dashboards}=await dashApi.list();
    function renderTbody(tbodyEl){
      tbodyEl.innerHTML='';
      if(!dashboards||!dashboards.length){tbodyEl.innerHTML='<tr><td colspan="6" style="padding:14px;color:var(--muted)">등록된 dashboard 없음</td></tr>';return;}
      for(const d of dashboards){
        const tr=document.createElement('tr');
        const isCurrent=d.root===DATA.root&&d.branch===(DATA.git_branch||'');
        const projName=(d.root||'').split('/').pop()||'?';
        tr.innerHTML=`<td><a href="http://localhost:${d.port}" target="_blank" class="port">${d.port} ↗</a>${isCurrent?'<span style="font-size:10px;color:var(--accent);margin-left:4px">← THIS</span>':''}</td><td>${esc(projName)}</td><td class="mono">${esc(d.branch||'?')}</td><td class="mono">${esc(d.commit||'?')}</td><td class="mono">${esc(d.started_at||'')}</td><td><button data-port="${d.port}" class="dash-stop-btn btn btn-danger">Stop</button></td>`;
        tbodyEl.appendChild(tr);
      }
      tbodyEl.querySelectorAll('.dash-stop-btn').forEach(b=>{b.onclick=async e=>{const port=parseInt(e.target.dataset.port);if(!confirm(`포트 ${port} dashboard를 종료할까요?`))return;e.target.disabled=true;e.target.textContent='Stopping…';const{ok,body}=await dashApi.stop(port);if(!ok)alert(`stop 실패: ${body.error||'unknown'}`);dashboardsRefresh();};});
    }
    const t1=document.querySelector('#dashboards-table tbody');if(t1)renderTbody(t1);
    const t2=document.querySelector('#exec-dashboards-table tbody');if(t2)renderTbody(t2);
    const ds=document.getElementById('dashboards-status');if(ds)ds.textContent=`${(dashboards||[]).length}개 · ${new Date().toLocaleTimeString()}`;
  }catch(e){
    const t1=document.querySelector('#dashboards-table tbody');
    if(t1)t1.innerHTML=`<tr><td colspan="6" style="color:var(--danger);padding:14px">갱신 실패: ${esc(e.message)}</td></tr>`;
  }
}
document.getElementById('dashboards-refresh').onclick=dashboardsRefresh;
dashboardsRefresh();setInterval(dashboardsRefresh,5000);

// ── Branches API ──────────────────────────────────────────────
const branchApi={
  list:async()=>(await fetch('/api/branches')).json(),
  spawn:async(branch)=>{const r=await fetch('/api/dashboard/spawn',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({branch})});return{ok:r.ok,body:await r.json()};},
};
const branchesList=document.getElementById('branches-list');
const branchesStatus=document.getElementById('branches-status');
async function branchesRefresh(){
  branchesStatus.textContent='Loading…';
  try{
    const{current,branches}=await branchApi.list();
    if(!branches||!branches.length){branchesList.innerHTML='<span style="color:var(--muted);font-size:12px">git 브랜치 미발견</span>';branchesStatus.textContent='';return;}
    branchesList.innerHTML='';
    for(const b of branches){
      const id='br_'+b.replace(/[^a-zA-Z0-9]/g,'_');
      const lbl=document.createElement('label');
      lbl.style.cssText='display:flex;gap:8px;align-items:center;cursor:pointer;font-size:13px;padding:4px 6px;';
      lbl.innerHTML=`<input type="radio" name="branch-select" value="${esc(b)}" id="${id}"${b===current?' checked':''} style="accent-color:var(--accent)"/><code style="flex:1;font-family:var(--font-mono);font-size:12px;color:${b===current?'var(--accent)':'var(--text)'}">${esc(b)}</code>${b===current?'<span style="font-family:var(--font-mono);font-size:10px;color:var(--ok);letter-spacing:.14em">CURRENT</span>':''}`;
      branchesList.appendChild(lbl);
    }
    // Also update exec branches if rendered
    const execBr=document.getElementById('exec-branches-list');
    if(execBr)execBr.innerHTML=branchesList.innerHTML;
    branchesStatus.textContent=`${branches.length}개 브랜치 (current: ${current||'?'})`;
  }catch(e){branchesList.innerHTML=`<span style="color:var(--danger)">로드 실패: ${esc(e.message)}</span>`;branchesStatus.textContent='';}
}
document.getElementById('branches-refresh').onclick=branchesRefresh;
document.getElementById('branches-spawn').onclick=async()=>{
  const selected=document.querySelector('input[name="branch-select"]:checked');
  if(!selected){alert('브랜치를 선택하세요.');return;}
  const branch=selected.value;
  branchesStatus.textContent=`Spawning dashboard for ${branch} ...`;
  const{ok,body}=await branchApi.spawn(branch);
  if(!ok){alert(`spawn 실패: ${body.error||'unknown'}\n\n${body.output||''}`);branchesStatus.textContent=`spawn 실패: ${body.error}`;return;}
  branchesStatus.textContent=`Spawned: ${body.url}`;
  window.open(body.url,'_blank');dashboardsRefresh();
};
branchesRefresh();
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
        _serve_with_api(out, args.port)

    return 0


# ───────────────────────────────────────────────────────────────────────
# Dev-server 제어 API + 정적 파일 서빙
# ───────────────────────────────────────────────────────────────────────

_servers_lock = __import__("threading").Lock()
_servers: dict[int, dict] = {}  # pid -> {pid, port, cwd, cmd, started_at}


def _find_free_port(start: int = 3000, end: int = 3099) -> int | None:
    import socket
    for p in range(start, end + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.1)
            try:
                s.bind(("127.0.0.1", p))
                return p
            except OSError:
                continue
    return None


def _kill_port(port: int) -> list[int]:
    """해당 포트 점유 프로세스 PID 들을 SIGTERM. 반환: 죽인 PID 목록."""
    import signal
    killed: list[int] = []
    try:
        out = subprocess.check_output(
            ["lsof", "-ti", f":{port}", "-sTCP:LISTEN"],
            text=True, stderr=subprocess.DEVNULL,
        ).strip()
    except subprocess.CalledProcessError:
        return killed
    for pid_str in out.splitlines():
        try:
            pid = int(pid_str.strip())
            os.kill(pid, signal.SIGTERM)
            killed.append(pid)
        except (ValueError, ProcessLookupError, PermissionError):
            pass
    return killed


def _serve_with_api(out: Path, start_port: int) -> None:
    import http.server
    import json as _json
    import signal as _signal
    import socketserver
    import urllib.parse

    os.chdir(out.parent)

    class Handler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, fmt, *args):
            # 노이즈 줄이기
            return

        def _send_json(self, status: int, payload: dict) -> None:
            body = _json.dumps(payload).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):
            # 루트 요청을 dashboard.html 로 자동 rewrite (디렉터리 listing 회피)
            # urllib.parse 가 ? 쿼리스트링 분리하므로 self.path 직접 비교
            if self.path == "/" or self.path == "" or self.path.startswith("/?"):
                self.path = "/dashboard.html" + self.path[1:]
            parsed = urllib.parse.urlparse(self.path)
            if parsed.path == "/api/servers":
                with _servers_lock:
                    # 죽은 프로세스 정리
                    alive: dict[int, dict] = {}
                    for pid, e in _servers.items():
                        try:
                            os.kill(pid, 0)
                            alive[pid] = e
                        except ProcessLookupError:
                            pass
                    _servers.clear()
                    _servers.update(alive)
                    return self._send_json(200, {"servers": list(_servers.values())})

            if parsed.path == "/api/dashboards":
                # ~/.methodology-dashboards.json 레지스트리 + 죽은 항목 정리
                import pathlib as _pl
                reg_file = _pl.Path.home() / ".methodology-dashboards.json"
                entries: list[dict] = []
                if reg_file.exists():
                    try:
                        entries = _json.loads(reg_file.read_text(encoding="utf-8"))
                    except Exception:
                        entries = []
                alive_dash: list[dict] = []
                for e in entries:
                    pid = e.get("pid")
                    if pid:
                        try:
                            os.kill(int(pid), 0)
                            alive_dash.append(e)
                        except (ProcessLookupError, ValueError, PermissionError):
                            continue
                    else:
                        alive_dash.append(e)
                if len(alive_dash) != len(entries):
                    try:
                        reg_file.write_text(_json.dumps(alive_dash, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
                    except Exception:
                        pass
                return self._send_json(200, {"dashboards": alive_dash})

            if parsed.path == "/api/branches":
                # 현재 root 의 git branch 목록 (로컬 + 원격)
                root = str(Path.cwd())
                try:
                    out = subprocess.check_output(
                        ["git", "-C", root, "branch", "-a", "--no-color"],
                        text=True, stderr=subprocess.DEVNULL,
                    )
                except Exception:
                    return self._send_json(200, {"current": None, "branches": []})
                current = None
                branches: list[str] = []
                for line in out.splitlines():
                    s = line.strip()
                    if not s:
                        continue
                    is_current = s.startswith("* ")
                    # *  현재 브랜치 / +  다른 worktree 에서 체크아웃 / -- detached HEAD
                    name = re.sub(r"^[*+-]\s+", "", s).strip()
                    # remotes/origin/HEAD -> origin/main 같은 심볼릭 참조 제외
                    if " -> " in name:
                        continue
                    # remotes/ 접두 제거 (선택적 표시용으로 유지)
                    if name.startswith("remotes/"):
                        name = name[len("remotes/"):]
                    if is_current:
                        current = name
                    if name not in branches:
                        branches.append(name)
                return self._send_json(200, {"current": current, "branches": branches})

            return super().do_GET()

        def do_POST(self):
            parsed = urllib.parse.urlparse(self.path)
            length = int(self.headers.get("Content-Length", 0))
            raw = self.rfile.read(length).decode("utf-8") if length else ""
            try:
                payload = _json.loads(raw) if raw else {}
            except _json.JSONDecodeError:
                return self._send_json(400, {"error": "invalid JSON"})

            if parsed.path == "/api/servers/start":
                cwd = payload.get("cwd", "").strip()
                cmd_raw = payload.get("cmd", "pnpm dev")
                cmd = cmd_raw.split() if isinstance(cmd_raw, str) else list(cmd_raw)
                if not cwd or not Path(cwd).is_dir():
                    return self._send_json(400, {"error": f"invalid cwd: {cwd}"})
                port = _find_free_port()
                if port is None:
                    return self._send_json(503, {"error": "포트 3000-3099 모두 점유"})
                env = os.environ.copy()
                env["PORT"] = str(port)
                try:
                    proc = subprocess.Popen(
                        cmd,
                        cwd=cwd,
                        env=env,
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL,
                        start_new_session=True,
                    )
                except FileNotFoundError as e:
                    return self._send_json(500, {"error": f"명령 미발견: {cmd[0]} ({e})"})
                entry = {
                    "pid": proc.pid,
                    "port": port,
                    "cwd": cwd,
                    "cmd": cmd,
                    "started_at": __import__("datetime").datetime.now().isoformat(timespec="seconds"),
                }
                with _servers_lock:
                    _servers[proc.pid] = entry
                return self._send_json(200, entry)

            if parsed.path.startswith("/api/servers/") and parsed.path.endswith("/stop"):
                try:
                    pid = int(parsed.path.split("/")[3])
                except (ValueError, IndexError):
                    return self._send_json(400, {"error": "invalid pid in path"})
                with _servers_lock:
                    entry = _servers.get(pid)
                if not entry:
                    return self._send_json(404, {"error": "추적 안 됨"})
                try:
                    os.killpg(os.getpgid(pid), _signal.SIGTERM)
                except ProcessLookupError:
                    pass
                except Exception as e:
                    return self._send_json(500, {"error": str(e)})
                with _servers_lock:
                    _servers.pop(pid, None)
                return self._send_json(200, {"stopped": pid})

            if parsed.path == "/api/servers/kill-range":
                p_from = int(payload.get("from", 3000))
                p_to = int(payload.get("to", 3099))
                killed_all: list[dict] = []
                for port in range(p_from, p_to + 1):
                    for pid in _kill_port(port):
                        killed_all.append({"pid": pid, "port": port})
                # 추적 dict 정리
                killed_pids = {k["pid"] for k in killed_all}
                with _servers_lock:
                    for pid in list(_servers.keys()):
                        if pid in killed_pids:
                            _servers.pop(pid, None)
                return self._send_json(200, {"killed": killed_all})

            if parsed.path == "/api/dashboard/spawn":
                # body: {"branch": "<name>"} — 그 브랜치 dashboard 를 별도 포트에 spawn
                branch_name = (payload.get("branch") or "").strip()
                if not branch_name:
                    return self._send_json(400, {"error": "branch 필요"})
                root = Path.cwd()
                meth = root / "60_tools" / "methodology.py"
                if not meth.exists():
                    return self._send_json(500, {"error": f"60_tools/methodology.py 미발견 ({meth})"})
                try:
                    out = subprocess.check_output(
                        [sys.executable, str(meth), "dashboard", "--branch", branch_name],
                        cwd=str(root), text=True, stderr=subprocess.STDOUT, timeout=30,
                    )
                except subprocess.CalledProcessError as e:
                    return self._send_json(500, {"error": "spawn 실패", "output": e.output})
                except subprocess.TimeoutExpired:
                    return self._send_json(504, {"error": "spawn 30초 초과"})
                # 출력에서 URL 추출
                m = re.search(r"http://localhost:(\d+)", out)
                if not m:
                    return self._send_json(500, {"error": "URL 미발견", "output": out})
                port = int(m.group(1))
                return self._send_json(200, {"port": port, "url": f"http://localhost:{port}", "branch": branch_name, "output": out})

            if parsed.path == "/api/dashboard/stop":
                # body: {"port": N} — 해당 dashboard 종료 (methodology dashboard stop)
                port = payload.get("port")
                if not port:
                    return self._send_json(400, {"error": "port 필요"})
                root = Path.cwd()
                meth = root / "60_tools" / "methodology.py"
                try:
                    subprocess.check_output(
                        [sys.executable, str(meth), "dashboard", "stop", "--port", str(int(port))],
                        cwd=str(root), text=True, stderr=subprocess.STDOUT, timeout=10,
                    )
                except subprocess.CalledProcessError as e:
                    return self._send_json(500, {"error": "stop 실패", "output": e.output})
                except subprocess.TimeoutExpired:
                    return self._send_json(504, {"error": "stop 10초 초과"})
                return self._send_json(200, {"stopped": int(port)})

            return self._send_json(404, {"error": "unknown endpoint"})

    class Server(socketserver.ThreadingTCPServer):
        allow_reuse_address = True
        daemon_threads = True

    port = start_port
    for _ in range(20):
        try:
            with Server(("127.0.0.1", port), Handler) as httpd:
                print(f"[serve] http://localhost:{port}/{out.name}", file=sys.stderr)
                print(f"[serve] dev-server API: /api/servers (GET/POST start|stop|kill-range)", file=sys.stderr)
                try:
                    httpd.serve_forever()
                except KeyboardInterrupt:
                    print("\n[stop]", file=sys.stderr)
                return
        except OSError as e:
            if e.errno == 48:  # Address already in use
                print(f"[warn] port {port} busy, trying {port+1}", file=sys.stderr)
                port += 1
                continue
            raise


if __name__ == "__main__":
    sys.exit(main())
