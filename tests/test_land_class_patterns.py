#!/usr/bin/env python3
"""METH-133(land) Class B/C 경로 스캐너 단위 테스트 (python3 tests/test_land_class_patterns.py).

plain assert + 자체 러너. CLASS_BC_PATTERNS 는 순수 정규식 표라 git repo 없이 검증한다.

fail-closed 설계(오탐은 싸고 미탐은 비싸다)를 **깨지 않으면서** 구조적 오탐만 걷어내는 것이
이 테스트의 목적이다. 그래서 두 방향을 같은 무게로 고정한다.

- `test_*_trigger*`   — 진짜 B/C 경로가 계속 걸리는가 (미탐 방지 · 이쪽이 더 비싸다)
- `test_*_not_*`      — 이름만 닮은 경로가 안 걸리는가 (오탐 방지)
- `test_bare_plan_*`  — 왜 지금 규칙이 이 모양인지의 근거(실측 숫자) 박제
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
        "billing/plan/limits.ts",     # billing 세그먼트로 걸린다
    ]:
        assert "과금·결제·가격" in _hits(path), f"미탐: {path}"


def test_plan_billing_compounds_trigger() -> None:
    """plan 이 과금 낱말과 붙은 복합어 — 다른 대안이 못 잡으므로 이 규칙이 필요하다.

    `plan_pricing.json` 의 `pricing` 은 `_` 뒤라 `(^|/)pricing` 에 안 걸린다.
    이 케이스를 위해 `plans?[._-](pricing|price|billing|tier|quota)` 를 둔다.
    """
    for path in [
        "config/plan_pricing.json",
        "src/plan-tier.ts",
        "app/plan_quota.ts",
        "lib/plan-billing.ts",
    ]:
        assert "과금·결제·가격" in _hits(path), f"미탐: {path}"


def test_plural_plans_triggers_but_singular_plan_does_not() -> None:
    """복수형 `plans` 만 요금제로 본다 — 단수 `plan` 은 기획 용법이 지배적이다.

    `plans.ts`·`plans/` 는 요금제 목록의 관용 표기라 과금으로 보는 편이 맞다.
    반면 단수 `plan.md`·`app/plan/page.js` 는 icons 실측에서 **전부 기획 문서·라우트**였다.
    단수까지 넣으면 기획 중심 레포에서 다시 오탐이 된다.
    """
    for path in ["src/plans.ts", "src/plans/index.ts"]:
        assert "과금·결제·가격" in _hits(path), f"미탐: {path}"
    for path in [
        "50_apps/plan-viewer/app/plan/page.js",   # 기획 뷰어의 plan 라우트
        "50_resources/prompts/plan.md",           # 기획 프롬프트 문서
    ]:
        assert "과금·결제·가격" not in _hits(path), f"오탐: {path}"


def test_bare_plan_would_be_catastrophic() -> None:
    """왜 단독 `plan` 을 넓은 경계로 두면 안 되는가 — 판별자로서 죽는다.

    icons 레포 실측(2502 경로): 단독 `plan` + `[./_-]` 는 **824개**를 물었다.
    레포의 3분의 1이 Class B 면 사람은 스캐너를 읽지 않고 `--no-ci-check` 로 간다.
    현재 패턴은 같은 레포에서 2건만 물고, 그 2건은 전부 진짜 `checkout/` 이다.

    이 테스트는 회귀 방지가 아니라 **근거의 박제**다 — 경계를 다시 넓히자는 제안이
    오면 이 숫자를 먼저 보게 한다.
    """
    import re as _re
    old = r"(^|/)(billing|payment|pricing|checkout|invoice|subscription|plan)s?[./_-]"
    # 옛 패턴이 *실제로* 물었던 경로만 — `(^|/)plan` 이라 `floor-plan` 처럼 plan 이
    # 세그먼트 중간에 오는 것은 옛 패턴도 안 물었다(그건 이 규칙의 피해자가 아니다).
    victims = [
        "50_apps/plan-viewer/components/BentoPopupLayout.jsx",
        "docs/plan-of-record.md",
    ]
    for path in victims:
        assert _re.search(old, path, _re.IGNORECASE), f"전제 오류 — 옛 패턴이 {path} 를 안 물었다"
        assert "과금·결제·가격" not in _hits(path), f"오탐 재발: {path}"


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



# ── 표현용 자산 제외 ──────────────────────────────────────────────────────────

def test_assets_are_excluded_from_triggers() -> None:
    """트리거 경로에 놓인 이미지·영상·폰트는 Class B/C 가 아니다.

    트리거는 «경로 단어»로 위험을 추정하는데, 자산은 그 경로에 있어도 스키마·인증·
    과금·계약 «로직»을 바꿀 수 없다. icons 실측: 인증 트리거 적중 25건 중 16건이
    `public/gallery/auth-*.jpg` 갤러리 스크린샷이었다 — 재촬영 PR 마다 Class B.
    """
    for path in [
        "public/gallery/auth-login.jpg",
        "assets/billing/pricing-hero.png",
        "static/legal/terms-banner.webp",
        "media/checkout/demo.mp4",
        "fonts/auth/Inter.woff2",
        "public/migrations/diagram.svg",
    ]:
        assert m._is_asset(path), f"자산으로 인식 못함: {path}"


def test_documents_are_not_treated_as_assets() -> None:
    """문서 확장자는 자산이 아니다 — 정책·약관·가격을 실제로 담는다.

    `legal/terms.pdf`·`pricing/plans.json` 은 Class C 판정 대상으로 남아야 한다.
    이 경계를 무너뜨리면 자산 제외가 곧 법무·과금 미탐이 된다.
    """
    for path in [
        "legal/terms.pdf",
        "legal/privacy.md",
        "billing/pricing.json",
        "policy/compliance.docx",
        "db/migrations/001.sql",
    ]:
        assert not m._is_asset(path), f"문서를 자산으로 오인: {path}"
    # 그리고 여전히 트리거에 걸려야 한다
    assert _hits("legal/terms.pdf"), "legal/terms.pdf 는 Class C 대상이어야 한다"
    assert _hits("billing/pricing.json"), "billing/pricing.json 은 과금 대상이어야 한다"


def test_asset_detection_ignores_path_position() -> None:
    """확장자만 본다 — 경로 어디에 있든 동일 판정."""
    assert m._is_asset("a/b/c/deep/auth/x.PNG"), "대문자 확장자"
    assert m._is_asset("x.jpg")
    assert not m._is_asset("src/auth/session.ts")
    assert not m._is_asset("noextension")

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
