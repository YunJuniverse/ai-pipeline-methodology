---
id: C-001
title: "프론트엔드 색 하드코딩 누적 → 드리프트·리브랜딩 마비 (디자인 토큰 미적용)"
domain: frontend-design-tokens
status: active
promoted_from: P-002
seen_in:
  - 2026-06-26   # gamblescan UIUX-001 — 실세계: 하드코딩 hex 3,030 codemod + 가드레일 등록
  - 2026-06-29   # 방법론 canonical 자산화(METH-049) + gamblescan UIUX-002(가드레일 갭 → 회색 32건 시정)
signature: "-\\[#[0-9a-fA-F]{6}\\]|(bg|text|border|ring|from|to|via|shadow|fill|stroke)-(slate|gray|zinc|neutral|stone|red|orange|amber|yellow|lime|green|emerald|teal|cyan|sky|blue|indigo|violet|purple|fuchsia|pink|rose)-[0-9]{2,3}"
verified_with:
  - claude-opus-4-8
deps_implicated:
  - "tailwindcss@^4"
  - "clsx@^2"
  - "tailwind-merge@^2"
created: 2026-06-29
last_hit: 2026-06-29
---

## 증상 (Symptom)

UI 코드에 색이 단일 출처 없이 하드코딩됨 — arbitrary hex(`bg-[#1a1a2e]`) + off-system Tailwind 팔레트(`text-gray-500`, `bg-slate-800`, `border-zinc-300`, `bg-amber-400` …)가 산재. 같은 "회색"이 6종으로 갈라지는 드리프트가 누적되고, 리브랜딩 시 전 파일을 일일이 고쳐야 해 사실상 마비.

## 근본 원인 (Root Cause)

색의 *단일 출처*(@theme 시맨틱 토큰)가 없고, 코드가 색을 *값/팔레트*로 직접 부른다. 가드레일이 없거나 *범위가 좁으면*(예: `text-` 회색만 검사) 재발이 CI를 통과해 누적된다.

## 솔루션 (Solution) — 4기둥 최소 토대 (거대 시스템 금지)

day-1에:
1. **토큰** — `@theme` 시맨틱 토큰(surfaces/text/border/brand/semantic) + 디자인 언어(radius/shadow/motion/type). *이름=역할*, 프로젝트마다 값만 조정.
2. **프리미티브** — `cn()`(twMerge+clsx) + Card/Button/Badge. 토큰만 소비.
3. **가드레일** — `check-no-arbitrary-color.sh`를 lint:tokens + CI + pre-push 3지점에 연결(fail-closed). **전 prefix × 전 팔레트 family**를 검사(아래 교훈 참조). 더미 위반으로 실검증.
4. **제약 문서** — `design-system.md`를 토큰 표로 채워 AI 생성 제약으로.

스타터: `50_resources/skeletons/frontend-design-tokens/base/`(C-001 bake-in). 규칙: 지침 20.

## 실세계 교훈 (gamblescan 검증)

1. **가드레일은 `text-`만이 아니라 *전 prefix*(`bg/border/ring/from/to/shadow/…`)를 검사해야 한다.** gamblescan은 가드레일 등록 후 "완료" 선언했으나 검사식이 `text-` 회색만이라 `bg-/border-/from-/shadow-` 회색 **32건(13파일)**이 CI 초록불 뒤로 누출됐다.
2. **off-system은 회색만이 아니다.** Tailwind 전 팔레트(amber/orange/yellow/red/blue…) 직접 사용도 토큰 우회다. gamblescan에 amber/orange **251건**이 잔존했다. → canonical 가드레일은 전 팔레트 family를 검사(`signature` 참조). 의도적 categorical/메달 색은 토큰 또는 `ALLOW_HEX`로 *명시* 분리.

## 안티패턴 (Anti-Pattern)

- 토큰 이름에 *값*을 박음(`--color-slate-800`) → 리브랜딩 때 이름까지 거짓. 역할로 명명.
- 가드레일을 켜고 *검증 안 함* / *범위 좁음*(text-only, gray-only) → 죽은·반쪽 가드레일.
- 기존 프로젝트 한 PR 빅뱅 전환 → 화면 단위 슬라이스 + 렌더/CSS 회귀 게이트.
- `ALLOW_HEX` 남발 → 무력화. 순백 max-contrast·메달 gold/silver/bronze 등 진짜 예외만.

## 관련 자료
- 지침 20 프론트엔드 디자인 토큰 시스템 규칙
- 지침 19 클린아키텍처·클린코드 (자매 가드레일 — 구조 품질)
- 지침 17 §4.2 Guardrails-by-Construction (상위 원칙)
- 스켈레톤 `50_resources/skeletons/frontend-design-tokens/` (bakes-in: C-001)
- 실세계 사례: gamblescan UIUX-001(토대)·UIUX-002(가드레일 갭 시정, PR #155)
