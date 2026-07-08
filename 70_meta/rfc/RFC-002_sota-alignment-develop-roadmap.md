---
id: RFC-002
title: 최신 하네스·루프·경험메모리 엔지니어링 대비 방법론 평가 + 발전 로드맵
status: accepted
proposed_by: claude-opus-4-8
proposed_at: 2026-07-08
accepted_at: 2026-07-08
accepted_via: 2026-Q3 분기 회고 (PR #44)
target_class: A
supersedes: null
relates_to: [RFC-001, 2026-Q3, MP-003]
---

# RFC-002 — SOTA(하네스·루프·경험메모리) 정합 평가 + 발전 로드맵

> 이 문서는 *로드맵*이다. 개별 항목은 각자의 change class로 별도 RFC/ADR·구현 커밋을 갖는다. 본 RFC 채택 = "이 로드맵을 방법론 진화 백로그로 인정"까지.

> **✅ 비준 (Accepted) — 2026-07-08.** `2026-Q3` 분기 회고(PR #44 머지)로 사람 게이트 통과 = 방법론 진화 백로그로 확정. 회고 §4가 우선순위를 지정: **P1** R1(Reflect/Learn 자동화 + 지표 인프라·thinktank 존폐) · **P2** R2(compaction) · **P3** 온보딩 다이어트. 개별 항목은 구현 시 각자의 change class를 따르며, Class B/C 항목(예: R6 게이트 다이어트)은 별도 ADR을 신설한다. 별도 단일 ADR로 승급하지 않는다(RFC-001 선례 — accepted Class A RFC는 로드맵/도구 변경이라 ADR 미승급).

## Context

2026-07 기준 최신 에이전트 엔지니어링 프레임(harness engineering · context engineering · loop engineering · experiential reflective learning)을 웹 리서치해 본 방법론의 구조를 대조 평가했다. 결론: **코어 설계 철학은 SOTA와 정합하거나 앞서 있으며, 약점은 단일 축 — 루프의 Reflect/Learn 자동화 + 런타임 규율(compaction·budget)에 국한**된다. 이 약점은 앞선 무게 감사(휴면 thinktank, ~9주 초과된 ROI 게이트)가 지목한 지점과 정확히 겹친다.

### 이미 SOTA 정합/선행인 것 (버리거나 갈아엎을 것 없음)

| 방법론 요소 | 대응 개념 | 판정 |
|---|---|---|
| L1 관찰로그 → L2 Catalog 승급(N≥2) → skeleton bake-in | Experiential Reflective Learning / ExpeL (궤적→재사용 휴리스틱 증류·승급) | SOTA 정합 |
| checkpoint·HANDOFF·TODO | Structured note-taking / 외부 메모리 (Anthropic) | 정본급 |
| 이식성 제0원칙(모델·세션·환경) | 벤더 중립 하네스 / control plane | 선행 (대부분 하네스는 벤더 락) |
| Guardrails-by-construction (fail-closed warn→error 래칫) | 하네스 안전 강제 · "guardrails before scaling" | 선행 |
| 5개 휴먼 게이트 | Human-in-the-loop gates (비가역 액션 전 필수 리뷰) | 정합 |
| bootstrap task-type + skeletons | 2-phase (initializer→coding agent) | 정합 |
| CLAUDE.md+HANDOFF 기본 부트, TODO/ADR 온디맨드 | Just-in-time 컨텍스트 검색 | 정합 |
| guide 04 산출물 채널 분리 | Context 위생 (signal>noise, context rot 방지) | 정합 |

## Proposal — 발전 로드맵 (우선순위순)

### R1 [HIGH · Class B] Reflect/Learn 아크 자동화 — 최대 레버
**갭:** ERL/ExpeL의 핵심은 휴리스틱을 *관련성 점수로 검색해 컨텍스트에 자동 주입*하는 것. 본 방법론의 Catalog `signature`는 regex 검색키일 뿐, 승급은 수동 PR, L3 thinktank는 휴면(무게 감사 확증). 루프에서 가장 가치 있는 단계가 가장 덜 자동화됨.
**제안:**
- (a) 세션 부팅 시 현재 작업과 관련성 높은 Catalog 엔트리를 top-k 자동 주입(현 memory recall과 Catalog를 연결).
- (b) thinktank를 wrap/ship 케이던스에 결합하거나, 최소한 "수동 승급이 정식"임을 문서·CLI 도크스트링에 반영(문서-현실 부패 해소).
**출처:** ERL(arXiv 2603.24639), Anthropic note-taking.

### R2 [HIGH · Class A] Compaction 프로토콜 신설
**갭:** Anthropic이 장기 실행의 1순위 기법으로 꼽는 compaction("한계 근처 요약·재시작, recall 최대화 후 precision")이 방법론에 부재. checkpoint는 세션 종료 시점 기준일 뿐 *긴 단일 세션의 compaction 규율*이 없음.
**제안:** "compaction 경계에서 무엇이 살아남는가" 스펙 신설(보존=아키텍처 결정·게이트 상태·미해결 open question / 폐기=원시 툴 출력·중복). checkpoint 트리거를 세션 종료뿐 아니라 compaction 경계에도 확장.
**출처:** Anthropic context engineering.

### R3 [MED · Class A] Budget & stop conditions 도입
**갭:** loop engineering은 토큰·비용 예산, no-progress 감지, 반복 캡을 필수로 봄(단일 ~4×, 멀티 ~15× 토큰). 방법론의 유일한 정지는 휴먼 게이트뿐 — 자율 진행 구간의 compute 규율 없음.
**제안:** 자율 진행(대규모 전파·리트로핏) 구간에 budget tracker + no-progress exit 지침. 자율성 선호(메모리 [[user-autonomy-multistep]])와 결합해 "예산 내 자율, 초과 시 사람에게 보고" 규율화.
**출처:** loop engineering.

### R4 [MED · Class A] 서브에이전트 오케스트레이션을 1급 자산으로
**갭:** Anthropic은 서브에이전트(컨텍스트 격리→1~2k 토큰 요약 반환)를 장기 작업 핵심으로 봄. 방법론은 "1인" 프레임이라 미명문화 — 정작 이 평가·감사·토론을 전부 서브에이전트 워크플로우로 수행함(패턴은 쓰는데 자산화 안 됨).
**제안:** 워크플로우/서브에이전트 패턴(context 격리 + 요약 반환 규약 + 적대적 검증)을 지침 또는 Catalog 자산으로 코드화.
**출처:** Anthropic sub-agents.

### R5 [MED · Class A] 관련성 기반 메모리 검색 업그레이드
**갭:** Catalog 검색이 regex `signature` 수준. ERL은 관련성 점수 top-후보 주입이 few-shot보다 우수함을 실증.
**제안:** signature(regex) → 관련성 스코어드 top-k 주입. R1과 통합 구현 가능.
**출처:** ERL, Anthropic JIT.

### R6 [통찰 · Class B/C] Inner/Outer 이중 루프 — 게이트 다이어트
**갭·통찰:** loop engineering의 dual-loop(inner=실행, outer=진행 감시·전략 리셋). 유저플로우상 인간이 5개 게이트에서 멈추는데, *기계적으로 검증 가능한 게이트*(예: Dev Spec→Build를 guardrail/eval로 판정 가능한 부분)는 자동 검증 게이트로 강등하고, 진짜 판단(Class C·브랜드·스코프)만 사람이 쥔다.
**효과:** 사람 부담(무게) ↓ · 통제 유지 — 무게 감사·유저플로우·루프 엔지니어링을 하나로 잇는 지점.
**주의:** 게이트 강등은 백서 §5 휴먼 게이트 구조 변경이라 Class C 가능성. 신중 검토.
**출처:** loop engineering dual-loop.

## Alternatives Considered

| 대안 | 트레이드오프 |
|---|---|
| **(채택)** 로드맵으로 남기고 항목별 별도 구현 | 가볍고 가역적. 각 항목이 자기 change class·검증을 가짐. 즉시 코어를 안 흔듦. |
| 백서에 SOTA 정합 원칙을 신규 명문화 | 과잉 — 코어는 이미 정합. 단일 리서치 근거로 헌법 팽창(§9 백서 부패 리스크). |
| 아무것도 안 함 (현 상태 유지) | 약점(Reflect/Learn 휴면)이 무게 감사에서 이미 확증됨 — 방치는 자가발전 정지 지속. |
| 발전 지점 전체를 한 번에 구현(빅뱅) | 방법론 자신의 빅뱅 금지 규율 위반. R1~R6은 독립적이라 순차가 맞음. |

## Risks

- **로드맵이 실행 안 되고 아스피레이셔널 문서로 남을 위험** — 무게 감사가 지목한 바로 그 실패 모드. 완화: R1·R2를 다음 회고(70_meta/retrospectives 첫 엔트리)의 명시 추적 항목으로 건다.
- **R1 자동 주입이 컨텍스트를 오염시킬 위험** — 관련성 낮은 Catalog 주입은 context rot. 완화: top-k 소량 + 관련성 임계.
- **R6 게이트 강등이 통제를 약화** — 사람 판단이 필요한 게이트를 잘못 자동화하면 Class C 사고. 완화: Class C 취급, 강등 후보를 명시 목록으로 폐쇄 관리.
- **단일 리서치 스냅샷 기반** — 2026-07 시점 프레임. SOTA는 이동한다. 완화: 분기 회고 시 재평가.

## Rollout

1. 본 RFC 머지(draft→accepted) = 로드맵 백로그 인정. TODO에 R1~R6 항목 등재.
2. **R2(compaction 프로토콜, Class A)** 먼저 — 가장 가볍고 즉시 효용. 신규 지침 또는 guide 03/04 인접 절.
3. **R1(Reflect/Learn 자동화, Class B)** — memory recall ↔ Catalog 연결 프로토타입 → 사람 머지.
4. R3·R4·R5는 R1/R2 검증 후. R6은 별도 RFC(Class C 검토).
5. 각 항목 구현 시 관찰 로그 + 필요 시 ADR. 성과는 70_meta/retrospectives에서 정량 검증(부팅 시간·인계 성공률·반복 마찰 감소).

## Open Questions

- R1의 "관련성"을 무엇으로 계산할지 — 임베딩 유사도 vs signature 매칭 강화 vs LLM 판정. 이식성 제0원칙상 임베딩 의존은 어댑터로 격리 필요.
- thinktank를 되살릴지 vs "수동 승급이 정식"으로 공식화하고 자동화 서사를 접을지 — 무게 감사와 이 RFC가 같은 질문에 수렴. 회고에서 판정.
- R6 게이트 강등이 실제로 무게를 줄이는지는 정량 측정 필요(현재는 가설).

## 참고 자료

- Anthropic — Effective harnesses for long-running agents: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- Anthropic — Effective context engineering for AI agents: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Agentic Loops: From ReAct to Loop Engineering (2026): https://datasciencedojo.com/blog/agentic-loops-explained-from-react-to-loop-engineering-2026-guide/
- Experiential Reflective Learning for Self-Improving LLM Agents (arXiv 2603.24639): https://arxiv.org/abs/2603.24639
- 관련: 무게 감사(휴면 thinktank·ROI 게이트 초과), guide 04 산출물 채널 분리, 백서 §5·§6·§8-5·§9
