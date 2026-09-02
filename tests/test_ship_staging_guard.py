#!/usr/bin/env python3
"""METH-142 · ship 스테이징 확인 가드 단위 테스트 (python3 tests/test_ship_staging_guard.py).

캡슐 `icons__2026-08-27_ship-add-all-on-shared-checkout`: 공유 체크아웃에서 `--no-add-all`
로 ship 하면 인덱스를 그대로 커밋한다 — 다른 세션이 스테이징해 둔 미완성 작업이 함께
커밋돼 프로덕션이 깨졌다. 가드는 «인덱스에 무엇이 담겼는지»를 밝히고 확인을 요구한다.
"""
from __future__ import annotations

import importlib.util
import subprocess
import tempfile
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "methodology", Path(__file__).resolve().parent.parent / "60_tools" / "methodology.py")
m = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(m)


def _git(t: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(t), *args], check=True,
                   capture_output=True)


def _repo(tmp: str) -> Path:
    t = Path(tmp)
    _git(t, "init", "-q", ".")
    _git(t, "config", "user.email", "t@example.com")
    _git(t, "config", "user.name", "t")
    (t / "mine.txt").write_text("a\n")
    (t / "theirs.txt").write_text("b\n")
    _git(t, "add", ".")
    _git(t, "commit", "-qm", "init")
    return t


def test_detects_index_only_path() -> None:
    """스테이징만 되어 있고 작업트리 변경이 없는 경로 = 확인 대상."""
    with tempfile.TemporaryDirectory() as tmp:
        t = _repo(tmp)
        (t / "mine.txt").write_text("mine-edit\n")      # 작업트리에서 편집 중 — 이 세션 것
        (t / "theirs.txt").write_text("theirs-edit\n")
        _git(t, "add", "theirs.txt")                    # 남이 스테이징해 둔 것
        assert m._externally_staged(t) == ["theirs.txt"]


def test_clean_index_is_silent() -> None:
    """인덱스가 비면 경고할 것이 없다 — 오탐 금지."""
    with tempfile.TemporaryDirectory() as tmp:
        t = _repo(tmp)
        (t / "mine.txt").write_text("mine-edit\n")
        assert m._externally_staged(t) == []


def test_untracked_not_counted() -> None:
    """미추적 신규 파일은 인덱스에 없으므로 대상 아님."""
    with tempfile.TemporaryDirectory() as tmp:
        t = _repo(tmp)
        (t / "new.txt").write_text("n\n")
        assert m._externally_staged(t) == []


def test_added_new_file_is_flagged() -> None:
    """새 파일을 add 해 두면 작업트리 diff 가 없어 확인 대상이 된다.

    이 세션이 직접 add 한 것도 걸린다 — 도구는 «누가» 스테이징했는지 알 수 없다.
    그래서 가드는 차단이 아니라 **목록을 보이고 확인을 요구**하고, 확인하면
    `--index-verified` 로 통과한다. 침묵하는 것보다 묻는 것이 싸다.
    """
    with tempfile.TemporaryDirectory() as tmp:
        t = _repo(tmp)
        (t / "new.txt").write_text("n\n")
        _git(t, "add", "new.txt")
        assert m._externally_staged(t) == ["new.txt"]


def main() -> int:
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    failed = 0
    for fn in tests:
        try:
            fn()
            print(f"  ok   {fn.__name__}")
        except AssertionError as e:
            failed += 1
            print(f"  FAIL {fn.__name__}: {e}")
        except Exception as e:  # noqa: BLE001 — 테스트 러너 경계
            failed += 1
            print(f"  ERR  {fn.__name__}: {type(e).__name__}: {e}")
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
