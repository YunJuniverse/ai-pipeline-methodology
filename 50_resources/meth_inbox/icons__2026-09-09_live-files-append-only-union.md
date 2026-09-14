---
id: icons__2026-09-09_live-files-append-only-union
origin_repo: icons
type: tool-change
target: "tool/ship"
refs:
  - "https://github.com/icons-hq/icons/pull/907"
  - "https://github.com/icons-hq/icons/pull/896"
  - "/tmp 자동 해소 스크립트 패턴: TODO 합집합·checkpoint 합집합·prompting-report=theirs·wrap-state=ours (세션마다 손으로 재작성)"
friction_ref: null
created: 2026-09-09T02:58:33Z
---

## 제안
라이브 파일 4종(TODO·HANDOFF·checkpoint·관찰로그)에 생성물 2종(prompting-report.md·.ai/wrap-state.json)까지 모든 PR 에 실려, 병렬 세션이 늘수록 PR 마다 같은 줄(Done 맨 위·checkpoint 맨 위·생성물 전체)이 충돌한다. 제안: ① .gitattributes 로 TODO.md·HANDOFF.md·.ai/checkpoint.md 를 merge=union, 생성물 2종은 merge 시 재생성(ours/theirs 무의미) ② Done 삽입·checkpoint 바통을 '맨 위 삽입' 에서 '자기 블록 append + boot 가 날짜 역순 정렬' 로 바꿔 삽입 지점 충돌을 없앰 ③ ship 이 생성물 2종을 별도 커밋(또는 커밋 제외)으로 분리. 충돌 표면을 줄이는 게 land 재시도보다 근본이다.

## 근거
- 2026-09-07~09 13건 PR 중 11건이 살아 있는 파일 충돌로 리베이스 — 내용 충돌은 0건, 전부 같은 삽입 지점·생성물

