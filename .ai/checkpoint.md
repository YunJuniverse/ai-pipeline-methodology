# Checkpoint — 2026-06-23 (METH-039 기획 craft 역주입: ICONS 학습 → 방법론, PR #30 머지 완료)

> ✅ METH-039: 적용 프로젝트 ICONS의 기획 학습 코퍼스(사업/서비스기획 강의·실무·케이스)를
> 정제한 `icons:40_dev/knowledge/` 6종을 방법론 업스트림으로 **역환류**.
> ① `20_guides` 지침 4종에 §19 "실무 craft 부록(현장 패턴·적용 프로젝트 환류)" 추가 —
>   10_사업기획서(핵심가치 도출·검증 우선순위 게이트·KPI 단위경제 트리·분석틀·보고서 worked-example),
>   11_서비스기획서(ASIS→TOBE·12단계 산출물 체계·데이터 무결성·정책 ON/OFF·스토리보드 8요소·Admin),
>   13_마케팅기획서(Triple Media·4유발 퍼널·채널별·E.C.C.S),
>   15_프로젝트_관리(WBS·Kick-off·제안 5단계).
> ② `50_resources/templates/` 기획 양식 6종 신설(requirements-spec·ia-spec·service-policy·
>   user-story·kpi-tree·wbs).
> 모두 일반 craft만(프로젝트 특화 제외)+출처 명시. shared 자산이라 본 upstream 이 정본 →
> 다운스트림(icons·ai-icons·gamblescan)은 `sync --apply` 로 수령. Class A.
> **PR #30 머지 완료**(2026-06-23 05:25 UTC, main `2c6e60c`, `origin/main` 동기).
> **잔여**: 다운스트림 `sync --apply` 전파(아직 미수행).

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: main checkout (branch `main`, head `2c6e60c`)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**라이브 파일 정리 (사용자: "라이브 파일 정리만")**:

- 부팅 점검에서 발견: METH-039 PR #30 은 **이미 머지**(2026-06-23 05:25 UTC,
  main `2c6e60c`, `origin/main` 0/0 동기, 워킹트리 clean) 됐는데, 라이브
  파일들이 머지 *이전* 시점에 쓰여 어긋나 있었음 —
  - HANDOFF "Working on: … PR 대기"
  - checkpoint 헤더 "잔여(Human): PR 생성·대표 머지"
  - checkpoint 본문 "방금 한 것"이 아직 METH-038 내용(헤더만 039)
- 조치(라이브 파일만 갱신, 신규 작업 미착수):
  - `HANDOFF.md` — Working on=없음(METH-039 머지 완료)/Next TODO=다운스트림
    sync 잔여+S-021 후보/Recent Changes 최상단 "PR #30 머지 완료"로 갱신.
  - `TODO.md` — METH-039 Done 항목 말미 "PR(대표 머지=승인 증빙)" →
    "PR #30 머지 완료(…) + 잔여 다운스트림 sync" 로 정정.
  - 본 `checkpoint.md` — 헤더 잔여 라인 정정 + 본문 전체를 현재 현실로 재작성.
  - observation 로그 1건(docs).
- 검증 근거: `gh pr view 30` → `MERGED`, `git rev-list --left-right --count
  main...origin/main` → `0 0`. 다운스트림 미전파 확인:
  `icons:50_resources/templates/` 에 METH-039 템플릿 6종 부재.

## ⚠️ 다음 사람: 우선 처리 후보

- **METH-039 다운스트림 `sync --apply` 전파 (잔여, 미수행)** — 업스트림
  정본 `/Users/hayden/methodology` 기준 dry-run → `--apply`:
  - `icons`(✅ 존재, 템플릿 6종 **미수령** 확인), `ai-icons`(✅ 존재, 미확인),
    `gamblescan`(✅ 존재, 미확인).
  - `cafe24` 는 `/Users/hayden/cafe24` 에 repo 없음 — **경로/대상 여부 사용자
    확인 필요** (이전 기록은 icons·ai-icons·cafe24·gamblescan 4개를 후보로 명시).
  - 전파 시 규칙: `--dry-run` 선검토 → 명시 경로 add(MC-001, `-A` 금지) →
    원격 선행분과 무겹침 확인 후 rebase(force push 금지) → 픽스 검증.

## 다음 사람에게 (구체적 첫 행동)

> 이번 세션은 **라이브 파일 정리만** 수행(METH-039 머지 완료 반영). 코드/방법론
> 자산 변경 없음. 활성 백로그 비움.

1. **다음 작업 지시 대기** — 사용자 지시 없으면 신규 작업 시작 금지.
2. 사용자가 "전파 진행" 지시 시 → 위 "다음 사람: 우선 처리 후보"의 다운스트림
   sync 수행 (cafe24 경로부터 확인).
3. 유력 신규 후보: **S-021 코드 sprint** (ship build 검증·hook 안전망 선결조건
   해소 완료 상태).

## 막혔던 지점 / 시도해봤지만 안 된 것

- 없음. 부팅 점검 → 라이브 파일 3종 + observe 갱신만. 부트 시 dashboard CLI
  정상 호출(http://localhost:8767, branch main, commit `2c6e60c`).

## 미해결 결정사항 (Open Questions)

- METH-039 다운스트림 대상에 `cafe24` 포함 여부 — `/Users/hayden/cafe24` repo
  부재. 경로가 다른지, 대상에서 제외인지 사용자 확인 필요.
- S-021 코드 sprint 진입 시 ship 의 test 단계 실측(현재 build 만 talmocom 으로
  간접 확인) — 코드 sprint 첫 ship 에서 자연 검증 예정.

## 환경 메모

- 본 작업 worktree: main checkout (branch `main`, head `2c6e60c`).
- 변경 파일: `HANDOFF.md`, `TODO.md`, `.ai/checkpoint.md`, 신규 observation 로그 1건.
  (코드·지침·템플릿 등 방법론 자산 변경 없음 — 라이브 파일 정리 한정.)
- 업스트림 정본: `/Users/hayden/methodology`. 다운스트림: icons·ai-icons·gamblescan
  (각 `/Users/hayden/<name>`), cafe24 경로 미확인.
