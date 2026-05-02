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
    graph_path = root / "docs" / "methodology-graph.json"
    todo_path = root / "TODO.md"
    if not todo_path.exists():
        # 템플릿이 루트에 없으면 템플릿을 미리보기로 사용
        todo_path = root / "docs" / "templates" / "TODO.md"
    sprints_path = root / "SPRINTS.md"
    if not sprints_path.exists():
        sprints_path = root / "docs" / "templates" / "SPRINTS.md"

    handoff_path = root / "HANDOFF.md"
    if not handoff_path.exists():
        handoff_path = root / "docs" / "templates" / "HANDOFF.md"

    claude_path = root / "CLAUDE.md"
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

    return {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "root": str(root),
        "graph": graph,
        "kanban": kanban,
        "sprints": sprints_json,
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
#graph{width:100%;height:640px;background:var(--panel2);border:1px solid var(--line);border-radius:10px}
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
    <div class="muted" style="margin-bottom:8px">노드를 드래그해서 정렬할 수 있습니다. 색상은 문서 유형을 나타냅니다.</div>
    <svg id="graph"></svg>
    <div class="legend" id="graph-legend"></div>
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

// ── 관계 그래프
let graphRendered = false;
function renderGraph(){
  if(graphRendered) return; graphRendered = true;
  const nodes = (DATA.graph.nodes||[]).map(n => ({...n}));
  const links = (DATA.graph.edges||[]).map(e => ({source:e.from, target:e.to, kind:e.kind, label:e.label}));
  const kinds = DATA.graph.kinds || {};

  const svg = d3.select('#graph');
  const w = svg.node().clientWidth, h = 640;
  svg.selectAll('*').remove();

  svg.append('defs').append('marker').attr('id','garr').attr('viewBox','0 -5 10 10')
    .attr('refX',18).attr('refY',0).attr('markerWidth',6).attr('markerHeight',6).attr('orient','auto')
    .append('path').attr('d','M0,-5L10,0L0,5').attr('fill','#475569');

  const sim = d3.forceSimulation(nodes)
    .force('link', d3.forceLink(links).id(d=>d.id).distance(110).strength(0.6))
    .force('charge', d3.forceManyBody().strength(-360))
    .force('center', d3.forceCenter(w/2, h/2))
    .force('collide', d3.forceCollide(38));

  const link = svg.append('g').selectAll('line').data(links).enter().append('line')
    .attr('stroke','#475569').attr('stroke-opacity',.6).attr('stroke-width',1.2)
    .attr('marker-end','url(#garr)');

  const node = svg.append('g').selectAll('g').data(nodes).enter().append('g')
    .call(d3.drag()
      .on('start', (e,d) => { if(!e.active) sim.alphaTarget(.3).restart(); d.fx=d.x; d.fy=d.y; })
      .on('drag',  (e,d) => { d.fx=e.x; d.fy=e.y; })
      .on('end',   (e,d) => { if(!e.active) sim.alphaTarget(0); d.fx=null; d.fy=null; }));

  node.append('circle').attr('r',16).attr('fill', d => kinds[d.kind]?.color || '#64748B')
    .attr('stroke','#0B0F1A').attr('stroke-width',2);
  node.append('text').attr('dy',32).attr('text-anchor','middle').attr('fill','#E5E7EB')
    .attr('font-size',11).text(d => d.label);
  node.append('title').text(d => `${d.label}\n${d.path||''}\n\n${d.role||''}`);

  sim.on('tick', () => {
    link.attr('x1',d=>d.source.x).attr('y1',d=>d.source.y).attr('x2',d=>d.target.x).attr('y2',d=>d.target.y);
    node.attr('transform', d=>`translate(${d.x},${d.y})`);
  });

  document.getElementById('graph-legend').innerHTML = Object.entries(kinds)
    .map(([k,v]) => `<span><span class="dot" style="background:${v.color}"></span>${k}</span>`).join('');
}

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
        with socketserver.TCPServer(("", args.port), handler) as httpd:
            print(f"[serve] http://localhost:{args.port}/{out.name}", file=sys.stderr)
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\n[stop]", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
