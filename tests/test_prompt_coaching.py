#!/usr/bin/env python3
"""METH-118(프롬프팅 코칭 루프) 단위 테스트 (python3 tests/test_prompt_coaching.py).

plain assert + 자체 러너. 파싱·렌더 왕복·집계·리포트 생성·발췌 상한 가드 검증.
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


def test_parse_prompting_full() -> None:
    ex = m.parse_prompting_item("웹페이지 수정|3|이쁘게 바꿔줘|참고 사이트·유지할 것·바꿀 것 순으로 제시|트리아지,정본|webpage-design-choice")
    assert ex["intent"] == "웹페이지 수정" and ex["rounds"] == 3
    assert ex["terms"] == ["트리아지", "정본"] and ex["situation"] == "webpage-design-choice"


def test_parse_prompting_minimal_fields() -> None:
    ex = m.parse_prompting_item("배포 확인|1||||")
    assert ex["vague"] is None and ex["correction"] is None and ex["terms"] == [] and ex["situation"] is None


def test_parse_prompting_rejects() -> None:
    for bad in ["필드부족|1|a|b|c",                       # 5필드
                "|1|a|b|c|d",                              # intent 없음
                "x|둘|a|b|c|d",                            # rounds 비정수
                "x|1|" + "가" * 201 + "|b|c|d",            # 발췌 상한
                "x|1|a|b|c|한글 태그"]:                     # 상황태그 비-kebab
        try:
            m.parse_prompting_item(bad)
        except ValueError:
            continue
        raise AssertionError(f"거부돼야 함: {bad}")


def _payload(prompting) -> dict:
    return {
        "session_id": "2026-07-29_coach-test", "agent": "a", "tool": "t", "host_os": "d",
        "domain": "fullstack", "task_type": "feature", "stack_used": ["python3"],
        "flow_used": "ad-hoc", "friction": [], "prompt_patterns": [], "rounds": [],
        "prompting": prompting, "summary": "요약", "created_at": "2026-07-29T00:00:00Z",
    }


def test_render_parse_roundtrip() -> None:
    prompting = {"rounds_total": 7, "exchanges": [
        m.parse_prompting_item("디자인 선택|4|이쁘게|참고안 3개 제시 후 선택|시안,해석 계약|webpage-design-choice"),
        m.parse_prompting_item("배포|1||||"),
    ]}
    text = m.render_observation(_payload(prompting))
    parsed = m.parse_prompting_block(text)
    assert parsed["rounds_total"] == 7 and len(parsed["exchanges"]) == 2
    ex = parsed["exchanges"][0]
    assert ex["rounds"] == 4 and ex["vague"] == "이쁘게" and ex["terms"] == ["시안", "해석 계약"]
    assert ex["situation"] == "webpage-design-choice"


def test_render_omits_block_when_empty() -> None:
    text = m.render_observation(_payload({"rounds_total": None, "exchanges": []}))
    assert "\nprompting:" not in text
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp) / "2026-07-29_coach-test.md"
        p.write_text(text, encoding="utf-8")
        assert m.validate_observation_file(p) == []


def test_report_aggregation() -> None:
    e1 = {"session_id": "2026-07-28_a", "date": "2026-07-28", "rounds_total": 4, "exchanges": [
        {"intent": "디자인", "rounds": 3, "vague": "이쁘게", "correction": "참고안 제시",
         "terms": ["시안"], "situation": "webpage-design-choice"}]}
    e2 = {"session_id": "2026-07-29_b", "date": "2026-07-29", "rounds_total": 2, "exchanges": [
        {"intent": "배포", "rounds": 1, "vague": None, "correction": None, "terms": ["시안"],
         "situation": None}]}
    report = m.build_prompt_report([e1, e2], "2026-07-29T00:00:00Z")
    assert "기록 세션 2건" in report and "평균 라운드 3.0" in report
    assert "**시안** — 2회 등장" in report
    assert "`webpage-design-choice` (1회)" in report
    assert "재지시(3라운드+) 1건" in report
    assert "PostHog" in report  # 확장 포인트 명시


def test_regenerate_report_from_files() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        obs = t / "50_resources" / "ai_observations"
        obs.mkdir(parents=True)
        prompting = {"rounds_total": 5, "exchanges": [
            m.parse_prompting_item("리포트|2|대충 정리해줘|산출물 형식·독자·분량 명시|트리아지|report-request")]}
        (obs / "2026-07-29_coach-test.md").write_text(
            m.render_observation(_payload(prompting)), encoding="utf-8")
        assert m._regenerate_prompt_report(t) is True
        report = (t / m.PROMPT_REPORT_PATH).read_text(encoding="utf-8")
        assert "대충 정리해줘" in report and "report-request" in report
        assert m._regenerate_prompt_report(t) is False  # 무변경이면 재작성 안 함


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
