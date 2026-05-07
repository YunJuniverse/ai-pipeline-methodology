# Claude Code Adapter

> Claude Code CLI에서 본 방법론을 사용할 때의 보조 지침.

## 자동 로드되는 것

Claude Code는 세션 시작 시 다음을 자동 컨텍스트에 포함:

- 루트 `CLAUDE.md` — *AI 운영 규칙*
- `.claude/settings.json` (있으면)

본 방법론은 위에 더해 **명시적**으로 다음을 요청:

- `.ai/context.json` — 부팅 컨텍스트
- `must_read` 배열의 파일들

## 첫 메시지 권장 형식

새 세션을 열 때 사용자가 다음 한 줄을 보내면 충분:

```
.ai/context.json을 읽고, must_read 배열의 파일들을 순서대로 읽어 부팅해줘. 그 다음 .ai/checkpoint.md의 "다음 사람에게" 첫 항목부터 시작.
```

## 세션 종료 자동화 (현재: 수동, 향후: hook)

**현재**: 세션 종료 직전에 사용자가 다음을 요청:

```
.ai/checkpoint.md를 이 세션 작업 내용으로 갱신해줘.
형식: 현재 .ai/checkpoint.md의 필수 섹션.
규칙: 과장·칭찬·추측 금지, 다음 AI가 이어받는 데 필요한 사실과 첫 행동만.
```

**향후 (TODO)**: `.claude/settings.json`의 `hooks.SessionEnd`에 checkpoint 자동 갱신 명령을 등록.
구현 시 `00_foundation/WHITEPAPER.md` §리스크 1(L1 자동기록 누락) 완화로 이어짐.

## 도구 매핑

| 본 방법론 동작 | Claude Code 구현 |
|---|---|
| 백서 검색 | `Read 00_foundation/WHITEPAPER.md` |
| 폴더 컨벤션 확인 | 백서 §부록 C 참조 |
| 대시보드 빌드·서빙 | `Bash python3 50_tools/generate-dashboard.py --serve` |
| 부팅·환경 검증 | `Bash python3 50_tools/methodology.py version` |
| 새 프로젝트에 적용 | `Bash python3 50_tools/methodology.py init <path>` |
| 기존 적용 프로젝트 갱신 | `Bash python3 50_tools/methodology.py sync --apply` |
| 폴더 단위 탐색 | `Glob "10_guides/*.md"` 등 |

## 주의

- worktree 환경에서 작업 중일 수 있음. `pwd`와 `git branch --show-current`로 항상 확인.
- Claude Code 자동 로드 컨텍스트가 본 방법론의 운영 규칙(`CLAUDE.md`)과 충돌 시, **`CLAUDE.md`가 이김** — 백서 §8-1 우선순위.
