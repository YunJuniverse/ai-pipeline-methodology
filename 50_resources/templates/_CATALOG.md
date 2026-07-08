# 템플릿 카탈로그 — 작업 모드별 선택 (`_CATALOG.md`)

> 방법론 템플릿이 25종 이상으로 늘었다. **모든 작업에 모든 템플릿을 쓰지 않는다** — 작업 *모드*에 맞는 세트만 고른다.
> CLAUDE.md §1 `Mode`에 모드를 적고, 이 카탈로그에서 그 모드의 권장 세트만 로드한다. (지침 `20_guides/00_AI_기획_프로젝트_운영_원칙.md` §11.5·11.7)
>
> **경로는 flat 유지** — 폴더로 나누지 않는다(기존 지침·문서의 참조 경로가 깨지므로). 분류는 이 문서가 담당한다.

---

## 1. 작업 모드 (6종) → 권장 세트

| 모드 | 용도 | 권장 템플릿 세트 |
|---|---|---|
| **planning** | 기획전용 (구현 안 함) | prd · requirements-spec · ia-spec · service-policy · user-story · kpi-tree · context-glossary · microcopy |
| **planning-handoff** | 기획전용 → *별도 사람 개발자*에게 인계 (AI 아닌 사람이 읽음) | `planning` 세트 + user-flow · functional-spec · wireframe-spec — **단, 지침 `20_guides/09_기획_핸드오프_재포맷_규칙.md`의 재포맷 규칙을 얹어 산출**(ASCII→실제 목업, ON/OFF→must/should, 의도·읽는 순서·질문 루프 추가). architecture·data-model은 개발자 소유이므로 제외(필요 시 끌어 씀) |
| **dev** | 개발전용 (기획 받아 구현) | architecture · data-model · api-contract · user-flow · wireframe-spec · functional-spec (작성·조합·인계 표준은 지침 `20_guides/21_개발명세_작성_지침.md`) |
| **fullstack** | 기획+개발 일괄 | `planning` ∪ `dev` + wbs |
| **agency** | 외주(수주·납품) SI 라이프사이클 | proposal-go-nogo · research-collection-checklist · profitability-sheet · execution-plan · wbs · qa-acceptance-plan · qa-test-scenario · qa-acceptance-signoff · operation-spec · post-launch-monitoring · work-request-ticket · glossary (+ 산출물은 `planning`/`dev`에서) |
| **lean** | 1인+AI 빠른 반복 | prd · architecture · context-glossary · ADR-template |
| **ops** | 런칭 후 운영 | operation-spec · post-launch-monitoring · work-request-ticket · qa-acceptance-plan · qa-test-scenario · qa-acceptance-signoff |

> **항상(모드 무관)**: `ADR-template`(비가역 결정) · 라이브 상태 파일 `TODO`·`HANDOFF`·`checkpoint`·`context.json`. `MASTER_PLAN`·`SPRINTS`는 `fullstack`/`dev`/`agency`에서 사용.

---

## 2. 템플릿 카탈로그 (25종, 카테고리별)

### 기획 (Planning)
| 템플릿 | 한 줄 |
|---|---|
| `prd.md` | 제품 요구사항(무엇) — 비전·목표/비목표·범위·기능요구(M/S·Pn=출시순서)·규제 요구사항·출시단계 |
| `requirements-spec.md` | 요구사항 추적 대장 — ID·중요도·출처(VOC)·수용여부 enum·사유·M/S+Pn |
| `ia-spec.md` | 정보구조 기능정의서 — 화면ID·Page Type·권한 매트릭스 |
| `service-policy.md` | 서비스 정책 정의서 — 반복규칙→ON(자동)/OFF(가이드), 2-시트 |
| `user-story.md` | 유저스토리·시나리오 — As-a/I-want/So-that + 내러티브 7요소 |
| `kpi-tree.md` | KPI 단위경제 트리 + 마켓플레이스 10-패널·분석방법 배터리 |
| `context-glossary.md` | 도메인 용어집 — 표준어 + `_Avoid_`(금지 동의어) + 예시 대화 |
| `microcopy.md` | UX 라이팅 — 에러·확인·공백 상태별 카피 + 보이스앤톤 |

### 개발명세 (Dev-spec)
| 템플릿 | 한 줄 |
|---|---|
| `architecture.md` | 아키텍처(어떻게) — as-built→목표→mock→real 이전경로·규제 기술매핑 |
| `data-model.md` | 데이터 모델 — 엔티티·필드·관계·무결성·마이그레이션 |
| `api-contract.md` | API·인터페이스 계약 — 엔드포인트·요청/응답·에러·버전·인증 (개발리드→개발자, FE/BE 병렬 조율축). functional-spec의 상위 시스템 레벨 |
| `user-flow.md` | 사용자 플로우 — 정상/대안/실패(+복구)/분기 |
| `wireframe-spec.md` | 화면설계(텍스트 ASCII) — 화면별 5블록·Empty/Loading/Error 3-state |
| `functional-spec.md` | 기능명세 — FS-ID·비즈니스 규칙·권한 매트릭스·예외(레이어별) |

### PM·일정
| 템플릿 | 한 줄 |
|---|---|
| `wbs.md` | 작업분해 — Step→Activity→Task·3점추정·직무 8레인 |

### 제안·수주 (Proposal / Agency)
| 템플릿 | 한 줄 |
|---|---|
| `proposal-go-nogo.md` | 제안여부검토서 — 8축 점수 → 진행/추가수집/포기 |
| `research-collection-checklist.md` | 자료수집표 — 경쟁/고객/사이트 현황 추적 |
| `profitability-sheet.md` | 수익율 관리표 — 직급단가×M/M + 간접비 + 월별 수익율 |
| `execution-plan.md` | 수행계획서 — 업무범위·M/M 매트릭스·RACI·산출물 4계층 |

### 검수 (QA)
| 템플릿 | 한 줄 |
|---|---|
| `qa-acceptance-plan.md` | 검수계획서 — 범위·환경·합격기준·예외약정 |
| `qa-test-scenario.md` | 검수 시나리오 — 무작위형/시나리오형 2모드·결과 enum |
| `qa-acceptance-signoff.md` | 검수확인서 — 양측 서명 sign-off(대금 근거) |

### 운영 (Ops)
| 템플릿 | 한 줄 |
|---|---|
| `operation-spec.md` | 운영명세서 — 일/주/월/수시·시스템·리포트 체계 |
| `post-launch-monitoring.md` | 오픈후 모니터링 리포트 — 결함 추적(접수/처리중/완료) |
| `work-request-ticket.md` | 업무요청·처리서 — 접수→영향분석→결정(운영 RFC) |
| `glossary.md` | 용어규약집 — 단계별 표준용어·개정이력 |

### 결정·계획 (항상/공용)
| 템플릿 | 한 줄 |
|---|---|
| `ADR-template.md` | 결정 기록 — 결정문장 제목·Considered Options·되돌리기 비용 |
| `MASTER_PLAN.md` | 개발 마스터플랜 — 비전→페이즈·게이트 매핑 |
| `SPRINTS.md` | 스프린트 추적 |

---

## 3. 모드 × 템플릿 매트릭스

> ✓ = 그 모드의 권장 세트. `agency`는 제안·검수·운영 산출물 + 실제 기획/개발 산출물(planning/dev)을 함께 쓴다.

| 템플릿 | planning | planning-handoff | dev | fullstack | agency | lean | ops |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| prd | ✓ | ✓ | | ✓ | ✓ | ✓ | |
| requirements-spec | ✓ | ✓ | | ✓ | ✓ | | |
| ia-spec | ✓ | ✓ | | ✓ | ✓ | | |
| service-policy | ✓ | ✓ | | ✓ | ✓ | | |
| user-story | ✓ | ✓ | | ✓ | ✓ | | |
| kpi-tree | ✓ | ✓ | | ✓ | ✓ | | |
| context-glossary | ✓ | ✓ | | ✓ | ✓ | ✓ | |
| microcopy | ✓ | ✓ | | ✓ | ✓ | | |
| architecture | | | ✓ | ✓ | ✓ | ✓ | |
| data-model | | | ✓ | ✓ | ✓ | | |
| api-contract | | | ✓ | ✓ | ✓ | | |
| user-flow | | ✓ | ✓ | ✓ | ✓ | | |
| wireframe-spec | | ✓† | ✓ | ✓ | ✓ | | |
| functional-spec | | ✓ | ✓ | ✓ | ✓ | | |
| wbs | | | | ✓ | ✓ | | |
| proposal-go-nogo | | | | | ✓ | | |
| research-collection-checklist | | | | | ✓ | | |
| profitability-sheet | | | | | ✓ | | |
| execution-plan | | | | | ✓ | | |
| qa-acceptance-plan | | | | | ✓ | | ✓ |
| qa-test-scenario | | | | | ✓ | | ✓ |
| qa-acceptance-signoff | | | | | ✓ | | ✓ |
| operation-spec | | | | | ✓ | | ✓ |
| post-launch-monitoring | | | | | ✓ | | ✓ |
| work-request-ticket | | | | | ✓ | | ✓ |
| glossary | | | | | ✓ | | |
| ADR-template | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| MASTER_PLAN | | | ✓ | ✓ | ✓ | | |
| SPRINTS | | | ✓ | ✓ | ✓ | | |

> **† `planning-handoff`의 산출물은 AI가 아닌 *사람 개발자*가 읽는다** — 위 세트를 지침 `20_guides/09_기획_핸드오프_재포맷_규칙.md`의 재포맷 규칙으로 변환해 산출한다: `wireframe-spec`은 ASCII 대신 **실제 목업/Figma**로, `service-policy`의 ON/OFF는 **must/should**로, `context-glossary`의 `_Avoid_`는 경량화, 그리고 **의도(왜)·읽는 순서·열린 질문 루프**를 얹는다. `architecture`·`data-model`은 개발자 소유이므로 기본 제외(필요 시 끌어 씀).

---

**원칙**: 모드는 *시작점*이지 족쇄가 아니다 — 필요하면 다른 모드의 템플릿을 끌어 쓰되, *불필요한 템플릿을 의무로 채우지 않는다*. 새 템플릿을 추가하면 이 카탈로그(카테고리·매트릭스·해당 모드 세트)도 함께 갱신한다.
