---
name: ai-relay
description: 다른 AI와의 릴레이 워크플로우 — 핸드오프 파일 생성, 릴레이 설계, 표준 프롬프트. "핸드오프", "릴레이", "ChatGPT에 넘겨", "피어리뷰", "다른 AI" 등 멀티AI 키워드 시 활성화.
---

# AI 릴레이 가이드

## 언제 사용하는가

- 다른 AI(ChatGPT, GenSpark 등)의 **피어리뷰**가 필요할 때
- **시각적 산출물**(PPT 등) 제작이 필요할 때
- **외부 리서치** 보강이 필요할 때
- Claude Code 세션 결과를 다른 도구로 넘길 때

## 핵심 원칙

1. **빌더와 리뷰어는 반드시 다른 AI** — 자기 편향 방지
2. **핸드오프 파일이 공유 메모리** — 산출물 + 핸드오프만 전달
3. **프로젝트 시작은 항상 Claude**
4. **이전 라운드 산출물은 넘기지 않는다** — 핸드오프가 누적 맥락 압축

---

## 핸드오프 파일 생성

사용자가 핸드오프를 요청하면 아래 구조로 생성한다:

```markdown
# HANDOFF NOTE

- **Project**: {CLAUDE.md에서 프로젝트명}
- **Version**: v{이전} → v{현재}
- **Current Stage**: {현재 파이프라인 Stage}
- **Completed by**: Claude
- **Date**: {오늘 날짜}

---

## OBJECTIVE (불변)
{CLAUDE.md 프로젝트 목적에서 가져옴. 매 핸드오프마다 동일 유지.}

---

## KEY DECISIONS SO FAR
- {CLAUDE.md 현재 상태의 확정 사항에서 가져옴}
- {이번 세션에서 추가된 결정 포함}

---

## WHAT CHANGED THIS ROUND
- {이번 세션에서 구체적으로 바뀐 것들}
- {추가/삭제/구조 변경 — diff 성격으로 간결하게}

---

## OPEN ISSUES

| # | Issue | Status | AI Recommendation |
|---|-------|--------|-------------------|
| 1 | {이슈} | 🟢 CLOSED / 🔴 OPEN / 🟡 NEW | {추천} |

> ⚠️ 사용자 검수: 다음 AI에 넘기기 전 이 테이블을 확인하세요.

---

## NEXT AGENT ROLE

- **Agent**: {다음 AI 이름}
- **Role**: Builder / Reviewer / Researcher / Visualizer
- **Task**: {구체적 작업}
- **Focus**: {집중 포인트}
- **Output expected**: {기대 산출물 파일명}
```

---

## 릴레이 설계서

릴레이를 시작하기 전에 반드시 설계서를 먼저 작성한다:

```markdown
# Relay Plan: {프로젝트명}

## PROJECT OBJECTIVE
{최종 목표 1~2줄}

## FINAL DELIVERABLE
- 형태: md / pptx / 코드
- 기대 분량: {대략적 규모}
- 마감: {있다면}

## RELAY SEQUENCE

| Stage | AI | Role | Task | Output |
|-------|-----|------|------|--------|
| 01 | Claude | Builder | 초안 작성 | draft_v1.md |
| 02 | ChatGPT | Reviewer | 피어리뷰 | review_v1.md |
| 03 | Claude | Builder | 리뷰 반영 수정 | draft_v2.md |
| 04 | {AI} | {Role} | {Task} | {Output} |

> 빌더와 리뷰어는 반드시 다른 AI로 배정.

## ROLE DEFINITIONS
- **Builder**: 구조화된 문서 작성, 수정 반영, 톤/포맷 일관성 유지
- **Reviewer**: 비판적 평가, 강점/약점/제안 구조
- **Researcher**: 외부 정보 수집, 근거/데이터/사례 보강
- **Visualizer**: 시각적 산출물 제작

## CONSTRAINTS & NOTES
- {프로젝트 특이사항, 제약조건}
```

---

## 표준 프롬프트

### 릴레이 전달 (모든 AI 공통)
```
첨부된 핸드오프 파일과 산출물을 읽고, NEXT AGENT ROLE에 명시된 작업을 수행해주세요.

작업 완료 후, 동일한 핸드오프 포맷으로 새 핸드오프 파일을 생성해주세요.
핸드오프에는 반드시 다음을 포함:
- OBJECTIVE 그대로 유지
- KEY DECISIONS에 새 결정사항 추가
- WHAT CHANGED에 이번 변경분 기록
- OPEN ISSUES 테이블 업데이트
- NEXT AGENT ROLE에 다음 단계 지시
```

### 리뷰어 특화
```
위 표준 프롬프트 + 리뷰는 아래 구조로:
1. 강점 (잘 된 부분)
2. 약점 (개선 필요)
3. 구체적 제안 (어떻게 고치면 좋을지)
4. 치명적 빠짐 (놓친 관점, 누락된 내용)
```

### 최종 단계
```
이번이 릴레이의 마지막 단계입니다.
OPEN ISSUES가 모두 해결되었는지 확인하고 최종 산출물을 완성해주세요.
핸드오프 대신 프로젝트 완료 요약을 작성해주세요:
- 최종 결과물 설명
- 전체 릴레이 주요 변경 히스토리
- 남은 후속 작업 (있다면)
```

---

## 파일 네이밍 규칙

```
{순번}_{AI이름}_{역할}_{버전}.md
```

예시: `01_claude_draft_v1.md`, `02_gpt_review_v1.md`, `03_claude_draft_v2.md`

---

## 확장 시나리오

| 시나리오 | 릴레이 흐름 | 산출물 |
|----------|------------|--------|
| 기획서 | Claude→ChatGPT→Claude→GenSpark | md, pptx |
| 블로그/리뷰 | Claude→ChatGPT→Claude | md |
| 투자 리서치 | Claude→GenSpark→Claude→ChatGPT→Claude | md |
| 바이브 코딩 | Claude→ChatGPT→Claude | md, 코드 |
| 프레젠테이션 | Claude→ChatGPT→GenSpark→Claude | md, pptx |

> 모든 시나리오에서 프로젝트 시작은 항상 Claude.
