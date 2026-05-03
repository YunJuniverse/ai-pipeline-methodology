"""v3.0 → v3.1 마이그레이션.

변경 요약:
- docs/archive/planning-guides/  →  10_guides/
- docs/templates/                →  40_resources/templates/
- docs/prompts/                  →  40_resources/prompts/
- docs/archive/{decisions,harness,legacy-methodology}/  →  90_archive/...
- docs/methodology-graph.json    →  methodology-graph.json (루트)
- docs/adr/                      →  30_dev/adr/
- docs/snapshots/                →  30_dev/snapshots/
- 신규 폴더 20_planning/, 30_dev/는 sync가 shared로 채움 (빈 디렉터리만 보장)

멱등성: 새 위치에 이미 콘텐츠가 있으면 이동을 skip.
"""

from __future__ import annotations

import shutil
from pathlib import Path

MOVES = [
    # (old_relative, new_relative)
    ("docs/archive/planning-guides", "10_guides"),
    ("docs/templates",               "40_resources/templates"),
    ("docs/prompts",                 "40_resources/prompts"),
    ("docs/archive/decisions",       "90_archive/decisions"),
    ("docs/archive/harness",         "90_archive/harness"),
    ("docs/archive/legacy-methodology", "90_archive/legacy-methodology"),
    ("docs/methodology-graph.json",  "methodology-graph.json"),
    ("docs/adr",                     "30_dev/adr"),
    ("docs/snapshots",               "30_dev/snapshots"),
]

ENSURE_DIRS = ["20_planning", "30_dev/adr", "30_dev/snapshots", "40_resources/templates", "40_resources/prompts"]


def _log(msg: str, dry: bool) -> None:
    prefix = "[migrate v3.0→v3.1]"
    print(f"{prefix} {'(dry-run) ' if dry else ''}{msg}")


def _move(src: Path, dst: Path, dry_run: bool) -> bool:
    if not src.exists():
        return False
    if dst.exists() and any(dst.iterdir() if dst.is_dir() else [True]):
        _log(f"skip (이미 존재): {dst.relative_to(dst.parents[len(dst.parents)-1])}", dry_run)
        return False
    _log(f"move: {src} → {dst}", dry_run)
    if not dry_run:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(src), str(dst))
    return True


def migrate(target: Path, dry_run: bool = False) -> None:
    moved = 0
    for old, new in MOVES:
        if _move(target / old, target / new, dry_run):
            moved += 1

    # 빈 docs/ 디렉터리 정리 (파일이 하나도 없으면 통째로 제거)
    docs_dir = target / "docs"
    if docs_dir.exists():
        has_files = any(p.is_file() for p in docs_dir.rglob("*"))
        if not has_files:
            _log("remove empty docs/ tree", dry_run)
            if not dry_run:
                try:
                    shutil.rmtree(docs_dir)
                except Exception as e:
                    _log(f"docs/ 정리 실패: {e}", dry_run)
        else:
            _log("docs/ 에 다른 파일이 남아있음 — 수동 확인 필요", dry_run)

    # 새 골격 디렉터리 보장 (sync가 채울 자리)
    for d in ENSURE_DIRS:
        p = target / d
        if not p.exists():
            _log(f"mkdir: {d}", dry_run)
            if not dry_run:
                p.mkdir(parents=True, exist_ok=True)

    _log(f"완료 — {moved}개 경로 이동", dry_run)
