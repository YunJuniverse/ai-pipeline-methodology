# Checkpoint — 2026-07-08 (METH-056 Compaction 프로토콜 구현 — RFC-002 R2)

> ✅ METH-056: RFC-002 로드맵의 **첫 실제 구현** — 진단·문서화를 넘어 약점(런타임 compaction 규율)을 고침.
> `20_guides/06_컨텍스트_컴팩션_프로토콜.md` 신설: compaction 경계 보존/폐기 규칙 + checkpoint를 세션 종료뿐
> 아니라 **compaction 경계·긴 세션 자연 경계**에서도 갱신(=세션 중간 인계) + pre-compaction 체크리스트.
> CLAUDE/AGENTS 세션 절차에 "컴팩션 경계 트리거" 편입(로드·준수 강제). README 06 + RFC-002 R2 ✅구현 표시.
> ⏭ 다음: guide 06 sync · P1(R1 Reflect/Learn 자동화, b 공식화 권장) · P3(온보딩 다이어트).
> (이 세션 main 반영: #41 guide 05 · #43 리넘버+RFC-002복구 · #44 회고 · #45 RFC-002 accepted.)

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-056-compaction-protocol` (main 직접 PR — 스택 금지)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-051 — 산출물 채널 분리 지침 04** (에이전트 토론 2회 + 사용자 스코프 확정):

- 발단: ai-icons 메모리 `audience_facing_docs_no_workflow_artifacts.md`(반복 피드백 3회 + "여러 번 말했다")를
  상류 방법론으로 격상할지 사용자가 질문 → 에이전트 토론(입론 찬성/반대/방법론적합성 → 교차 반론 → 심판).
- 토론 결론: **ELEVATE_WITH_CONDITIONS** — 백서 §2 신규 원칙(헌법) 직행은 단일 도메인 N≥2라 부당(§9·§12 위반),
  C-001 선례(단일 프로젝트→active)대로 **전-도메인 지침**이 정확한 고도. "절대"는 "라우팅+예외군"으로 완화.
- 사용자 스코프 확정(2축): ① 청중 축 = "맥락 없는 외부 사람에게 공유되는가"로 트리거 —
  **기획서(30_planning)·서비스페이지·앱UI·브랜드카피 = 포함 / 그 기획서를 만드는 메타문서 = 면제.**
  ② 주제 축 = 산출물이 그 메타에 *관한* 것이면 예외(changelog·릴리스노트·API 문서·ADR·README 버전배지).
- 변경(PR1):
  - `20_guides/04_산출물_채널_분리_규칙.md` 신설(9절: 왜=백서 종속·두 채널 정의·트리거·판정 2축·배제 3종+예외군·
    메타 라우팅·§7 강제 스펙·타 지침 경계·격상 이력). status:active, ai_relevance:foundational.
  - `CLAUDE.md`·`AGENTS.md` File Roles 표에 "Output channel" 행 신설(기존 6행은 메시지 채널만 규율하던 빈칸).
  - `20_guides/README.md` 메타밴드 카탈로그에 02·03·04 등재.
- 백서 미수정 — 제0·제2·§8-4·§8-5를 WHY로 인용만. §7 grep 래칫은 스펙만(fail-open 금지라 반쪽 가드 안 만듦).

## 같은 세션의 후속 (METH-052 = 스택 PR 2/2)

- **방법론 무게 감사**(에이전트 16개): MIXED — 코어는 정당, 군살은 국소(온보딩 밴드 중복·휴면 thinktank·
  ~9주 초과 ROI 게이트). "방법론_백서_가이드"·70_meta·30_planning stub·AGENTS 미러·템플릿 32는 load-bearing 방어.
- **SOTA 평가**(웹 리서치): 코어가 harness/context/loop engineering·ERL과 정합/선행. 약점=Reflect/Learn 자동화 +
  compaction·budget 규율(휴면 thinktank와 동일 지점).
- **`70_meta/rfc/RFC-002_sota-alignment-develop-roadmap.md`** 신설(draft) — R1~R6 발전 로드맵.

## 다음 사람에게 (구체적 첫 행동)

1. METH-056 PR(compaction 프로토콜) 리뷰·머지 → guide 06 다운스트림 sync(20_guides shared).
2. **P1 (RFC-002 R1) 지표 인프라 + thinktank 존폐** 결정·구현 — b(수동 승급 공식화 + 지표 로깅) 권장. 회고가 최우선으로 꼽은 항목.
3. P3 온보딩 밴드 다이어트(무게 감사 MED: HOW_TO_APPLY §6 → CLAUDE 링크 축약).

## 미해결 결정사항 (Open Questions)

- RFC-002 R6(휴먼 게이트 다이어트)은 백서 §5 구조 변경이라 Class C 가능 — 별도 RFC 검토.
- thinktank를 되살릴지 vs "수동 승급이 정식"으로 공식화할지 — 무게 감사와 RFC-002가 같은 질문에 수렴, 회고에서 판정.
- guide 04 §7 강제 래칫 실제 CI 구현 시점 — RFC-002 R1/R2와 함께.

## 환경 메모

- 브랜치: `claude/meth-051-output-channel-separation`(PR1). PR2는 이 브랜치 위에 스택.
- PR1 변경: `20_guides/04_*.md`(신규) + `CLAUDE.md`·`AGENTS.md`(File Roles 행) + `20_guides/README.md` + 라이브 4종.
- PR2 변경: `70_meta/rfc/RFC-002_*.md`(신규) + 라이브 4종(증분).
