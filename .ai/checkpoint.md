# Checkpoint — 2026-07-08 (METH-053 guide 04→05 리넘버 + RFC-002 복구)

> ✅ METH-053: ① 상류 산출물 채널 분리 지침 `04`→`05` 리넘버(ai-icons·icons-invest 커스텀 04 doc_id
> 충돌 회피) + guide 02 §8 지침번호 예약(상류 00–89 / 다운스트림 90–99). ② **RFC-002 복구** —
> METH-052(#42)가 스택 PR 함정으로 main 미도달·고아화되어 파일 복원, main 직접 PR로 재포함.
> ⚠️ 교훈: 스택 PR은 base PR 먼저 머지 시 stale 브랜치로 머지돼 고아화 — 앞으로 main 직접 PR 순차 진행.
> 다음: `70_meta/retrospectives` 첫 회고(무게 감사 HIGH + 이 두 교훈 정식화).

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-053-guide-renumber` (main 직접 PR — 스택 금지)

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

1. METH-053 PR(main 직접) 리뷰·머지 — guide 04→05 리넘버 + guide 02 §8 + RFC-002 복구.
2. 머지 후 `70_meta/retrospectives` 첫 회고 작성(무게 감사 HIGH + 스택-머지 고아 교훈 + guide-04 충돌 교훈 정식화).
3. 회고에서 RFC-002 draft→accepted 판정 → R2(compaction, Class A)부터. guide 05 다운스트림 sync(충돌 해소됨).

## 미해결 결정사항 (Open Questions)

- RFC-002 R6(휴먼 게이트 다이어트)은 백서 §5 구조 변경이라 Class C 가능 — 별도 RFC 검토.
- thinktank를 되살릴지 vs "수동 승급이 정식"으로 공식화할지 — 무게 감사와 RFC-002가 같은 질문에 수렴, 회고에서 판정.
- guide 04 §7 강제 래칫 실제 CI 구현 시점 — RFC-002 R1/R2와 함께.

## 환경 메모

- 브랜치: `claude/meth-051-output-channel-separation`(PR1). PR2는 이 브랜치 위에 스택.
- PR1 변경: `20_guides/04_*.md`(신규) + `CLAUDE.md`·`AGENTS.md`(File Roles 행) + `20_guides/README.md` + 라이브 4종.
- PR2 변경: `70_meta/rfc/RFC-002_*.md`(신규) + 라이브 4종(증분).
