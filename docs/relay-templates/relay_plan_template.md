# Relay Plan: {프로젝트명}

> 프로젝트 시작 시 Claude에서 작성. 릴레이 전 과정의 설계도 역할.

---

## PROJECT OBJECTIVE
{이 프로젝트의 최종 목표를 1~2줄로 명확하게}

## FINAL DELIVERABLE
- 형태: {md / pptx / 코드 / 기타}
- 기대 분량: {대략적 규모}
- 마감: {있다면}

---

## RELAY SEQUENCE

| Stage | AI | Role | Task | Output |
|-------|-----|------|------|--------|
| 01 | Claude | Builder | 초안 작성 | draft_v1.md |
| 02 | ChatGPT | Reviewer | 피어리뷰 | review_v1.md |
| 03 | Claude | Builder | 리뷰 반영 수정 | draft_v2.md |
| 04 | GenSpark | Visualizer | PPT 제작 | presentation.pptx |

> 필요에 따라 Stage를 추가/삭제/순서 변경.
> **빌더와 리뷰어는 반드시 다른 AI로 배정.**

---

## ROLE DEFINITIONS

### Builder (Claude)
- 구조화된 문서 작성, 수정 반영
- 톤과 포맷 일관성 유지 책임

### Reviewer ({AI 이름})
- 비판적 관점에서 평가
- 구체적 개선 제안 포함
- 강점/약점/제안 구조로 리뷰

### Researcher ({AI 이름})
- 외부 정보 수집 및 정리
- 근거 자료, 데이터, 사례 보강

### Visualizer ({AI 이름})
- 시각적 산출물 제작
- 핸드오프의 지시사항 기반으로 슬라이드/차트 생성

---

## CONSTRAINTS & NOTES
- {프로젝트 특이사항, 제약조건, 참고사항}
- {예: "기술 용어는 한영 병기", "분량 10페이지 이내"}
