#!/usr/bin/env python3
"""METH-133(land) Class B/C 경로 스캐너 단위 테스트 (python3 tests/test_land_class_patterns.py).

plain assert + 자체 러너. CLASS_BC_PATTERNS 는 순수 정규식 표라 git repo 없이 검증한다.

fail-closed 설계(오탐은 싸고 미탐은 비싸다)를 **깨지 않으면서** 구조적 오탐만 걷어내는 것이
이 테스트의 목적이다. 그래서 두 방향을 같은 무게로 고정한다.

- `test_*_triggers`   — 진짜 B/C 경로가 계속 걸리는가 (미탐 방지 · 이쪽이 더 비싸다)
- `test_*_not_*`      — 이름만 닮은 경로가 안 걸리는가 (오탐 방지)
"""
from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "methodology",
    Path(__file__).resolve().parent.parent / "60_tools" / "methodology.py",
)
m = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(m)


def _hits(path: str) -> list[str]:
    """경로 하나에 걸리는 트리거 설명 목록 — _classify_change 의 판정과 동일 규칙."""
    return [
        label
        for label, pattern in m.CLASS_BC_PATTERNS
        if re.search(pattern, path, re.IGNORECASE)
    ]


# ── 과금·결제·가격 ────────────────────────────────────────────────────────────

def test_billing_paths_trigger() -> None:
    """진짜 과금 경로는 계속 Class B/C 로 걸려야 한다 (미탐 방지)."""
    for path in [
        "src/billing/index.ts",
        "app/payment/checkout.ts",
        "lib/pricing.ts",
        "server/invoice_pdf.py",
        "api/subscription-webhook.ts",
        "src/plans.ts",              # 요금제 목록 — 파일명 전체가 plan
        "src/plan.ts",
        "billing/plan/limits.ts",    # 세그먼트 전체가 plan
    ]:
        assert "과금·결제·가격" in _hits(path), f"미탐: {path}"


def test_plan_compound_is_accepted_coverage_loss() -> None:
    """`plan` 복합어는 놓친다 — 감수한 대가이지 사고가 아니다.

    `plan` 은 요금제 밖에서도 흔한 수식어라 경계를 `[./]`(세그먼트·파일명 전체)로
    좁혔다. 그 결과 `plan_limits.json` 처럼 plan 이 수식어로 쓰인 진짜 과금 파일은
    이 낱말로는 안 걸린다. 실제 과금 코드는 거의 언제나 billing·pricing·subscription
    이 경로 어딘가에 함께 있어 그쪽으로 걸리므로(아래 대조군) 순손실은 작다.

    이 테스트는 그 대가를 **눈에 보이게** 고정한다 — 나중에 경계를 다시 넓히려는
    사람이 무엇을 사고 무엇을 파는지 알고 결정하도록.
    """
    assert "과금·결제·가격" not in _hits("config/plan_limits.json")
    # 대조군 — 같은 파일이 과금 맥락 안에 있으면 여전히 걸린다
    assert "과금·결제·가격" in _hits("billing/plan_limits.json")
    assert "과금·결제·가격" in _hits("src/pricing/plan_limits.json")


def test_plan_viewer_is_not_billing() -> None:
    """`plan-viewer`(기획 현황 뷰어)는 요금제가 아니다 — icons 레포 실사례.

    이 오탐 하나가 `50_apps/plan-viewer/` 아래 **모든** 변경을 Class B 로 만들어
    자동 머지를 영구 불가능하게 했다. 문서 본문 단어 오탐과 달리 경로라 회피 불가.
    """
    for path in [
        "50_apps/plan-viewer/components/BentoPopupLayout.jsx",
        "50_apps/plan-viewer/package.json",
        "plan-viewer/next.config.js",
    ]:
        assert "과금·결제·가격" not in _hits(path), f"오탐: {path}"


def test_planning_words_are_not_billing() -> None:
    """기획(planning)·평면도(planner) 계열도 요금제가 아니다."""
    for path in [
        "30_planning/service-spec.md",
        "src/planner/schedule.ts",
        "docs/plan-of-record.md",
        "app/floor-plan/view.tsx",
    ]:
        assert "과금·결제·가격" not in _hits(path), f"오탐: {path}"


# ── 나머지 트리거 회귀 (이번 변경이 다른 줄을 건드리지 않았는지) ──────────────

def test_other_triggers_still_fire() -> None:
    cases = [
        ("db/migrations/001_init.sql", "DB 마이그레이션·스키마"),
        ("prisma/schema.prisma", "DB 마이그레이션·스키마"),
        ("src/auth/session.ts", "인증·인가"),
        ("lib/permissions.ts", "인증·인가"),
        ("api/openapi.yaml", "외부 API 계약"),
        ("proto/user.proto", "외부 API 계약"),
        ("jobs/cron.ts", "백그라운드 작업·스케줄러·큐"),
        (".github/workflows/ci.yml", "CI·배포 파이프라인"),
        ("vercel.json", "CI·배포 파이프라인"),
        ("legal/terms.md", "법무·정책·공개 메시지"),
    ]
    for path, label in cases:
        assert label in _hits(path), f"미탐: {path} → {label}"


def test_ordinary_paths_are_class_a() -> None:
    """평범한 변경은 아무 트리거도 걸리지 않아야 한다."""
    for path in [
        "src/components/Button.tsx",
        "README.md",
        "50_apps/plan-viewer/components/aouad/AouadSample.jsx",
        "tests/test_land_class_patterns.py",
    ]:
        assert _hits(path) == [], f"오탐: {path} → {_hits(path)}"


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
