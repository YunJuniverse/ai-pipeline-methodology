# Checkpoint — 2026-07-29 (METH-129 작성 — AI 디자인 방법론 5종)

> ✅ 사용자 확정("5개 전부") → 지침 25·26·27 신설 + 20 v2·22 v3 보강 완료. branch `docs/meth-129-ai-design-guides`, PR 대기. 머지 후 sync-all 전파.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-fable-5 · Tool: claude-code-desktop · Host: darwin 25.5.0
- Branch `docs/meth-129-ai-design-guides` (base=main, branch-first)

## 방금 한 것

- **지침 25 · AI 디자인 공통 규범(신설)**: 리서치 §0의 9원칙 승급 — ①모델 추상화(벤더 소멸 3건) ②캐논 우선 ③provenance=저작권 증빙(문체부 안내서·Thaler) ④2단 생성+선별 KPI(3회 상한) ⑤사람 게이트 3위치 표 ⑥2층 검증(지침 23 인스턴스) ⑦텍스트·로고 생성 금지 ⑧slop 금지 목록 ⑨법무 게이트(AI기본법 표시·무료 티어 금지·유사 IP 폐기·소송 중 모델 유예·플랫폼 정책).
- **지침 26 · 이미지·캐릭터(신설)**: 역할 매트릭스(GPT Image 2·NB Pro·FLUX LoRA·Ideogram·Firefly 면책·Midjourney 유예), 일관성 사다리(정본 시트 동결→레퍼런스 주입→LoRA ~$8), 파이프라인(인페인팅 우선·클린 베이스 후 업스케일), 검수 2단+인쇄 크기, 에셋 명명·approved 분리·provenance.
- **지침 27 · 영상(신설)**: 7단 파이프라인(스크립트 사람 먼저·샷 4~8초 분해), 샷 스펙 YAML 스키마(model은 역할 참조), 프롬프트 5부 구조·레퍼런스 캐논·First/Last Frame, 비용 공식+시도계수, QA 체크 8항.
- **지침 20 v2**: §9 신설 — DESIGN.md 의무(미학 방향+레퍼런스+금지 기본값+토큰 참조), 3안 픽 게이트(픽 후 전면 재생성 금지), 시스템 정렬(Tailwind v4 @theme·DTCG·shadcn registry·MCP 조회), 품질 게이트(axe 차단·시각 회귀·AI 티 테스트 4축 중 3축).
- **지침 22 v3**: §7b 신설 — 결정론 레이아웃 린트 4종(build 체크 fail-closed)·패널 taxonomy 주입·Vega-Lite 차트 계층(VLM 수치 검증 금지)·리플렉션 루프(예산 상한)·경계 2종(HTML 경유 금지·상용 API 소재까지).
- README v4.3(카탈로그 3행 추가·이력). TODO METH-129 → InProgress(AC 체크).

## 다음 구체 행동

1. 이 PR(`docs/meth-129-ai-design-guides` → main) 머지 → sync-all 전파(20_guides shared) → METH-129 Done(maincheck 후) — 전파되면 12개 repo 전부에서 AI 디자인 작업이 이 규범을 따름.
2. 후속 후보(백로그 미등록): 스켈레톤 `ai-asset-pipeline`(canon/·approved/·provenance 레저·샷 스펙 템플릿) — 실제 이미지/영상 작업 첫 착수 시 함께 만드는 게 효율적.
3. 별도 트랙: RFC-003 관찰 · repo 과제 5건 · grooman sync · 도구 지형 분기 재검증(10월경).

## 막힌 것
- 없음.

## 환경
- macOS, python3. 대시보드 http://localhost:8765.
