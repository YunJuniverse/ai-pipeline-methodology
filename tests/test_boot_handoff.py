#!/usr/bin/env python3
"""boot 의 HANDOFF 'Working on' 파서 단위 테스트 (의존성 없음 — python3 tests/test_boot_handoff.py).

METH-108: 파서는 `- **Working on**:` (볼드)만 기대했지만 init 스캐폴드는
`- Working on:` (비볼드)로 생성 → 새 다운스트림 boot 가 '(미기재)' 표시.
_handoff_working_on 은 양쪽 형식을 모두 허용해야 한다.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "60_tools"))

_spec = importlib.util.spec_from_file_location(
    "methodology",
    Path(__file__).resolve().parent.parent / "60_tools" / "methodology.py",
)
m = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(m)


def test_bold_format() -> None:
    txt = "# HANDOFF.md\n\n- **Working on**: METH-108 파서 정합\n- **Current mode**: fullstack\n"
    assert m._handoff_working_on(txt) == "METH-108 파서 정합"


def test_plain_format_from_legacy_scaffold() -> None:
    txt = "# HANDOFF.md\n\n- Working on: invest-ops 부트스트랩\n- Current mode: planning-only\n"
    assert m._handoff_working_on(txt) == "invest-ops 부트스트랩"


def test_empty_value_returns_none() -> None:
    # 스캐폴드 직후 값이 비어 있으면 미기재로 처리
    txt = "- **Working on**:\n- **Current mode**: dev\n"
    assert m._handoff_working_on(txt) is None


def test_missing_line_returns_none() -> None:
    assert m._handoff_working_on("# HANDOFF.md\n\n## Current Focus\n") is None


def test_scaffold_template_matches_parser() -> None:
    # 회귀 가드: 템플릿 형식이 다시 파서와 어긋나면 즉시 실패
    tpl = (
        Path(__file__).resolve().parent.parent
        / "50_resources" / "templates" / "HANDOFF.md"
    ).read_text(encoding="utf-8")
    assert "- **Working on**:" in tpl, "HANDOFF 템플릿의 Working on 라인이 파서 기대 형식(볼드)이 아님"


def main() -> int:
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    failed = 0
    for t in tests:
        try:
            t()
            print(f"  ok  {t.__name__}")
        except AssertionError as e:
            failed += 1
            print(f"FAIL  {t.__name__}: {e}")
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
