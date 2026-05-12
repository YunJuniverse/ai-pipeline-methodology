#!/usr/bin/env python3
"""methodology — CLI for distributing & updating the methodology in projects.

Commands
--------
  methodology init <path> --type fullstack|planning-only [--label NAME]
      새 프로젝트에 방법론을 주입한다.

  methodology sync [--apply] [--target <version>]
      현재 폴더(.methodology-version 보유)를 업스트림과 동기화한다.
      --apply 없이 호출하면 변경 미리보기만 출력 (드라이런).

  methodology status
      적용된 버전과 업스트림 버전을 비교한다.

  methodology diff <path>
      특정 파일에서 sync가 어떤 변경을 가할지 단일 파일 diff 표시.

  methodology version
      이 메소돌로지 자신의 버전을 출력한다.

  methodology observe --slug <kebab-slug> --summary <text> [options]
      L1 AI 관찰 로그를 생성한다.

  methodology observe --validate <path>
      L1 AI 관찰 로그의 필수 필드와 경로 규칙을 검증한다.

  methodology catalog init|status|seed-pending
      Pending Lesson과 active Catalog 흐름을 관리한다.

  methodology skeleton init|build|apply
      도메인 skeleton base/lock/apply v0 흐름을 실행한다.

  methodology thinktank
      L1 관찰 로그 기반 주간 인사이트 리포트를 생성한다.

Classification
--------------
  shared          — sync가 항상 덮어쓴다 (10_guides/, 40_resources/, 그래프, 대시보드)
  init_scaffolds  — init이 1회 생성, sync는 절대 안 건드린다 (20_planning/, 30_dev/)
  managed         — sync가 마커 사이만 머지한다 (CLAUDE.md, AGENTS.md)
  project_local   — 프로젝트 산출물, sync 무관 (HANDOFF/TODO/code/...)

Markers
-------
  managed 파일에서 다음 마커 쌍 사이만 sync가 갱신한다:

      <!-- methodology:managed:start id=<block-id> -->
      ...
      <!-- methodology:managed:end -->
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import shutil
import subprocess
import sys
from datetime import date, datetime, timezone
from difflib import unified_diff
from pathlib import Path
from typing import Any, Callable

# ─── 메소돌로지 자체 버전 ───────────────────────────────────────────────────
METHODOLOGY_VERSION = "v3.2"

METHODOLOGY_ROOT = Path(__file__).resolve().parent.parent

# ─── 매니페스트 ─────────────────────────────────────────────────────────────
MANIFEST = {
    # sync가 항상 덮어쓰는 디렉터리·파일 (재귀 복사)
    "shared_paths": [
        "10_guides",
        "40_resources/templates",
        "40_resources/prompts",
        "40_resources/catalog/_README.md",
        "40_resources/skeletons/_README.md",
        "40_resources/ai_observations/_README.md",
        "50_tools/methodology-graph.json",
        "50_tools/generate-dashboard.py",
        "50_tools/methodology.py",
        "00_foundation/WHITEPAPER.md",
        "00_foundation/HOW_TO_APPLY.md",
        "00_foundation/KICKOFF_PROMPT.md",
        "00_foundation/DIAGRAM.md",
        ".ai/schema",
        ".ai/adapters",
        "ONBOARDING.md",
    ],
    # init이 1회 생성하는 디렉터리·파일 (sync 무시)
    "init_paths": [
        "20_planning",
        "30_dev",
        "40_resources/catalog/_pending",
        "40_resources/catalog/archived",
        "40_resources/skeletons",
        "40_resources/ai_observations",
    ],
    # init이 src→dst 매핑으로 복사하는 단일 파일들 (PROJECT_NAME 치환 가능)
    "init_files": [
        # (src_in_methodology, dst_in_project, substitute)
        ("CLAUDE.md", "CLAUDE.md", True),
        ("AGENTS.md", "AGENTS.md", True),
        ("40_resources/templates/HANDOFF.md", "HANDOFF.md", True),
        ("40_resources/templates/TODO.md", "TODO.md", True),
        ("40_resources/templates/context.json", ".ai/context.json", True),
        ("40_resources/templates/checkpoint.md", ".ai/checkpoint.md", True),
    ],
    # sync가 마커 사이만 머지하는 파일
    "managed_files": [
        "CLAUDE.md",
        "AGENTS.md",
    ],
    # 절대로 외부 프로젝트에 주입되면 안 되는 경로 (메타-방법론 등)
    # MANIFEST는 whitelist 방식이라 1차 안전 — excluded_paths는 2차 안전망.
    # init/sync 시작 시 검증되며, shared_paths/init_paths/init_files와 겹치면 즉시 fail.
    "excluded_paths": [
        "60_meta",
    ],
}

MARKER_RE = re.compile(
    r"<!--\s*methodology:managed:start\s+id=([\w\-]+)\s*-->(.*?)<!--\s*methodology:managed:end\s*-->",
    re.DOTALL,
)

VERSION_FILE_NAME = ".methodology-version"
META_ROOT = Path("60_meta")
OBSERVATION_DIR = Path("40_resources/ai_observations")
CATALOG_DIR = Path("40_resources/catalog")
SKELETONS_DIR = Path("40_resources/skeletons")
INSIGHTS_DIR = Path("30_dev/snapshots/insights")
OBSERVATION_TASK_TYPES = {"bootstrap", "feature", "bugfix", "refactor", "research", "docs"}
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
OBSERVATION_FILE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}_[a-z0-9]+(?:-[a-z0-9]+)*\.md$")


# ─── 유틸 ───────────────────────────────────────────────────────────────────


def info(msg: str) -> None:
    print(f"\033[36m[info]\033[0m {msg}")


def ok(msg: str) -> None:
    print(f"\033[32m[ok]\033[0m {msg}")


def warn(msg: str) -> None:
    print(f"\033[33m[warn]\033[0m {msg}")


def err(msg: str) -> None:
    print(f"\033[31m[err]\033[0m {msg}", file=sys.stderr)


def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def write_text(p: Path, content: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")


def utc_stamp() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def utc_date() -> str:
    return datetime.now(timezone.utc).date().isoformat()


def host_os_label() -> str:
    try:
        system = subprocess.check_output(["uname", "-s"], text=True).strip().lower()
        release = subprocess.check_output(["uname", "-r"], text=True).strip()
        return f"{system}-{release}"
    except Exception:
        return "unknown"


def upstream_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "-C", str(METHODOLOGY_ROOT), "rev-parse", "--short", "HEAD"],
            text=True,
        ).strip()
    except Exception:
        return "unknown"


def substitute(content: str, label: str, mode: str | None, today: str) -> str:
    out = content.replace("[PROJECT_NAME]", label)
    if mode:
        out = out.replace("[fullstack / planning-only]", mode)
        out = out.replace("[PROJECT_MODE]", mode)
    out = out.replace("[YYYY-MM-DD]", today)
    return out


# ─── 마커 머지 ──────────────────────────────────────────────────────────────


def parse_managed_blocks(text: str) -> dict[str, str]:
    return {m.group(1): m.group(0) for m in MARKER_RE.finditer(text)}


def merge_managed(source_text: str, target_text: str) -> tuple[str, dict]:
    """target의 마커 블록을 source의 같은 id 블록으로 교체.

    반환: (새 target_text, 통계 dict)
    """
    src_blocks = parse_managed_blocks(source_text)
    tgt_blocks = parse_managed_blocks(target_text)

    replaced = 0
    untouched = 0
    deprecated = []  # target에는 있지만 source에 없는 id

    def _sub(m: re.Match) -> str:
        nonlocal replaced, untouched
        block_id = m.group(1)
        if block_id in src_blocks:
            new_block = src_blocks[block_id]
            if new_block.strip() == m.group(0).strip():
                untouched += 1
            else:
                replaced += 1
            return new_block
        deprecated.append(block_id)
        return m.group(0)

    new_text = MARKER_RE.sub(_sub, target_text)

    # source에는 있지만 target에 없는 id → 끝에 추가
    new_in_source = [bid for bid in src_blocks if bid not in tgt_blocks]
    if new_in_source:
        added_blocks = "\n\n".join(src_blocks[bid] for bid in new_in_source)
        new_text = new_text.rstrip() + "\n\n" + added_blocks + "\n"

    return new_text, {
        "replaced": replaced,
        "untouched": untouched,
        "deprecated": deprecated,
        "added": new_in_source,
    }


# ─── 버전 파일 ──────────────────────────────────────────────────────────────


def load_version_file(target: Path) -> dict:
    p = target / VERSION_FILE_NAME
    if not p.exists():
        return {}
    return json.loads(read_text(p))


def write_version_file(target: Path, label: str | None) -> None:
    payload = {
        "methodology_version": METHODOLOGY_VERSION,
        "applied_at": str(date.today()),
        "applied_from": "ai-pipeline-methodology",
        "upstream_commit": upstream_commit(),
        "project_label": label,
    }
    write_text(target / VERSION_FILE_NAME, json.dumps(payload, indent=2, ensure_ascii=False) + "\n")


# ─── L1 관찰 로그 ───────────────────────────────────────────────────────────


def load_ai_context(root: Path) -> dict:
    p = root / ".ai" / "context.json"
    if not p.exists():
        return {}
    try:
        return json.loads(read_text(p))
    except json.JSONDecodeError:
        return {}


def yaml_scalar(value: str | None) -> str:
    if value is None:
        return "null"
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def parse_friction_item(raw: str, index: int) -> dict:
    parts = raw.split("|")
    if len(parts) != 4:
        raise ValueError("--friction 형식은 'where|cost_minutes|resolution|repeat_of' 입니다")
    where, cost, resolution, repeat_of = [p.strip() for p in parts]
    try:
        cost_minutes = int(cost)
    except ValueError as exc:
        raise ValueError("friction cost_minutes는 정수여야 합니다") from exc
    repeat_value = None if repeat_of in {"", "null", "none", "-"} else repeat_of
    return {
        "id": f"F-{index:03d}",
        "where": where,
        "cost_minutes": cost_minutes,
        "resolution": resolution,
        "repeat_of": repeat_value,
    }


def render_observation(payload: dict) -> str:
    lines = [
        "---",
        f"session_id: {payload['session_id']}",
        "authored_by:",
        f"  agent: {yaml_scalar(payload['agent'])}",
        f"  tool: {yaml_scalar(payload['tool'])}",
        f"  host_os: {yaml_scalar(payload['host_os'])}",
        f"domain: {payload['domain']}",
        f"task_type: {payload['task_type']}",
        "stack_used:",
    ]
    for stack in payload["stack_used"]:
        lines.append(f"  - {yaml_scalar(stack)}")
    lines.append(f"flow_used: {payload['flow_used']}")

    friction = payload["friction"]
    if friction:
        lines.append("friction:")
        for item in friction:
            lines.extend([
                f"  - id: {item['id']}",
                f"    where: {yaml_scalar(item['where'])}",
                f"    cost_minutes: {item['cost_minutes']}",
                f"    resolution: {yaml_scalar(item['resolution'])}",
                f"    repeat_of: {item['repeat_of'] or 'null'}",
            ])
    else:
        lines.append("friction: []")

    patterns = payload["prompt_patterns"]
    if patterns:
        lines.append("prompt_patterns:")
        for index, intent in enumerate(patterns, start=1):
            lines.extend([
                f"  - intent: {yaml_scalar(intent)}",
                "    success: true",
                f"    rounds: {payload['rounds'][index - 1]}",
            ])
    else:
        lines.append("prompt_patterns: []")

    lines.extend([
        "---",
        "",
        payload["summary"].strip(),
        "",
    ])
    return "\n".join(lines)


def validate_observation_file(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f"파일 없음: {path}"]
    if not OBSERVATION_FILE_RE.match(path.name):
        errors.append("파일명은 YYYY-MM-DD_<kebab-slug>.md 형식이어야 합니다")
    text = read_text(path)
    if "/Users/" in text or "\\Users\\" in text:
        errors.append("절대 사용자 경로가 포함되어 있습니다")
    if not text.startswith("---\n"):
        errors.append("YAML frontmatter 시작 마커가 없습니다")
        return errors
    try:
        _, frontmatter, body = text.split("---", 2)
    except ValueError:
        errors.append("YAML frontmatter 종료 마커가 없습니다")
        return errors

    required_snippets = [
        "session_id:",
        "authored_by:",
        "  agent:",
        "  tool:",
        "  host_os:",
        "domain:",
        "task_type:",
        "stack_used:",
        "flow_used:",
        "friction:",
        "prompt_patterns:",
    ]
    for snippet in required_snippets:
        if snippet not in frontmatter:
            errors.append(f"필수 필드 누락: {snippet.strip()}")

    session_match = re.search(r"^session_id:\s*([^\s]+)\s*$", frontmatter, flags=re.MULTILINE)
    if session_match and session_match.group(1) != path.stem:
        errors.append("session_id는 파일명(.md 제외)과 같아야 합니다")
    task_match = re.search(r"^task_type:\s*([^\s]+)\s*$", frontmatter, flags=re.MULTILINE)
    if task_match and task_match.group(1) not in OBSERVATION_TASK_TYPES:
        errors.append(f"task_type은 {', '.join(sorted(OBSERVATION_TASK_TYPES))} 중 하나여야 합니다")
    if re.search(r"^\s*-\s*\[?None\]?\s*$", frontmatter, flags=re.MULTILINE):
        errors.append("빈 배열은 [None] 대신 []로 기록해야 합니다")
    paragraphs = [p for p in body.strip().split("\n\n") if p.strip()]
    if len(paragraphs) != 1:
        errors.append("자유서술은 1단락이어야 합니다")
    elif len(paragraphs[0]) > 220:
        errors.append("자유서술이 너무 깁니다")
    return errors


def parse_observation_frontmatter(path: Path) -> dict[str, Any]:
    text = read_text(path)
    if not text.startswith("---\n"):
        return {}
    try:
        _, frontmatter, _body = text.split("---", 2)
    except ValueError:
        return {}
    out: dict[str, Any] = {"path": str(path.relative_to(METHODOLOGY_ROOT))}
    current = None
    for raw in frontmatter.splitlines():
        line = raw.rstrip()
        if not line.strip():
            continue
        top = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if top:
            current = top.group(1)
            value = top.group(2).strip()
            out[current] = value.strip('"') if value else []
            continue
        item = re.match(r"^\s+-\s+(.+)$", line)
        if item and current:
            out.setdefault(current, [])
            if isinstance(out[current], list):
                out[current].append(item.group(1).strip().strip('"'))
    return out


def cmd_observe(args: argparse.Namespace) -> int:
    if args.validate:
        path = Path(args.validate)
        errors = validate_observation_file(path)
        if errors:
            for item in errors:
                err(item)
            return 1
        ok(f"observation valid: {path}")
        return 0

    if not args.slug or not args.summary:
        err("observe 생성에는 --slug 와 --summary 가 필요합니다")
        return 2
    if not SLUG_RE.match(args.slug):
        err("--slug 는 영문 소문자/숫자/kebab-case 여야 합니다")
        return 2
    if args.task_type not in OBSERVATION_TASK_TYPES:
        err(f"--task-type 은 {', '.join(sorted(OBSERVATION_TASK_TYPES))} 중 하나여야 합니다")
        return 2

    ctx = load_ai_context(METHODOLOGY_ROOT)
    agent = args.agent or ctx.get("last_session", {}).get("agent", {}).get("model") or "unknown"
    tool = args.tool or ctx.get("last_session", {}).get("agent", {}).get("tool") or "unknown"
    host_os = args.host_os or ctx.get("last_session", {}).get("host_os") or host_os_label()
    domain = args.domain or ctx.get("project", {}).get("domain") or "meta"
    stack_used = args.stack or ["python3", f"methodology@{METHODOLOGY_VERSION}"]
    intents = args.intent or ["l1 observation capture"]
    rounds = args.rounds or [1 for _ in intents]
    if len(rounds) != len(intents):
        err("--rounds 개수는 --intent 개수와 같아야 합니다")
        return 2

    try:
        friction = [parse_friction_item(raw, i) for i, raw in enumerate(args.friction or [], start=1)]
    except ValueError as exc:
        err(str(exc))
        return 2

    date_part = args.date or utc_date()
    session_id = f"{date_part}_{args.slug}"
    output = METHODOLOGY_ROOT / OBSERVATION_DIR / f"{session_id}.md"
    if output.exists() and not args.force:
        err(f"이미 존재합니다: {output.relative_to(METHODOLOGY_ROOT)} (--force 로 덮어쓰기)")
        return 1

    payload = {
        "session_id": session_id,
        "agent": agent,
        "tool": tool,
        "host_os": host_os,
        "domain": domain,
        "task_type": args.task_type,
        "stack_used": stack_used,
        "flow_used": args.flow_used,
        "friction": friction,
        "prompt_patterns": intents,
        "rounds": rounds,
        "summary": args.summary,
        "created_at": utc_stamp(),
    }
    content = render_observation(payload)
    if args.dry_run:
        print(content)
        return 0
    write_text(output, content)
    errors = validate_observation_file(output)
    if errors:
        for item in errors:
            err(item)
        return 1
    ok(f"observation created: {output.relative_to(METHODOLOGY_ROOT)}")
    return 0


# ─── L2 Catalog / Pending Lesson ────────────────────────────────────────────


def catalog_dirs() -> dict[str, Path]:
    base = METHODOLOGY_ROOT / CATALOG_DIR
    return {
        "base": base,
        "pending": base / "_pending",
        "archived": base / "archived",
    }


def ensure_catalog_dirs() -> None:
    for p in catalog_dirs().values():
        p.mkdir(parents=True, exist_ok=True)
    for p in [catalog_dirs()["pending"] / ".gitkeep", catalog_dirs()["archived"] / ".gitkeep"]:
        if not p.exists():
            write_text(p, "")


def count_markdown(path: Path, prefix: str | None = None) -> int:
    if not path.exists():
        return 0
    files = [p for p in path.glob("*.md") if p.name != "_README.md"]
    if prefix:
        files = [p for p in files if p.name.startswith(prefix)]
    return len(files)


def cmd_catalog(args: argparse.Namespace) -> int:
    ensure_catalog_dirs()
    dirs = catalog_dirs()
    if args.catalog_cmd == "init":
        ok("catalog dirs ready: 40_resources/catalog/{_pending,archived}")
        return 0
    if args.catalog_cmd == "status":
        print(f"pending {count_markdown(dirs['pending'])}")
        print(f"active  {count_markdown(dirs['base'], 'C-')}")
        print(f"archive {count_markdown(dirs['archived'])}")
        return 0
    if args.catalog_cmd == "seed-pending":
        target = dirs["pending"] / "P-001_git-write-lock.md"
        if target.exists() and not args.force:
            warn(f"exists: {target.relative_to(METHODOLOGY_ROOT)}")
            return 0
        content = """---
id: P-001
title: "Git metadata write blocked in sandboxed agent session"
domain: meta
status: pending
source_observations:
  - 2026-05-07_l1-observe-flow
signature: "git.*(index.lock|refs).*Operation not permitted|cannot lock ref"
created: 2026-05-08
last_seen: 2026-05-07
promotion_rule: "Promote to active Catalog after N>=2 observations or explicit human approval."
---

## 증상 (Symptom)

Agent can edit workspace files but cannot create Git lock/ref files under `.git/`, so branch creation, staging, commit, or push fails.

## 임시 해결 (Current Workaround)

Leave file changes in the workspace and ask the human to run Git commands from a local terminal with normal repository permissions.

## 승급 조건

Same friction appears in another L1 observation, or a human explicitly approves active Catalog promotion.
"""
        write_text(target, content)
        ok(f"pending lesson seeded: {target.relative_to(METHODOLOGY_ROOT)}")
        return 0
    err("unknown catalog command")
    return 2


# ─── L2 Skeleton ────────────────────────────────────────────────────────────


def skeleton_domain_dir(domain: str) -> Path:
    return METHODOLOGY_ROOT / SKELETONS_DIR / domain


def list_base_files(base_dir: Path) -> list[str]:
    if not base_dir.exists():
        return []
    return [
        str(p.relative_to(base_dir))
        for p in sorted(base_dir.rglob("*"))
        if p.is_file()
    ]


def load_catalog_entry(entry_id: str) -> dict[str, str]:
    base = METHODOLOGY_ROOT / CATALOG_DIR
    matches = list(base.glob(f"{entry_id}_*.md"))
    if not matches:
        return {"id": entry_id, "status": "missing", "path": ""}
    p = matches[0]
    text = read_text(p)
    title_match = re.search(r"^title:\s*\"?(.+?)\"?\s*$", text, flags=re.MULTILINE)
    return {
        "id": entry_id,
        "status": "found",
        "path": str(p.relative_to(METHODOLOGY_ROOT)),
        "title": title_match.group(1) if title_match else entry_id,
    }


def cmd_skeleton(args: argparse.Namespace) -> int:
    if not SLUG_RE.match(args.domain):
        err("domain은 영문 소문자/숫자/kebab-case 여야 합니다")
        return 2
    domain_dir = skeleton_domain_dir(args.domain)
    base_dir = domain_dir / "base"
    bakes_in = domain_dir / "bakes-in.json"
    lock_path = domain_dir / "skeleton.lock.json"

    if args.skeleton_cmd == "init":
        base_dir.mkdir(parents=True, exist_ok=True)
        readme = base_dir / "README.md"
        if not readme.exists():
            write_text(readme, f"# {args.domain} base\n\nMinimal portable base for `{args.domain}` skeleton.\n")
        if not bakes_in.exists():
            payload = {
                "schema_version": "1.0",
                "domain": args.domain,
                "base_version": "v0",
                "catalog_entries": [],
                "verified_with": [],
                "last_built": None,
            }
            write_text(bakes_in, json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
        ok(f"skeleton initialized: {domain_dir.relative_to(METHODOLOGY_ROOT)}")
        return 0

    if args.skeleton_cmd == "build":
        if not bakes_in.exists():
            err(f"missing {bakes_in.relative_to(METHODOLOGY_ROOT)} — run skeleton init first")
            return 1
        config = json.loads(read_text(bakes_in))
        entries = [load_catalog_entry(e) for e in config.get("catalog_entries", [])]
        lock = {
            "schema_version": "1.0",
            "domain": args.domain,
            "base_version": config.get("base_version", "v0"),
            "built_at": utc_stamp(),
            "base_files": list_base_files(base_dir),
            "catalog_entries": entries,
        }
        write_text(lock_path, json.dumps(lock, indent=2, ensure_ascii=False) + "\n")
        readme_lines = [
            f"# Skeleton: {args.domain}",
            "",
            f"- Base version: `{lock['base_version']}`",
            f"- Base files: {len(lock['base_files'])}",
            f"- Catalog entries: {len(entries)}",
            "",
            "## Prevented Problems",
            "",
        ]
        if entries:
            readme_lines.extend(f"- `{e['id']}`: {e.get('title', e['status'])}" for e in entries)
        else:
            readme_lines.append("- No active Catalog entries baked in yet.")
        write_text(domain_dir / "README.md", "\n".join(readme_lines) + "\n")
        ok(f"skeleton built: {lock_path.relative_to(METHODOLOGY_ROOT)}")
        return 0

    if args.skeleton_cmd == "apply":
        if not lock_path.exists():
            err(f"missing {lock_path.relative_to(METHODOLOGY_ROOT)} — run skeleton build first")
            return 1
        target = Path(args.target).resolve()
        if target.exists() and any(target.iterdir()) and not args.force:
            err(f"target {target} is not empty (--force to apply anyway)")
            return 1
        target.mkdir(parents=True, exist_ok=True)
        n = copy_path(base_dir, target, dry_run=False)
        write_text(target / ".methodology-skeleton.json", read_text(lock_path))
        ok(f"skeleton applied: {args.domain} -> {target} ({n} base files)")
        return 0

    err("unknown skeleton command")
    return 2


# ─── L3 Thinktank v0 ────────────────────────────────────────────────────────


def observation_files() -> list[Path]:
    base = METHODOLOGY_ROOT / OBSERVATION_DIR
    if not base.exists():
        return []
    return sorted(p for p in base.glob("*.md") if OBSERVATION_FILE_RE.match(p.name))


def cmd_thinktank(args: argparse.Namespace) -> int:
    files = observation_files()
    observations = [parse_observation_frontmatter(p) for p in files]
    friction_lines: list[str] = []
    for p in files:
        text = read_text(p)
        for match in re.finditer(r"where:\s*\"?(.+?)\"?\s*$", text, flags=re.MULTILINE):
            friction_lines.append(match.group(1))
    counts: dict[str, int] = {}
    for item in friction_lines:
        counts[item] = counts.get(item, 0) + 1

    now = datetime.now(timezone.utc)
    iso_year, iso_week, _ = now.isocalendar()
    out_dir = METHODOLOGY_ROOT / INSIGHTS_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"{iso_year}-W{iso_week:02d}_thinktank.md"
    lines = [
        f"# Thinktank v0 — {iso_year}-W{iso_week:02d}",
        "",
        "> Snapshot. Generated from L1 observations and repository metadata.",
        "",
        "## Inputs",
        "",
        f"- Observation files: {len(files)}",
        f"- Generated at: {utc_stamp()}",
        "",
        "## Repeated Friction Candidates",
        "",
    ]
    if counts:
        for name, count in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
            marker = "PROMOTE-CANDIDATE" if count >= 2 else "watch"
            lines.append(f"- `{marker}` x{count}: {name}")
    else:
        lines.append("- No friction entries yet.")
    lines.extend([
        "",
        "## Observations",
        "",
    ])
    for obs in observations:
        lines.append(f"- `{obs.get('session_id', 'unknown')}` — domain `{obs.get('domain', '?')}`, task `{obs.get('task_type', '?')}`")
    write_text(out, "\n".join(lines) + "\n")
    ok(f"thinktank report: {out.relative_to(METHODOLOGY_ROOT)}")
    return 0


# ─── 마이그레이션 ───────────────────────────────────────────────────────────


def list_migrations() -> list[tuple[str, str, Path]]:
    """(from_version, to_version, path) 리스트, 버전 순서로 정렬."""
    mig_dir = METHODOLOGY_ROOT / "migrations"
    if not mig_dir.exists():
        return []
    out = []
    for p in mig_dir.glob("v*_to_v*.py"):
        m = re.match(r"^(v[\d.]+)_to_(v[\d.]+)\.py$", p.name)
        if m:
            out.append((m.group(1), m.group(2), p))
    out.sort(key=lambda x: _ver_key(x[0]))
    return out


def _ver_key(v: str) -> tuple[int, ...]:
    return tuple(int(x) for x in v.lstrip("v").split("."))


def find_migration_chain(from_v: str, to_v: str) -> list[tuple[str, str, Path]]:
    """from_v → to_v로 가는 마이그레이션 체인."""
    all_mig = list_migrations()
    chain = []
    cur = from_v
    while cur != to_v:
        nxt = next(((f, t, p) for f, t, p in all_mig if f == cur), None)
        if not nxt:
            break
        chain.append(nxt)
        cur = nxt[1]
        if _ver_key(cur) >= _ver_key(to_v):
            break
    return chain


def run_migration(target: Path, mig_path: Path, dry_run: bool) -> None:
    spec = importlib.util.spec_from_file_location(mig_path.stem, mig_path)
    if not spec or not spec.loader:
        err(f"failed to load migration {mig_path}")
        return
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if not hasattr(mod, "migrate"):
        err(f"migration {mig_path.name} has no migrate(target, dry_run) function")
        return
    mod.migrate(target, dry_run=dry_run)


# ─── 동작: copy_path / merge_path ───────────────────────────────────────────


def copy_path(src: Path, dst: Path, dry_run: bool, *, prune: bool = False) -> int:
    """src → dst 재귀 복사. prune=True면 src에 없는 파일을 dst에서 제거.

    반환: 변경된 파일 수 (생성/덮어쓰기/삭제 모두 포함)
    """
    changes = 0
    if src.is_file():
        if not dst.exists() or read_text(src) != read_text(dst) if src.suffix in {".md", ".json", ".py", ".yaml", ".yml", ".sh"} else (not dst.exists() or src.read_bytes() != dst.read_bytes()):
            changes = 1
            if not dry_run:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
        return changes

    if not src.is_dir():
        return 0

    for sp in src.rglob("*"):
        if sp.is_dir():
            continue
        rel = sp.relative_to(src)
        dp = dst / rel
        same = dp.exists() and dp.is_file() and sp.read_bytes() == dp.read_bytes()
        if not same:
            changes += 1
            if not dry_run:
                dp.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(sp, dp)

    if prune and dst.is_dir():
        src_files = {sp.relative_to(src) for sp in src.rglob("*") if sp.is_file()}
        for dp in dst.rglob("*"):
            if not dp.is_file():
                continue
            rel = dp.relative_to(dst)
            if rel not in src_files:
                changes += 1
                if not dry_run:
                    dp.unlink()
    return changes


def merge_managed_file(src: Path, dst: Path, dry_run: bool) -> dict:
    if not dst.exists():
        # 프로젝트에 아예 없으면 통째로 복사
        if not dry_run:
            shutil.copy2(src, dst)
        return {"copied_new": True, "replaced": 0, "untouched": 0, "deprecated": [], "added": []}
    src_text = read_text(src)
    dst_text = read_text(dst)
    new_text, stats = merge_managed(src_text, dst_text)
    if new_text != dst_text and not dry_run:
        write_text(dst, new_text)
    stats["changed"] = new_text != dst_text
    return stats


# ─── 안전망: excluded_paths 검증 ────────────────────────────────────────────


def assert_excluded_paths_safe() -> None:
    """MANIFEST.excluded_paths가 shared/init_paths/init_files와 겹치지 않는지 검증.

    겹치면 즉시 fail — 메타-방법론 등 격리되어야 하는 경로가
    실수로 주입 대상에 추가된 사고를 차단한다.
    """
    excluded = set(MANIFEST.get("excluded_paths", []))
    if not excluded:
        return

    def violates(path: str) -> str | None:
        for ex in excluded:
            if path == ex or path.startswith(ex + "/"):
                return ex
        return None

    offenders: list[tuple[str, str]] = []
    for rel in MANIFEST["shared_paths"]:
        ex = violates(rel)
        if ex:
            offenders.append((f"shared_paths:{rel}", ex))
    for rel in MANIFEST["init_paths"]:
        ex = violates(rel)
        if ex:
            offenders.append((f"init_paths:{rel}", ex))
    for src_rel, dst_rel, _ in MANIFEST["init_files"]:
        for tag, p in (("init_files.src", src_rel), ("init_files.dst", dst_rel)):
            ex = violates(p)
            if ex:
                offenders.append((f"{tag}:{p}", ex))

    if offenders:
        err("MANIFEST excluded_paths 위반 — 다음 경로가 격리 디렉터리 안에 있습니다:")
        for where, ex in offenders:
            err(f"  {where}  ⊂  {ex}/")
        err("60_meta/ 같은 메타-방법론 자산이 외부 프로젝트에 주입되면 안 됩니다.")
        raise SystemExit(3)


# ─── 명령: init ─────────────────────────────────────────────────────────────


def cmd_init(args: argparse.Namespace) -> int:
    assert_excluded_paths_safe()
    target = Path(args.path).resolve()
    label = args.label or target.name
    mode = args.type
    today = str(date.today())

    if target.exists() and any(target.iterdir()):
        err(f"target {target} is not empty — use sync instead")
        return 1

    target.mkdir(parents=True, exist_ok=True)
    info(f"init: {target}  label={label}  type={mode}")

    # 1) shared_paths 복사
    for rel in MANIFEST["shared_paths"]:
        src = METHODOLOGY_ROOT / rel
        dst = target / rel
        if src.exists():
            n = copy_path(src, dst, dry_run=False)
            ok(f"shared    {rel}  ({n} files)")

    # 2) init_paths 복사 (v0 스켈레톤)
    for rel in MANIFEST["init_paths"]:
        src = METHODOLOGY_ROOT / rel
        dst = target / rel
        if src.exists():
            n = copy_path(src, dst, dry_run=False)
            ok(f"scaffold  {rel}  ({n} files)")

    # 3) init_files (치환 적용)
    for src_rel, dst_rel, sub in MANIFEST["init_files"]:
        src = METHODOLOGY_ROOT / src_rel
        dst = target / dst_rel
        if not src.exists():
            warn(f"init_file missing in source: {src_rel}")
            continue
        content = read_text(src)
        if sub:
            content = substitute(content, label, mode, today)
        write_text(dst, content)
        ok(f"file      {dst_rel}")

    # 4) .github/PULL_REQUEST_TEMPLATE.md (있으면)
    pr_src = METHODOLOGY_ROOT / ".github" / "PULL_REQUEST_TEMPLATE.md"
    if pr_src.exists():
        write_text(target / ".github" / "PULL_REQUEST_TEMPLATE.md", read_text(pr_src))
        ok("file      .github/PULL_REQUEST_TEMPLATE.md")

    # 5) fullstack 시 src/, tests/
    if mode == "fullstack":
        (target / "src").mkdir(exist_ok=True)
        (target / "tests" / "unit").mkdir(parents=True, exist_ok=True)
        (target / "tests" / "integration").mkdir(parents=True, exist_ok=True)
        ok("dir       src/, tests/")

    # 6) .methodology-version
    write_version_file(target, label)
    ok(f"version   {VERSION_FILE_NAME} → {METHODOLOGY_VERSION}")

    info("done. 다음:")
    print("  cd", target)
    print("  python3 50_tools/generate-dashboard.py --serve   # 대시보드 확인")
    print(f"  방법론 갱신 시: python3 {METHODOLOGY_ROOT}/50_tools/methodology.py sync --apply")
    return 0


# ─── 명령: sync ─────────────────────────────────────────────────────────────


def cmd_sync(args: argparse.Namespace) -> int:
    assert_excluded_paths_safe()
    target = Path(args.path or ".").resolve()
    apply = args.apply
    dry = not apply

    vinfo = load_version_file(target)
    if not vinfo:
        err(f"{VERSION_FILE_NAME} 없음 — 이 폴더는 methodology init으로 만든 프로젝트가 아닙니다.")
        err("처음 적용한다면: 50_tools/methodology.py init <path> 또는 빈 .methodology-version 파일 만들고 재시도")
        return 2

    cur_v = vinfo.get("methodology_version", "v0.0")
    target_v = args.target or METHODOLOGY_VERSION
    info(f"sync: {target}  ({cur_v} → {target_v})  {'DRY-RUN' if dry else 'APPLY'}")

    # 1) 마이그레이션 실행
    chain = find_migration_chain(cur_v, target_v)
    if cur_v != target_v and not chain:
        warn(f"마이그레이션 경로 없음: {cur_v} → {target_v}. 직접 적용으로 진행.")
    for f, t, p in chain:
        info(f"migrate   {f} → {t}  ({p.name})")
        run_migration(target, p, dry_run=dry)

    # 2) shared_paths: 항상 덮어쓰기
    total_changes = 0
    for rel in MANIFEST["shared_paths"]:
        src = METHODOLOGY_ROOT / rel
        dst = target / rel
        if not src.exists():
            continue
        n = copy_path(src, dst, dry_run=dry, prune=src.is_dir())
        if n:
            total_changes += n
            tag = "would update" if dry else "updated"
            ok(f"shared    {tag:13s} {rel}  ({n} files)")

    # 3) managed_files: 마커 머지
    for rel in MANIFEST["managed_files"]:
        src = METHODOLOGY_ROOT / rel
        dst = target / rel
        if not src.exists():
            continue
        stats = merge_managed_file(src, dst, dry_run=dry)
        if stats.get("copied_new"):
            ok(f"managed   created {rel}")
            total_changes += 1
        elif stats.get("changed"):
            tag = "would merge" if dry else "merged"
            msg = f"managed   {tag:13s} {rel}  (replaced={stats['replaced']}, added={len(stats['added'])}, deprecated={len(stats['deprecated'])})"
            ok(msg)
            if stats["deprecated"]:
                warn(f"          deprecated 블록 (확인 필요): {', '.join(stats['deprecated'])}")
            total_changes += 1
        else:
            info(f"managed   unchanged   {rel}")

    # 4) 버전 파일 갱신
    if not dry:
        write_version_file(target, vinfo.get("project_label"))
        ok(f"version   {VERSION_FILE_NAME} → {target_v}")
    else:
        info(f"version   would set {VERSION_FILE_NAME} → {target_v}")

    if dry:
        info(f"총 {total_changes}개 변경 예정. 적용하려면 --apply")
    else:
        ok(f"sync 완료. 총 {total_changes}개 파일 변경.")
    return 0


# ─── 명령: status ───────────────────────────────────────────────────────────


def cmd_status(args: argparse.Namespace) -> int:
    target = Path(args.path or ".").resolve()
    vinfo = load_version_file(target)
    if not vinfo:
        err(f"{VERSION_FILE_NAME} 없음 — methodology 적용 안 된 폴더")
        return 2
    cur_v = vinfo.get("methodology_version", "?")
    print(f"project          {target}")
    print(f"applied version  {cur_v}")
    print(f"upstream version {METHODOLOGY_VERSION}")
    print(f"upstream commit  {upstream_commit()}")
    if cur_v != METHODOLOGY_VERSION:
        chain = find_migration_chain(cur_v, METHODOLOGY_VERSION)
        if chain:
            print(f"migrations needed: {len(chain)}")
            for f, t, p in chain:
                print(f"  {f} → {t}  ({p.name})")
        else:
            print("migrations:      (직접 동기화)")
    else:
        print("status:          최신 ✓")
    return 0


# ─── 명령: diff ─────────────────────────────────────────────────────────────


def cmd_diff(args: argparse.Namespace) -> int:
    target = Path(args.path or ".").resolve()
    rel = args.file
    src = METHODOLOGY_ROOT / rel
    dst = target / rel
    if not src.exists():
        err(f"upstream에 없음: {rel}")
        return 1
    if not dst.exists():
        info(f"{rel} 은 새 파일 — 전체가 추가될 예정")
        print(read_text(src))
        return 0

    if rel in MANIFEST["managed_files"]:
        new_text, stats = merge_managed(read_text(src), read_text(dst))
        old_text = read_text(dst)
        info(f"managed merge: replaced={stats['replaced']}, added={len(stats['added'])}, deprecated={len(stats['deprecated'])}")
    else:
        old_text = read_text(dst)
        new_text = read_text(src)
        info("shared overwrite (전체 교체)")

    if old_text == new_text:
        ok("동일 — 변경 없음")
        return 0

    diff = unified_diff(old_text.splitlines(keepends=True), new_text.splitlines(keepends=True),
                        fromfile=f"a/{rel}", tofile=f"b/{rel}")
    sys.stdout.writelines(diff)
    return 0


# ─── 명령: version ──────────────────────────────────────────────────────────


def cmd_version(args: argparse.Namespace) -> int:
    print(f"methodology {METHODOLOGY_VERSION}  ({upstream_commit()})  @ {METHODOLOGY_ROOT}")
    return 0


def cmd_manifest_check(args: argparse.Namespace) -> int:
    """MANIFEST excluded_paths 안전망을 명시적으로 검증.

    겹침이 있으면 SystemExit(3)으로 fail. CI에서 호출 권장.
    """
    excluded = MANIFEST.get("excluded_paths", [])
    info(f"checking MANIFEST safety net — excluded_paths: {excluded or '(empty)'}")
    assert_excluded_paths_safe()
    ok("excluded_paths 검증 통과 — 격리된 경로가 주입 대상에 포함되어 있지 않음.")
    # 추가 정보 — 격리 디렉터리 실제 존재 여부
    for ex in excluded:
        p = METHODOLOGY_ROOT / ex
        marker = "✓ 존재" if p.exists() else "○ 미존재(선택)"
        print(f"  {ex}: {marker}")
    return 0


# ─── main ──────────────────────────────────────────────────────────────────


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="methodology", description="방법론 배포·갱신 CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    pi = sub.add_parser("init", help="새 프로젝트에 방법론 주입")
    pi.add_argument("path", help="대상 디렉터리 (없으면 생성)")
    pi.add_argument("--type", choices=["fullstack", "planning-only"], default="fullstack")
    pi.add_argument("--label", help="프로젝트 라벨 (기본: 디렉터리명)")
    pi.set_defaults(func=cmd_init)

    ps = sub.add_parser("sync", help="현재 폴더를 업스트림과 동기화")
    ps.add_argument("--apply", action="store_true", help="실제 적용 (없으면 dry-run)")
    ps.add_argument("--target", help="목표 버전 (기본: 최신)")
    ps.add_argument("--path", help="대상 폴더 (기본: 현재 디렉터리)")
    ps.set_defaults(func=cmd_sync)

    pst = sub.add_parser("status", help="버전 비교")
    pst.add_argument("--path", help="대상 폴더 (기본: 현재)")
    pst.set_defaults(func=cmd_status)

    pd = sub.add_parser("diff", help="단일 파일이 어떻게 갱신되는지 표시")
    pd.add_argument("file", help="대상 폴더 기준 상대 경로")
    pd.add_argument("--path", help="대상 폴더 (기본: 현재)")
    pd.set_defaults(func=cmd_diff)

    pv = sub.add_parser("version", help="메소돌로지 버전 출력")
    pv.set_defaults(func=cmd_version)

    pmc = sub.add_parser("manifest-check", help="MANIFEST excluded_paths 안전망 검증")
    pmc.set_defaults(func=cmd_manifest_check)

    po = sub.add_parser("observe", help="L1 AI 관찰 로그 생성·검증")
    po.add_argument("--slug", help="파일명 slug (영문 소문자/숫자/kebab-case)")
    po.add_argument("--summary", help="자유서술 1단락")
    po.add_argument("--task-type", choices=sorted(OBSERVATION_TASK_TYPES), default="docs")
    po.add_argument("--domain", help="도메인 식별자 (기본: .ai/context.json project.domain)")
    po.add_argument("--agent", help="작성 AI 모델 (기본: .ai/context.json last_session.agent.model)")
    po.add_argument("--tool", help="호스팅 도구 (기본: .ai/context.json last_session.agent.tool)")
    po.add_argument("--host-os", help="호스트 OS 라벨 (기본: .ai/context.json 또는 uname)")
    po.add_argument("--stack", action="append", help="사용한 스택/도구. 여러 번 지정 가능")
    po.add_argument("--flow-used", default="ad-hoc", help="skeleton:<id>-<version> 또는 ad-hoc")
    po.add_argument("--intent", action="append", help="프롬프트 intent. 여러 번 지정 가능")
    po.add_argument("--rounds", action="append", type=int, help="각 intent의 turn 수. --intent와 같은 개수")
    po.add_argument("--friction", action="append", help="'where|cost_minutes|resolution|repeat_of' 형식. 여러 번 지정 가능")
    po.add_argument("--date", help="UTC 날짜 YYYY-MM-DD (기본: 오늘 UTC)")
    po.add_argument("--force", action="store_true", help="동일 파일이 있으면 덮어쓰기")
    po.add_argument("--dry-run", action="store_true", help="파일을 쓰지 않고 출력")
    po.add_argument("--validate", help="기존 observation 파일 검증")
    po.set_defaults(func=cmd_observe)

    pc = sub.add_parser("catalog", help="Catalog/Pending Lesson 흐름 관리")
    csub = pc.add_subparsers(dest="catalog_cmd", required=True)
    ci = csub.add_parser("init", help="catalog 하위 디렉터리 생성")
    ci.set_defaults(func=cmd_catalog)
    cs = csub.add_parser("status", help="pending/active/archive 개수 출력")
    cs.set_defaults(func=cmd_catalog)
    cp = csub.add_parser("seed-pending", help="첫 Pending Lesson seed 생성")
    cp.add_argument("--force", action="store_true")
    cp.set_defaults(func=cmd_catalog)

    psk = sub.add_parser("skeleton", help="Skeleton build/apply v0")
    sksub = psk.add_subparsers(dest="skeleton_cmd", required=True)
    ski = sksub.add_parser("init", help="도메인 skeleton 초기화")
    ski.add_argument("domain")
    ski.set_defaults(func=cmd_skeleton)
    skb = sksub.add_parser("build", help="bakes-in.json 기준 lock/README 생성")
    skb.add_argument("domain")
    skb.set_defaults(func=cmd_skeleton)
    ska = sksub.add_parser("apply", help="skeleton base와 lock을 대상 폴더에 적용")
    ska.add_argument("domain")
    ska.add_argument("target")
    ska.add_argument("--force", action="store_true")
    ska.set_defaults(func=cmd_skeleton)

    pt = sub.add_parser("thinktank", help="L3 Thinktank v0 리포트 생성")
    pt.set_defaults(func=cmd_thinktank)

    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
