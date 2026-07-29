# Checkpoint — 2026-07-29 (지침 20 v3 — 기본 실수 3층 방어)

> ✅ 사용자 반복 실수(다크 대비·간격 붙음) 환류 — 지침 20 v3 + METH-130(UI repo 실설치) 등록. #135는 cherry-pick 통합 후 close. branch `docs/guide-20-v3-defense`, PR 대기.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-fable-5 · Tool: claude-code-desktop · Host: darwin 25.5.0
- Branch `docs/guide-20-v3-defense` (base=main c93dcfa + #135 기록 cherry-pick, branch-first)

## 방금 한 것

- **#135 처리**: OPEN 상태에서 새 작업이 라이브 파일을 겹치게 되어 — 스택-PR 금지 규칙에 따라 #135의 기록 커밋(b2f05c70)을 이 브랜치에 cherry-pick하고 #135는 사유 코멘트와 함께 close. 단일 main 직행 PR로 통합(내용 유실 없음).
- **지침 20 v3**: 사용자 지적 반복 실수 2종의 구조적 방어 —
  - §4 가드레일 표에 **절대색 직접 사용 fail 행**(`text-black`·`text-white`·`bg-black`·`bg-white` — 다크모드 미반전의 근원).
  - §9.5 신설 "기본 실수 3층 방어": 1층 구조(시맨틱 토큰=자동 반전·`<Section>/<Stack>` 프리미티브 내장 간격, "기본 패딩 0+개별 부여" 구조 금지 — tshome 실사고 계보) / 2층 기계(axe 대비 PR 차단·opacity 누적 병행·인접 bounding box 간격 린트·양모드 스크린샷·computed 확인) / 3층 friction 기록.
- **METH-130 등록**(Backlog): UI repo 6곳(tshome·talmo·lifeManager·icons-marketing·gamblescan·icons) 실설치 — axe 게이트·간격 스크립트·절대색 차단 확장·프리미티브 점검 + 더미 위반 실효 증명. 규칙 전파(sync)와 별개로 게이트 설치는 repo별 작업.

## 다음 구체 행동

1. 이 PR(`docs/guide-20-v3-defense` → main) 머지 → sync-all 전파(지침 20 shared) → 이후 각 UI repo 세션에서 METH-130 항목 참조해 설치.
2. 잔여 트랙: 스켈레톤 ai-asset-pipeline(첫 실작업 시) · RFC-003 관찰 · repo 과제(METH-130 포함 6곳+기존 5건) · grooman sync · 월간 전수조사 2회차(8월 말).

## 막힌 것
- 없음.

## 환경
- macOS, python3. 대시보드 http://localhost:8765.
