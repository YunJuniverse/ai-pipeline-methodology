#!/usr/bin/env python3
"""METH-151 — 전수조사 판단 7지점(ADR-006) 중 도구 반영분 회귀 테스트.

D1 checkpoint 세션 절 회전 · D2 land 머지 기록 · D3 같은 날 관찰로그 갱신 인정 ·
D4 공유 체크아웃 가드 범위 · D5 land 필수 체크.
"""
from __future__ import annotations

import importlib.util
import os
import subprocess
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "methodology", Path(__file__).resolve().parent.parent / "60_tools" / "methodology.py")
m = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(m)

_ENV = {"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t", "GIT_COMMITTER_NAME": "t",
        "GIT_COMMITTER_EMAIL": "t@t", "PATH": os.environ.get("PATH", "/usr/bin:/bin")}


def _git(t: Path, *a: str) -> str:
    return subprocess.run(["git", "-C", str(t), *a], check=True, capture_output=True, text=True, env=_ENV).stdout


def _repo(tmp: str) -> Path:
    t = Path(tmp)
    _git(t, "init", "-q", ".")
    (t / "README.md").write_text("r")
    _git(t, "add", "-A")
    _git(t, "commit", "-q", "-m", "init")
    return t


# ── D2 land 기록 — AC 가 다 닫힌 항목만 Done 으로, 진행형 항목은 기록만
TODO = """# TODO

## InProgress

### METH-201 · 끝나는 일
- **acceptance criteria**:
  - [x] 구현
  - [ ] PR 머지 + maincheck → Done 전이

### METH-202 · 여러 PR 로 끝나는 일
- **acceptance criteria**:
  - [x] PR 1
  - [ ] PR 2 반영

### METH-203 · 무관
- [ ] x

## Blocked

## Done

### METH-100 · 옛 완료
"""


def test_land_record_moves_only_finished_items() -> None:
    new, moved, noted = m._land_record_todo(TODO, {"METH-201", "METH-202"}, 190, "abcd1234", "2026-11-09")
    assert moved == ["METH-201"] and noted == ["METH-202"], (moved, noted)
    done = new.split("## Done", 1)[1]
    assert done.index("METH-201") < done.index("METH-100")           # 최신이 맨 위
    assert "- [x] PR 머지 + maincheck → Done 전이" in done
    assert "PR #190 · main `abcd1234`" in done
    inprog = new.split("## InProgress", 1)[1].split("## Blocked", 1)[0]
    assert "METH-202" in inprog and "landed" in inprog and "METH-201" not in inprog
    assert "METH-203" in inprog and inprog.count("landed") == 1      # 무관 항목은 손대지 않는다


def test_land_record_noop_for_unknown_ids() -> None:
    new, moved, noted = m._land_record_todo(TODO, {"LM-9"}, 1, "x", "2026-11-09")
    assert new == TODO and not moved and not noted


# ── D1 checkpoint 세션 절 회전
def test_checkpoint_keeps_latest_sessions() -> None:
    head = "# 세션 체크포인트\n\n> 바통\n\n"
    secs = "".join(f"## 2026-11-0{i} · s{i}\n\n### 방금 한 것\n- {i}\n\n" for i in (9, 8, 7, 6, 5))
    kept, arch, n = m._rotate_checkpoint_sessions(head + secs, keep=3)
    assert n == 2 and "s9" in kept and "s7" in kept and "s6" not in kept
    assert "s6" in arch and "s5" in arch and kept.startswith("# 세션 체크포인트")
    same, _, zero = m._rotate_checkpoint_sessions(head + "## 2026-11-09 · only\n", keep=3)
    assert zero == 0 and same == head + "## 2026-11-09 · only\n"


# ── D5 필수 체크
def test_required_checks_must_pass() -> None:
    rows = [{"name": "vercel-preview", "state": "SUCCESS"}, {"name": "test", "state": "SKIPPED"}]
    assert m._missing_required(rows, ["test"]) == ["test"]          # 프리뷰만 green — 거부
    assert m._missing_required(rows, ["unit"]) == ["unit"]          # 부재도 거부
    assert m._missing_required([{"name": "test", "state": "SUCCESS"}], ["test"]) == []


def test_required_checks_read_from_version_file() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        (t / m.VERSION_FILE_NAME).write_text('{"version": "v4.0", "required_checks": ["validate"]}')
        assert m._required_checks(t) == ["validate"]
        (t / m.VERSION_FILE_NAME).write_text('{"version": "v4.0"}')
        assert m._required_checks(t) == []


# ── D3 같은 날 관찰로그 갱신
def test_same_day_observation_update_counts() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        t = _repo(tmp)
        d = t / "50_resources/ai_observations"
        d.mkdir(parents=True)
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        (d / f"{today}_work.md").write_text("v1")
        (d / "2020-01-01_old.md").write_text("old")
        _git(t, "add", "-A"); _git(t, "commit", "-q", "-m", "obs")
        cur = [f"50_resources/ai_observations/{today}_work.md", "50_resources/ai_observations/2020-01-01_old.md"]
        assert m._observations_updated_today(t, cur) == []              # 안 바꿨으면 인정 안 함
        (d / f"{today}_work.md").write_text("v2")
        (d / "2020-01-01_old.md").write_text("edited")
        assert m._observations_updated_today(t, cur) == [cur[0]]        # 옛 날짜 로그 수정은 인정 안 함


# ── D4 공유 체크아웃 가드 — 미추적 신규 파일만
def test_shared_guard_ignores_tracked_edits_and_own_log() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        t = _repo(tmp)
        wt = Path(tmp).parent / (Path(tmp).name + "-wt")
        _git(t, "worktree", "add", "-q", "--detach", str(wt))
        try:
            (t / "README.md").write_text("edited")                       # 추적 파일 수정
            assert m._shared_checkout_foreign_files(t) is None
            d = t / "50_resources/ai_observations"; d.mkdir(parents=True)
            (d / "2026-11-09_mine.md").write_text("m")                    # 이 세션 로그 1건
            assert m._shared_checkout_foreign_files(t) is None
            time.sleep(0.01)
            (d / "2026-11-09_other.md").write_text("o")                   # 2건 = 남의 로그 신호
            r = m._shared_checkout_foreign_files(t)
            assert r and len(r[1]) == 2, r
            (d / "2026-11-09_other.md").unlink()
            (t / "foreign.txt").write_text("f")
            r = m._shared_checkout_foreign_files(t)
            assert r and r[1] == ["foreign.txt"], r
        finally:
            _git(t, "worktree", "remove", "--force", str(wt))


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
