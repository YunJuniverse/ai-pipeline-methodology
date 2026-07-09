---
session_id: 2026-07-09_meth-071-data-model-refresh
authored_by:
  agent: "gpt-5"
  tool: "codex-desktop"
  host_os: "darwin-26.4.1-arm64"
domain: meta
task_type: docs
stack_used:
  - "python3"
  - "methodology@v4.0"
flow_used: ad-hoc
friction: []
prompt_patterns:
  - intent: "l1 observation capture"
    success: true
    rounds: 1
---

데이터 모델 심화(문서별 9번, 개발명세 계열 마무리). 웹리서치(PostgreSQL·pgvector·OWASP·RFC 9562) → data-model.md 강화. §1 Mermaid ERD(crow's foot), 키 전략(surrogate/UUIDv7·ULID·opaque public ID), Fields에 Key/Constraints/Indexed, §4 cascade(CASCADE/RESTRICT/SET NULL 고아방지), 제약(NOT NULL/UNIQUE/CHECK/enum), history 전략(soft-delete/SCD2/append-only/bi-temporal+감사컬럼), 인덱스 원칙(FK 명시·복합·covering·partial), §7 expand-contract 무중단 마이그레이션(3단계·가역·lock-safe), §6 PII 분류/보존/GDPR 삭제(파생 벡터·캐시·백업), §8 벡터/pgvector(조건부·HNSW). 3NF 기본·비정규화 사유. _CATALOG 갱신. branch-first 준수.
