#!/usr/bin/env python3
"""METH-147 도구 묶음 단위 테스트 (python3 tests/test_meth147_tools.py).

캡슐 5회차 반영분 — observe 세로줄 파서 · wrap baseline HEAD 재계산 · ship 공유 체크아웃 가드 ·
reserve 번호 산출 · land local-ci 전제 · boot preflight · wrap ADR 인용 검사.
"""
from __future__ import annotations

import importlib.util
import json
import subprocess
import tempfile
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "methodology", Path(__file__).resolve().parent.parent / "60_tools" / "methodology.py")
m = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(m)


def _git(t: Path, *a: str) -> str:
    return subprocess.run(["git", "-C", str(t), *a], check=True, capture_output=True, text=True).stdout


def _repo(tmp: str) -> Path:
    t = Path(tmp)
    _git(t, "init", "-q", ".")
    _git(t, "config", "user.email", "t@example.com")
    _git(t, "config", "user.name", "t")
    (t / ".ai").mkdir()
    (t / "HANDOFF.md").write_text("# HANDOFF.md\n\n- **Working on**: x\n")
    (t / "TODO.md").write_text("# TODO\n\n## Blocked\n\n## Done\n")
    (t / ".ai" / "checkpoint.md").write_text("# cp\n")
    _git(t, "add", ".")
    _git(t, "commit", "-qm", "init")
    return t


# ── #9 observe: resolution 본문의 세로줄 허용
def test_friction_pipe_inside_resolution() -> None:
    item = m.parse_friction_item("where|10|grep 'a|b' 로 찾음 — 세로줄 포함|null", 0)
    assert item["where"] == "where" and item["cost_minutes"] == 10
    assert "a|b" in item["resolution"]


def test_friction_too_few_fields_still_errors() -> None:
    try:
        m.parse_friction_item("where|10|only-three", 0)
    except ValueError:
        return
    raise AssertionError("3필드가 통과됐다")


# ── 판단 ① wrap baseline = HEAD
def test_head_wrap_state_matches_committed_files() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        t = _repo(tmp)
        st = m.head_wrap_state(t)
        assert st and st["source"] == "HEAD"
        assert st["files"]["HANDOFF.md"]["sha256"] == m.file_sha256(t / "HANDOFF.md")
        (t / "HANDOFF.md").write_text("# HANDOFF.md\n\n- **Working on**: 바뀜\n")
        st2 = m.head_wrap_state(t)
        assert st2["files"]["HANDOFF.md"]["sha256"] != m.file_sha256(t / "HANDOFF.md")  # 작업트리 변경 감지 가능
        assert not (t / ".ai" / "wrap-state.json").exists()   # 파일을 쓰지 않는다


def test_head_wrap_state_none_outside_git() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        assert m.head_wrap_state(Path(tmp)) is None


# ── 묶음 A ship: 공유 체크아웃 감지
def test_shared_checkout_detected_only_in_main_with_worktrees() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        t = _repo(tmp)
        assert m._shared_checkout_foreign_files(t) is None          # 워크트리 1개
        wt = Path(tmp) / "wt"
        _git(t, "worktree", "add", "-q", "--detach", str(wt))
        (t / "foreign.txt").write_text("남의 파일\n")
        r = m._shared_checkout_foreign_files(t)
        assert r and r[0] == 2 and "foreign.txt" in r[1]
        assert m._shared_checkout_foreign_files(wt) is None          # 격리 워크트리 안에서는 안 걸린다
        _git(t, "worktree", "remove", "--force", str(wt))


# ── 판단 ③ reserve 번호 산출
def test_max_todo_id_scans_prefix_only() -> None:
    assert m._max_todo_id("METH-147 · x\n### METH-150\nOTHER-999", "METH") == 150
    assert m._max_todo_id("", "METH") == 0


# ── #8 local-ci 전제: Blocked 에 CI 결제 판정
def test_blocked_ci_decision_required() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        (t / "TODO.md").write_text("# TODO\n\n## Blocked\n\n### X · CI 결제 안 함 — PM 판정\n\n## Done\n")
        assert m._blocked_has_ci_decision(t)
        (t / "TODO.md").write_text("# TODO\n\n## Blocked\n\n## Done\n")
        assert not m._blocked_has_ci_decision(t)


# ── #19 boot preflight
def test_required_local_files_missing() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        (t / m.VERSION_FILE_NAME).write_text(json.dumps({"required_local_files": [".deploy.env", "README.md"]}))
        (t / "README.md").write_text("r")
        assert m._required_local_files_missing(t) == [".deploy.env"]


# ── #11 wrap ADR 인용 검사
def test_adr_citation_missing_flagged() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        t = _repo(tmp)
        (t / "40_dev" / "adr").mkdir(parents=True)
        (t / "40_dev" / "adr" / "ADR-0011-x.md").write_text("# ADR-0011\n")
        (t / "note.md").write_text("근거: ADR-0011 §1 과 ADR-0029 폭발 그래프 금지\n")
        out = m._adr_citations_missing(t)
        assert ("note.md", "ADR-0029") in out and all(c != "ADR-0011" for _, c in out)


def main() -> int:
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    failed = 0
    for fn in tests:
        try:
            fn(); print(f"  ok   {fn.__name__}")
        except AssertionError as e:
            failed += 1; print(f"  FAIL {fn.__name__}: {e}")
        except Exception as e:  # noqa: BLE001
            failed += 1; print(f"  ERR  {fn.__name__}: {type(e).__name__}: {e}")
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
