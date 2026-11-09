#!/usr/bin/env python3
"""METH-149 전수조사(2026-10-10~11-09) 도구 결함 회귀 테스트.

각 테스트는 다운스트림 실측 사고를 재현하는 negative case 를 품는다(지침 23 §4 — 가드의
«통과»는 약하고 «거부»가 강하다: 막아야 할 입력이 실제로 막히는지부터 고정).
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


def _raises(fn, *a) -> bool:
    try:
        fn(*a)
    except ValueError:
        return True
    return False


# ── observe friction — 무효 phase 가 repeat_of 로 새던 무음 오파싱 (cafe24 `execute`·`investigate`)
def test_invalid_phase_rejected() -> None:
    assert _raises(m.parse_friction_item, "원격 셸|15|ssh -A 로 해소|talmo-backup|execute", 1)
    assert _raises(m.parse_friction_item, "x|5|y|null|investigate", 1)


def test_valid_phase_and_pipe_in_resolution_still_parse() -> None:
    it = m.parse_friction_item("x|5|y|null|verify", 1)
    assert it["phase"] == "verify" and it["repeat_of"] is None
    it = m.parse_friction_item("grep|8|grep a|b 로 확인|dead-domain-cleanup", 1)   # resolution 안의 세로줄
    assert it["repeat_of"] == "dead-domain-cleanup" and "a|b" in it["resolution"]


def test_repeat_of_not_a_repeat_tokens_normalize_to_null() -> None:
    # ai-icons 실측 12건 — kebab 슬러그로 통과해 thinktank 가짜 앵커가 됐다
    for tok in ("new", "first-seen", "initial", "n/a"):
        assert m.normalize_repeat_of(tok) is None, tok
    assert m.normalize_repeat_of("2026-10-29_trust-recompute") == "2026-10-29_trust-recompute"


# ── reserve — 접두어 추론·0 채움·아카이브 (lifeManager id/METH-1·gamblescan I18N-002 재발급)
def test_reserve_infers_prefix_from_todo() -> None:
    todo = "## Ready\n### LM-190 · a\n### LM-191 · b\n### METH-3 · 인용\n"
    assert m._infer_todo_prefix(todo) == "LM"
    assert m._infer_todo_prefix("# 빈 TODO\n") is None


def test_reserve_keeps_zero_padding_width() -> None:
    assert m._todo_id_width("### I18N-002 · x\n### I18N-010", "I18N") == 3
    assert m._todo_id_width("### LM-190", "LM") == 0


def test_reserve_scans_rotated_archives() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        arc = t / "40_dev/snapshots/live-archive"
        arc.mkdir(parents=True)
        (arc / "2026-10-01_todo-done.md").write_text("### NEWS-005 · 지난 완료\n")
        texts = m._todo_archive_texts(t)
        assert max(m._max_todo_id(x, "NEWS") for x in texts) == 5


# ── 라이브 파일 — 줄수 우회(긴 줄·글자 수)·제목 부연·깨진 헤더
def test_done_heading_with_suffix_counts() -> None:
    todo = "## Done (최근 6건 — 이전은 아카이브)\n### A-1 · x\n### A-2 · y\n## Notes\n"
    assert m._todo_done_count(todo) == 2                       # 완전일치였을 때 0 — 상한 무력
    assert m._kanban_heading("## Blocked — 외부 게이트", "## Blocked")
    assert not m._kanban_heading("## Blockers", "## Blocked")


def test_broken_kanban_header_is_error() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        (t / "TODO.md").write_text(
            "# TODO\n## Backlog\n## Ready\n## InProgress`, `## Blocked`, `## Done\n### X-1 ✅\n"
            "## InProgress\n## Blocked\n## Done\n")
        errors, _ = m.live_file_structure_issues(t)
        assert any("깨진 헤더" in e for e in errors), errors


def test_char_and_line_length_warnings() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        recent = "\n".join(f"- 2026-11-0{i % 9 + 1} — r{i}" for i in range(15))
        (t / "HANDOFF.md").write_text(
            "# HANDOFF\n- **Working on**: " + "가" * 1500 + "\n## Recent Changes\n" + recent + "\n")
        (t / "TODO.md").write_text("## Ready\n### A-1 · 끝남 ✅\n### A-2 · ~~취소~~\n## Done\n")
        w = " | ".join(m._live_file_char_warnings(t))
        assert "1,000자 넘는 줄 1개" in w, w
        assert "Recent Changes 15건" in w, w
        assert "Done 밖에 완료 표기" in w and "2건" in w, w
        (t / "HANDOFF.md").write_text("# HANDOFF\n- **Working on**: 짧다\n")
        (t / "TODO.md").write_text("## Ready\n### A-1 · 남음\n## Done\n")
        assert m._live_file_char_warnings(t) == []             # 정상 파일엔 침묵


# ── land — TODO change-class 우선 (drip-chat-planning Class C 항목 자동 머지)
def test_todo_change_class_blocks_auto_merge() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        (t / "TODO.md").write_text(
            "## Ready\n### DRIP-008 · 공개 정책 확정\n- **mode**: planning / **change-class**: C / **owner**: Human\n"
            "### DRIP-009 · 오탈자\n- **change-class**: A\n")
        ids = m._pr_todo_ids({"title": "docs: DRIP-008 정책 표"}, "docs/drip-009-typo")
        assert ids == {"DRIP-008", "DRIP-009"}
        assert m._todo_change_class(t, ids) == [("DRIP-008", "C")]
        assert m._todo_change_class(t, {"DRIP-009"}) == []


def test_pr_todo_ids_from_lowercase_branch() -> None:
    assert "LM-192" in m._pr_todo_ids({"title": "feat: password vault"}, "feat/lm-192-password-vault")


def test_snapshot_paths_excluded_from_class_scan() -> None:
    assert "40_dev/snapshots/2026-10-15_runner/worker.py".startswith(m.CLASS_SCAN_EXCLUDED_PREFIXES)
    assert not "server/worker.py".startswith(m.CLASS_SCAN_EXCLUDED_PREFIXES)   # 진짜 워커는 계속 검사


# ── ADR 인용 — `NNNN-title.md` 도 존재로 인정 (drip-chat-planning ship 마다 오경고 10건)
def test_adr_citation_accepts_both_filename_forms() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        subprocess.run(["git", "-C", str(t), "init", "-q", "."], check=True)
        subprocess.run(["git", "-C", str(t), "commit", "-q", "--allow-empty", "-m", "i"], check=True,
                       env={"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t", "GIT_COMMITTER_NAME": "t",
                            "GIT_COMMITTER_EMAIL": "t@t", "PATH": "/usr/bin:/bin:/usr/local/bin:/opt/homebrew/bin"})
        (t / "40_dev/adr").mkdir(parents=True)
        (t / "40_dev/adr/0001-pricing.md").write_text("# 0001")
        (t / "40_dev/adr/ADR-002-x.md").write_text("# 002")
        (t / "doc.md").write_text("ADR-0001 과 ADR-002 를 따른다. ADR-0009 는 없다.")
        missing = [c for _, c in m._adr_citations_missing(t)]
        assert missing == ["ADR-0009"], missing


# ── ship — 새 대용량 파일 (lifeManager 무관 문서 2.4MB 혼입)
def test_large_new_files_detected() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        subprocess.run(["git", "-C", str(t), "init", "-q", "."], check=True)
        (t / "deck.pptx").write_bytes(b"\0" * (m.LARGE_NEW_FILE_BYTES + 10))
        (t / "small.md").write_text("x")
        subprocess.run(["git", "-C", str(t), "add", "-A"], check=True)
        big = m._large_new_files(t)
        assert [p for p, _ in big] == ["deck.pptx"], big


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
