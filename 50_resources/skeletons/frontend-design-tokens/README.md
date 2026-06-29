# frontend-design-tokens skeleton

> 프론트엔드 디자인 토큰 토대 — day-1에 까는 **4기둥 최소 토대**(거대 시스템 아님).
> 규칙: [지침 20](../../../20_guides/20_프론트엔드_디자인_토큰_시스템_규칙.md) · 패턴: [P-002](../../catalog/_pending/P-002_frontend-design-tokens.md)

## 이 스켈레톤이 day-1에 막는 것
- arbitrary hex (`bg-[#1a1a2e]`) 산재 → 리브랜딩 마비
- off-system 회색 (`text-gray-500` 6종) 드리프트
- 색 정의가 컴포넌트마다 흩어짐(단일 출처 없음)

## 4기둥
| 기둥 | 파일 |
|------|------|
| ① 토큰 | `base/theme/tokens.css` (@theme 시맨틱 토큰 + 디자인 언어) |
| ② 프리미티브 | `base/lib/cn.ts`, `base/components/primitives/` (Card/Button/Badge) |
| ③ 가드레일 | `base/guardrails/check-no-arbitrary-color.sh` + `wiring.md` |
| ④ 제약 문서 | `base/design-system.md` |

## 적용
```bash
python3 60_tools/methodology.py skeleton apply frontend-design-tokens ../my-project
```
적용 후: deps 설치(`clsx`, `tailwind-merge`) → `tokens.css` 값을 브랜드에 맞게 조정 →
가드레일 3지점 연결(`base/guardrails/wiring.md`) → 더미 위반으로 검증.

> base_version v1 · 검증: claude-opus-4-8 · catalog bake-in 없음(P-002는 _pending, N≥2 승급 후 합류).
