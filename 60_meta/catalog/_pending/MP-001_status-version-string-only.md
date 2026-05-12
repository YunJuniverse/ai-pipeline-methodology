---
id: MP-001
title: "methodology status가 버전 문자열만 비교 — 같은 v3.1 안의 commit 격차 미감지"
domain: meta-methodology
status: pending
seen_in:
  - 2026-05-12
signature: "methodology.*status.*최신.*✓.*적용된.*옛.*commit"
verified_with:
  - claude-sonnet-4-6
deps_implicated:
  - 50_tools/methodology.py
created: 2026-05-12
last_hit: 2026-05-12
---

## 증상

`python3 50_tools/methodology.py status --path <project>` 출력:

```
applied version  v3.1
upstream version v3.1
status:          최신 ✓
```

그러나 실제로는 적용 시점의 `upstream_commit`과 현재 origin commit이 다르며, 그 사이에 *MANIFEST 확장·새 디렉터리·구조 재편* 등 무시 못 할 격차가 누적되어 있다. 사용자(및 AI 보조자)는 "최신"이라는 표시를 *그대로 신뢰*하여 격차를 놓치기 쉽다.

본 저장소의 v3.1 → v3.2 마이그레이션 중 icons/gamblescan/talmocom 세 프로젝트 모두에서 *"최신 ✓"으로 잘못 표시*되어 발견됨.

## 근본 원인

`cmd_status`가 *메이저 버전 문자열*(예: `v3.1` vs `v3.2`)만 비교한다. 같은 메이저 버전 안에서의 *upstream commit 격차*를 검출하는 로직이 없다.

## 솔루션 (제안 — RFC-001 후보)

- `.methodology-version`에 이미 저장된 `upstream_commit`을 *origin/main의 commit*과 비교
- 다르면 "behind upstream — <commit short>" 같은 부가 표시
- 또는 *sync에 의미 있는 변경*이 있는지 dry-run으로 미리 검증해 표시 (더 정확하지만 비용 큼)
- 최소안: commit hash 차이만 표시. 사용자가 dry-run 결정.

## 안티패턴

- ❌ `status` 출력을 *그대로 신뢰* (실측 검증 생략)
- ❌ 버전 문자열만으로 "동기 상태" 판정
- ❌ 같은 버전 안의 *내부 진화*를 자동 마이그레이션이 잡을 거라고 가정 — `migrations/`는 *버전 bump*에만 트리거됨

## 관련 자료

- 메타 관찰: `60_meta/observations/2026-05-12_v3.1-to-v3.2-migration.md` §F-001
- RFC-001 (예정): `60_meta/rfc/RFC-001_status-upstream-commit-check.md`
- 코드: `50_tools/methodology.py` `cmd_status`

## 승급 조건

- N≥2 목격 시 active 승급 (현재 N=1)
- 또는 사람이 명시 승인 시 PR/ADR에 이유 명시
