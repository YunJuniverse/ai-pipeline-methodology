# Checkpoint — 2026-07-08 (METH-062 API 계약 템플릿 + 개발명세 작성 지침)

> ✅ METH-062: "개발기획서 필요?" 질문 → **단일 개발기획서=반대**(재번들=단일출처 위반).
> 대신 진짜 공백 2개: ① 신규 템플릿 `api-contract.md`(FE/BE 병렬 조율축) ② 신규 지침 21(개발명세 6종 조합·읽는 순서).
> METH-061(09 핸드오프 재포맷, **PR #51 머지 완료**)의 짝 — 09=누가 읽나, 21=무엇을 어떻게 조합하나.
> ⚠️ 062는 원래 #51 브랜치에 얹었으나 푸시-머지 타이밍이 어긋나 #51엔 061만 머지됨 → 062 커밋 `169a3c2`를
> main 기준 새 브랜치로 cherry-pick 복구 → 별도 PR로 진행(작업 손실 0).
> 🏁 다음: 062 PR 리뷰·머지. 이후 09·21·api-contract를 다운스트림 sync에 포함. METH-060 잔여(ai-icons 번호 정리) 유효.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-062-api-contract-devspec` (main 기준, 062 복구 — main 직접 PR)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**한 세션에 짝지어진 두 작업 — METH-061(핸드오프 재포맷) + METH-062(개발명세/API 계약).** 둘 다 "기획→개발 인계" 테마. 061은 **PR #51로 머지 완료**. 062는 처음에 #51 브랜치에 얹었으나(커밋 `169a3c2`) 푸시-머지 타이밍이 어긋나 #51엔 061 커밋만 담겨 머지됨 → 062를 **main 기준 새 브랜치로 cherry-pick 복구**해 별도 PR로 올린다(작업 손실 0, 커밋 온전 보존).

**METH-062 — API 계약 템플릿 + 개발명세 작성 지침** (사용자 질문 "개발기획서 필요?"):
- **판단: 단일 개발기획서=반대.** architecture+wbs+master_plan+adr의 재번들이라 단일출처·중복금지(File Roles) 위반.
  그 질문이 드러낸 *진짜 공백 2개*를 대신 채움:
  - ① 신규 `50_resources/templates/api-contract.md` — 엔드포인트·요청/응답·에러포맷(`code`로 분기)·상태코드
    규약·버전정책·공유스키마(data-model 링크·중복금지)·Open 계약질문(§5). **개발리드→개발자 FE/BE 병렬 조율축**,
    functional-spec(기능단위)의 상위 시스템 레벨. `_CATALOG` dev/fullstack/agency 세트+매트릭스 편입.
  - ② 신규 `20_guides/21_개발명세_작성_지침.md` — 개발명세 6종 원본경계·개발자용 "여기서 시작" 읽는 순서
    (무엇→접근→데이터→계약→기능규칙→화면→누가언제)·dev-spec-review 게이트·재번들 금지·09/18/19 경계. README §3.5.
  - 방법론 기획-헤비(10~17)/개발명세-라이트 보정. 09=누가 읽나, 21=무엇을 어떻게 조합하나.

**METH-061 — planning-handoff 모드 + 재포맷 규칙** (선행, 사용자 발의):
- 핵심 통찰: **AI용 명세=생성 계약(빈틈0) / 사람용 명세=소통 계약(의도공유+생산적 마찰).** 재포맷=얇은 변환
  (뼈대 유지 + AI 전용 인코딩만 재포맷 + 사람 레이어 추가). 신규 지침 09 + `_CATALOG` 7번째 모드 `planning-handoff`
  + 모드 열거 5곳 전파(CLAUDE·AGENTS·guide00·README·백서가이드). ai_observations 2곳은 역사기록이라 미변경.

## 다음 사람에게 (구체적 첫 행동)

1. PR #51 리뷰·머지 (METH-061 + 062 통합).
2. **다음 다운스트림 sync 시 guide 09·21 + `api-contract.md`를 전파 대상에 포함**(shared_paths 편입 확인).
3. METH-060 잔여 유효: **ai-icons 번호 정리(별건 repo 세션)** — 커스텀 `21_산출물채널분리`→상류 `05` dedup +
   레거시 `04`·`05_회의록`을 guide 02 §8 예약범위(90+) 마이그레이션 → sync 재개. cafe24·icons-invest는 dirty 정리 후.

## 미해결 결정사항 (Open Questions)

- **planning-handoff 세트 스코프**(사용자 확정): planning ∪ {user-flow·functional-spec·wireframe-spec}, architecture·
  data-model·api-contract 제외(개발자 소유). 실사용에서 개발자가 data-model까지 원하면 확장 검토.
- api-contract의 OpenAPI 기계판독 강제(스펙-문서 일치 CI)·guide 09 §4.2 매체전환(ASCII→Figma) 강제 — N≥2 재현 시 래칫.
- RFC-002 R6(휴먼 게이트 다이어트)은 백서 §5 구조 변경이라 Class C 가능 — 별도 RFC.

## 환경 메모

- 061 = **PR #51 머지 완료**(main = merge `58a2aac`): `20_guides/09_*.md`(신규) + `_CATALOG.md`(모드) + `CLAUDE.md`·`AGENTS.md` + `20_guides/00`·`README.md` §3.1 + `10_foundation/방법론_백서_가이드.md`.
- 062 = **새 브랜치 `claude/meth-062-api-contract-devspec`**(main 기준 cherry-pick `169a3c2` → `f284633`): `50_resources/templates/api-contract.md`(신규) + `20_guides/21_*.md`(신규) + `_CATALOG.md`(dev세트·§2·매트릭스) + `20_guides/README.md` §3.5 + 라이브 4종.
- 정리 예정: 구 브랜치 `claude/meth-061-planning-handoff-mode`(169a3c2 보유)는 062 머지 후 삭제.
