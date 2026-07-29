---
doc_id: rfc-003
title: 라이브 파일 3종 동시 갱신 의무와 병렬 작업 충돌 — 갱신 시점 재설계
status: draft
created: 2026-07-29
decides_by: Human (Class C성 — 운영 규칙 §2 변경)
---

# RFC-003 · 라이브 파일 병렬 충돌 — 갱신 시점 재설계

## 문제 (전수조사 P10, 2026-07-29)

방법론은 매 작업 단위 종료 시 라이브 파일 3종(HANDOFF·TODO·checkpoint)+관찰로그 갱신을 wrap으로 의무화한다. 이 설계가 병렬 작업과 정면 충돌한다:

- **gamblescan friction 원문**: "방법론이 매 작업마다 HANDOFF/TODO/checkpoint 갱신을 의무화해서 **병렬 PR은 구조적으로 100% 충돌**한다" → 채택 해법이 "열린 PR은 하나만 유지" = **처리량을 방법론이 1로 고정**.
- **icons**: 머지 충돌 3회 전부 동일 핫스팟(checkpoint·live 파일·CLAUDE managed 블록) — 멀티 세션 동시 편집 구조.
- **icons-marketing**: 문서 PR #17이 #16과 라이브 파일 충돌.
- **ai-icons**: 동일 머신 병행 세션 `git add -A`가 남의 미커밋 라이브 파일 갱신분을 흡수 + 티켓 번호 선점 5회.

즉 라이브 파일이 "모든 작업이 반드시 쓰는 단일 파일"이라 병렬성의 병목이자 충돌 유발원이다.

## 목표·비목표

- 목표: 병렬 PR N개가 라이브 파일 때문에 충돌하지 않을 것. 콜드스타트 부팅 계약(HANDOFF+checkpoint 요지)은 유지.
- 비목표: 라이브 파일 폐지, wrap 의무 폐지, 부팅 프라이머 약화.

## 대안

| 안 | 내용 | 장점 | 단점 |
|---|---|---|---|
| A. 현행 유지 | 직렬 머지 원칙(열린 PR 1개) | 변경 없음, 단순 | 처리량 1 고정 — 병렬 수요가 있는 repo(icons·ai-icons)에서 이미 파산 |
| B. 갱신 시점 분리 | 코드 PR은 코드만, 라이브 파일은 머지 직후 main에 별도 docs 커밋(또는 자동 봇 커밋) | 코드 PR 무충돌, 이력 깔끔 | "머지 후 갱신"을 잊으면 stale — 자동화(머지 훅) 필요. main 직접 커밋은 no-direct-push 원칙과 조정 필요 |
| C. append-only 세션 로그 | 세션별 파일(예: `.ai/sessions/<date>_<slug>.md`)에 append — 충돌 원천 불가. HANDOFF·checkpoint는 주기적 컴팩션(사람 또는 boot가 최근 N개 요약) | 병렬 완전 안전, 관찰로그와 동형 | 부팅 프라이머가 "합성"을 요구 — boot가 컴팩션 안 하면 파편화. 파일 수 증가 |
| D. 티켓 단위 샤딩 | TODO를 티켓별 파일로 분해(`todos/METH-NNN.md`), HANDOFF는 생성물로 격하 | TODO 충돌 소멸, 칸반은 빌드 산출물 | 구조 대수술 — v4.0 계약(칸반 파서·wrap·대시보드) 전면 개정 |

## 잠정 권고 (결정 아님)

**B+C 혼합**: 코드 PR에서 라이브 파일 제외(B) + checkpoint를 세션별 append 파일로 전환하고 boot가 최신 요지를 합성(C의 절반). TODO·HANDOFF는 머지 시점 갱신. 단, 이는 백서 §2-2·CLAUDE §2 wrap 계약 변경이라 **사람 결정 필요**.

## 결정 조건·다음 단계

- 병렬 세션이 일상인 repo(icons·ai-icons)에서 충돌 빈도를 2주 더 관찰(friction `where: "라이브 파일 병렬 충돌"` 통일 표기로 집계).
- 채택 시 wrap·boot·대시보드 파서·pre-push 훅 영향 범위 산정 후 Class C로 이행.
- 기각 시 A를 명문화(열린 PR 1개 원칙을 지침으로).

## 근거

- `40_dev/snapshots/2026-07-29_전레포-월간-전수조사-마찰-인사이트.md` §1 P10
- gamblescan `2026-07-16_live-state-085-applied` friction 원문
