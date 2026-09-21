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


# ── METH-148 판단 ① friction phase (선택 필드, 닫힌 5값)
def test_friction_phase_optional_trailing_field() -> None:
    it = m.parse_friction_item("배포|30|자격증명 없음 a|b|null|deploy", 0)
    assert it["phase"] == "deploy" and it["repeat_of"] is None and "a|b" in it["resolution"]
    it2 = m.parse_friction_item("배포|30|원인|null", 0)
    assert "phase" not in it2                          # 선택 — 없어도 유효


def test_friction_phase_unknown_value_not_consumed() -> None:
    # 닫힌 5값이 아닌 마지막 토큰은 phase 로 먹지 않는다 → repeat_of 로 남는다
    it = m.parse_friction_item("w|5|r|x|some-slug", 0)
    assert "phase" not in it and it["repeat_of"] == "some-slug"


# ── METH-148 thinktank 마찰 비용 회고
def test_friction_retro_aggregates_cost_month_repeat_phase() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)
        def obs(name: str, items: str) -> Path:
            p = d / name
            p.write_text("---\nsession_id: x\nfriction:\n" + items + "prompt_patterns: []\n---\n")
            return p
        f1 = obs("2026-08-01_a.md", "  - id: F-001\n    where: \"w1\"\n    cost_minutes: 30\n    resolution: \"r\"\n    repeat_of: null\n    phase: diagnose\n")
        f2 = obs("2026-09-02_b.md", "  - id: F-001\n    where: \"w2\"\n    cost_minutes: 10\n    resolution: \"r\"\n    repeat_of: prior-slug\n")
        out = "\n".join(m._friction_retro_section([f1, f2]))
        assert "2건 · 40분" in out and "재발(repeat_of) 1건 10분" in out and "(**25%**)" in out
        assert "phase 기입률: **1/2**" in out and "diagnose 1건 30분" in out
        assert "| 2026-08 | 1 | 30 | 0 |" in out and "| 2026-09 | 1 | 10 | 10 |" in out



def test_adr_citation_repo_qualified_skipped() -> None:
    """`icons:ADR-0029` 처럼 repo 를 붙인 인용은 다른 repo 의 ADR — 경고하지 않는다(METH-148)."""
    with tempfile.TemporaryDirectory() as tmp:
        t = _repo(tmp)
        (t / "40_dev" / "adr").mkdir(parents=True)
        (t / "note.md").write_text("사례: icons:ADR-0029 조항 · 그리고 ADR-0077 (이 repo 에 없음)\n")
        out = m._adr_citations_missing(t)
        assert ("note.md", "ADR-0077") in out and all(c != "ADR-0029" for _, c in out)



def test_adr_citation_ignores_code_examples() -> None:
    """형식 예시(인라인 코드·코드 블록)는 인용이 아니다 — 지침 02·18 오경고 방지(METH-148)."""
    with tempfile.TemporaryDirectory() as tmp:
        t = _repo(tmp)
        (t / "40_dev" / "adr").mkdir(parents=True)
        (t / "note.md").write_text("형식: `ADR-001`\n```yaml\nblocking: [ADR-005]\n```\n진짜 인용 ADR-0088\n")
        out = [c for _, c in m._adr_citations_missing(t)]
        assert out == ["ADR-0088"], out



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
