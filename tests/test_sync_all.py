#!/usr/bin/env python3
"""sync-all 발견·가드 로직 단위 테스트 (의존성 없음 — python3 tests/test_sync_all.py).

테스트 인프라(pytest)가 없어 plain assert + 자체 러너로 구성한다.
파일시스템/ git 을 건드리는 cmd_sync_all 전체가 아니라, 판단 로직
(_discover_downstreams / _sync_all_skip_reason / _is_behind)만 검증한다.
"""
from __future__ import annotations

import argparse
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


def _mk_project(root: Path, name: str, has_version: bool = True) -> Path:
    d = root / name
    d.mkdir(parents=True)
    if has_version:
        (d / m.VERSION_FILE_NAME).write_text('{"methodology_version": "v4.0"}')
    return d


def test_discover_picks_only_versioned_dirs() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        _mk_project(root, "alpha")
        _mk_project(root, "beta")
        _mk_project(root, "not-a-project", has_version=False)
        (root / "loose-file.txt").write_text("x")
        found = {p.name for p in m._discover_downstreams(root)}
        assert found == {"alpha", "beta"}, found


def test_discover_excludes_methodology_root() -> None:
    # METHODOLOGY_ROOT 자신은 발견 대상에서 제외된다.
    parent = m.METHODOLOGY_ROOT.parent
    found = m._discover_downstreams(parent)
    assert m.METHODOLOGY_ROOT not in [p.resolve() for p in found]


def test_discover_sorted() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        for n in ["zeta", "alpha", "mid"]:
            _mk_project(root, n)
        names = [p.name for p in m._discover_downstreams(root)]
        assert names == sorted(names), names


def _args(include_dirty: bool = False, allow_nonmain: bool = False) -> argparse.Namespace:
    return argparse.Namespace(include_dirty=include_dirty, allow_nonmain=allow_nonmain)


def test_skip_non_git() -> None:
    s = {"branch": None, "dirty": 0, "path": Path("/x")}
    assert m._sync_all_skip_reason(s, _args()) is not None


def test_skip_dirty_by_default_and_override() -> None:
    s = {"branch": "main", "dirty": 3, "path": Path("/x")}
    assert "미커밋" in m._sync_all_skip_reason(s, _args())
    assert m._sync_all_skip_reason(s, _args(include_dirty=True)) is None


def test_skip_nonmain_by_default_and_override() -> None:
    s = {"branch": "feature/x", "dirty": 0, "path": Path("/x")}
    assert "기본 브랜치" in m._sync_all_skip_reason(s, _args())
    assert m._sync_all_skip_reason(s, _args(allow_nonmain=True)) is None


def test_clean_main_not_skipped() -> None:
    for br in ("main", "master"):
        s = {"branch": br, "dirty": 0, "path": Path("/x")}
        assert m._sync_all_skip_reason(s, _args()) is None, br


def test_dirty_takes_precedence_over_nonmain() -> None:
    # dirty 이면서 비-main 일 때 dirty 사유가 먼저 잡힌다(진행 중 작업 보호 우선).
    s = {"branch": "feature/x", "dirty": 2, "path": Path("/x")}
    assert "미커밋" in m._sync_all_skip_reason(s, _args())


def test_is_behind() -> None:
    assert m._is_behind({"version": "v3.0", "applied_commit": "abc"}, "abc") is True
    assert m._is_behind({"version": m.METHODOLOGY_VERSION,
                         "applied_commit": "old"}, "new") is True
    assert m._is_behind({"version": m.METHODOLOGY_VERSION,
                         "applied_commit": "same"}, "same") is False
    assert m._is_behind({"version": m.METHODOLOGY_VERSION,
                         "applied_commit": "unknown"}, "new") is False


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
