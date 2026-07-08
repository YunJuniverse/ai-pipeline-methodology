# Checkpoint — 2026-07-08 (METH-061 planning-handoff 모드 코드화)

> ✅ METH-061: 방법론 기본 가정(1인+AI, 산출물=AI 입력)이 "기획 전담자 → 별도 *사람* 개발자"
> 분업에서 깨지는 경우를 코드화. 신규 지침 `20_guides/09_기획_핸드오프_재포맷_규칙.md` +
> `_CATALOG.md` 7번째 모드 `planning-handoff` + 모드 열거 5곳 전파.
> 🏁 다음: PR 리뷰·머지. 이후 guide 09를 다운스트림 sync 대상에 포함. METH-060 잔여(ai-icons 번호 정리 등) 유효.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-061-planning-handoff-mode` (main 직접 PR — 스택 금지)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-061 — planning-handoff 모드 + 재포맷 규칙** (사용자 발의):

- 발단: 사용자가 "개발 전담자가 따로 있어 기획만 전담하고, 산출물을 *사람*이 읽는 포맷으로
  재작동시켜야 할 때 기획서를 어떻게 쓰나"를 질문. 이는 방법론 기본 가정(1인+AI, 산출물=AI 입력)이
  깨지는 경우 → 별도 모드로 코드화.
- 핵심 통찰(전면 재작성 반대): **AI용 명세 = 생성 계약(기계는 질문 안 함 → 빈틈 0),
  사람용 명세 = 소통 계약(사람은 되묻고 판단 → 의도 공유 + 생산적 마찰 설계).**
  재포맷 = 얇은 변환: ① 뼈대(ID·수용기준·권한 매트릭스)는 독자 불문 유지, ② AI 전용 인코딩만
  재포맷(ASCII 와이어프레임→실제 목업, service-policy ON/OFF→must/should, glossary `_Avoid_` 경량화),
  ③ 사람 레이어 추가(의도·읽는 순서·목업·질문 루프·우선순위).
- 변경:
  - `20_guides/09_기획_핸드오프_재포맷_규칙.md` 신설(6절: 왜=계약 전환·대원칙 얇은 변환·5축 표·
    템플릿별 유지/재프레임/매체전환/추가·타 지침 및 agency 모드와의 경계·유래). status:active, foundational.
  - `50_resources/templates/_CATALOG.md`: §1 모드표에 `planning-handoff` 행 + §3 매트릭스에 컬럼 신설
    + `wireframe-spec`에 †각주(재포맷 오버레이 설명).
  - 모드 열거 5곳 전파: `CLAUDE.md`·`AGENTS.md` §1 Mode + `20_guides/00` §11.8(+ planning-handoff 설명 블록)
    + `20_guides/README.md` §3.1(guide 09 등재) + `10_foundation/방법론_백서_가이드.md` 용어표.
  - `ai_observations/` 2곳(2026-06-23·24, 6모드 열거)은 *역사 기록*이라 미변경(메시지 채널 규율).

## 다음 사람에게 (구체적 첫 행동)

1. METH-061 PR 리뷰·머지.
2. **다음 다운스트림 sync 시 guide 09를 전파 대상에 포함**(shared_paths에 자동 편입되는지 확인).
3. METH-060 잔여 유효: **ai-icons 번호 정리(별건 repo 세션)** — 커스텀 `21_산출물채널분리`→상류 `05` dedup +
   레거시 `04`·`05_회의록`을 guide 02 §8 예약범위(90+) 마이그레이션 → sync 재개. cafe24·icons-invest는 dirty 정리 후.

## 미해결 결정사항 (Open Questions)

- **planning-handoff 세트 스코프**(이번에 판단, 사용자 조정 가능): planning ∪ {user-flow·functional-spec·
  wireframe-spec}, architecture·data-model 제외(개발자 소유). 실사용에서 개발자가 data-model까지 원하면 확장 검토.
- guide 09 §4.2 매체 전환(ASCII→Figma)을 CI로 강제할지 — N≥2 재현 시 별도 래칫(현재는 사람·AI 규율).
- RFC-002 R6(휴먼 게이트 다이어트)은 백서 §5 구조 변경이라 Class C 가능 — 별도 RFC.

## 환경 메모

- 브랜치: `claude/meth-061-planning-handoff-mode`. main 직접 PR(스택 금지).
- 변경: `20_guides/09_*.md`(신규) + `_CATALOG.md` + `CLAUDE.md`·`AGENTS.md` + `20_guides/00`·`README.md`
  + `10_foundation/방법론_백서_가이드.md` + 라이브 4종(TODO·HANDOFF·checkpoint·관찰로그).
