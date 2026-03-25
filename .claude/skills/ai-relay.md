---
name: ai-relay
description: 하네스 기반 멀티AI 릴레이 가이드. 피어리뷰, 외부 리서치, 시각화 작업을 스프린트 문서 체계와 연결한다.
---

# AI Relay Guide

## 언제 사용하는가

- 다른 AI에게 피어리뷰를 맡길 때
- 외부 리서치 보강이 필요할 때
- PPT 같은 시각 산출물이 필요할 때
- 스프린트 결과를 외부 AI에게 검토시킬 때

---

## 핵심 원칙

1. Builder와 Reviewer는 분리한다
2. 릴레이는 현재 스프린트와 현재 버전 기준으로 보낸다
3. 산출물보다 맥락 압축 문서가 우선이다
4. 릴레이 결과도 다시 인간 승인 체계 안으로 가져온다

---

## 기본 전달 세트

릴레이 시 보낼 기본 세트는 아래다.

- 현재 relevant 문서
- 현재 버전
- 현재 스프린트
- 현재 목표
- 현재 open issues
- 요청받은 역할

가능하면 아래 중 필요한 것만 보낸다.

- research summary
- planning doc excerpt
- development spec excerpt
- sprint completion report
- sprint feedback report
- executive decision brief

---

## Handoff Note 구조

```markdown
# HANDOFF NOTE

- Project:
- Current Version:
- Current Sprint:
- Current Phase:
- Completed By:
- Date:

## OBJECTIVE

## WHY THIS RELAY IS HAPPENING

## CURRENT CONTEXT
- Relevant artifacts:
- Relevant constraints:
- Approval boundaries:

## WHAT CHANGED THIS ROUND

## OPEN ISSUES

## REQUEST FOR NEXT AGENT
- Role:
- Task:
- Output expected:
- What not to change:
```

---

## Relay Plan 구조

```markdown
# Relay Plan

## Objective

## Final Deliverable

## Current Sprint Context

## Relay Sequence
| Stage | AI | Role | Task | Output |

## Approval Notes
- What needs human approval before adoption:
- What can be treated as advisory only:
```

---

## 리뷰어 지침

리뷰어에게는 아래 기준을 우선 요청한다.

1. 계획 대비 구현 일치도
2. 레퍼런스 대비 괴리
3. 휴먼리더블 가독성
4. QA / UX 리스크
5. 다음 스프린트에서 반드시 반영할 항목

---

## 릴레이 후 처리

릴레이 결과를 받으면 아래 중 어디에 반영할지 판단한다.

- `sprint-completion-report`
- `sprint-feedback-report`
- `executive-decision-brief`
- `approval-log`
- planning docs next version
- development spec next version

릴레이 결과를 그대로 채택하지 말고,
반드시 인간 검토 또는 승인 조건을 확인한다.
