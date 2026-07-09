# Checkpoint — 2026-07-09 (METH-067 PRD 심화 · AI 시대 PRD + metric tree)

> ✅ METH-067: 문서별 심화 5번 = PRD. 웹리서치(AI-era PRD·HEART·North Star·RAT) → `prd.md` 강화(이미 탄탄 → 진짜 공백만, lean 유지).
> 핵심: **AI는 확률적이라 이진 AC로 품질 표현 불가 → §9 AI 제품 요구(eval 임계 3단·가드레일·실패→fallback)**.
> 🏁 다음: PR 리뷰·머지 → 문서별 심화 계속(대상 선정).

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-067-prd-refresh` (fresh main 기준, #56 머지 후 pull — 프로세스 교훈 준수)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-067 — PRD(prd.md) 심화** (문서별 심화 프로그램 5번):

- **방법**: 웹리서치 서브에이전트, *델타만*(일반 PRD 구조는 063/064에서 이미 커버) — AI-era PRD·성공지표 프레임·에이전트 소비·안티패턴·가정 검증에 집중. 현행 prd(11섹션, 이미 탄탄) gap → 진짜 공백만 추가, lean(2-3p) 유지.
- **변경 (`50_resources/templates/prd.md`)**:
  - **§9 AI 제품 요구 (조건부)** — 핵심 델타. AI는 확률적 → 이진 §5 AC로 품질 표현 불가:
    9.1 **품질 bar**(차원별 지표·측정법[알고/AI-judge/사람]·평가셋 + **임계 3단 launch/target/aspirational**, 분포·신뢰구간)
    9.2 **가드레일**(입력필터·출력검증·행동경계·에스컬레이션)
    9.3 **실패모드→fallback**(품질실패/가용성실패[5~15s 지연·스트리밍])
    9.4 모델전략·비용(주/fallback/저비용·인터랙션당 최대비용). *상세는 16/17 링크*.
  - **§4.3 불변식(DO-NOT-CHANGE)** — AI 구현자 보호 표면(스키마·API·인증), Class B 짝.
  - **§5** 각 요구에 테스트가능 AC(원자 술어) + 입출력 예시 → 에이전트 소비. requirements-spec/functional-spec에 링크(복사금지).
  - **§11 성공지표 metric tree** — North Star + HEART input + **가드레일/카운터 지표**(절대 나빠지면 안 됨) · AI는 모델품질/제품성과 분리.
  - **§12 가정 검증 레지스터** — 검증계획·confidence·**RAT**(가장 위험한 가정, 빌드 전 싼 테스트).
  - 리빙문서 버전 헤더 + _CATALOG 한줄 갱신.

## 다음 사람에게 (구체적 첫 행동)

1. METH-067 PR 리뷰·머지.
2. **문서별 심화 계속** — 대상 합의. 남은 것: `kpi-tree`·`context-glossary`(기획 계열), 다른 기획서 지침(운영 12·마케팅 13·브랜드 14·PM 15·AI기능 16·평가 17), 개발명세(`architecture`·`data-model`).
3. 심화 산출물 실사용 시 실전 예를 지침 §19 craft로 환류.
4. **누적 심화(063~067)를 다운스트림에 일괄 sync** 검토 + METH-060 잔여(ai-icons 번호 정리 등).

## 미해결 결정사항 (Open Questions)

- 문서별 심화가 여러 PR 누적 — 다운스트림 sync를 세트로 한 번에 할 타이밍.
- prd §9 AI 블록 vs 서비스기획서 §6.13~6.15 vs guide 16 — 세 곳의 AI-진입 경계: prd=lean 모드 제품레벨 bar / 서비스기획서=풀 기획 진입점 / 16=원본. 중복 아닌 계층. 실사용에서 재확인.
- 갱신 템플릿군 lean 유지 지속 점검(prd는 조건부 §9로 비-AI 프로젝트엔 부담 0).

## 환경 메모

- 브랜치: `claude/meth-067-prd-refresh` (fresh main 기준). main 직접 PR.
- 변경: `50_resources/templates/prd.md`(재작성) + `_CATALOG.md`(한줄) + 라이브 4종.
- 문서별 심화 진척: 063 사업기획서(#53)·064 서비스기획서(#54)·065 자식8종(#55)·066 요구사항(#56) 머지 / 067 PRD(이번).
