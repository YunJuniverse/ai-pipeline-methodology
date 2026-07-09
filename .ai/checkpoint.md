# Checkpoint — 2026-07-09 (METH-084 skeleton 서브시스템 활성화)

> ✅ METH-084: 사용자 "skeleton 필요한가?" 점검 → **유지 판정**(고유 환류 루프·자기완결·실체 있음, AI-LOG와 다름). 저활용 상태라 **활성화**: 파이프라인 end-to-end 검증 + 죽은 필드(`last_built`) 제거.
> 🏁 다음: PR 리뷰·머지 → **누적 다운스트림 sync(073~084)** 또는 agency/ops 템플릿·나머지 메타 지침. skeleton 후속=레슨→catalog 축적.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-084-skeleton-activation` (#72 머지된 main tip 기준, branch-first 준수)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-084 — `50_resources/skeletons/` 서브시스템 활성화 + 죽은 필드 정리** (사용자 "이거 필요한가?" 점검에서 파생):

- **판정**: 유지. AI-LOG(유령·삼중 중복·헌법 오염)와 달리 skeleton은 **catalog→skeleton→새 프로젝트 주입 = 고유 환류 루프**(백서 §5 L2), 자기완결(세션 컨텍스트 미오염), base에 실체 코드 있음. 진짜 문제는 중복이 아니라 *저활용*(catalog active 1개, 이력 빈약).
- **활성화 조치**:
  - ① **end-to-end 검증** — `skeleton build frontend-design-tokens` + `apply`(스크래치패드)로 init→build→apply 전 구간 정상 확인(9 base files + `.methodology-skeleton.json` 주입). 파이프라인 작동함.
  - ② **죽은 필드 제거** — `bakes-in.json.last_built`는 `init`에서 `null`로만 쓰이고 build가 갱신 안 하며 아무도 참조 안 함(실제 빌드시각 SSOT = lock `built_at`). AI-LOG 유령 필드와 동종 → `cmd_skeleton` init 페이로드(methodology.py) + `frontend-design-tokens`/`meta` bakes-in.json + `_README.md` 스키마 예시에서 제거. `_README`에 "bakes-in=사람 입력만, 빌드시각은 lock" 명문화.
  - 양 도메인(frontend-design-tokens·meta) lock 재빌드(built_at=2026-07-09). build 재실행으로 JSON 유효성 확인.
- **변경 파일**: `60_tools/methodology.py`, `50_resources/skeletons/{_README.md, frontend-design-tokens/{bakes-in.json,skeleton.lock.json}, meta/{bakes-in.json,skeleton.lock.json}}` + 라이브 4종.

## 다음 사람에게 (구체적 첫 행동)

1. METH-084 PR 리뷰·머지.
2. **누적 다운스트림 sync(2차) 강력 추천** — gamblescan·icons 072까지 반영 → **073~084 추가 필요**(지침·prompts·헌법·_CATALOG·skeleton 등 shared_paths). 홀드 3곳(ai-icons·cafe24·icons-invest) clean 후.
3. **skeleton 후속(지속)** — 적용 프로젝트에서 레슨 만날 때마다 `catalog`에 C-NNN 추가 → 관련 도메인 `bakes-in.json`에 넣고 `skeleton build`. 이게 "활성화"의 지속 실행분. 새 프론트 도메인 스켈레톤(예: webapp-next) 신설도 후보.
4. 남은 후보 — agency/ops 템플릿(proposal-go-nogo·qa-*·operation-spec·profitability-sheet·execution-plan·work-request-ticket·wbs·glossary), 메타/dev 지침(02~09·19~20). graph.json 노드(02~09·19~21).

## 미해결 결정사항 (Open Questions)

- 점검·활성화 사이클을 여기서 일단락할지 vs 계속할지 — 사용자 판단.
- 2차 다운스트림 sync 타이밍(073~084 누적) — 반영할 축적분 큼.

## 환경 메모

- 브랜치: `claude/meth-084-skeleton-activation` (#72 머지된 main tip 기준). branch-first 준수.
- 진척: 063~071 템플릿 + 072 sync(#61) + 073~078 지침군 + 079 오케(#68) + 080 마스터플랜(#69) + 081 prompts(#70) + 082 운영원칙(#71) + 083 메타파일(#72) + **084 skeleton(이번)**.
