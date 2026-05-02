#!/usr/bin/env python3
"""generate-dashboard.py — project dashboard generator v2.

Static mode:
    python3 generate-dashboard.py
    open dashboard.html

Live mode (recommended during work):
    python3 generate-dashboard.py --serve [--port 8765]
    # opens http://localhost:8765, auto-reloads on file changes
"""

import argparse
import http.server
import json
import os
import re
import socketserver
import threading
import time
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Data collection
# ---------------------------------------------------------------------------

PLAN_TYPES = [
    ("business",  "사업기획서"),
    ("service",   "서비스기획서"),
    ("ops",       "운영기획서"),
    ("marketing", "마케팅기획서"),
    ("brand",     "브랜드기획서"),
    ("pm",        "PM기획서"),
]


def read_file(path: str) -> str:
    try:
        return Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def get_project_name() -> str:
    claude_md = read_file("CLAUDE.md")
    m = re.search(r"\*\*Project Name\*\*:\s*(.+)", claude_md)
    if m:
        name = m.group(1).strip()
        if name not in ("[PROJECT_NAME]", ""):
            return name
    return Path.cwd().name


def parse_frontmatter(content: str) -> dict:
    """Parse YAML-like frontmatter block."""
    m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not m:
        return {}
    result = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            result[k.strip()] = v.strip().strip('"').strip("'")
    return result


def get_plan_versions() -> dict:
    """Return {type: [{"version", "date", "status", "path", "supersedes", "trigger"}]}"""
    plans = {}
    for ptype, _ in PLAN_TYPES:
        folder = Path(f"docs/snapshots/plans/{ptype}")
        if not folder.exists():
            plans[ptype] = []
            continue
        versions = []
        for f in sorted(folder.glob("v*.md")):
            if f.name == ".gitkeep":
                continue
            content = f.read_text(encoding="utf-8")
            fm = parse_frontmatter(content)
            first_line = next(
                (l.lstrip("# ").strip() for l in content.splitlines() if l.strip() and not l.startswith("---")),
                f.name,
            )
            versions.append({
                "version": fm.get("version", "?"),
                "date": fm.get("date", ""),
                "status": fm.get("status", "draft"),
                "supersedes": fm.get("supersedes", ""),
                "trigger": fm.get("trigger", ""),
                "adr": fm.get("adr", ""),
                "path": str(f),
                "title": first_line,
                "name": f.name,
            })
        plans[ptype] = sorted(versions, key=lambda x: x["version"])
    return plans


def get_dev_specs() -> list:
    folder = Path("docs/snapshots/dev-specs")
    if not folder.exists():
        return []
    specs = []
    for f in sorted(folder.glob("v*.md")):
        if f.name == ".gitkeep":
            continue
        content = f.read_text(encoding="utf-8")
        fm = parse_frontmatter(content)
        first_line = next(
            (l.lstrip("# ").strip() for l in content.splitlines() if l.strip() and not l.startswith("---")),
            f.name,
        )
        specs.append({
            "version": fm.get("version", "?"),
            "date": fm.get("date", ""),
            "status": fm.get("status", "draft"),
            "path": str(f),
            "title": first_line,
            "name": f.name,
        })
    return sorted(specs, key=lambda x: x["version"])


def get_pending_ideas() -> list:
    folder = Path("briefs/updates")
    if not folder.exists():
        return []
    return [
        {"name": f.name, "path": str(f)}
        for f in sorted(folder.iterdir())
        if f.is_file() and f.name != ".gitkeep"
    ]


def get_briefs() -> list:
    folder = Path("briefs")
    if not folder.exists():
        return []
    return [
        f.name
        for f in sorted(folder.iterdir())
        if f.is_file() and f.name != ".gitkeep"
    ]


def get_adrs() -> list:
    adr_dir = Path("docs/adr")
    if not adr_dir.exists():
        return []
    results = []
    for f in sorted(f for f in adr_dir.glob("*.md") if f.name != ".gitkeep"):
        content = f.read_text(encoding="utf-8")
        first_line = next(
            (l.lstrip("# ").strip() for l in content.splitlines() if l.strip()), f.name
        )
        results.append({"path": str(f), "title": first_line, "name": f.name})
    return results


def get_dependencies() -> dict:
    """Auto-detect dependency manifests."""
    deps = {}
    manifests = {
        "package.json": _parse_package_json,
        "requirements.txt": _parse_requirements_txt,
        "pyproject.toml": _parse_pyproject_toml,
        "Gemfile": _parse_gemfile,
    }
    for filename, parser in manifests.items():
        if Path(filename).exists():
            deps[filename] = parser(filename)
    return deps


def _parse_package_json(path: str) -> list:
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        result = []
        for section in ("dependencies", "devDependencies"):
            for name, ver in (data.get(section) or {}).items():
                result.append({"name": name, "version": ver, "section": section})
        return result
    except Exception:
        return []


def _parse_requirements_txt(path: str) -> list:
    result = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = re.match(r"([A-Za-z0-9_\-]+)\s*([><=!~].+)?", line)
        if m:
            result.append({
                "name": m.group(1),
                "version": (m.group(2) or "").strip(),
                "section": "runtime",
            })
    return result


def _parse_pyproject_toml(path: str) -> list:
    result = []
    content = Path(path).read_text(encoding="utf-8")
    m = re.search(r"\[tool\.poetry\.dependencies\](.*?)(\[|\Z)", content, re.DOTALL)
    if m:
        for line in m.group(1).splitlines():
            line = line.strip()
            if "=" in line and not line.startswith("#"):
                k, _, v = line.partition("=")
                result.append({"name": k.strip(), "version": v.strip().strip('"'), "section": "runtime"})
    return result


def _parse_gemfile(path: str) -> list:
    result = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        m = re.match(r"\s*gem\s+['\"]([^'\"]+)['\"](?:\s*,\s*['\"]([^'\"]+)['\"])?", line)
        if m:
            result.append({"name": m.group(1), "version": m.group(2) or "", "section": "runtime"})
    return result


def detect_phase_state(plans: dict, dev_specs: list, todo: str, handoff: str) -> dict:
    """Detect current project phase for onboarding guide."""
    briefs_files = [f for f in Path("briefs").iterdir() if f.is_file() and f.name != ".gitkeep"] if Path("briefs").exists() else []
    pending = get_pending_ideas()

    # Count plan docs with at least one version
    plans_written = sum(1 for v in plans.values() if v)
    plans_approved = sum(1 for v in plans.values() if v and any(x["status"] == "approved" for x in v))

    has_dev_spec = bool(dev_specs)
    dev_spec_approved = any(s["status"] == "approved" for s in dev_specs) if dev_specs else False
    has_todo_items = bool(re.search(r"### TODO-\d+", todo))
    has_pending_ideas = bool(pending)

    if not briefs_files:
        return {"state": "setup", "label": "Setup", "phase": 0}
    if plans_written == 0:
        return {"state": "phase1_ready", "label": "Phase 1 준비", "phase": 1}
    if plans_written < 6:
        return {"state": "phase1_progress", "label": f"Phase 1 진행 중 ({plans_written}/6)", "phase": 1}
    if plans_approved < 6:
        return {"state": "phase1_review", "label": "Phase 1 검토 대기", "phase": 1}
    if not has_dev_spec:
        return {"state": "phase2_ready", "label": "Phase 2 준비", "phase": 2}
    if not dev_spec_approved:
        return {"state": "phase2_review", "label": "Phase 2 검토 대기", "phase": 2}
    if has_pending_ideas:
        return {"state": "replan", "label": "재기획 트리거 있음", "phase": 3}
    return {"state": "dev", "label": "Phase 3 개발 중", "phase": 3}


def collect_data() -> dict:
    plans = get_plan_versions()
    dev_specs = get_dev_specs()
    todo = read_file("TODO.md")
    handoff = read_file("HANDOFF.md")
    phase_state = detect_phase_state(plans, dev_specs, todo, handoff)

    return {
        "projectName": get_project_name(),
        "generatedAt": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "handoff": handoff,
        "todo": todo,
        "diagram": read_file("DIAGRAM.md"),
        "plans": plans,
        "devSpecs": dev_specs,
        "pendingIdeas": get_pending_ideas(),
        "briefs": get_briefs(),
        "adrs": get_adrs(),
        "dependencies": get_dependencies(),
        "phaseState": phase_state,
        "planTypes": PLAN_TYPES,
    }


# ---------------------------------------------------------------------------
# Guide content (onboarding)
# ---------------------------------------------------------------------------

GUIDE_PROMPTS = {
    "setup": {
        "title": "🚀 시작하기",
        "message": "briefs/ 폴더에 아이디어 노트, PDF, 초안 기획서를 넣어주세요.",
        "prompt": "CLAUDE.md와 HANDOFF.md를 읽고 프로젝트를 초기화해줘.\n\n1. CLAUDE.md와 AGENTS.md의 Project Settings 빈칸을 채워줘.\n2. briefs/ 폴더 안의 파일 목록을 확인하고 어떤 자료가 있는지 요약해줘.\n3. docs/prompts/plan-routing.md를 읽고 Phase 1 기획서 작성 계획을 제안해줘.\n4. HANDOFF.md를 초기화해줘 (현재 상태: Phase 1 준비 중).",
        "action": "AI에 복사해서 보내기",
    },
    "phase1_ready": {
        "title": "📋 Phase 1 시작",
        "message": "briefs/ 자료가 준비됐습니다. 이제 6종 기획서 작성을 시작하세요.",
        "prompt": "CLAUDE.md와 HANDOFF.md를 읽고 briefs/ 폴더의 파일들을 분석해줘.\ndocs/prompts/plan-routing.md의 지침에 따라 기획서 작성 계획을 수립하고\n사업기획서 v1을 먼저 작성해줘.",
        "action": "Phase 1 시작 프롬프트 복사",
    },
    "phase1_progress": {
        "title": "📋 Phase 1 진행 중",
        "message": "6종 기획서를 순서대로 완성하세요. 아래 Phase 1 섹션에서 현황을 확인하세요.",
        "prompt": None,
        "action": None,
    },
    "phase1_review": {
        "title": "🔍 Phase 1 검토 대기",
        "message": "6종 기획서가 모두 작성됐습니다. docs/snapshots/plans/ 에서 각 기획서를 검토하세요.",
        "prompt": "6종 기획서 검토 완료했어. Phase 2 진행해줘.\ndocs/prompts/dev-spec.md의 지침에 따라 개발명세서 v1을 작성해줘.\n승인된 6종 기획서를 모두 참조해서 작성하고,\n각 기능의 Change Class를 판별해줘.\ndocs/snapshots/dev-specs/v1-[오늘날짜].md 에 저장해줘.",
        "action": "Phase 2 승인 + 개발명세서 요청 프롬프트 복사",
    },
    "phase2_ready": {
        "title": "📝 Phase 2 시작",
        "message": "6종 기획서가 승인됐습니다. 개발명세서 작성을 요청하세요.",
        "prompt": "6종 기획서를 바탕으로 docs/prompts/dev-spec.md의 지침에 따라 개발명세서 v1을 작성해줘.\n각 기능의 Change Class를 판별하고 이유를 명시해줘.\ndocs/snapshots/dev-specs/v1-[오늘날짜].md 에 저장해줘.",
        "action": "개발명세서 작성 요청 프롬프트 복사",
    },
    "phase2_review": {
        "title": "🔍 Phase 2 검토 대기",
        "message": "개발명세서가 작성됐습니다. docs/snapshots/dev-specs/ 에서 검토하세요.",
        "prompt": "개발명세서 승인했어. Phase 3 개발 시작해줘.\n승인된 개발명세서를 기반으로 TODO.md를 작업 단위로 분해해줘.\n각 TODO 항목에 Change Class와 acceptance criteria를 넣어줘.\nHANDOFF.md를 'Phase 3 — 개발 진행 중'으로 업데이트해줘.",
        "action": "Phase 3 승인 + 개발 시작 프롬프트 복사",
    },
    "replan": {
        "title": "🔄 재기획 트리거 감지",
        "message": "briefs/updates/ 에 새 파일이 있습니다. 변경 영향 분석을 요청하세요.",
        "prompt": "briefs/updates/ 에 새 파일을 추가했어.\ndocs/prompts/re-plan.md의 지침에 따라 변경 영향을 분석해줘.\n어떤 기획서가 업데이트 필요한지 먼저 알려줘. 구현은 확인 후 진행해.",
        "action": "재기획 영향 분석 프롬프트 복사",
    },
    "dev": {
        "title": "⚙️ Phase 3 개발 중",
        "message": "개발이 진행 중입니다. TODO 백로그를 확인하고 작업하세요.",
        "prompt": None,
        "action": None,
    },
}

GLOSSARY = {
    "Change Class": "변경 영향도. A=일반 구현, B=기술적 영향 큰 변경 (DB·인증·외부 API 등), C=대외 영향 (가격·법무·브랜드·공개 릴리스)",
    "Phase": "briefs → 6종 기획서(1) → 개발명세서(2) → 개발(3)의 4단계 진행 흐름",
    "Snapshot": "날짜가 찍힌 산출물. 현재 진실의 출처가 아님. 절대 live source로 취급하지 않음",
    "ADR": "Architecture Decision Record. 코드만 봐서는 이유를 알 수 없는 중요한 결정을 기록하는 문서",
    "HANDOFF": "지금 이 순간의 상태만 담는 살아있는 파일. 항상 150줄 이하로 유지",
    "Gate": "사람의 명시적 승인이 있어야만 다음 단계로 진행할 수 있는 지점",
    "re-plan": "개발 중 새 아이디어나 방향 변경이 생겼을 때 기획서를 새 버전으로 업데이트하는 과정",
    "Evidence Needed": "기획서 작성 중 근거 자료가 없어서 가정으로 처리한 항목. 사람이 확인하고 채워야 함",
}


# ---------------------------------------------------------------------------
# HTML generation
# ---------------------------------------------------------------------------

def build_html(data: dict, serve_mode: bool = False) -> str:
    data_json = json.dumps(data, ensure_ascii=False)
    guide_json = json.dumps(GUIDE_PROMPTS, ensure_ascii=False)
    glossary_json = json.dumps(GLOSSARY, ensure_ascii=False)
    sse_script = """
    // SSE live reload
    const evtSource = new EventSource('/events');
    evtSource.onmessage = () => location.reload();
    evtSource.onerror = () => evtSource.close();
    """ if serve_mode else ""

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{data['projectName']} — Dashboard</title>
<script src="https://cdn.jsdelivr.net/npm/marked@9/marked.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{
  --bg:#0f1117;--surface:#1a1d27;--surface2:#22263a;--surface3:#2a2f45;
  --border:#2e3350;--text:#e2e8f0;--muted:#7c85a2;--accent:#6c8ef7;
  --green:#22c55e;--orange:#f59e0b;--red:#ef4444;--purple:#a855f7;
  --blue:#3b82f6;--gray:#64748b;
  --class-a:#22c55e;--class-b:#f59e0b;--class-c:#ef4444;
  --r:8px;--font:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  --mono:"SF Mono","Fira Code",monospace;
}}
body{{font-family:var(--font);background:var(--bg);color:var(--text);min-height:100vh;font-size:14px;line-height:1.6}}

/* Layout */
.layout{{display:grid;grid-template-columns:220px 1fr;min-height:100vh}}

/* Sidebar */
.sidebar{{background:var(--surface);border-right:1px solid var(--border);padding:0;position:sticky;top:0;height:100vh;overflow-y:auto;display:flex;flex-direction:column}}
.sidebar-header{{padding:16px 20px;border-bottom:1px solid var(--border)}}
.sidebar-header .proj{{font-size:14px;font-weight:600;word-break:break-word}}
.sidebar-header .meta{{font-size:11px;color:var(--muted);margin-top:3px}}
.phase-bar{{padding:12px 16px;border-bottom:1px solid var(--border);background:var(--surface2)}}
.phase-dots{{display:flex;gap:6px;align-items:center;margin-bottom:6px}}
.phase-dot{{width:10px;height:10px;border-radius:50%;background:var(--border);flex-shrink:0}}
.phase-dot.active{{background:var(--accent)}}
.phase-dot.done{{background:var(--green)}}
.phase-label{{font-size:11px;color:var(--muted)}}
.nav-section{{padding:8px 0}}
.nav-label{{font-size:10px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);padding:6px 20px 3px}}
.nav-item{{display:block;padding:7px 20px;color:var(--muted);cursor:pointer;border-left:3px solid transparent;transition:all .15s;font-size:13px;background:none;border-top:none;border-right:none;border-bottom:none;width:100%;text-align:left}}
.nav-item:hover{{color:var(--text);background:var(--surface2)}}
.nav-item.active{{color:var(--accent);border-left-color:var(--accent);background:rgba(108,142,247,.08)}}
.nav-badge{{float:right;background:var(--surface3);color:var(--muted);font-size:10px;padding:1px 6px;border-radius:10px;margin-top:1px}}
.nav-badge.warn{{background:rgba(239,68,68,.2);color:var(--red)}}

/* Main */
.main{{padding:28px 36px;overflow-y:auto}}
.section{{display:none}}
.section.active{{display:block}}

/* Guide Strip */
.guide-strip{{background:var(--surface2);border:1px solid var(--border);border-radius:var(--r);padding:16px 20px;margin-bottom:20px;position:relative}}
.guide-strip.hidden{{display:none}}
.guide-state{{font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:var(--accent);margin-bottom:6px}}
.guide-message{{font-size:13px;color:var(--text);margin-bottom:12px}}
.guide-prompt-box{{background:var(--bg);border:1px solid var(--border);border-radius:6px;padding:10px 14px;font-family:var(--mono);font-size:11px;color:var(--muted);white-space:pre-wrap;margin-bottom:10px;max-height:120px;overflow-y:auto}}
.guide-actions{{display:flex;gap:8px;align-items:center}}
.btn{{padding:6px 14px;border-radius:6px;font-size:12px;font-weight:600;cursor:pointer;border:none;transition:all .15s}}
.btn-primary{{background:var(--accent);color:#fff}}
.btn-primary:hover{{background:#5a7ef0}}
.btn-secondary{{background:var(--surface3);color:var(--muted)}}
.btn-secondary:hover{{color:var(--text)}}
.guide-toggle{{position:absolute;top:12px;right:14px;font-size:11px;color:var(--muted);cursor:pointer;background:none;border:none;padding:2px 6px;border-radius:4px}}
.guide-toggle:hover{{color:var(--text);background:var(--surface3)}}

/* Hero stats */
.hero-stats{{display:grid;grid-template-columns:repeat(auto-fill,minmax(130px,1fr));gap:8px;margin-bottom:20px}}
.stat-card{{background:var(--surface);border:1px solid var(--border);border-radius:var(--r);padding:12px 16px}}
.stat-count{{font-size:26px;font-weight:700}}
.stat-label{{font-size:11px;color:var(--muted);margin-top:2px}}
.stat-card.green .stat-count{{color:var(--green)}}
.stat-card.orange .stat-count{{color:var(--orange)}}
.stat-card.red .stat-count{{color:var(--red)}}
.stat-card.blue .stat-count{{color:var(--blue)}}
.stat-card.purple .stat-count{{color:var(--purple)}}

/* Two-column layout */
.two-col{{display:grid;grid-template-columns:1fr 340px;gap:16px}}
@media(max-width:1000px){{.two-col{{grid-template-columns:1fr}}}}

/* Cards */
.card{{background:var(--surface);border:1px solid var(--border);border-radius:var(--r);padding:18px 20px;margin-bottom:14px}}
.card-title{{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);margin-bottom:12px}}

/* Section titles */
.sec-title{{font-size:18px;font-weight:600;margin-bottom:20px;color:var(--text)}}

/* Badges */
.badge{{display:inline-block;font-size:10px;font-weight:700;padding:2px 7px;border-radius:4px;letter-spacing:.04em;text-transform:uppercase}}
.badge-a{{background:rgba(34,197,94,.15);color:var(--class-a)}}
.badge-b{{background:rgba(245,158,11,.15);color:var(--class-b)}}
.badge-c{{background:rgba(239,68,68,.15);color:var(--class-c)}}
.badge-approved{{background:rgba(34,197,94,.15);color:var(--green)}}
.badge-draft{{background:rgba(100,116,139,.15);color:var(--gray)}}
.badge-review{{background:rgba(245,158,11,.15);color:var(--orange)}}

/* Plan version tree */
.plan-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:10px;margin-bottom:14px}}
.plan-card{{background:var(--surface);border:1px solid var(--border);border-radius:var(--r);padding:14px 16px}}
.plan-card.empty{{border-style:dashed;opacity:.6}}
.plan-name{{font-size:12px;font-weight:600;margin-bottom:8px}}
.plan-versions{{display:flex;flex-direction:column;gap:5px}}
.plan-ver{{display:flex;align-items:center;gap:8px;font-size:12px;padding:4px 8px;border-radius:5px;background:var(--surface2)}}
.plan-ver .vnum{{font-family:var(--mono);font-size:11px;color:var(--accent);min-width:24px}}
.plan-ver .vdate{{color:var(--muted);font-size:11px;flex:1}}
.plan-ver.latest{{background:var(--surface3)}}
.plan-empty{{font-size:12px;color:var(--muted);padding:4px 0}}

/* Dev spec list */
.spec-list{{display:flex;flex-direction:column;gap:8px}}
.spec-item{{display:flex;align-items:center;gap:10px;padding:10px 14px;background:var(--surface2);border-radius:6px;border:1px solid var(--border)}}
.spec-ver{{font-family:var(--mono);font-size:12px;color:var(--accent);min-width:30px}}
.spec-info{{flex:1}}
.spec-title{{font-size:13px;font-weight:500}}
.spec-date{{font-size:11px;color:var(--muted)}}

/* Pending ideas */
.idea-item{{display:flex;align-items:center;gap:10px;padding:8px 12px;background:rgba(239,68,68,.06);border:1px solid rgba(239,68,68,.2);border-radius:6px;margin-bottom:6px}}
.idea-icon{{font-size:14px}}
.idea-name{{font-size:13px;flex:1}}

/* TODO */
.todo-board{{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-bottom:16px}}
.todo-stat{{background:var(--surface);border:1px solid var(--border);border-radius:var(--r);padding:12px;text-align:center}}
.todo-stat .count{{font-size:26px;font-weight:700}}
.todo-stat .label{{font-size:11px;color:var(--muted)}}
.todo-stat.ready .count{{color:var(--blue)}}
.todo-stat.progress .count{{color:var(--purple)}}
.todo-stat.blocked .count{{color:var(--red)}}
.todo-stat.done .count{{color:var(--gray)}}

.todo-sec-hdr{{font-size:12px;font-weight:600;padding:8px 0 6px;margin-top:6px;border-bottom:1px solid var(--border);margin-bottom:8px;display:flex;align-items:center;gap:8px}}
.todo-item{{background:var(--surface);border:1px solid var(--border);border-radius:var(--r);padding:12px 14px;margin-bottom:7px}}
.todo-item-hdr{{display:flex;align-items:flex-start;gap:8px;margin-bottom:5px}}
.todo-id{{font-family:var(--mono);font-size:11px;color:var(--muted);white-space:nowrap;margin-top:1px}}
.todo-title{{font-size:13px;font-weight:500;flex:1}}
.todo-meta{{font-size:11px;color:var(--muted);display:flex;gap:10px;flex-wrap:wrap}}
.todo-criteria{{margin-top:7px;padding-top:7px;border-top:1px solid var(--border)}}
.todo-criteria li{{font-size:12px;color:var(--muted);list-style:none;padding:2px 0}}

/* Timeline */
.timeline{{position:relative;padding-left:20px}}
.tl-item{{position:relative;padding:0 0 12px 16px;border-left:2px solid var(--border)}}
.tl-item:last-child{{border-left-color:transparent}}
.tl-dot{{position:absolute;left:-5px;top:4px;width:8px;height:8px;border-radius:50%;background:var(--accent)}}
.tl-time{{font-size:11px;color:var(--muted);margin-bottom:2px}}
.tl-text{{font-size:13px}}

/* Dependencies */
.dep-section{{margin-bottom:16px}}
.dep-file{{font-size:11px;font-weight:700;color:var(--muted);margin-bottom:8px;text-transform:uppercase;letter-spacing:.06em}}
.dep-table{{width:100%;border-collapse:collapse}}
.dep-table th{{background:var(--surface2);padding:6px 10px;text-align:left;font-size:11px;font-weight:600;border:1px solid var(--border)}}
.dep-table td{{padding:5px 10px;border:1px solid var(--border);font-size:12px;font-family:var(--mono)}}
.dep-section-label{{font-size:10px;color:var(--muted)}}

/* Diagrams */
.diagram-block{{background:var(--surface);border:1px solid var(--border);border-radius:var(--r);padding:20px;margin-bottom:14px;overflow-x:auto}}
.diagram-title{{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.05em;color:var(--muted);margin-bottom:14px}}

/* File list */
.file-list{{list-style:none}}
.file-item{{display:flex;align-items:center;gap:10px;padding:9px 12px;border:1px solid var(--border);border-radius:var(--r);margin-bottom:6px;background:var(--surface)}}
.file-item:hover{{background:var(--surface2)}}
.file-icon{{font-size:15px;flex-shrink:0}}
.file-info{{flex:1;min-width:0}}
.file-title{{font-size:13px;font-weight:500;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}
.file-name{{font-size:11px;color:var(--muted);font-family:var(--mono);margin-top:1px}}

/* Markdown */
.md-content h1{{font-size:17px;font-weight:600;margin:18px 0 9px;color:var(--text)}}
.md-content h2{{font-size:14px;font-weight:600;margin:16px 0 7px;color:var(--text);border-bottom:1px solid var(--border);padding-bottom:5px}}
.md-content h3{{font-size:13px;font-weight:600;margin:12px 0 5px;color:var(--text)}}
.md-content p{{margin-bottom:7px}}
.md-content ul,.md-content ol{{padding-left:18px;margin-bottom:7px}}
.md-content li{{margin-bottom:2px}}
.md-content code{{font-family:var(--mono);background:var(--surface2);padding:1px 5px;border-radius:4px;font-size:12px;color:#a5b4fc}}
.md-content pre{{background:var(--surface2);border:1px solid var(--border);border-radius:var(--r);padding:12px 14px;overflow-x:auto;margin-bottom:10px}}
.md-content pre code{{background:none;padding:0;color:var(--text)}}
.md-content blockquote{{border-left:3px solid var(--accent);padding-left:10px;color:var(--muted);margin-bottom:7px}}
.md-content table{{width:100%;border-collapse:collapse;margin-bottom:10px}}
.md-content th{{background:var(--surface2);padding:7px 10px;text-align:left;font-size:12px;font-weight:600;border:1px solid var(--border)}}
.md-content td{{padding:6px 10px;border:1px solid var(--border)}}
.md-content hr{{border:none;border-top:1px solid var(--border);margin:14px 0}}
.md-content a{{color:var(--accent)}}

/* Collapsible */
.collapsible{{background:var(--surface);border:1px solid var(--border);border-radius:var(--r);margin-bottom:10px}}
.collapsible-hdr{{padding:12px 16px;cursor:pointer;display:flex;align-items:center;gap:8px;font-size:13px;font-weight:500;user-select:none}}
.collapsible-hdr:hover{{background:var(--surface2);border-radius:var(--r)}}
.collapsible-arrow{{color:var(--muted);font-size:11px;transition:transform .2s;margin-left:auto}}
.collapsible-hdr.open .collapsible-arrow{{transform:rotate(90deg)}}
.collapsible-body{{display:none;padding:0 16px 16px}}
.collapsible-body.open{{display:block}}

/* Tooltip */
[data-tip]{{position:relative;cursor:help;border-bottom:1px dashed var(--muted)}}
[data-tip]:hover::after{{content:attr(data-tip);position:absolute;bottom:100%;left:0;background:var(--surface3);border:1px solid var(--border);border-radius:6px;padding:6px 10px;font-size:12px;white-space:pre-wrap;max-width:280px;z-index:99;pointer-events:none;color:var(--text)}}

/* Empty */
.empty{{text-align:center;padding:32px;color:var(--muted);font-size:13px}}

/* Live indicator */
.live-dot{{width:7px;height:7px;border-radius:50%;background:var(--green);display:inline-block;animation:pulse 2s infinite;margin-right:4px}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.4}}}}

::-webkit-scrollbar{{width:5px;height:5px}}
::-webkit-scrollbar-track{{background:transparent}}
::-webkit-scrollbar-thumb{{background:var(--border);border-radius:3px}}
</style>
</head>
<body>
<script>
const DATA = {data_json};
const GUIDES = {guide_json};
const GLOSSARY = {glossary_json};
</script>

<div class="layout">
  <nav class="sidebar">
    <div class="sidebar-header">
      <div class="proj" id="sb-proj"></div>
      <div class="meta" id="sb-meta"></div>
    </div>
    <div class="phase-bar">
      <div class="phase-dots" id="phase-dots"></div>
      <div class="phase-label" id="phase-label"></div>
    </div>
    <div class="nav-section">
      <div class="nav-label">현황</div>
      <button class="nav-item active" onclick="switchTab('overview',this)">🏠 개요</button>
      <button class="nav-item" onclick="switchTab('plans',this)">📋 6종 기획서 <span class="nav-badge" id="nb-plans"></span></button>
      <button class="nav-item" onclick="switchTab('todo',this)">✅ 백로그 <span class="nav-badge" id="nb-todo"></span></button>
    </div>
    <div class="nav-section">
      <div class="nav-label">문서</div>
      <button class="nav-item" onclick="switchTab('devspec',this)">📝 개발명세서</button>
      <button class="nav-item" onclick="switchTab('diagrams',this)">🔀 다이어그램</button>
      <button class="nav-item" onclick="switchTab('adrs',this)">📌 ADR</button>
      <button class="nav-item" onclick="switchTab('deps',this)">📦 의존성</button>
    </div>
    <div class="nav-section">
      <div class="nav-label">자료</div>
      <button class="nav-item" onclick="switchTab('briefs',this)">📁 Briefs <span class="nav-badge warn" id="nb-ideas"></span></button>
      <button class="nav-item" onclick="switchTab('guide',this)">📚 가이드</button>
      <button class="nav-item" onclick="switchTab('handoff',this)">📄 HANDOFF</button>
    </div>
  </nav>

  <main class="main">

    <!-- OVERVIEW -->
    <div id="tab-overview" class="section active">
      <div class="sec-title">🏠 개요</div>

      <!-- Guide Strip -->
      <div class="guide-strip" id="guide-strip">
        <button class="guide-toggle" onclick="toggleGuide()" id="guide-toggle-btn">가이드 숨김</button>
        <div class="guide-state" id="gs-state"></div>
        <div class="guide-message" id="gs-message"></div>
        <div class="guide-prompt-box" id="gs-prompt" style="display:none"></div>
        <div class="guide-actions" id="gs-actions"></div>
      </div>

      <!-- Stats -->
      <div class="hero-stats" id="hero-stats"></div>

      <!-- Two col -->
      <div class="two-col">
        <div>
          <!-- Pending ideas -->
          <div id="pending-ideas-section"></div>

          <!-- Phase 1 quick status -->
          <div class="card">
            <div class="card-title">📋 Phase 1 — 6종 기획서</div>
            <div class="plan-grid" id="overview-plans"></div>
          </div>

          <!-- Recent HANDOFF -->
          <div class="card">
            <div class="card-title">📄 HANDOFF 현재 상태</div>
            <div id="overview-handoff" class="md-content"></div>
          </div>
        </div>

        <div>
          <!-- Activity timeline -->
          <div class="card">
            <div class="card-title">⚡ 최근 활동</div>
            <div class="timeline" id="timeline"></div>
          </div>

          <!-- Dev spec quick -->
          <div class="card">
            <div class="card-title">📝 개발명세서</div>
            <div class="spec-list" id="overview-specs"></div>
          </div>

          <!-- Active links from HANDOFF -->
          <div class="card">
            <div class="card-title">🔗 활성 링크</div>
            <div id="active-links" class="md-content"></div>
          </div>
        </div>
      </div>
    </div>

    <!-- PLANS -->
    <div id="tab-plans" class="section">
      <div class="sec-title">📋 6종 기획서</div>
      <div id="plans-content"></div>
    </div>

    <!-- TODO -->
    <div id="tab-todo" class="section">
      <div class="sec-title">✅ 백로그</div>
      <div class="todo-board" id="todo-stats"></div>
      <div id="todo-sections"></div>
    </div>

    <!-- DEV SPEC -->
    <div id="tab-devspec" class="section">
      <div class="sec-title">📝 개발명세서</div>
      <div id="devspec-content"></div>
    </div>

    <!-- DIAGRAMS -->
    <div id="tab-diagrams" class="section">
      <div class="sec-title">🔀 다이어그램</div>
      <div id="diagrams-content"></div>
    </div>

    <!-- ADR -->
    <div id="tab-adrs" class="section">
      <div class="sec-title">📌 ADR</div>
      <ul class="file-list" id="adrs-list"></ul>
    </div>

    <!-- DEPS -->
    <div id="tab-deps" class="section">
      <div class="sec-title">📦 의존성</div>
      <div id="deps-content"></div>
    </div>

    <!-- BRIEFS -->
    <div id="tab-briefs" class="section">
      <div class="sec-title">📁 Briefs</div>
      <div id="pending-ideas-full"></div>
      <ul class="file-list" id="briefs-list"></ul>
    </div>

    <!-- GUIDE -->
    <div id="tab-guide" class="section">
      <div class="sec-title">📚 방법론 가이드</div>
      <div id="guide-content"></div>
    </div>

    <!-- HANDOFF -->
    <div id="tab-handoff" class="section">
      <div class="sec-title">📄 HANDOFF.md</div>
      <div class="card">
        <div id="handoff-full" class="md-content"></div>
      </div>
    </div>

  </main>
</div>

<script>
{sse_script}
mermaid.initialize({{startOnLoad:false, theme:'dark', securityLevel:'loose'}});

// ── helpers ──────────────────────────────────────────────────────────
function badge(cls) {{
  const map = {{A:'badge-a',B:'badge-b',C:'badge-c',approved:'badge-approved',draft:'badge-draft',review:'badge-review'}};
  const labels = {{A:'Class A',B:'Class B',C:'Class C',approved:'승인됨',draft:'초안',review:'검토 중'}};
  return `<span class="badge ${{map[cls]||'badge-draft'}}">${{labels[cls]||cls}}</span>`;
}}

function statusBadge(s) {{
  if (s === 'approved') return badge('approved');
  if (s === 'review') return badge('review');
  return badge('draft');
}}

function e(id) {{ return document.getElementById(id); }}

function copyToClipboard(text) {{
  navigator.clipboard.writeText(text).then(() => {{
    const el = e('copy-feedback');
    if (el) {{ el.textContent = '✓ 복사됨'; setTimeout(()=>el.textContent='',2000); }}
  }});
}}

// ── tab switching ─────────────────────────────────────────────────────
function switchTab(name, btn) {{
  document.querySelectorAll('.section').forEach(s=>s.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(n=>n.classList.remove('active'));
  e('tab-'+name).classList.add('active');
  if (btn) btn.classList.add('active');
  if (name === 'diagrams') renderDiagrams();
}}

// ── sidebar meta ──────────────────────────────────────────────────────
e('sb-proj').textContent = DATA.projectName;
const liveHtml = {str(serve_mode).lower()} ? '<span class="live-dot"></span>' : '';
e('sb-meta').innerHTML = liveHtml + DATA.generatedAt + ' 생성';

// ── phase dots ────────────────────────────────────────────────────────
(function() {{
  const ps = DATA.phaseState;
  const phases = ['Setup','Phase 1','Phase 2','Phase 3'];
  const dots = phases.map((_,i) => {{
    let cls = '';
    if (i < ps.phase) cls = 'done';
    else if (i === ps.phase) cls = 'active';
    return `<div class="phase-dot ${{cls}}" title="${{phases[i]}}"></div>`;
  }}).join('<span style="color:var(--muted);font-size:9px">›</span>');
  e('phase-dots').innerHTML = dots;
  e('phase-label').textContent = ps.label;
}})();

// ── guide strip ───────────────────────────────────────────────────────
(function() {{
  const hidden = localStorage.getItem('guideHidden') === '1';
  const gs = e('guide-strip');
  const ps = DATA.phaseState;
  const g = GUIDES[ps.state] || GUIDES['dev'];
  e('gs-state').textContent = g.title;
  e('gs-message').textContent = g.message;
  if (g.prompt) {{
    e('gs-prompt').style.display = 'block';
    e('gs-prompt').textContent = g.prompt;
    e('gs-actions').innerHTML = `
      <button class="btn btn-primary" onclick="copyToClipboard(GUIDES['${{ps.state}}'].prompt)">
        📋 ${{g.action}}
      </button>
      <span id="copy-feedback" style="font-size:12px;color:var(--green)"></span>`;
  }}
  if (hidden) gs.classList.add('hidden');
  e('guide-toggle-btn').textContent = hidden ? '가이드 표시' : '가이드 숨김';
}})();

function toggleGuide() {{
  const gs = e('guide-strip');
  const hidden = gs.classList.toggle('hidden');
  localStorage.setItem('guideHidden', hidden ? '1' : '0');
  e('guide-toggle-btn').textContent = hidden ? '가이드 표시' : '가이드 숨김';
}}

// ── hero stats ────────────────────────────────────────────────────────
(function() {{
  const plansDone = Object.values(DATA.plans).filter(v=>v.length>0).length;
  const specsCount = DATA.devSpecs.length;
  const todo = parseTodo(DATA.todo);
  const pending = DATA.pendingIdeas.length;

  const cards = [
    {{count: `${{plansDone}}/6`, label:'기획서 작성', cls:'blue'}},
    {{count: specsCount, label:'개발명세서', cls:'purple'}},
    {{count: todo.progress.length, label:'진행 중', cls:'purple'}},
    {{count: todo.blocked.length + pending, label:'주의 필요', cls: todo.blocked.length+pending>0?'red':'green'}},
    {{count: todo.done.length, label:'완료', cls:'green'}},
  ];
  e('hero-stats').innerHTML = cards.map(c=>
    `<div class="stat-card ${{c.cls}}"><div class="stat-count">${{c.count}}</div><div class="stat-label">${{c.label}}</div></div>`
  ).join('');

  // nav badges
  const plansBadgeCls = plansDone < 6 ? 'warn' : '';
  e('nb-plans').className = 'nav-badge ' + plansBadgeCls;
  e('nb-plans').textContent = plansDone + '/6';
  e('nb-todo').textContent = todo.ready.length + todo.progress.length;
  e('nb-ideas').textContent = pending > 0 ? pending + ' 새 아이디어' : '';
  e('nb-ideas').style.display = pending > 0 ? '' : 'none';
}})();

// ── pending ideas ─────────────────────────────────────────────────────
function renderPendingIdeas(containerId) {{
  const el = e(containerId);
  if (!DATA.pendingIdeas.length) {{ el.innerHTML = ''; return; }}
  el.innerHTML = `
    <div class="card" style="border-color:rgba(239,68,68,.3)">
      <div class="card-title" style="color:var(--red)">🆕 보류 중 아이디어 (briefs/updates/)</div>
      ${{DATA.pendingIdeas.map(i=>`
        <div class="idea-item">
          <span class="idea-icon">💡</span>
          <span class="idea-name">${{i.name}}</span>
        </div>`).join('')}}
      <div style="margin-top:10px;font-size:12px;color:var(--muted)">
        재기획 프롬프트 → KICKOFF_PROMPT.md 의 "재기획" 섹션 참조
      </div>
    </div>`;
}}
renderPendingIdeas('pending-ideas-section');
renderPendingIdeas('pending-ideas-full');

// ── overview plans ────────────────────────────────────────────────────
(function() {{
  const html = DATA.planTypes.map(([ptype, pname]) => {{
    const vers = DATA.plans[ptype] || [];
    const latest = vers[vers.length - 1];
    if (!vers.length) {{
      return `<div class="plan-card empty"><div class="plan-name">${{pname}}</div><div class="plan-empty">미작성</div></div>`;
    }}
    const verHtml = vers.map((v,i) =>
      `<div class="plan-ver ${{i===vers.length-1?'latest':''}}">
        <span class="vnum">v${{v.version}}</span>
        <span class="vdate">${{v.date}}</span>
        ${{statusBadge(v.status)}}
      </div>`
    ).join('');
    return `<div class="plan-card"><div class="plan-name">${{pname}}</div><div class="plan-versions">${{verHtml}}</div></div>`;
  }}).join('');
  e('overview-plans').innerHTML = html;
}})();

// ── overview HANDOFF ──────────────────────────────────────────────────
(function() {{
  const raw = DATA.handoff;
  const section = raw.match(/## Current Focus([\\s\\S]*?)(?=##|$)/);
  e('overview-handoff').innerHTML = marked.parse(section ? '## Current Focus' + section[1] : (raw || '_HANDOFF.md 없음_'));
}})();

// ── active links ──────────────────────────────────────────────────────
(function() {{
  const raw = DATA.handoff;
  const section = raw.match(/## Active Links([\\s\\S]*?)(?=##|$)/);
  e('active-links').innerHTML = marked.parse(section ? '## Active Links' + section[1] : '_링크 없음_');
}})();

// ── timeline ──────────────────────────────────────────────────────────
(function() {{
  const events = [];
  DATA.devSpecs.forEach(s => events.push({{time: s.date, text: `개발명세서 ${{s.name}} 작성됨`}}));
  DATA.adrs.forEach(a => events.push({{time: '', text: `ADR: ${{a.title}}`}}));
  Object.entries(DATA.plans).forEach(([ptype, vers]) => {{
    vers.forEach(v => events.push({{time: v.date, text: `${{DATA.planTypes.find(p=>p[0]===ptype)?.[1]||ptype}} v${{v.version}} ${{v.status === 'approved' ? '승인됨' : '작성됨'}}`}}));
  }});
  events.sort((a,b) => (b.time||'').localeCompare(a.time||''));
  const show = events.slice(0,8);
  e('timeline').innerHTML = show.length
    ? show.map(ev=>`<div class="tl-item"><div class="tl-dot"></div><div class="tl-time">${{ev.time||'날짜 미상'}}</div><div class="tl-text">${{ev.text}}</div></div>`).join('')
    : '<div class="empty">활동 기록 없음</div>';
}})();

// ── overview specs ────────────────────────────────────────────────────
(function() {{
  const el = e('overview-specs');
  if (!DATA.devSpecs.length) {{ el.innerHTML = '<div class="empty">개발명세서 없음</div>'; return; }}
  el.innerHTML = DATA.devSpecs.map(s=>`
    <div class="spec-item">
      <span class="spec-ver">v${{s.version}}</span>
      <div class="spec-info"><div class="spec-title">${{s.title}}</div><div class="spec-date">${{s.date}}</div></div>
      ${{statusBadge(s.status)}}
    </div>`).join('');
}})();

// ── plans tab ─────────────────────────────────────────────────────────
(function() {{
  const html = DATA.planTypes.map(([ptype, pname]) => {{
    const vers = DATA.plans[ptype] || [];
    const inner = vers.length
      ? vers.map((v,i) => `
          <div class="plan-ver ${{i===vers.length-1?'latest':''}}">
            <span class="vnum">v${{v.version}}</span>
            <span class="vdate">${{v.date}}</span>
            ${{statusBadge(v.status)}}
            <span style="flex:1"></span>
            <span style="font-size:11px;color:var(--muted)">${{v.name}}</span>
            ${{v.trigger&&v.trigger!=='initial'?`<span style="font-size:11px;color:var(--orange)" title="트리거: ${{v.trigger}}">🔄</span>`:''}}
          </div>`).join('')
      : '<div class="plan-empty">아직 작성되지 않았습니다.</div>';
    return `
      <div class="collapsible">
        <div class="collapsible-hdr ${{vers.length?'':''}}" onclick="toggleCollapsible(this)">
          <span>${{pname}}</span>
          ${{vers.length ? statusBadge(vers[vers.length-1].status) : '<span class="badge badge-draft">미작성</span>'}}
          <span class="collapsible-arrow">▶</span>
        </div>
        <div class="collapsible-body ${{vers.length?'open':''}}">
          <div class="plan-versions">${{inner}}</div>
        </div>
      </div>`;
  }}).join('');
  e('plans-content').innerHTML = html;
}})();

// ── todo ──────────────────────────────────────────────────────────────
function parseTodo(raw) {{
  const s = {{ready:[],progress:[],blocked:[],done:[]}};
  let cur = null, item = null;
  const smap = {{'## ready':'ready','## in progress':'progress','## blocked':'blocked','## done':'done'}};
  for (const line of (raw||'').split('\\n')) {{
    const lo = line.toLowerCase().trim();
    const k = Object.keys(smap).find(k => lo === k);
    if (k) {{ if(item&&cur) s[cur].push(item); item=null; cur=smap[k]; continue; }}
    if (!cur) continue;
    if (/^###\\s+TODO-/i.test(line)) {{
      if(item&&cur) s[cur].push(item);
      const idM = line.match(/TODO-\\d+/i);
      item = {{id:idM?idM[0].toUpperCase():'',title:'',changeClass:'A',owner:'',criteria:[],notes:''}};
      continue;
    }}
    if (!item) continue;
    let m;
    if ((m=line.match(/^-\\s*title:\\s*(.+)/))) item.title=m[1];
    else if ((m=line.match(/^-\\s*change-class:\\s*([ABC])/i))) item.changeClass=m[1].toUpperCase();
    else if ((m=line.match(/^-\\s*owner:\\s*(.+)/))) item.owner=m[1];
    else if ((m=line.match(/^-\\s*notes:\\s*(.+)/))) item.notes=m[1];
    else if ((m=line.match(/^\\s*-\\s*\\[[ x]\\]\\s*(.+)/i)))
      item.criteria.push({{done:line.includes('[x]')||line.includes('[X]'),text:m[1]}});
  }}
  if(item&&cur) s[cur].push(item);
  return s;
}}

function renderTodoItem(item) {{
  const crit = item.criteria.length
    ? `<div class="todo-criteria"><ul>${{item.criteria.map(c=>`<li>${{c.done?'☑':'☐'}} ${{c.text}}</li>`).join('')}}</ul></div>` : '';
  return `<div class="todo-item">
    <div class="todo-item-hdr">
      <span class="todo-id">${{item.id}}</span>
      <span class="todo-title">${{item.title||'(제목 없음)'}}</span>
      ${{badge(item.changeClass)}}
    </div>
    <div class="todo-meta">${{item.owner?`<span>담당: ${{item.owner}}</span>`:''}}${{item.notes?`<span>${{item.notes}}</span>`:''}}</div>
    ${{crit}}
  </div>`;
}}

(function() {{
  const s = parseTodo(DATA.todo);
  e('todo-stats').innerHTML = [
    {{k:'ready',l:'Ready',c:'ready'}},{{k:'progress',l:'In Progress',c:'progress'}},
    {{k:'blocked',l:'Blocked',c:'blocked'}},{{k:'done',l:'Done',c:'done'}}
  ].map(x=>`<div class="todo-stat ${{x.c}}"><div class="count">${{s[x.k].length}}</div><div class="label">${{x.l}}</div></div>`).join('');

  const sections = [
    {{key:'progress',label:'In Progress',badge:'badge-review'}},
    {{key:'ready',label:'Ready',badge:'badge-draft'}},
    {{key:'blocked',label:'Blocked',badge:'badge-c'}},
    {{key:'done',label:'Done',badge:''}}
  ];
  e('todo-sections').innerHTML = sections.map(sec => {{
    if (!s[sec.key].length) return '';
    return `<div class="todo-sec-hdr"><span class="badge ${{sec.badge}}">${{sec.label}}</span><span style="color:var(--muted);font-size:12px">${{s[sec.key].length}}개</span></div>
    ${{s[sec.key].map(renderTodoItem).join('')}}`;
  }}).join('') || '<div class="empty">TODO 항목 없음</div>';
}})();

// ── dev spec tab ──────────────────────────────────────────────────────
(function() {{
  const el = e('devspec-content');
  if (!DATA.devSpecs.length) {{ el.innerHTML = '<div class="empty">개발명세서 없음<br><small>Phase 2 프롬프트로 작성을 요청하세요.</small></div>'; return; }}
  el.innerHTML = DATA.devSpecs.map(s => `
    <div class="card">
      <div class="card-title">개발명세서 v${{s.version}} — ${{s.date}} ${{statusBadge(s.status)}}</div>
      <div style="font-size:12px;color:var(--muted);font-family:var(--mono)">${{s.path}}</div>
    </div>`).join('');
}})();

// ── diagrams ──────────────────────────────────────────────────────────
let diagramsRendered = false;
function renderDiagrams() {{
  if (diagramsRendered) return; diagramsRendered = true;
  const raw = DATA.diagram || '';
  const el = e('diagrams-content');
  const parts = raw.split(/^##\\s+/m).filter(Boolean);
  if (!parts.length) {{ el.innerHTML = '<div class="empty">다이어그램 없음</div>'; return; }}
  let html = '';
  parts.forEach((part,i) => {{
    const lines = part.split('\\n');
    const title = lines[0].trim();
    const body = lines.slice(1).join('\\n');
    const mm = body.match(/```mermaid([\\s\\S]*?)```/);
    if (mm) {{
      html += `<div class="diagram-block"><div class="diagram-title">${{title}}</div><div class="mermaid" id="mm${{i}}">${{mm[1].trim()}}</div></div>`;
    }} else {{
      html += `<div class="diagram-block"><div class="diagram-title">${{title}}</div><div class="md-content">${{marked.parse(body)}}</div></div>`;
    }}
  }});
  el.innerHTML = html;
  mermaid.run();
}}

// ── ADR ───────────────────────────────────────────────────────────────
(function() {{
  const el = e('adrs-list');
  if (!DATA.adrs.length) {{ el.innerHTML = '<div class="empty">ADR 없음</div>'; return; }}
  el.innerHTML = DATA.adrs.map(a=>`
    <li class="file-item"><span class="file-icon">📌</span>
    <div class="file-info"><div class="file-title">${{a.title}}</div><div class="file-name">${{a.name}}</div></div></li>`).join('');
}})();

// ── deps ──────────────────────────────────────────────────────────────
(function() {{
  const el = e('deps-content');
  const deps = DATA.dependencies;
  if (!Object.keys(deps).length) {{
    el.innerHTML = '<div class="empty">의존성 파일 없음<br><small>package.json, requirements.txt, pyproject.toml, Gemfile 을 감지합니다.</small></div>';
    return;
  }}
  el.innerHTML = Object.entries(deps).map(([file, pkgs]) => {{
    if (!pkgs.length) return '';
    const rows = pkgs.map(p=>`<tr><td>${{p.name}}</td><td>${{p.version||'-'}}</td><td><span class="dep-section-label">${{p.section||'-'}}</span></td></tr>`).join('');
    return `<div class="dep-section">
      <div class="dep-file">${{file}} — ${{pkgs.length}}개</div>
      <table class="dep-table"><thead><tr><th>패키지</th><th>버전</th><th>섹션</th></tr></thead><tbody>${{rows}}</tbody></table>
    </div>`;
  }}).join('') || '<div class="empty">파싱된 패키지 없음</div>';
}})();

// ── briefs ────────────────────────────────────────────────────────────
(function() {{
  const el = e('briefs-list');
  if (!DATA.briefs.length) {{ el.innerHTML = '<div class="empty">briefs/ 없음 — 아이디어 노트, PDF를 넣으세요.</div>'; return; }}
  el.innerHTML = DATA.briefs.map(f=>`
    <li class="file-item"><span class="file-icon">📁</span>
    <div class="file-info"><div class="file-title">${{f}}</div></div></li>`).join('');
}})();

// ── HANDOFF full ─────────────────────────────────────────────────────
e('handoff-full').innerHTML = marked.parse(DATA.handoff || '_HANDOFF.md 없음_');

// ── Guide tab ─────────────────────────────────────────────────────────
(function() {{
  const steps = [
    {{n:'0', title:'Phase 0 — 프로젝트 초기화', body:'init-project.sh 실행 후 briefs/ 에 자료를 넣고 Phase 0 킥오프 프롬프트를 보낸다.'}},
    {{n:'1A-F', title:'Phase 1 — 6종 기획서', body:'KICKOFF_PROMPT.md 의 Phase 1-A ~ 1-F 를 순서대로 요청. 각 기획서는 docs/snapshots/plans/{type}/v1-날짜.md 에 저장됨.'}},
    {{n:'🔒', title:'Gate 1 — 6종 검토 + 승인', body:'모든 기획서 검토 후 "6종 기획서 검토 완료했어. Phase 2 진행해줘." 메시지를 보낸다.'}},
    {{n:'2', title:'Phase 2 — 개발명세서', body:'6종 기획서를 종합해서 개발명세서를 작성. Change Class 목록 포함. docs/snapshots/dev-specs/ 에 저장.'}},
    {{n:'🔒', title:'Gate 2 — 명세서 검토 + 승인', body:'"개발명세서 승인했어. Phase 3 개발 시작해줘." 메시지를 보낸다.'}},
    {{n:'3', title:'Phase 3 — 개발', body:'TODO.md 분해 → Class A/B/C 구분 → 구현 → PR → merge → HANDOFF 갱신 반복.'}},
    {{n:'🔄', title:'재기획 — 새 아이디어 발생 시', body:'briefs/updates/ 에 파일 추가 후 re-plan 프롬프트 실행. 영향 분석 → 승인 → 기획서 v(N+1) 업데이트.'}},
  ];

  const glossaryHtml = Object.entries(GLOSSARY).map(([k,v])=>
    `<div class="collapsible">
      <div class="collapsible-hdr" onclick="toggleCollapsible(this)">
        <span style="font-family:var(--mono)">${{k}}</span>
        <span class="collapsible-arrow">▶</span>
      </div>
      <div class="collapsible-body" style="padding:8px 16px 14px;font-size:13px;color:var(--muted)">${{v}}</div>
    </div>`
  ).join('');

  e('guide-content').innerHTML = `
    <div class="card">
      <div class="card-title">단계별 가이드</div>
      ${{steps.map(s=>`
        <div style="display:flex;gap:12px;margin-bottom:14px;align-items:flex-start">
          <div style="background:var(--accent);color:#fff;border-radius:6px;padding:3px 8px;font-size:11px;font-weight:700;white-space:nowrap;flex-shrink:0">${{s.n}}</div>
          <div><div style="font-size:13px;font-weight:600;margin-bottom:3px">${{s.title}}</div>
          <div style="font-size:12px;color:var(--muted)">${{s.body}}</div></div>
        </div>`).join('')}}
    </div>
    <div class="card">
      <div class="card-title">용어 사전</div>
      ${{glossaryHtml}}
    </div>`;
}})();

// ── collapsible ───────────────────────────────────────────────────────
function toggleCollapsible(hdr) {{
  hdr.classList.toggle('open');
  const body = hdr.nextElementSibling;
  body.classList.toggle('open');
}}
</script>
</body>
</html>"""


# ---------------------------------------------------------------------------
# File watcher
# ---------------------------------------------------------------------------

WATCH_PATTERNS = [
    "HANDOFF.md", "TODO.md", "DIAGRAM.md", "CLAUDE.md",
    "package.json", "requirements.txt", "pyproject.toml", "Gemfile",
]

WATCH_DIRS = [
    "briefs", "briefs/updates",
    "docs/snapshots/plans", "docs/snapshots/dev-specs",
    "docs/adr",
]


def get_watched_mtimes() -> dict:
    mtimes = {}
    for f in WATCH_PATTERNS:
        p = Path(f)
        if p.exists():
            mtimes[f] = p.stat().st_mtime
    for d in WATCH_DIRS:
        dp = Path(d)
        if dp.exists():
            for fp in dp.rglob("*.md"):
                mtimes[str(fp)] = fp.stat().st_mtime
    return mtimes


# ---------------------------------------------------------------------------
# Server
# ---------------------------------------------------------------------------

_sse_clients: list = []
_sse_lock = threading.Lock()
_dashboard_html = ""
_serve_mode = False


def notify_reload():
    with _sse_lock:
        for q in list(_sse_clients):
            try:
                q.put("reload")
            except Exception:
                pass


def watcher_thread(interval: float = 1.0):
    prev = get_watched_mtimes()
    while True:
        time.sleep(interval)
        curr = get_watched_mtimes()
        if curr != prev:
            prev = curr
            global _dashboard_html
            _dashboard_html = build_html(collect_data(), serve_mode=True)
            notify_reload()


class Handler(http.server.BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass  # suppress request logs

    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(_dashboard_html.encode("utf-8"))

        elif self.path == "/events":
            import queue
            q: queue.Queue = queue.Queue()
            with _sse_lock:
                _sse_clients.append(q)
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.send_header("Cache-Control", "no-cache")
            self.send_header("Connection", "keep-alive")
            self.end_headers()
            try:
                while True:
                    try:
                        msg = q.get(timeout=15)
                        self.wfile.write(f"data: {msg}\n\n".encode())
                        self.wfile.flush()
                    except Exception:
                        self.wfile.write(b": ping\n\n")
                        self.wfile.flush()
            except (BrokenPipeError, ConnectionResetError):
                pass
            finally:
                with _sse_lock:
                    try:
                        _sse_clients.remove(q)
                    except ValueError:
                        pass
        else:
            self.send_response(404)
            self.end_headers()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Project dashboard generator")
    parser.add_argument("--serve", action="store_true", help="Start live server")
    parser.add_argument("--port", type=int, default=8765, help="Server port (default: 8765)")
    args = parser.parse_args()

    if args.serve:
        global _dashboard_html, _serve_mode
        _serve_mode = True
        _dashboard_html = build_html(collect_data(), serve_mode=True)

        wt = threading.Thread(target=watcher_thread, daemon=True)
        wt.start()

        try:
            with socketserver.TCPServer(("", args.port), Handler) as httpd:
                url = f"http://localhost:{args.port}"
                print(f"✓ Dashboard live at {url}")
                print(f"  파일 변경 감지 중 (자동 새로고침)")
                print(f"  종료: Ctrl+C")
                import webbrowser
                webbrowser.open(url)
                httpd.serve_forever()
        except OSError as exc:
            if "Address already in use" in str(exc):
                print(f"✗ 포트 {args.port}가 이미 사용 중입니다.")
                print(f"  다른 포트를 지정하려면: --port N")
            else:
                raise
    else:
        data = collect_data()
        html = build_html(data, serve_mode=False)
        Path("dashboard.html").write_text(html, encoding="utf-8")
        print(f"✓ dashboard.html 생성 완료 — {data['generatedAt']}")
        print(f"  open dashboard.html")
        print(f"  실시간 모드: python3 generate-dashboard.py --serve")


if __name__ == "__main__":
    main()
