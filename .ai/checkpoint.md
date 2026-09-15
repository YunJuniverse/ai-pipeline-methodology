# 세션 체크포인트

> 세션 서사 바통. 누적 상태는 `HANDOFF.md`.

## 방금 한 것 (2026-09-15 · METH-147 PR 1 도구 묶음)

사용자가 판단 3지점을 전부 권고안대로 확정했다. 도구 묶음을 먼저 넣었다.

- **wrap baseline = HEAD 재계산** — `head_wrap_state()` 가 HEAD 블롭 sha 로 baseline 을 만든다. ship 은 `commit_wrap_state` 를 더 이상 부르지 않고, 생성물 2종(`.ai/wrap-state.json`·`50_resources/prompting-report.md`)을 `git rm --cached` + `.gitignore` 블록으로 커밋에서 뺀다(파일은 남는다). 실 repo 에서 동치 확인(라이브 파일 미편집 → 4/4 미갱신, wrap-state 무접촉).
- **ship 공유 체크아웃 가드** — 워크트리 ≥2 이고 현재가 주 체크아웃이면 커밋 후보를 열거하고 `--allow-shared` 없이는 거부. 격리 워크트리 안에서는 안 걸린다.
- **`reserve`** — `id/METH-N` 원격 태그로 원자 예약. e2e: METH-4 → 5 → (6 선점) → 7.
- **land** — DIRTY 면 origin/base 머지·재푸시 1회 후 CI 재실행 대기 / 실패 체크가 전부 «스텝 0개»면 내용 오류가 아니라 경합·CI 부재로 분류(billing annotation 판독) / `--local-ci` 는 TODO Blocked 의 PM 판정 + 로컬 재현(manifest·wrap read-only·observe validate 전수·tests) 통과 시에만.
- observe `parse_friction_item` rsplit(세로줄 허용) · boot `required_local_files` preflight · wrap ADR 인용 검사(warn).
- `.gitattributes`(TODO·HANDOFF union) 를 shared_paths 에 추가.
- 테스트 9건 신설, 전체 96/96. `ship --land` 의 Namespace 에 `local_ci` 누락을 발견해 고쳤다(AttributeError 였을 것).

**이 ship 자체가 상류 이행이다** — 이 커밋에서 wrap-state·prompting-report 가 인덱스에서 빠지고 `.gitignore` 블록이 들어간다.

## 다음 구체 행동

1. land → **PR 2**: 지침 05 §9 확장·§9b 8·9항 / 19 §8b.4 / 23 §1-4·§1-5 1줄·§2 애니메이션·§2-6 부재 관측조건 / 24 §2b 제보 트리아지·§4 벤더 JS·§4b 보강 / **30 v3**(§6 리베이스 라이브 파일·§7 ID 예약·§8 생성물·union) / CLAUDE.md·AGENTS.md Blocked dedupe 1줄 / README 현황표 / C-002 승급(P-004 → active) / P-006·007·008.
2. **PR 3**: `_inbox` 23건 정리(원장 68 유지) → 전파 11 repo(`methodology.py`·`.gitattributes`·지침) → 훅 3 repo 재설치 → 다운스트림에서 생성물 2종이 다음 ship 에 인덱스에서 빠지는지 1곳 확인.
3. 주의: 전파 후 다운스트림 첫 ship 이 `.gitignore` 를 바꾸고 생성물을 빼는 커밋을 만든다 — 정상.

## 막힌 것

- 없음.

## 환경

- repo: `/Users/hayden/methodology` · branch `feat/meth-147-tools`
