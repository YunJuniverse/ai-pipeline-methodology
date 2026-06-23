# 사용자 플로우 (User Flow) — 템플릿

> 용도: 화면/기능 단위 사용자 흐름 — 정상·대안·실패·분기를 표로 분리. 지침 `20_guides/11_서비스기획서_작성_지침.md` §19.2(⑥ 플로우차트) · `20_guides/18_개발_마스터_플랜_작성_지침.md` §18.5 참조.

| 항목 | 내용 |
|------|------|
| 버전 / 작성일 / Status | |
| 기반 문서 (상류) | |
| 범위 (Phase/Sprint) | |

## Flow: <플로우명>

### 1. Objective
- User goal:
- Business goal:

### 2. Entry Conditions
- (진입 전제: 로그인 상태·선행 데이터 등)

### 3. Main Flow
```
[Start] → [Step 1] → [Step 2] → [End]
```

### 4. Alternate Flows

| 분기 지점 | 조건 | 대안 경로 |
|---|---|---|
| | | |

### 5. Failure Flows

| Step | 실패 조건 | Recovery (복구 동작) |
|---|---|---|
| | | |

### 6. Decision Points

| 분기 | 판단 기준(Criteria) | Next Step |
|---|---|---|
| | | |

### 7. Screens Touched
- (화면ID / 라우트 경로 나열)

**원칙**: 정상 경로만 그리지 않는다 — Alternate·Failure(+Recovery)·Decision을 *표로 분리*해야 구현·QA가 빠짐없이 따라온다. 각 화면은 Empty/Loading/Error 3-state 전제.
