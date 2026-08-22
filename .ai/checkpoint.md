# Checkpoint — 2026-08-22 (METH-116 정련 브랜치 main 리베이스 — 지침 22 v2·v3 병합 승계)

> ✅ `docs/guide-22-ir-deck-methodology`(정련 커밋 1개)를 61커밋 앞선 main 위로 리베이스. 충돌 5파일 해소 — 지침 22 는 v2·v3 내용을 **승계 통합**, 라이브 상태 파일은 최신(main) 채택.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-opus-5 · Tool: claude-code-desktop · Host: darwin 25.5.0
- Branch `docs/guide-22-ir-deck-methodology` (base=main, 리베이스 후 main+1) — 신설분 PR #112 는 이미 land

## 방금 한 것

- **리베이스 배경 확인**: 이 브랜치의 *신설분*은 PR #112 로 이미 머지(`285041e`)됐고, 그 뒤 main 에서 지침 22 가 **v2(METH-128)·v3(METH-129)** 로 두 번 더 진화. 남은 정련 커밋은 v1 기준 §2 전면 재작성이라 정면 충돌 — 기계적 해소 불가 판정.
- **충돌 5파일 해소**:
  - `20_guides/22_IR_...지침.md` — 정련의 **2트랙·6단계(P0~P5)** 모델 채택 + 그대로 두면 유실될 **v2 불변규율 4(파일=유일 소스)·5(안정 슬라이드 ID) 승계**(규율 6개로 통합), v2 **P3 리드백 게이트를 신 P4 행으로 이관**, 변경이력 v1~v3 보존 + **v4(2026-08-22) 추가**.
  - `TODO.md` — main 의 METH-137 Done 유지 + METH-116 **정련** 항목 별도 추가(신설분 land 기록 명시).
  - `HANDOFF.md` — Recent Changes 는 main 최신 5건 유지 + 정련 1줄 추가, Working on 갱신.
  - `.ai/checkpoint.md`·`.ai/wrap-state.json` — **최신(main) 채택**. 세션 스냅샷/생성물이라 07-25 서사로 되감지 않음.
- **검증**: source CI 동등 체크 로컬 통과 — `manifest-check` ✓ · observation lint 전건 ✓ · `generate-dashboard.py` ✓(kanban 7 cards).
- 백업 ref `backup/pre-rebase-guide22`(= 리베이스 전 `5153171`) 보존.

## 다음 구체 행동

1. force-push 후 **정련분 PR 생성** — #112 는 신설분으로 이미 머지됐으므로 새 PR 필요. Class A.
2. `20_guides/README.md:183` 현황표가 지침 22 를 아직 **v1** 로 표기 — v2·v3 때도 누락된 기존 갭. v4 로 정정(현황표·§3.6 요약·변경이력 v4.x) 필요.
3. 머지 후 `sync-all` 로 다운스트림 전파(지침 22·스켈레톤 `ir-deck-build` 는 shared_paths 여부 확인 후).

## 현재 열린 트랙 (콜드스타트용)

- **METH-116 정련**: 본 브랜치 — PR 대기.
- **METH-134/135 잔여**: 실험 모드 첫 실전 적용 · 자율주행 첫 실주행 + 권한 allowlist.
- **METH-130**(Backlog): UI repo 6곳 방어층 설치. **METH-113**(Backlog): retrofit.
- 후속 후보: capsule 발신 시점 id 검증 · 월간 전수조사 2회차(8월 말) · graph.json outbox/collect/land 노드.

## 막힌 것
- 없음. (지침 22 병합은 v2·v3 규율을 모두 승계했으나, 6단계 재편으로 §1.2 서술("디자인 계약 고정 후 콘텐츠 주입")이 신 모델과 어긋남 — 사람 확인 후 문구 정리 권장.)

## 환경
- macOS, python3. 대시보드 http://localhost:8768.
