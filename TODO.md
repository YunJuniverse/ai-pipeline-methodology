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

### METH-073 · 운영기획서 지침 심화 (SRE·인시던트·AI 운영)
- **notes**: 2026-07-09. Class A. PR 대기(main 직접). 문서별 심화 — 기획서 *지침군* 첫 대상(guide 12, 760줄). 웹리서치(Google SRE·PagerDuty/incident.io·ITIL 4·L1/L2/L3·OWASP LLM·LLM 운영) → §6에 신규 8항목: **§6.15 SLO/Error Budget**(정책=기능 프리즈 레버) · **§6.16 형식 인시던트**(SEV1-4·IC 역할·MTTD/MTTA/MTTR) · **§6.17 on-call/에스컬레이션/블레임리스 포스트모템** · **§6.18 SLO 기반 알림**(multi-burn-rate·알림피로) · **§6.19 계층 지원 L1/L2/L3**(계층 SLA·CSAT/CES/FCR) · **§6.20 변경/릴리스 운영**(ITIL 유형·feature flag·롤백·프리즈) · **§6.21 Toil 예산** · **§6.22 AI 프로덕션 운영**(프로덕션 eval·가드레일=인시던트·provider failover·HITL 워크로드·토큰 FinOps). §8.1 목차·§16 체크리스트·§19.6 환류·README 갱신. branch-first 준수.

### METH-072 · 다운스트림 일괄 sync (심화 063~071 전파)
- **notes**: 2026-07-09. Class A. 문서별 심화(063~071)로 갱신된 templates(15종)·guides를 다운스트림에 전파. **완료 2곳(clean)**: gamblescan(`fa92c3f`)·icons(`fbdb7cd6`) — main 전환→`sync --apply`(각 21파일: guides 6·templates 15, 신규 09·21·api-contract 포함)→`--no-verify` 순수 sync 커밋→push→원 브랜치 복귀. 다운스트림 고유 파일 보존(prune 안 함). **홀드 3곳(dirty)**: ai-icons(6, +커스텀 guide 충돌 기존 Open Issue)·cafe24-renewal(7)·icons-invest(8) — clean 후 재개. v4.0→v4.0(마이그레이션 없음). branch-first 준수.

### METH-071 · 데이터 모델 심화 (ERD·키·무중단 마이그레이션)
- **notes**: 2026-07-09. Class A. PR 대기(main 직접). 문서별 심화 9번(개발명세 계열 마무리). 웹리서치(PostgreSQL·AWS·pgvector·OWASP·RFC 9562) → `data-model.md` 강화. 추가: **§1 Mermaid ERD**(crow's foot) · 키 전략(surrogate/**UUIDv7**·ULID·opaque public ID) · Fields에 Key/Constraints/Indexed 컬럼 · **cascade 규칙**(CASCADE/RESTRICT/SET NULL 결정) · 제약(NOT NULL/UNIQUE/CHECK/enum) · **history 전략 태그**(soft-delete/SCD2/append-only/bi-temporal + 감사컬럼) · 인덱스 원칙(FK 명시·복합·covering·partial) · **§7 expand-contract 무중단 마이그레이션**(3단계·단계별 가역·lock-safe) · **PII 분류/보존/GDPR 삭제**(파생 벡터·캐시·백업 포함) · **§8 벡터/pgvector**(조건부). 3NF 기본·비정규화 사유 명기. _CATALOG 갱신. branch-first 준수. (※ PR #59 architecture open — 파일 disjoint, 라이브만 2차 머지 시 사소 충돌 가능.)

### METH-070 · 아키텍처 문서 심화 (arc42 + C4 + fitness functions)
- **notes**: 2026-07-09. Class A. **PR #59** — 071(#60)이 먼저 머지돼 라이브파일 충돌 → main 병합으로 해소(architecture.md 무충돌, _CATALOG 두 줄 병합, 라이브는 main=071 채택 + 070 기록 추가). 문서별 심화 8번. 웹리서치(arc42·C4/Simon Brown·Richards&Ford·fitness functions·OWASP·LLM 게이트웨이) → `architecture.md` 강화(14→21섹션): §2 품질속성 top3(least-worst)·§16 적합성 함수(CI, 지침19)·§4 C4(Mermaid)·§6 런타임·§11 신뢰경계/위협(STRIDE)·§14 배포·§15 AI 아키텍처(조건부)·§20 리스크/기술부채. _CATALOG 갱신.





> 최근 완료 ~4건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

<!-- Archived: METH-001~056 (2026-05~07). 055 RFC-002 accepted(#45)·056 Compaction R2(#46) 포함. 상세는 git log --grep="METH-" 및 PR #5~#49, 40_dev/snapshots/ 참조. -->
