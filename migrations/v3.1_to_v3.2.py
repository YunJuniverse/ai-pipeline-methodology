"""v3.1 → v3.2 마이그레이션.

변경 요약 (옛 v3.1 구조 → 새 v3.2 구조):

이동 (옛 → 새):
- methodology.py             →  60_tools/methodology.py
- generate-dashboard.py      →  60_tools/generate-dashboard.py
- methodology-graph.json     →  60_tools/methodology-graph.json
- DIAGRAM.md                 →  10_foundation/DIAGRAM.md
- HOW_TO_APPLY.md            →  10_foundation/HOW_TO_APPLY.md
- KICKOFF_PROMPT.md          →  10_foundation/KICKOFF_PROMPT.md
- 50_resources/onboarding/   →  10_foundation/  (경쟁 안 — 중간 경로 정리)

신규 디렉터리 생성 (sync가 다음 단계에서 shared 파일 채움):
- 10_foundation/
- 60_tools/
- .ai/schema/
- .ai/adapters/
- 50_resources/catalog/{_pending,archived}/
- 50_resources/skeletons/
- 50_resources/ai_observations/

신규 파일은 sync가 shared_paths/init_files를 통해 자동 채움:
- 10_foundation/WHITEPAPER.md (shared)
- ONBOARDING.md (shared)
- .ai/context.json, .ai/checkpoint.md (init_files — *기존에 없을 때만* 생성)
- .ai/schema/*, .ai/adapters/* (shared)

보존 (절대 안 건드림):
- CLAUDE.md, AGENTS.md, HANDOFF.md, TODO.md  — 사용자 콘텐츠
- 30_planning/, 40_dev/  — 사용자 산출물
- 적용 프로젝트 고유 파일 (src/, tests/, package.json 등)

멱등성: 새 위치에 이미 콘텐츠가 있으면 이동을 skip.
주입 격리: 70_meta/는 본 마이그레이션이 절대 *생성*하지 않는다 (메타-방법론 격리).
"""

from __future__ import annotations

import json
import shutil
from datetime import date
from pathlib import Path

# (old_relative, new_relative) — 단일 파일 또는 디렉터리 이동
MOVES = [
    # 옛 루트 CLI/데이터 → 60_tools/
    ("methodology.py", "60_tools/methodology.py"),
    ("generate-dashboard.py", "60_tools/generate-dashboard.py"),
    ("methodology-graph.json", "60_tools/methodology-graph.json"),
    # 옛 루트 온보딩·다이어그램 → 10_foundation/
    ("DIAGRAM.md", "10_foundation/DIAGRAM.md"),
    ("HOW_TO_APPLY.md", "10_foundation/HOW_TO_APPLY.md"),
    ("KICKOFF_PROMPT.md", "10_foundation/KICKOFF_PROMPT.md"),
    # 중간 경쟁 경로(있을 수 있는 옛 시도) → 10_foundation/
    ("50_resources/onboarding/DIAGRAM.md", "10_foundation/DIAGRAM.md"),
    ("50_resources/onboarding/HOW_TO_APPLY.md", "10_foundation/HOW_TO_APPLY.md"),
    ("50_resources/onboarding/KICKOFF_PROMPT.md", "10_foundation/KICKOFF_PROMPT.md"),
]

# 빈 디렉터리 보장 (sync 가 shared_paths/init_paths 로 채움)
ENSURE_DIRS = [
    "10_foundation",
    "60_tools",
    ".ai/schema",
    ".ai/adapters",
    "50_resources/catalog/_pending",
    "50_resources/catalog/archived",
    "50_resources/skeletons",
    "50_resources/ai_observations",
]

# 절대 *생성하지 않는* 경로 — 메타-방법론 격리.
# 방어적 검증: 본 마이그레이션이 실수로 이 경로를 만들지 않도록 한다.
NEVER_CREATE = ["70_meta"]


def _log(msg: str, dry: bool) -> None:
    prefix = "[migrate v3.1→v3.2]"
    print(f"{prefix} {'(dry-run) ' if dry else ''}{msg}")


def _is_nonempty(p: Path) -> bool:
    if not p.exists():
        return False
    if p.is_file():
        return p.stat().st_size > 0
    return any(p.iterdir())


def _move(src: Path, dst: Path, dry_run: bool) -> bool:
    if not src.exists():
        return False
    # 멱등성: 새 위치에 이미 내용이 있으면 source를 *제거*만 (옛 잔재 정리)
    if _is_nonempty(dst):
        if src.exists():
            _log(f"new exists, removing stale source: {src}", dry_run)
            if not dry_run:
                if src.is_dir():
                    shutil.rmtree(src)
                else:
                    src.unlink()
        return False
    _log(f"move: {src} → {dst}", dry_run)
    if not dry_run:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(src), str(dst))
    return True


def _read_label(target: Path) -> str:
    """`.methodology-version`의 project_label 또는 폴더명을 반환."""
    vfile = target / ".methodology-version"
    if vfile.exists():
        try:
            data = json.loads(vfile.read_text(encoding="utf-8"))
            label = data.get("project_label")
            if label:
                return str(label)
        except Exception:
            pass
    return target.name


def _substitute(content: str, label: str, today: str) -> str:
    out = content.replace("[PROJECT_NAME]", label)
    out = out.replace("[YYYY-MM-DD]", today)
    out = out.replace("[PROJECT_MODE]", "applied-project")
    out = out.replace("[fullstack / planning-only]", "applied-project")
    return out


def _materialize_l0(target: Path, label: str, dry_run: bool) -> int:
    """L0 핵심 파일(.ai/context.json, .ai/checkpoint.md)을 *없을 때만* 생성.

    이미 존재하면 사용자 콘텐츠 — 절대 덮어쓰지 않는다.
    템플릿은 본 마이그레이션이 직접 임베드한 *최소* 버전을 사용한다.
    (적용 프로젝트의 templates 폴더는 sync 이전 단계라 비어 있을 수 있음.)
    """
    today = str(date.today())
    created = 0

    context_path = target / ".ai" / "context.json"
    if not context_path.exists():
        _log(f"materialize: .ai/context.json (label={label})", dry_run)
        if not dry_run:
            context_path.parent.mkdir(parents=True, exist_ok=True)
            context_path.write_text(_substitute(_CONTEXT_TEMPLATE, label, today), encoding="utf-8")
        created += 1

    checkpoint_path = target / ".ai" / "checkpoint.md"
    if not checkpoint_path.exists():
        _log(f"materialize: .ai/checkpoint.md", dry_run)
        if not dry_run:
            checkpoint_path.parent.mkdir(parents=True, exist_ok=True)
            checkpoint_path.write_text(_substitute(_CHECKPOINT_TEMPLATE, label, today), encoding="utf-8")
        created += 1

    return created


# ─── 임베디드 템플릿 (마이그레이션이 자기 안에 들고 다님) ──────────────────────


_CONTEXT_TEMPLATE = """\
{
  "schema_version": "1.0",
  "schema_url": ".ai/schema/context.schema.json",
  "project": {
    "name": "[PROJECT_NAME]",
    "kind": "applied-project",
    "domain": null,
    "started_on": "[YYYY-MM-DD]"
  },
  "current_phase": {
    "stage": "stage-1",
    "label": "v3.2 업그레이드 직후 — 도메인 식별·첫 TODO 정렬",
    "since": "[YYYY-MM-DD]"
  },
  "active_skeleton": null,
  "last_session": {
    "ended_at": "[YYYY-MM-DD]T00:00:00Z",
    "agent": {
      "model": "unknown",
      "tool": "unknown",
      "version": "0"
    },
    "host_os": "unknown",
    "checkpoint_file": ".ai/checkpoint.md"
  },
  "must_read": [
    "ONBOARDING.md",
    "10_foundation/WHITEPAPER.md",
    "CLAUDE.md",
    "HANDOFF.md",
    ".ai/checkpoint.md"
  ],
  "must_read_optional": [
    "README.md",
    "20_guides/README.md"
  ],
  "active_todos": [],
  "active_catalog_hits": [],
  "adapters_present": ["generic", "claude"]
}
"""


_CHECKPOINT_TEMPLATE = """\
# Checkpoint — [PROJECT_NAME] v3.2 업그레이드 직후

> Live handoff for the next AI or person.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: (next-session-will-fill)
- Tool: (next-session-will-fill)
- Host: (next-session-will-fill)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` as the immediate handoff.
4. Start from the first actionable item in "다음 사람에게".

## 방금 한 것 (정확히)

- 방법론 v3.1 → v3.2 마이그레이션 적용 ([YYYY-MM-DD]).
- 폴더 재구조화: `10_foundation/`, `60_tools/`, `.ai/` 신설.
- L0 이식성 코어 도입 — `context.json`, `checkpoint.md`, schema/, adapters/.
- `50_resources/{catalog,skeletons,ai_observations}/` 골격 신설.

## 다음 사람에게 (구체적 첫 행동)

1. `.ai/context.json` 의 `project.domain` 을 실제 값으로 채울 것
   (예: `webapp-next`, `data-pipeline`, `slack-bot`).
2. `HANDOFF.md` 의 *Current Focus* 를 본 프로젝트의 실제 첫 작업으로 갱신.
3. 첫 작업이 끝나면 본 checkpoint 를 갱신
   — 형식: `10_foundation/WHITEPAPER.md` §2-2.

## 막혔던 지점

- 없음 (마이그레이션 직후).

## 미해결 결정사항 (Open Questions)

- 도메인 식별자 (`project.domain`).
- 적용할 Skeleton 도메인 (있으면).

## 환경 메모

- 본 프로젝트는 `applied-project` 종류로 운영 중.
- 70_meta/ 는 본 프로젝트에 *주입되지 않음* (메타-방법론 격리).
"""


def migrate(target: Path, dry_run: bool = False) -> None:
    moved = 0
    for old, new in MOVES:
        if _move(target / old, target / new, dry_run):
            moved += 1

    # 새 골격 디렉터리 보장
    for d in ENSURE_DIRS:
        p = target / d
        if not p.exists():
            _log(f"mkdir: {d}", dry_run)
            if not dry_run:
                p.mkdir(parents=True, exist_ok=True)

    # L0 핵심 파일 생성 (없을 때만)
    label = _read_label(target)
    materialized = _materialize_l0(target, label, dry_run)
    if materialized:
        _log(f"materialized {materialized} L0 file(s)", dry_run)

    # 메타-방법론 격리 안전망 — 마이그레이션이 60_meta를 생성하지 않는지 검증
    for forbidden in NEVER_CREATE:
        p = target / forbidden
        if p.exists():
            _log(
                f"⚠ {forbidden}/ 가 적용 프로젝트에 존재합니다 — 외부 프로젝트에 메타-방법론이 새어나갔을 가능성. 수동 확인 필요.",
                dry_run,
            )

    # 빈 50_resources/onboarding/ 정리 (이동 후 잔재)
    onboarding_dir = target / "50_resources" / "onboarding"
    if onboarding_dir.exists():
        has_files = any(p.is_file() for p in onboarding_dir.rglob("*"))
        if not has_files:
            _log("remove empty 50_resources/onboarding/", dry_run)
            if not dry_run:
                try:
                    shutil.rmtree(onboarding_dir)
                except Exception as e:
                    _log(f"50_resources/onboarding/ 정리 실패: {e}", dry_run)
        else:
            _log("50_resources/onboarding/ 에 다른 파일이 남아있음 — 수동 확인 필요", dry_run)

    _log(f"완료 — {moved}개 경로 이동", dry_run)
