# Checkpoint — 2026-07-09 (METH-066 요구사항정의서 심화 · ISO/IEC/IEEE 29148)

> ✅ METH-066: 문서별 심화 4번 = 요구사항정의서. 웹리서치(29148·BABOK·RTM) → `requirements-spec` 대장 강화.
> functional-spec(EARS)의 *상류 = shall 대장*. 추가: 유형·인수기준·검증(I/A/D/T)·상태 생명주기·하위추적·변경등급·품질특성·RTM.
> 🏁 다음: PR 리뷰·머지 → 문서별 심화 계속(대상 선정).

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-066-requirements-spec-refresh` (fresh main 기준, #55 머지 후 pull — 프로세스 교훈 준수)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-066 — 요구사항정의서(requirements-spec) 심화** (문서별 심화 프로그램 4번):

- **방법**: 웹리서치 서브에이전트 1차 소스(ISO/IEC/IEEE 29148 SRS·BABOK 요구 분류·RTM·검증방법·우선순위·요구 생명주기) → 현행 대장(15줄, 단일 표) gap → 적용.
- **핵심 포지셔닝**: `requirements-spec` = *상류 대장*(VOC→요구→수용→추적, **shall** 선언형), `functional-spec` = 하류 구현 명세(**EARS**). 둘의 문법을 분리 유지.
- **변경 (`50_resources/templates/requirements-spec.md`)**:
  - **§1 범위·전제**(목적·제약·가정·정의) 섹션 신설.
  - **대장 컬럼 확장**: 유형(BABOK 계층: business/stakeholder/functional/**NFR**/transition/constraint) · **인수기준**(측정가능) · **검증방법(I/A/D/T)** · **상태 생명주기**(제안→검토→승인→구현→검증 / 보류·반려·취소, 사유필수) · **하위추적(FS-ID/US/TC)** · **변경등급(A/B/C)**.
  - **§3 작성 규율**: shall 규약(shall/should/will/may) · atomic(and/or 금지) · 금지 모호어 · 개별 9특성 + SET 5특성(29148).
  - **§4 검증방법 범례**(Inspection/Analysis/Demonstration/Test).
  - **§5 우선순위 프레임**: MoSCoW+Pn 기본 / 버킷 내 WSJF·RICE / 발굴 Kano.
  - **§6 RTM 양방향**: 후방(출처)·전방(테스트), **링크 복사금지**(하류는 요구ID 참조).
  - 경량 최소 컬럼 명시(과설계 방지) + `_CATALOG.md` 한줄 갱신.

## 다음 사람에게 (구체적 첫 행동)

1. METH-066 PR 리뷰·머지.
2. **문서별 심화 계속** — 대상 사용자와 합의. 기획 계열 남은 것: `prd` · `kpi-tree` · `context-glossary`. 또는 다른 기획서 지침(운영 12·마케팅 13·브랜드 14)·PM 15·AI기능 16·평가 17.
3. 심화 산출물 실사용 시 실전 예(EARS/의사결정표/29148 검증)를 지침 §19 craft로 환류.
4. 갱신 템플릿들을 다음 다운스트림 sync 대상에 포함. METH-060 잔여(ai-icons 번호 정리 등).

## 미해결 결정사항 (Open Questions)

- 문서별 심화 완료 후 "심화 세트"를 다운스트림에 일괄 sync하는 타이밍 — 여러 PR 누적됐으니 한 번에.
- 요구사항 대장 컬럼이 13개로 늘어 넓음 — 경량 최소 6컬럼 병기로 완화. 실사용에서 폭 불편하면 상세/RTM을 별 표로 분리 검토.
- 갱신된 템플릿군이 lean 원칙과 충돌 없는지 지속 점검(각 1스크린 유지 목표).

## 환경 메모

- 브랜치: `claude/meth-066-requirements-spec-refresh` (fresh main 기준). main 직접 PR.
- 변경: `50_resources/templates/requirements-spec.md`(재작성) + `_CATALOG.md`(한줄) + 라이브 4종.
- 선행 061~065 = PR #51~#55 머지 완료(main 반영).
