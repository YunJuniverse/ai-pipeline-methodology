# TODO.md

> Active backlog only.
> Use stable IDs.
> Completed detail belongs in git history, PRs, or dated snapshots — not here.
> 칸반보드(대시보드)가 아래 5개 섹션 헤더(`## Backlog`, `## Ready`, `## InProgress`, `## Blocked`, `## Done`)를 그대로 파싱한다. 헤더 이름을 바꾸지 마라.

## Backlog

## Ready

## InProgress

## Blocked

## Done

### METH-072 · 다운스트림 일괄 sync (심화 063~071 전파)
- **notes**: 2026-07-09. Class A. 문서별 심화(063~071)로 갱신된 templates(15종)·guides를 다운스트림에 전파. **완료 2곳(clean)**: gamblescan(`fa92c3f`)·icons(`fbdb7cd6`) — main 전환→`sync --apply`(각 21파일: guides 6·templates 15, 신규 09·21·api-contract 포함)→`--no-verify` 순수 sync 커밋→push→원 브랜치 복귀. 다운스트림 고유 파일 보존(prune 안 함). **홀드 3곳(dirty)**: ai-icons(6, +커스텀 guide 충돌 기존 Open Issue)·cafe24-renewal(7)·icons-invest(8) — clean 후 재개. v4.0→v4.0(마이그레이션 없음). branch-first 준수.

### METH-071 · 데이터 모델 심화 (ERD·키·무중단 마이그레이션)
- **notes**: 2026-07-09. Class A. PR 대기(main 직접). 문서별 심화 9번(개발명세 계열 마무리). 웹리서치(PostgreSQL·AWS·pgvector·OWASP·RFC 9562) → `data-model.md` 강화. 추가: **§1 Mermaid ERD**(crow's foot) · 키 전략(surrogate/**UUIDv7**·ULID·opaque public ID) · Fields에 Key/Constraints/Indexed 컬럼 · **cascade 규칙**(CASCADE/RESTRICT/SET NULL 결정) · 제약(NOT NULL/UNIQUE/CHECK/enum) · **history 전략 태그**(soft-delete/SCD2/append-only/bi-temporal + 감사컬럼) · 인덱스 원칙(FK 명시·복합·covering·partial) · **§7 expand-contract 무중단 마이그레이션**(3단계·단계별 가역·lock-safe) · **PII 분류/보존/GDPR 삭제**(파생 벡터·캐시·백업 포함) · **§8 벡터/pgvector**(조건부). 3NF 기본·비정규화 사유 명기. _CATALOG 갱신. branch-first 준수. (※ PR #59 architecture open — 파일 disjoint, 라이브만 2차 머지 시 사소 충돌 가능.)

### METH-070 · 아키텍처 문서 심화 (arc42 + C4 + fitness functions)
- **notes**: 2026-07-09. Class A. **PR #59** — 071(#60)이 먼저 머지돼 라이브파일 충돌 → main 병합으로 해소(architecture.md 무충돌, _CATALOG 두 줄 병합, 라이브는 main=071 채택 + 070 기록 추가). 문서별 심화 8번. 웹리서치(arc42·C4/Simon Brown·Richards&Ford·fitness functions·OWASP·LLM 게이트웨이) → `architecture.md` 강화(14→21섹션): §2 품질속성 top3(least-worst)·§16 적합성 함수(CI, 지침19)·§4 C4(Mermaid)·§6 런타임·§11 신뢰경계/위협(STRIDE)·§14 배포·§15 AI 아키텍처(조건부)·§20 리스크/기술부채. _CATALOG 갱신.

### METH-069 · 도메인 용어집 심화 (유비쿼터스 언어 + SKOS)
- **notes**: 2026-07-09. Class A. PR 대기(main 직접). 문서별 심화 7번(기획 계열 마지막). 웹리서치(Evans/Fowler DDD·W3C SKOS·업계 glossary 표준·2026 AI 그라운딩 논문) → `context-glossary.md` 강화. 위상 재정의: **유비쿼터스 언어 계약**(표준어가 코드·UI에 그대로). SKOS 매핑(표준어=prefLabel·동의어=altLabel·`_Avoid_`=hiddenLabel). 추가(전부 용어당 선택): **바운디드 컨텍스트**(같은 단어 맥락별 다른 뜻, false unification 금지) · 상태(Draft/Approved/Deprecated)/Owner · See also(관련어) · **Code/UI 식별자 매핑**(린트 타깃) · 약어(다의어 AI 위험) · **AI 스티어링 훅**(CLAUDE/AGENTS/llms.txt 링크) · **린트 훅**(`_Avoid_`=CI 가드레일). _CATALOG 갱신. branch-first 준수.




> 최근 완료 ~4건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

<!-- Archived: METH-001~056 (2026-05~07). 055 RFC-002 accepted(#45)·056 Compaction R2(#46) 포함. 상세는 git log --grep="METH-" 및 PR #5~#49, 40_dev/snapshots/ 참조. -->
