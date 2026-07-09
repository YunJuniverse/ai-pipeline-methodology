# Checkpoint — 2026-07-09 (METH-081 prompts/ 층 전면 현행화)

> ✅ METH-081: 사용자 질문(운영원칙 지침00·prompts 역할)에서 **프롬프트층이 나머지 방법론과 심하게 drift** 발견(라우터 079 문제와 동종) → 전면 현행화.
> 핵심: 입력 `briefs/`→`00_briefs/current/`, 산출 `snapshots/plans/vN`→`30_planning/` 라이브, "항상 6종"→모드 선택, **목차 복제 제거**(구조 SSOT=지침, 080과 동형 교정). +ai-feature(16)·eval-guardrail(17) 신설 + `_README.md` 신설.
> 🏁 다음: PR 리뷰·머지 → 남은 후보(agency/ops 템플릿·메타 지침) 또는 **누적 다운스트림 sync(073~081)**.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-081-prompts-modernization` (#69 머지된 main tip 기준, branch-first 준수)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-081 — `50_resources/prompts/` 층 전면 현행화** (사용자 질문 "운영원칙·prompts 역할이 뭐냐"에서 파생):

- **역할 정리(질문 답)**: 방법론 3층 = **지침**(20_guides, 표준·목차) → **템플릿**(50_resources/templates, 빈 양식) → **프롬프트**(50_resources/prompts, 복붙 실행 지시). 운영원칙(지침00)은 그 위 최상위 헌법(문서 위계·SSOT·Eval-First·금지패턴·품질).
- **발견한 drift**: 프롬프트가 구모델 고착 — 입력 `briefs/`(존재 안 함, 실제 `00_briefs/current/`), 산출 `40_dev/snapshots/plans/xxx/vN`(존재 안 함, 실제 `30_planning/NN_*.md` 라이브), "항상 6종 전체"(모드 선택 로딩과 충돌), 심화분(12~17)·모드·개발명세 미반영, _README 부재.
- **고친 것 (17 파일)**:
  - 기획서 프롬프트 6종 재작성(business/service/ops/marketing/brand/pm) → `30_planning/` 라이브 산출 + 심화 포인트 반영 + **목차 복제 제거**(지침이 구조 SSOT).
  - **신설 2종**: `ai-feature.md`(16)·`eval-guardrail.md`(17) — 기획서 8종 전체 커버(기존 6종만 있었음).
  - 코드-역문서화 4종(architecture/data-model/api-spec/service-spec) → "전방 설계=템플릿 vs 역문서화=프롬프트" 역할 명확화, 스냅샷 경로 유지.
  - `dev-spec.md` 현행화(지침21·개발명세 5종·planning-handoff 분기), `plan-routing`/`re-plan`/`plan` 현행화.
  - **`_README.md` 신설**: 프롬프트↔지침↔템플릿↔모드 매핑표(_CATALOG 대응).
  - 상위 문서 정정: `README.md`·`50_resources/_README.md`의 "스냅샷 생성 프롬프트"→"AI 실행 프롬프트".
- **sync**: `50_resources/prompts`가 통째로 shared_path → 신규 파일 포함 자동 전파(별도 등록 불필요).

## 다음 사람에게 (구체적 첫 행동)

1. METH-081 PR 리뷰·머지.
2. **심화 프로그램 현황**: 템플릿 13종(063~071)·기획서 지침군 6종(073~078)·오케스트레이션(079)·마스터플랜 SSOT(080)·prompts 층(081). 남은 후보 — agency/ops 템플릿(proposal-go-nogo·qa-*·operation-spec·profitability-sheet·execution-plan·work-request-ticket·wbs·glossary), 메타/dev 지침(00·02~09·19~20). ※ 지침00(운영원칙)도 후보 — 이번에 읽어보니 573줄 성숙하나 심화분(12~17) 신규 영역 반영은 점검 여지.
3. **누적 다운스트림 sync(2차)** — gamblescan·icons 072까지 반영 → **073~081 추가 필요**. 홀드 3곳(ai-icons·cafe24·icons-invest) clean 후.
4. **graph.json 노드 완성**(별건) — guide 02~09·19~21.

## 미해결 결정사항 (Open Questions)

- 심화 프로그램을 여기서 일단락할지 vs agency/ops·메타 지침(특히 운영원칙00)까지 이어갈지 — 사용자 판단.
- 2차 다운스트림 sync 타이밍(073~081 누적).

## 환경 메모

- 브랜치: `claude/meth-081-prompts-modernization` (#69 머지된 main tip 기준). branch-first 준수.
- 변경: `50_resources/prompts/` 17개(수정 14 + 신설 3: _README·ai-feature·eval-guardrail) + `README.md` + `50_resources/_README.md` + 라이브 4종.
- 진척: 063~071 템플릿 + 072 sync(#61) + 073~078 지침군(#62~#67) + 079 오케(#68) + 080 마스터플랜(#69) + **081 prompts(이번)**.
