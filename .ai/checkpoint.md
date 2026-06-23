# Checkpoint — 2026-06-23 (METH-043 icons-ip 경량 문서 craft 역주입)

> ✅ METH-043: 적용 프로젝트 **icons-ip**(방법론 미적용 lean 코드베이스)의 PRD/ARCHITECTURE/
> ADR 작성 방식에서 *받아들일 만한 순수 doc craft*를 방법론으로 역주입. GitHub-Issues 트래커는
> 방법론 file-based(TODO.md) 설계와 충돌이라 제외(AI/Human 담당축은 이미 METH-040 §19.6).
> ① 신규 템플릿 3종: `prd.md`(무엇·M/S·Pn=출시순서·규제 요구사항 표·현황 갭) · `architecture.md`
>   (어떻게·as-built→목표→이전경로·규제 기술매핑) · `context-glossary.md`(도메인 용어집
>   `_Avoid_`+예시 대화). ② `ADR-template.md` 강화(제목=결정문장·Considered Options·되돌리기 비용).
> ③ `requirements-spec.md` M/S+Pn 보강 · 지침 00 §11.5~11.7(경량 모드·문서 충돌 surfacing·작업유형
>   라우팅). Class A. **별도 PR**(main 기준 브랜치, PR #31과 craft 파일 비충돌).

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/inject-lean-doc-craft-from-icons-ip` (main 기준, head `2c6e60c`)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-043 icons-ip 경량 문서 craft 역주입** (사용자: "여기서 PRD 등 작성 방식 중
이 경량 방법론에서 받아들일 만한 내용이 있어?" → "니 추천대로 진행"):

- 분석: `/Users/hayden/icons-ip`(방법론 미적용, Next.js 16+Supabase lean 코드베이스)의
  CLAUDE.md(`@AGENTS.md` 포인터)·AGENTS.md·CONTEXT.md·docs/{PRD,ARCHITECTURE,adr,agents} 정독.
  GitHub Issues+Project+AGENTS.md+mattpocock/skills 기반 *Next-Gen lean 파이프라인*.
- 판단: 순수 doc craft(전이 가능) vs 운영모델 차이(린 vs 헤비, 의도적) 구분. 채택 7종:
  PRD↔ARCHITECTURE 짝 문서 / 규제 2-table / as-built→목표→이전경로 / ADR 강화 /
  CONTEXT `_Avoid_`+예시대화 / M/S+Pn 태깅 / 문서 충돌 surfacing+라우팅. **제외**: GitHub-Issues
  트래커(방법론 file-based 설계 충돌).
- 작성: 신규 `prd.md`·`architecture.md`·`context-glossary.md`, `ADR-template.md` 재작성,
  `requirements-spec.md` §⑤ 보강, 지침 00 §11.5~11.7 신설.
- 검증 예정: wrap 4/4 → ship → PR. 도메인 특화(가챠/굿즈/카드) 전부 제외, 일반 craft만.

## ⚠️ 다음 사람: 우선 처리 후보 (병렬 PR 2개 주의)

- **METH-043 PR** (이 브랜치) + **PR #31**(METH-040/041/042, 브랜치 `…from-gamblescan`)이
  *병렬*로 떠 있다. craft 파일은 서로 비충돌(METH-043=신규 prd/arch/context-glossary+ADR/
  requirements/지침00 / PR #31=지침 10~18 §19+기획·개발명세 템플릿). 단 **라이브 파일
  (HANDOFF/TODO/checkpoint)은 두 브랜치가 각각 수정** → *둘째로 머지되는 PR*에서 라이브 파일
  합류(rebase) 필요. 권장: PR #31 먼저 머지 → METH-043 rebase(라이브 파일만 수동 합류).
- 머지 후 **다운스트림 sync**: METH-039~043 합산하여 icons·ai-icons·gamblescan `sync --apply`.
  cafe24 경로 미확인(`/Users/hayden/cafe24` repo 부재 — 사용자 확인).
- **METH-044 (백로그 등록, 머지 후 capstone)**: 모드별 템플릿 선택 체계(`_CATALOG.md` + CLAUDE.md
  Mode 확장 `[planning/dev/fullstack/agency/lean/ops]`). 설계 확정본은 TODO.md Backlog 참조.
  #31/#32 머지 후 clean main에서 착수(25종 전체 참조 필요). 사용자 승인 완료(타이밍="머지 후").

## 다음 사람에게 (구체적 첫 행동)

1. 사용자 지시 대기. 신규 작업 시작 금지.
2. PR #31 / METH-043 PR 머지 순서·라이브 파일 합류는 위 "우선 처리 후보" 참조.

## 막혔던 지점 / 시도해봤지만 안 된 것

- 없음. icons-ip office 변환 불필요(전부 md). 병렬 PR 라이브 파일 충돌은 *예견된* 것이라
  HANDOFF/TODO/본 checkpoint에 합류 필요를 명시해 둠.

## 미해결 결정사항 (Open Questions)

- 경량 문서 모드(PRD/ARCHITECTURE/CONTEXT)를 *언제* 풀 기획서군 대신 쓸지의 판단 기준은
  지침 00 §11.5에 "프로젝트 성격"으로만 둠 — 더 구체적 게이트가 필요하면 후속 ADR.
- icons-ip의 `ready-for-agent`/`ready-for-human` 라벨은 METH-040 담당축(AI/Human)과 중복이라
  미채택 — 향후 TODO 라벨 통합 시 재검토 여지.

## 환경 메모

- 브랜치: `claude/inject-lean-doc-craft-from-icons-ip` (main `2c6e60c` 기준).
- 변경: 신규 `50_resources/templates/{prd,architecture,context-glossary}.md`,
  `ADR-template.md`·`requirements-spec.md` 편집, `20_guides/00_*.md` §11.5~11.7, 라이브 4종.
- 출처 프로젝트: icons-ip `/Users/hayden/icons-ip` (ICONS 기획 → icons-ip PRD 단방향, ADR-0013).
