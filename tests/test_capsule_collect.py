#!/usr/bin/env python3
"""캡슐 outbox / collect 판단 로직 단위 테스트 (METH-117 — python3 tests/test_capsule_collect.py).

테스트 인프라(pytest)가 없어 plain assert + 자체 러너로 구성한다.
git·네트워크를 건드리는 collect 전체가 아니라 순수 로직
(render/validate/parse/_collect_plan/_capsule_policy/capsule_files)만 검증한다.
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


def _payload(**over) -> dict:
    base = {
        "id": "myrepo__2026-07-29_ppt-deck",
        "origin_repo": "myrepo",
        "type": "guide-update",
        "target": "guide-22",
        "refs": ["abc1234", "40_dev/snapshots/x.md"],
        "friction_ref": None,
        "created": "2026-07-29T00:00:00Z",
        "summary": "차트 파이프라인을 지침 22에 추가 제안",
        "evidence": ["빌드 3회 재사용"],
    }
    base.update(over)
    return base


def test_render_validate_roundtrip() -> None:
    text = m.render_capsule(_payload())
    errors = m.validate_capsule_text(text, "2026-07-29_ppt-deck.md", "myrepo")
    assert errors == [], errors


def test_parse_frontmatter_fields() -> None:
    meta = m.parse_capsule_frontmatter(m.render_capsule(_payload()))
    assert meta["id"] == "myrepo__2026-07-29_ppt-deck"
    assert meta["origin_repo"] == "myrepo"
    assert meta["type"] == "guide-update"
    assert meta["target"] == "guide-22"
    assert meta["refs"] == ["abc1234", "40_dev/snapshots/x.md"]


def test_validate_rejects_bad_type() -> None:
    text = m.render_capsule(_payload(type="brilliant-idea"))
    errors = m.validate_capsule_text(text, "2026-07-29_ppt-deck.md", "myrepo")
    assert any("type" in e for e in errors), errors


def test_validate_rejects_id_mismatch() -> None:
    text = m.render_capsule(_payload(id="otherrepo__2026-07-29_ppt-deck"))
    errors = m.validate_capsule_text(text, "2026-07-29_ppt-deck.md", "myrepo")
    assert any("id" in e for e in errors), errors


def test_validate_rejects_body_dump() -> None:
    # 포인터+요약 원칙 — 본문 원문 덤프 차단
    text = m.render_capsule(_payload(evidence=["줄"] * (m.CAPSULE_BODY_MAX_LINES + 10)))
    errors = m.validate_capsule_text(text, "2026-07-29_ppt-deck.md", "myrepo")
    assert any("원문 덤프" in e for e in errors), errors


def test_validate_rejects_no_frontmatter() -> None:
    errors = m.validate_capsule_text("그냥 텍스트", "2026-07-29_x.md", "myrepo")
    assert errors, errors


def test_collect_plan_dedupes_by_ledger() -> None:
    text = m.render_capsule(_payload())
    ledger = {"collected": {"myrepo__2026-07-29_ppt-deck": {"repo": "myrepo"}}}
    new_items, dup = m._collect_plan({"2026-07-29_ppt-deck.md": text}, "myrepo", ledger)
    assert new_items == [] and dup == 1, (new_items, dup)


def test_collect_plan_new_capsule_passes() -> None:
    text = m.render_capsule(_payload())
    new_items, dup = m._collect_plan({"2026-07-29_ppt-deck.md": text}, "myrepo", {"collected": {}})
    assert dup == 0 and len(new_items) == 1, (new_items, dup)
    name, cid, _ = new_items[0]
    assert name == "2026-07-29_ppt-deck.md" and cid == "myrepo__2026-07-29_ppt-deck"


def test_collect_plan_fallback_id_without_frontmatter() -> None:
    # frontmatter 없는(구식/손상) 캡슐도 repo__stem 폴백 id로 원장 관리
    new_items, _ = m._collect_plan({"2026-07-29_raw.md": "본문만"}, "repox", {"collected": {}})
    assert new_items[0][1] == "repox__2026-07-29_raw"


def test_capsule_files_ignores_readme_and_badnames() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        d = base / m.OUTBOX_DIR
        d.mkdir(parents=True)
        (d / "_README.md").write_text("doc")
        (d / "notes.md").write_text("잘못된 이름")
        (d / "2026-07-29_good.md").write_text("ok")
        names = [p.name for p in m.capsule_files(base)]
        assert names == ["2026-07-29_good.md"], names


def test_capsule_policy_restricted() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        (base / m.VERSION_FILE_NAME).write_text(
            '{"methodology_version": "v4.0", "capsule_policy": "restricted"}')
        assert m._capsule_policy(base) == "restricted"
        (base / m.VERSION_FILE_NAME).write_text('{"methodology_version": "v4.0"}')
        assert m._capsule_policy(base) == "open"


def test_capsule_secret_scan() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        d = base / m.OUTBOX_DIR
        d.mkdir(parents=True)
        rel = str(m.OUTBOX_DIR / "2026-07-29_x.md")
        (base / rel).write_text("api_key = 'sk-abcdefghijklmnop1234'")
        assert m._capsule_content_hits(base, rel) is True
        (base / rel).write_text("정상 제안 — refs: abc1234")
        assert m._capsule_content_hits(base, rel) is False


def test_thinktank_cross_repo_marking_logic() -> None:
    # _thinktank_capsule_section은 METHODOLOGY_ROOT 의존이라 로직만 재현 검증:
    # 같은 target을 서로 다른 repo가 보내면 CROSS-REPO 마킹 대상
    a = m.parse_capsule_frontmatter(m.render_capsule(_payload()))
    b = m.parse_capsule_frontmatter(m.render_capsule(_payload(
        id="other__2026-07-29_ppt-deck", origin_repo="other")))
    repos = {a["origin_repo"], b["origin_repo"]}
    assert a["target"] == b["target"] and len(repos) == 2


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
