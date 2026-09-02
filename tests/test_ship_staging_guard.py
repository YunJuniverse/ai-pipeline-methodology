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


# ── METH-142 · 훅 sync 면제를 «변경 경로» 로 판정 (캡슐 아님 — 3회 재발한 자체 마찰)
# 예전 훅은 커밋 메시지 접두어 목록으로만 sync 를 면제해 `chore: 방법론 sync …` 가 막혔다.
# 셸 분기 자체는 A/B/C 실 push 로 증명했고(같은 PR 본문), 여기서는 그 분기가 딛고 선
# 단일 소스(`shared-paths`)와 템플릿 내용을 고정한다.

def test_shared_paths_covers_sync_targets() -> None:
    out = m.MANIFEST["shared_paths"]
    for rel in ["20_guides", "60_tools/methodology.py", "60_tools/build-guard.sh"]:
        assert rel in out, rel


def test_hook_template_judges_by_path_not_only_message() -> None:
    """훅 템플릿이 경로 판정 분기를 담고 있는가 — 메시지 단독 판정으로 되돌아가면 실패."""
    src = (Path(__file__).resolve().parent.parent / "60_tools" / "methodology.py").read_text()
    assert "shared-paths" in src            # 단일 소스 호출
    assert "PUSH_RANGE" in src              # 푸시 범위로 변경 경로 산출
    assert "관리 경로 밖 변경이 있다" in src   # 경로 밖이면 검증 진행(무음 우회 금지)



def test_hook_sync_path_check_disables_quotepath() -> None:
    """한글 경로 함정 — core.quotePath 기본값이면 `git diff --name-only` 가 경로를
    "20_guides/30_\\353\\217..." 로 이스케이프해 관리 경로 패턴에 안 걸린다.
    ai-icons·lifeManager 에서 sync push 가 차단된 실사고(METH-145). ASCII 픽스처만으로
    증명했던 A/B/C 가 이걸 못 잡았다 — 이 테스트가 그 구멍을 고정한다."""
    src = (Path(__file__).resolve().parent.parent / "60_tools" / "methodology.py").read_text()
    assert 'git -c core.quotePath=false diff --name-only "$PUSH_RANGE"' in src



# ── METH-146 · 훅의 wrap 은 읽기 전용 (pre-push 가 repo 를 dirty 로 만들던 부작용)
# 훅 경로의 wrap 이 프롬프팅 리포트를 재생성하고 wrap-state 를 부트스트랩해, push 가
# 실패해도 파일이 남았다 → 다음 sync-all 이 «진행 중 작업»으로 오인해 skip(하루 2회).

import argparse


def _live_dir(tmp: str) -> Path:
    t = Path(tmp)
    (t / ".ai").mkdir()
    (t / "HANDOFF.md").write_text("# HANDOFF.md\n\n- **Working on**: x\n")
    (t / "TODO.md").write_text("# TODO\n\n## Done\n")
    return t


def test_wrap_read_only_writes_nothing() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        t = _live_dir(tmp)
        before = {p.relative_to(t) for p in t.rglob("*") if p.is_file()}
        rc = m.cmd_wrap(argparse.Namespace(path=str(t), strict=True, read_only=True))
        after = {p.relative_to(t) for p in t.rglob("*") if p.is_file()}
        assert rc == 0 and after == before, after - before


def test_wrap_without_read_only_bootstraps_state() -> None:
    """대조군 — 플래그 없으면 baseline 을 쓴다(정상 wrap 의 의도된 동작)."""
    with tempfile.TemporaryDirectory() as tmp:
        t = _live_dir(tmp)
        m.cmd_wrap(argparse.Namespace(path=str(t), strict=True, read_only=False))
        assert (t / ".ai" / "wrap-state.json").exists()


def test_hook_template_runs_wrap_read_only() -> None:
    src = (Path(__file__).resolve().parent.parent / "60_tools" / "methodology.py").read_text()
    assert 'wrap --strict --read-only' in src



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
