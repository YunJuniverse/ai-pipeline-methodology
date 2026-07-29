#!/usr/bin/env python3
"""METH-120(maincheck)·METH-121(observe 스키마 강제) 단위 테스트 (python3 tests/test_maincheck_observe.py).

plain assert + 자체 러너. maincheck은 임시 git repo로 실검증,
observe는 순수 로직(normalize_repeat_of/parse_friction_item/validate/warnings)만.
"""
from __future__ import annotations

import argparse
import subprocess
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


def test_repeat_of_null_variants() -> None:
    for v in ["", "null", "none", "no", "-", "repeat_of:none"]:
        assert m.normalize_repeat_of(v) is None, v


def test_repeat_of_prefix_pollution_stripped() -> None:
    assert m.normalize_repeat_of("repeat_of:d3-tick-zero") == "d3-tick-zero"
    assert m.normalize_repeat_of("repeat_of:repeat_of:kanban-drag") == "kanban-drag"


def test_repeat_of_valid_forms() -> None:
    assert m.normalize_repeat_of("mobile-ui-fixes") == "mobile-ui-fixes"
    assert m.normalize_repeat_of("2026-07-15_ai-icons-talmo-sync") == "2026-07-15_ai-icons-talmo-sync"
    assert m.normalize_repeat_of("C-014") == "C-014"


def test_repeat_of_rejects_bare_yes_and_freetext() -> None:
    for bad in ["yes", "repeat", "reviews 중복 삽입 지뢰와 동류", "TALMO-064 판매량 로직"]:
        try:
            m.normalize_repeat_of(bad)
        except ValueError:
            continue
        raise AssertionError(f"거부돼야 함: {bad}")


def test_friction_item_normalizes_repeat_of() -> None:
    item = m.parse_friction_item("어디|10|해법|repeat_of:anchor-slug", 1)
    assert item["repeat_of"] == "anchor-slug"
    item2 = m.parse_friction_item("어디|10|해법|null", 2)
    assert item2["repeat_of"] is None and item2["id"] == "F-002"


def test_multiple_frictions_get_sequential_ids() -> None:
    items = [m.parse_friction_item(r, i) for i, r in enumerate(
        ["a|1|r|null", "b|2|r|null", "c|3|r|null"], start=1)]
    assert [i["id"] for i in items] == ["F-001", "F-002", "F-003"]


def _obs_payload(**over) -> dict:
    base = {
        "session_id": "2026-07-29_test-entry",
        "agent": "claude-fable-5", "tool": "claude-code", "host_os": "darwin",
        "domain": "fullstack", "task_type": "feature",
        "stack_used": ["python3"], "flow_used": "ad-hoc",
        "friction": [], "prompt_patterns": [], "rounds": [],
        "summary": "요약", "created_at": "2026-07-29T00:00:00Z",
    }
    base.update(over)
    return base


def test_render_empty_prompt_patterns_validates() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp) / "2026-07-29_test-entry.md"
        p.write_text(m.render_observation(_obs_payload()), encoding="utf-8")
        errors = m.validate_observation_file(p)
        assert errors == [], errors


def test_validate_rejects_polluted_repeat_of_in_file() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp) / "2026-07-29_test-entry.md"
        friction = [{"id": "F-001", "where": "w", "cost_minutes": 5,
                     "resolution": "r", "repeat_of": "자유 서술 텍스트"}]
        p.write_text(m.render_observation(_obs_payload(friction=friction)), encoding="utf-8")
        errors = m.validate_observation_file(p)
        assert any("repeat_of" in e for e in errors), errors


def test_quality_warnings_flag_unknown_and_boilerplate() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp) / "2026-07-29_test-entry.md"
        payload = _obs_payload(agent="unknown", tool="unknown", domain="meta",
                               prompt_patterns=["l1 observation capture"], rounds=[1])
        p.write_text(m.render_observation(payload), encoding="utf-8")
        warns = m.observation_quality_warnings(p)
        assert any("unknown" in w for w in warns), warns
        assert any("meta" in w for w in warns), warns
        assert any("상용구" in w for w in warns), warns


def _git(cwd: Path, *args: str) -> str:
    return subprocess.check_output(["git", "-C", str(cwd), *args], text=True,
                                   stderr=subprocess.DEVNULL).strip()


def test_maincheck_detects_unreached_commit() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        remote = Path(tmp) / "remote.git"
        subprocess.run(["git", "init", "-q", "--bare", "-b", "main", str(remote)], check=True)
        work = Path(tmp) / "work"
        subprocess.run(["git", "clone", "-q", str(remote), str(work)], check=True,
                       stderr=subprocess.DEVNULL)
        _git(work, "config", "user.email", "t@t"); _git(work, "config", "user.name", "t")
        (work / "a.txt").write_text("a")
        _git(work, "add", "a.txt"); _git(work, "commit", "-q", "-m", "on-main")
        _git(work, "push", "-q", "origin", "main")
        reached = _git(work, "rev-parse", "HEAD")
        _git(work, "checkout", "-q", "-b", "feat/x")
        (work / "b.txt").write_text("b")
        _git(work, "add", "b.txt"); _git(work, "commit", "-q", "-m", "stranded")
        stranded = _git(work, "rev-parse", "HEAD")

        ns_ok = argparse.Namespace(path=str(work), sha=[reached], no_fetch=True)
        ns_bad = argparse.Namespace(path=str(work), sha=[stranded], no_fetch=True)
        ns_mixed = argparse.Namespace(path=str(work), sha=[reached, stranded], no_fetch=True)
        assert m.cmd_maincheck(ns_ok) == 0
        assert m.cmd_maincheck(ns_bad) == 1
        assert m.cmd_maincheck(ns_mixed) == 1


def test_maincheck_bad_ref() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp)
        subprocess.run(["git", "init", "-q", "-b", "main", str(work)], check=True)
        ns = argparse.Namespace(path=str(work), sha=["HEAD"], no_fetch=True)
        assert m.cmd_maincheck(ns) == 1  # 원격 없음 → 실패


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
