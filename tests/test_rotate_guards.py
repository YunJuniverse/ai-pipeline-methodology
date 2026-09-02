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
    new_text, archive, moved, undated = m._rotate_todo_done(text, keep=4)
    assert moved == 3 and undated == 7  # 날짜 없는 항목은 미판정으로 집계
    for k in ["T-000", "T-001", "T-002", "T-003"]:
        assert f"### {k}" in new_text
    for k in ["T-004", "T-005", "T-006"]:
        assert f"### {k}" not in new_text and f"### {k}" in archive
    assert "## Blocked" in new_text and "### B-1" in new_text  # 다른 섹션 무손상
    assert "안내문에" in new_text  # 6행류 안내문 무손상 (index 오매칭 계보 방지)


def test_rotate_todo_noop_within_cap() -> None:
    text = _todo(3)
    new_text, archive, moved, _ = m._rotate_todo_done(text, keep=4)
    assert moved == 0 and archive == "" and new_text == text


def _todo_dated(dates: list[str]) -> str:
    """날짜를 가진 Done 항목들 — 문서 순서는 인자 순서 그대로."""
    items = "".join(
        f"### T-{i:03d} · 항목{i}\n- **notes**: {d} 완료\n\n" for i, d in enumerate(dates))
    return f"# TODO.md\n\n## Blocked\n\n## Done\n\n{items}"


# ── METH-142 · Done 순서 가정 검사 (캡슐 icons__2026-08-22_rotate-assumes-sorted-done)
# `items[:keep]` 는 «문서 상위 N건»인데 docstring 은 «최신 keep건»이라 주장했다.
# 순서가 어긋나면 최신 항목이 조용히 아카이브된다 — negative case 로 실효를 고정한다.

def test_rotate_aborts_when_archiving_newer_than_kept() -> None:
    # 유지 2건(08-01·07-01) 아래에 08-20 이 있다 — 경계를 넘는 역전
    text = _todo_dated(["2026-08-01", "2026-07-01", "2026-08-20"])
    try:
        m._rotate_todo_done(text, keep=2)
    except m.RotateOrderError as e:
        assert "2026-08-20" in str(e) and "--force-order" in str(e)
        return
    raise AssertionError("역전을 감지하지 못했다 — 최신 항목이 조용히 아카이브된다")


def test_rotate_force_order_overrides() -> None:
    text = _todo_dated(["2026-08-01", "2026-07-01", "2026-08-20"])
    _, archive, moved, _ = m._rotate_todo_done(text, keep=2, force_order=True)
    assert moved == 1 and "T-002" in archive  # 의도된 순서면 통과시킨다


def test_rotate_passes_when_order_is_newest_first() -> None:
    text = _todo_dated(["2026-08-20", "2026-08-01", "2026-07-01"])
    _, archive, moved, undated = m._rotate_todo_done(text, keep=2)
    assert moved == 1 and undated == 0 and "T-002" in archive


def test_rotate_undated_items_do_not_trigger_abort() -> None:
    # 날짜 없는 항목은 판정 대상이 아니다 — 검사 못 함 ≠ 위반 (지침 23 §1-2)
    text = _todo(6)
    _, _, moved, undated = m._rotate_todo_done(text, keep=4)
    assert moved == 2 and undated == 6


def test_item_date_uses_latest_date_in_item() -> None:
    # 착수일(07-25)이 아니라 최근 활동일(08-22)을 항목 시점으로 본다 — METH-116 실사례
    assert m._item_date("### X\n- notes: 2026-07-25 착수, 2026-08-22 land\n") == "2026-08-22"
    assert m._item_date("### Y\n- notes: 날짜 없음\n") is None


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


# ── METH-142 · 라이브 파일 구조 검증 (상류 실사고 2026-09-02)
# 인덱스 기반 편집으로 `# HANDOFF.md` 제목이 덮이고 Working-on 이 둘이 된 채
# PR 6개를 지났다 — boot 가 첫 매치만 읽어 출력은 정상으로 보였기 때문이다.

def test_structure_flags_duplicate_working_on_as_error() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        (t / "HANDOFF.md").write_text(
            "- **Working on**: 새 작업(제목을 덮은 줄)\n\n> Live state file.\n\n"
            "- **Working on**: 옛 작업(스테일)\n- **Blockers**: none.\n")
        errors, warns = m.live_file_structure_issues(t)
        assert any("Working on" in e and "2개" in e for e in errors), errors
        assert any("제목" in w for w in warns), warns


def test_structure_absence_is_warning_not_error() -> None:
    """부재·드리프트는 경고다 — 다운스트림 12곳 실측에서 부재가 흔했다(오탐 금지)."""
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        (t / "HANDOFF.md").write_text("# HANDOFF.md\n\n- **Blockers**: none.\n")
        (t / "TODO.md").write_text("# TODO\n\n## Done\n")
        errors, warns = m.live_file_structure_issues(t)
        assert errors == [], errors
        assert any("Working on" in w for w in warns)
        assert any("Backlog" in w for w in warns)


def test_structure_duplicate_kanban_section_is_error() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        (t / "TODO.md").write_text("# TODO\n\n## Done\n\n### A\n\n## Done\n")
        errors, _ = m.live_file_structure_issues(t)
        assert any("## Done" in e for e in errors), errors


def test_structure_clean_files_are_silent() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        (t / "HANDOFF.md").write_text(
            "# HANDOFF.md\n\n- **Working on**: 하나뿐\n\n## Active Links\n\n## Recent Changes\n- x\n")
        (t / "TODO.md").write_text(
            "# TODO\n\n## Backlog\n\n## Ready\n\n## InProgress\n\n## Blocked\n\n## Done\n")
        assert m.live_file_structure_issues(t) == ([], [])


def test_structure_accepts_non_bold_working_on() -> None:
    """boot 파서(METH-114)가 비볼드 형식을 허용하므로 검사도 같은 계약을 따른다."""
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        (t / "HANDOFF.md").write_text("# HANDOFF.md\n\n- Working on: 비볼드 스캐폴드 형식\n")
        errors, warns = m.live_file_structure_issues(t)
        assert errors == [] and not any("Working on" in w for w in warns)



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
