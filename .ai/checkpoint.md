# Checkpoint — 2026-07-29 (METH-118 구현 — 프롬프팅 코칭 루프)

> ✅ 구현·테스트 완료 — 사용자 직접 요청분(프롬프팅 자가 교정 리포트). branch `feat/meth-118-prompt-coaching`, PR 대기. 머지 후 sync-all 전파.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-fable-5 · Tool: claude-code-desktop · Host: darwin 25.5.0
- Branch `feat/meth-118-prompt-coaching` (base=main, branch-first)

## 방금 한 것

- **기록층**: `parse_prompting_item`("intent|rounds|모호발췌|교정안|용어콤마|상황태그", 발췌 200자 가드·상황태그 kebab 강제) + observe `--rounds-total`(상시 의무)·`--prompting`(반복 가능) → 프론트매터 `prompting:` 블록 렌더. 빈 세션은 블록 생략(minimal). 품질 경고에 "prompting 미기록" 추가.
- **집계·리포트층**: `parse_prompting_block`(파일→구조)·`collect_prompting_entries`(target 전체)·`build_prompt_report`(순수 함수 — 요지 1줄·세션별 라운드 추이 14일·모호→교정 최근 20·용어 사전 빈도순·상황별 플레이북·토큰 프록시(총/평균 라운드·재지시 3+)·PostHog 확장 포인트 주석). `prompt-report` 명령 + **wrap이 자동 재생성**(무변경 시 스킵, 실패해도 wrap 안 막음). boot [4a-2]가 리포트 "요지" 1줄 표시.
- **판단 시점·스코프 명시**: 리포트 헤더 + 모듈 주석 + CLAUDE/AGENTS wrap 규칙(④에 상시 기록 의무 추가) — 판단은 wrap 시 그 세션 AI, 원문 저장 금지, v1 교차-repo 제외.
- **안전**: ship sensitive 내용 스캔을 관찰로그(.md)까지 확장(발췌에 시크릿 유입 차단).
- 테스트: `tests/test_prompt_coaching.py` 7종(파싱 거부 5케이스·렌더↔파서 왕복·빈 블록 생략·집계 수치·파일 기반 재생성·무변경 스킵). 회귀 총 51종 통과.

## 다음 구체 행동

1. 이 PR(`feat/meth-118-prompt-coaching` → main) 머지 → sync-all 전파(methodology.py·CLAUDE/AGENTS) → METH-118·121 Done(maincheck 후).
2. 전파되면 전 repo 세션이 wrap 때 라운드 수를 상시 기록 — 리포트는 repo별 `50_resources/prompting-report.md`에 자동 축적. 사용자는 boot 헤드라인 또는 파일 직접 열람.
3. 이 wrap의 observe가 **첫 실데이터**(이 세션의 실제 교정 사례 2건) — dogfood로 리포트 생성 확인 예정.
4. 남은 트리아지 산출: 지침 123·124 신설, METH-125~128, RFC-003 관찰, repo 과제(비대 5곳 rotate 등).

## 막힌 것
- 없음.

## 환경
- macOS, python3. 대시보드 http://localhost:8765.
