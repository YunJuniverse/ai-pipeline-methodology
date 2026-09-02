---
id: icons__2026-08-27_structural-edit-by-line-not-regex
origin_repo: icons
type: guide-update
target: "guide-19"
refs:
  - "https://github.com/icons-hq/icons/pull/456"
friction_ref: null
created: 2026-08-27T00:59:07Z
---

## 제안
마크다운 표·데이터 배열처럼 구조가 있는 텍스트는 정규식 범위 매칭 대신 행 단위로 편집하고 편집 후 구조를 검증하자. 비탐욕 매칭도 대상 파일의 서식이 바뀌면 경계를 넘어 무관한 블록을 먹는다. 한 세션에서 두 번 재발했다.

## 근거
- 표 구분선 일괄 치환이 무관한 5열 표를 6열로 깨뜨림 — 헤더·구분선 열 수 비교 스크립트로 발견
- 배열 항목이 한 줄로 압축돼 있어 블록 스캔이 배열을 넘어 다음 export 두 개를 삭제 — 되돌린 뒤 행 단위로 재작업

