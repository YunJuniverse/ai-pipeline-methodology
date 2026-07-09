# Checkpoint — 2026-07-09 (METH-071 데이터 모델 심화 · ERD·키·무중단 마이그레이션)

> ✅ METH-071: 문서별 심화 9번(개발명세 계열 마무리) = data-model. 웹리서치(PostgreSQL·pgvector·OWASP·RFC 9562) → 강화.
> 핵심: Mermaid ERD · UUIDv7 키 · cascade · history 전략(SCD2/soft-delete) · **expand-contract 무중단 마이그레이션**(Class B rollback 증거) · PII/GDPR(파생 포함) · 벡터(조건부).
> 🏁 다음: PR 리뷰·머지 → 심화 계속(기획서 지침군/agency 템플릿) 또는 **누적 다운스트림 sync**.
> ⚙️ **070(#59) 충돌 해소 병합**(이 브랜치): 071(#60) 선머지로 라이브파일 충돌 → `git merge main`으로 해소(architecture.md 무충돌·_CATALOG 두 줄 병합·라이브=main/071 채택+070 기록). push 후 #59 머지 → 그다음 다운스트림 sync(063~071 전체).

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-071-data-model-refresh` (fresh main=069 기준 — 070 #59 미머지, data-model과 disjoint. branch-first 준수)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-071 — 데이터 모델(data-model.md) 심화** (문서별 심화 프로그램 9번, 개발명세 계열 마무리):

- **방법**: 웹리서치 1차 소스(PostgreSQL docs·AWS/DynamoDB·pgvector·OWASP LLM Top10·RFC 9562·Kimball SCD2·expand-contract). 현행 7섹션(Entity/Fields/Relationships/Integrity/Privacy/Migration/Changelog) gap.
- **변경 (`50_resources/templates/data-model.md`)**:
  - **§1 Mermaid ERD**(crow's foot, diagrams-as-code) 신설.
  - **키 전략**: surrogate 기본 · 분산/외부노출 = **UUIDv7/ULID**(시간정렬 인덱스 지역성; UUIDv4 PK 비권장) · 외부는 opaque public ID. §2 Entity List에 PK전략·History 컬럼.
  - **Fields**: Key(PK/FK/UK)·Constraints(default·CHECK·enum)·Indexed?(왜) 컬럼 추가.
  - **§4 Relationships**: **On Delete/Update**(CASCADE 일회용부품 / RESTRICT 독립중요 / SET NULL) — 고아 방지 스펙.
  - **§5 Integrity**: 제약(스키마에 박기) · 감사컬럼 · **history 전략 태그**(soft-delete[GDPR 삭제 불충족]·SCD2·append-only·bi-temporal) · 인덱스 원칙(FK 명시·복합·covering·partial).
  - **§6 PII**: 분류(public/internal/PII/민감)·암호화·접근·보존·삭제 표 + **GDPR Art.17**(파생 벡터·캐시·백업까지).
  - **§7 Migration = Expand→Backfill(청크)→Contract**(단계별 가역·lock-safe `CONCURRENTLY`) = Class B rollback 증거.
  - **§8 AI/Vector**(조건부): `vector(N)`·모델·전처리·HNSW·삭제 tombstone.
  - 3NF 기본·비정규화 사유 명기 · 스키마 계약 버전 api-contract 연동 · _CATALOG 갱신.

## 다음 사람에게 (구체적 첫 행동)

1. METH-071 PR 리뷰·머지. **#59(070 architecture) 먼저 머지 권장** — 그 후 071 머지 시 라이브 파일(TODO/HANDOFF/checkpoint) 사소한 충돌만 해소(내용 파일은 disjoint라 무충돌).
2. **문서별 심화** — 기획+개발명세 *템플릿* 계열 완료(063~071). 남은 축: 기획서 *지침*군(운영 12·마케팅 13·브랜드 14·PM 15·AI기능 16·평가 17), agency/ops 템플릿(proposal·qa·operation·profitability·execution-plan·wbs 등).
3. **누적 심화(063~071)를 다운스트림에 일괄 sync** — 강력 권장 타이밍(9개 PR 상당 쌓임).
4. METH-060 잔여(ai-icons 번호 정리 등).

## 미해결 결정사항 (Open Questions)

- 070(#59)·071 병행 PR — 라이브 파일 2차 머지 충돌 예상(내용 무충돌). 머지 순서 #59→071 권장.
- 누적 심화 sync 타이밍(세트로).
- 심화 템플릿군 lean 유지 — data-model은 다수 조건부(벡터·SCD2·bi-temporal)라 기본은 최소, 필요분만.

## 환경 메모

- 브랜치: `claude/meth-071-data-model-refresh` (fresh main=069 기준). main 직접 PR. branch-first 준수.
- 변경: `50_resources/templates/data-model.md`(재작성) + `_CATALOG.md`(한줄) + 라이브 4종.
- 문서별 심화 진척: 063#53·064#54·065#55·066#56·068#57·069#58 머지 / 067 main직접(A) / 070 architecture #59 open / 071 data-model(이번). **기획+개발명세 템플릿 계열 완료.**
