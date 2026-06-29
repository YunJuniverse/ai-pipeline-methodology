---
id: P-002
title: "프론트엔드 색 하드코딩 누적 → 드리프트·리브랜딩 마비 (디자인 토큰 미적용)"
domain: frontend-design-tokens
status: tentative
source_observations:
  - 2026-06-26_gamblescan-uiux-001        # 실세계: 하드코딩 hex 3,030 codemod + 가드레일 등록
  - 2026-06-29_design-token-foundation     # 방법론 canonical 자산화(METH-049)
  - 2026-06-29_gamblescan-uiux-002         # 실세계: 가드레일 text-only 갭 → 회색 32건 누출 시정
signature: "-\\[#[0-9a-fA-F]{6}\\]|(bg|text|border|ring|from|to|shadow)-(gray|slate|zinc|neutral|stone)-[0-9]{2,3}"
verified_with:
  - claude-opus-4-8
deps_implicated:
  - "tailwindcss@^4"
  - "clsx@^2"
  - "tailwind-merge@^2"
created: 2026-06-29
last_seen: 2026-06-29
promotion_rule: "Promote to active Catalog after N>=2 observations or explicit human approval."
promotion_status: "N>=2 충족 (gamblescan 실세계 적용 + 방법론 canonical). C-NNN 승급 후보 — 사람 승인 대기."
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

## 실세계 검증 (gamblescan, 2026-06-29)

canonical 스켈레톤(METH-049)을 gamblescan 적용 사례에 교차 검증한 결과 **패턴 자체의 교훈 2건**:

1. **가드레일은 `text-` 만이 아니라 *전 prefix*를 검사해야 한다.** gamblescan은 가드레일을 등록하고
   "전체 완료" 선언했으나, 검사식이 `text-(gray|slate|…)`만이라 `bg-/border-/from-/shadow-` 회색
   **32건(13파일)**이 CI 초록불 뒤로 누출돼 있었다. canonical 스켈레톤은 처음부터 전 prefix를 검사하므로
   이 갭이 없다 → **canonical이 옳다는 실증.** (교훈: 가드레일 등록 ≠ 완전. prefix 커버리지 확인 필수.)
2. **off-system은 회색만이 아니다.** gamblescan에 `amber/orange *-NNN` **251건** + yellow가 잔존 —
   메달 Gold/Bronze·상태·차트 등. 현 canonical 가드레일은 회색-family + arbitrary hex만 잡는다.
   → **canonical 가드레일·가이드 §4를 *비-회색 Tailwind 팔레트 직접 사용*까지 broaden** 검토(향후 P-002
   파생 또는 별도 패턴). 단, 의도적 categorical 팔레트는 토큰/allowlist로 명시 분리.

## 승급 조건 / 현황

**N≥2 충족**: gamblescan(실세계, hex 3,030 codemod + 가드레일) + 방법론 canonical 자산화.
→ active Catalog `C-NNN` 승급 + 스켈레톤 `bakes-in.json` 합류 **후보**. 규칙상 *사람 머지*로 활성 이동.
승급 시 위 교훈 2를 반영해 canonical 가드레일 broaden 동반 권장. 모델/스택이 다르면
`verified_with`/`deps_implicated` 갱신.

## 관련 자료
- 지침 20 프론트엔드 디자인 토큰 시스템 규칙
- 지침 19 클린아키텍처·클린코드 (자매 가드레일 — 구조 품질)
- 지침 17 §4.2 Guardrails-by-Construction (상위 원칙)
- 스켈레톤 `50_resources/skeletons/frontend-design-tokens/`
