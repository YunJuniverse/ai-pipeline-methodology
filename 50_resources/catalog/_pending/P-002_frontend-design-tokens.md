---
id: P-002
title: "프론트엔드 색 하드코딩 누적 → 드리프트·리브랜딩 마비 (디자인 토큰 미적용)"
domain: frontend-design-tokens
status: pending
source_observations:
  - 2026-06-29_design-token-foundation
signature: "-\\[#[0-9a-fA-F]{6}\\]|(bg|text|border)-(gray|slate|zinc|neutral|stone)-[0-9]{2,3}"
verified_with:
  - claude-opus-4-8
deps_implicated:
  - "tailwindcss@^4"
  - "clsx@^2"
  - "tailwind-merge@^2"
created: 2026-06-29
last_seen: 2026-06-29
promotion_rule: "Promote to active Catalog after N>=2 observations or explicit human approval."
---

## 증상 (Symptom)

UI 코드에 색이 단일 출처 없이 하드코딩됨 — arbitrary hex(`bg-[#1a1a2e]`)와 off-system 회색(`text-gray-500`, `bg-slate-800`, `zinc-N`)이 산재. 같은 "회색"이 6종으로 갈라지는 드리프트가 누적되고, 리브랜딩 시 전 파일을 일일이 고쳐야 해 사실상 마비.

## 임시 해결 / 적용 토대 (Current Solution)

day-1에 **4기둥 최소 토대**를 깐다(거대 디자인 시스템 금지):
1. **토큰** — `@theme` 시맨틱 토큰(surfaces/text/border/brand/semantic) + 디자인 언어(radius/shadow/motion/type). *이름=역할*, 프로젝트마다 값만 조정.
2. **프리미티브** — `cn()`(twMerge+clsx) + Card/Button/Badge. 토큰만 소비.
3. **가드레일** — `check-no-arbitrary-color.sh`를 lint:tokens + CI + pre-push 3지점에 연결(fail-closed). arbitrary hex·off-system 회색 발견 시 빌드 fail.
4. **제약 문서** — `design-system.md`를 토큰 표로 채워 AI 생성 제약으로.

스타터: `50_resources/skeletons/frontend-design-tokens/base/`. 규칙: 지침 20.

## 안티패턴 (Anti-Pattern)

- 토큰 이름에 *값*을 박음(`--color-slate-800`) → 리브랜딩 때 이름까지 거짓이 됨. 역할로 명명.
- 가드레일을 켜고 *검증 안 함* → 더미 위반으로 차단 확인 안 하면 죽은 가드레일.
- 기존 프로젝트를 한 PR로 빅뱅 전환 → 화면 단위 슬라이스 + 렌더 회귀 게이트로.
- `ALLOW_HEX` 남발 → 가드레일 무력화. 순백 max-contrast·메달 gold/silver 등 진짜 예외만.

## 승급 조건

동일 마찰(색 하드코딩 토대 주입)이 다른 도메인/프로젝트의 L1 관찰에서 1회 더 나타나면(N≥2) active Catalog(`C-NNN`) 승급 후보 → 사람 머지 후 스켈레톤 `bakes-in.json`에 합류. 모델/스택이 다르면 `verified_with`/`deps_implicated` 갱신.

## 관련 자료
- 지침 20 프론트엔드 디자인 토큰 시스템 규칙
- 지침 19 클린아키텍처·클린코드 (자매 가드레일 — 구조 품질)
- 지침 17 §4.2 Guardrails-by-Construction (상위 원칙)
- 스켈레톤 `50_resources/skeletons/frontend-design-tokens/`
