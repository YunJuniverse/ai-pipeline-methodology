# ADR-001: Pending Lesson과 Catalog 승급 흐름 분리

## Status

accepted

## Date

2026-05-08

## Context

백서 v0.2.0은 "같은 문제에 두 번 부딪히지 않는다"를 핵심 원칙으로 둔다. 동시에 1회 발생한 마찰을 바로 active Catalog와 Skeleton에 반영하면 노이즈가 누적된다. 따라서 1회 해결된 문제와 반복 검증된 문제를 서로 다른 상태로 관리해야 한다.

## Decision

`50_resources/catalog/_pending/`을 Pending Lesson 저장소로 사용한다.

- 1회 해결된 문제는 Pending Lesson으로 기록할 수 있다.
- 동일 마찰 N>=2회 또는 사람의 명시 승인이 있을 때만 active Catalog로 승급한다.
- active Catalog만 Skeleton에 bake-in 할 수 있다.
- Pending Lesson 추가는 Class A, active Catalog 승급은 Class B로 처리한다.

## Impact Scope

- `50_resources/catalog/_README.md`의 운영 규칙
- `60_tools/methodology.py catalog` 명령
- 향후 `thinktank` 승급 후보 생성 방식
- 향후 Skeleton bake-in 대상 필터링

## Rollback Plan

`_pending/`을 제거하지 않고 active 승급 절차만 비활성화한다. 이미 생성된 Pending Lesson은 raw 학습 데이터로 보존하고, Skeleton bake-in 대상에서 계속 제외한다.
