---
id: MP-002
title: "sync의 init_files가 기존 적용 프로젝트 마이그레이션에 적용 안 됨"
domain: meta-methodology
status: pending
seen_in:
  - 2026-05-12
signature: "sync.*init_files.*기존.*프로젝트.*\\.ai/context\\.json.*미생성"
verified_with:
  - claude-sonnet-4-6
deps_implicated:
  - 50_tools/methodology.py
  - migrations/*.py
created: 2026-05-12
last_hit: 2026-05-12
---

## 증상

새 버전에서 `init_files`에 `(40_resources/templates/context.json, .ai/context.json, True)` 같은 항목이 추가되어도, *기존 적용 프로젝트는 sync로 마이그레이션될 때* 이 파일을 받지 못한다. `sync`는 *shared_paths만 덮어쓰고 init_files는 init 단계 전용*이기 때문.

v3.1 → v3.2 마이그레이션 초기 dry-run에서 `.ai/context.json` / `.ai/checkpoint.md`가 *출력에 안 보임*을 발견 — L0 핵심 파일이 마이그레이션에서 빠지는 사고가 될 뻔함.

## 근본 원인

`sync` 의 의도된 보수성 — *사용자가 수정한 init_files* (예: CLAUDE.md, HANDOFF.md)를 절대 덮어쓰지 않기 위해 sync는 init_files를 건드리지 않는다. 그러나 *기존에 없던 init_file이 신규 추가*된 경우, 적용 프로젝트는 영원히 그 파일을 못 받음.

## 솔루션 (v3.1→v3.2에서 적용한 방식)

`migrations/v3.1_to_v3.2.py`에 `_materialize_l0()` 함수 추가:
- *없을 때만* 생성 (멱등성·사용자 콘텐츠 보존)
- 마이그레이션 스크립트가 *임베디드 템플릿*을 직접 들고 다님 (templates 디렉터리 의존성 회피 — sync가 templates를 먼저 채우기 *전* 단계라 templates 비어있을 수 있음)
- `.methodology-version`에서 project_label 추출 → 치환

## 더 일반화된 솔루션 (RFC 후보)

- MANIFEST에 `migration_init_files` 카테고리 신설 — *기존 프로젝트 마이그레이션 시에만* 작동하는 init_files
- `cmd_sync`가 마이그레이션 단계에서 이 카테고리를 *없을 때만* 적용
- 임베디드 템플릿 우회 가능 (templates에서 직접 읽기)

## 안티패턴

- ❌ 신규 init_files를 *기존 프로젝트가 자동으로 받을 것*이라고 가정
- ❌ sync 출력에 안 보이는 *예상 파일*을 그냥 넘김 — dry-run 결과를 *기대 목록 vs 실측*으로 명시 비교 필수
- ❌ 마이그레이션 스크립트에서 templates 디렉터리 의존 (sync 순서상 templates가 채워지기 *전* 단계)

## 관련 자료

- 메타 관찰: `60_meta/observations/2026-05-12_v3.1-to-v3.2-migration.md` §F-002
- 적용 예: `migrations/v3.1_to_v3.2.py` `_materialize_l0`
- 코드: `50_tools/methodology.py` `cmd_sync`, MANIFEST

## 승급 조건

- N≥2 목격 시 active 승급 (현재 N=1)
- 다음 v3.x 마이그레이션에서 *어떤 새 init_file을 추가하면서 동일 문제 재발*하면 자동 hit
