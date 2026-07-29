#!/usr/bin/env python3
"""METH-122(rotate·경성 한도·신선도) 단위 테스트 (python3 tests/test_rotate_guards.py).

plain assert + 자체 러너. 순수 텍스트 로직(_rotate_*)과 파일 기반 한도 검사만 검증.
"""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "60_tools"))
import importlib.util

_spec = importlib.util.spec_from_file_location(
    "methodology",
    Path(__file__).resolve().parent.parent / "60_tools" / "methodology.py",
)
m = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(m)


def _todo(n_done: int) -> str:
    items = "".join(f"### T-{i:03d} · 항목{i}\n- **notes**: n{i}\n\n" for i in range(n_done))
    return ("# TODO.md\n\n> 안내문에 `## Done`)를 그대로 파싱한다는 문장이 있다.\n\n"
            "## Backlog\n\n### B-1 · 백로그\n- x\n\n## Ready\n\n## InProgress\n\n## Blocked\n\n"
            f"## Done\n\n{items}> 꼬리 주석\n")


def test_rotate_todo_keeps_newest_and_archives_rest() -> None:
    text = _todo(7)
    new_text, archive, moved = m._rotate_todo_done(text, keep=4)
    assert moved == 3
    for k in ["T-000", "T-001", "T-002", "T-003"]:
        assert f"### {k}" in new_text
    for k in ["T-004", "T-005", "T-006"]:
        assert f"### {k}" not in new_text and f"### {k}" in archive
    assert "## Blocked" in new_text and "### B-1" in new_text  # 다른 섹션 무손상
    assert "안내문에" in new_text  # 6행류 안내문 무손상 (index 오매칭 계보 방지)


def test_rotate_todo_noop_within_cap() -> None:
    text = _todo(3)
    new_text, archive, moved = m._rotate_todo_done(text, keep=4)
    assert moved == 0 and archive == "" and new_text == text


def _handoff(n_bullets: int) -> str:
    bullets = "".join(f"- 2026-07-{i:02d}: **변경{i}** — 내용\n" for i in range(1, n_bullets + 1))
    return ("# HANDOFF.md\n\n- **Working on**: **작업** (2026-07-29) — 진행\n\n"
            f"## Recent Changes\n\n> 최근 5건만 유지\n\n{bullets}")


def test_rotate_recent_changes() -> None:
    text = _handoff(8)
    new_text, archive, moved = m._rotate_recent_changes(text, keep=5)
    assert moved == 3
    assert new_text.count("- 2026-07-") == 5 and archive.count("- 2026-07-") == 3
    assert "- 2026-07-01" in new_text and "- 2026-07-06" in archive
    assert "> 최근 5건만 유지" in new_text  # 머리 주석 보존


def test_rotate_recent_noop() -> None:
    text = _handoff(4)
    _, archive, moved = m._rotate_recent_changes(text, keep=5)
    assert moved == 0 and archive == ""


def test_hard_violations_thresholds() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        (t / ".ai").mkdir()
        (t / "HANDOFF.md").write_text("\n" * 200)          # 150 < 200 < 300 — 연성만
        (t / ".ai" / "checkpoint.md").write_text("\n" * 500)  # > 400 — 경성
        (t / "TODO.md").write_text(_todo(25))               # Done 25 > 20 — 경성
        hard = m.live_file_hard_violations(t)
        assert len(hard) == 2, hard
        assert any("checkpoint" in v for v in hard) and any("Done 25건" in v for v in hard)
        soft = m.live_file_size_warnings(t)
        assert any("HANDOFF" in w for w in soft)


def test_staleness_needs_git() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        # git repo 아님 → 커밋 날짜 없음 → 경고 없음 (안전 기본값)
        assert m.staleness_warnings(Path(tmp)) == []


def main() -> int:
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    failed = 0
    for t in tests:
        try:
            t()
            print(f"  ok   {t.__name__}")
        except AssertionError as e:
            failed += 1
            print(f"  FAIL {t.__name__}: {e}")
        except Exception as e:  # noqa: BLE001 — 테스트 러너 경계
            failed += 1
            print(f"  ERR  {t.__name__}: {type(e).__name__}: {e}")
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
