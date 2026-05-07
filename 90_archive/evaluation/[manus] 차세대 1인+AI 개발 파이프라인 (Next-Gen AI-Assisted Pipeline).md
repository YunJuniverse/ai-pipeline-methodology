# 차세대 1인+AI 개발 파이프라인 (Next-Gen AI-Assisted Pipeline)

**작성자**: Manus (External Auditor)
**대상 프로젝트**: GambleScan
**작성일**: 2026-03-29

---

## 1. 개요: "Code as Truth, Docs on Demand"

기존의 파이프라인은 "문서가 항상 최신 상태를 유지해야 한다"는 엔터프라이즈급 애자일의 환상에 빠져 있었습니다. 그 결과 AI는 코딩보다 문서 업데이트에 더 많은 토큰과 컨텍스트를 낭비했습니다.

새로운 파이프라인의 핵심 철학은 **"코드가 유일한 진실의 원천(Source of Truth)이며, 문서는 인간이 원할 때 코드로부터 즉시 생성(Generate on Demand)한다"**는 것입니다. 이를 통해 AI의 컨텍스트 윈도우를 온전히 '문제 해결'과 '코드 품질'에 집중시키면서도, 투자자나 외부 이해관계자에게 보여줄 완벽한 문서를 언제든 뽑아낼 수 있습니다 [1].

---

## 2. 차세대 파이프라인 4대 원칙

### 원칙 1: 3-File Context System (초경량 상태 관리)
AI가 매번 읽어야 하는 문서를 단 3개로 제한하여 컨텍스트 오염을 방지합니다.
1. **`README.md`**: 프로젝트의 목적, 기술 스택, 실행 방법 (불변/정적 정보)
2. **`CLAUDE.md`**: AI를 위한 시스템 프롬프트, 코딩 컨벤션, 에러 처리 규약 (규칙)
3. **`HANDOFF.md`**: 현재 진행 상태, DB 스키마 요약, 미해결 이슈, 다음 작업 목표 (동적 상태)

### 원칙 2: TDD for AI (테스트 기반 검증)
AI가 스스로 "피드백 보고서"를 쓰며 잘했다고 거짓말(Hallucination)하는 것을 막습니다.
- **Before**: 코딩 → AI가 피드백 보고서 작성 → 다음 단계
- **After**: 인간이 요구사항을 담은 **테스트 코드(E2E/Unit)를 먼저 작성** (또는 AI에게 작성 지시) → AI가 코딩 → **테스트 통과(Green)** 시 완료 간주

### 원칙 3: Physical Human Gate (물리적 통제)
문서상의 "승인 대기"는 AI의 자율 주행 모드에서 무시됩니다.
- AI는 `main` 브랜치에 직접 푸시할 수 없습니다.
- AI는 기능 구현 후 **새 브랜치를 파고 PR(Pull Request)을 생성**하는 것까지만 수행합니다.
- 인간이 코드를 리뷰하고 Merge 버튼을 누르는 행위 자체가 유일한 Approval Gate입니다.

### 원칙 4: On-Demand Documentation (필요할 때만 문서 생성)
기획서, 명세서, 아키텍처 문서를 미리 만들어두고 유지보수하지 마십시오.
- 인간이 특정 문서가 필요할 때 (예: "투자자에게 보여줄 사업기획서가 필요해", "현재 DB 구조를 다이어그램으로 그려줘"), AI에게 **현재 코드베이스를 읽고 문서를 역산(Reverse-engineer)하여 생성**하도록 지시합니다.
- 생성된 문서는 일회성(Snapshot)으로 취급하며, 코드가 바뀌면 문서를 수정하는 것이 아니라 나중에 다시 생성합니다.

---

## 3. 새로운 워크플로 (The Workflow)

### Step 1: Planning (인간 주도)
- 인간이 `TODO.md` 또는 GitHub Issues에 이번에 만들 기능의 요구사항을 Bullet point로 적습니다.
- (선택) 복잡한 로직이라면 `spec.md`를 하나 만들어 AI와 대화하며 엣지 케이스를 정리합니다 [1].

### Step 2: Execution (AI 주도)
- AI에게 프롬프트: *"TODO.md의 1번 항목을 구현해. 구현이 끝나면 테스트를 돌리고, 통과하면 새 브랜치로 PR을 올려."*
- AI는 `CLAUDE.md`의 규칙과 `HANDOFF.md`의 상태를 읽고 코드를 작성합니다.

### Step 3: Verification (물리적 Gate)
- 인간이 PR을 리뷰합니다.
- 수정이 필요하면 PR 코멘트로 지시합니다.
- 완벽하면 인간이 Merge합니다.

### Step 4: State Update (상태 동기화)
- Merge 직후, AI에게 지시: *"방금 작업한 내용을 바탕으로 HANDOFF.md의 진행 상태와 DB 스키마를 업데이트해."*
- 스프린트 보고서는 작성하지 않습니다.

---

## 4. 즉시 실행 가능한 TODO 리스트

현재 GambleScan 프로젝트를 새 파이프라인으로 전환하기 위한 구체적인 액션 아이템입니다.

### Phase 1: 문서 다이어트 (Documentation Diet)
- [ ] `docs/planning/` 디렉토리 전체를 `docs/archive/planning/`으로 이동
- [ ] `docs/development/` 디렉토리 전체를 `docs/archive/development/`로 이동
- [ ] `docs/sprints/` 디렉토리 전체를 `docs/archive/sprints/`로 이동
- [ ] `docs/agile-templates/` 디렉토리 삭제 (더 이상 템플릿 채우기 놀이를 하지 않음)
- [ ] `CLAUDE.md`에서 "Phase 0~10 파이프라인" 및 "Human Approval Gates" 섹션 삭제

### Phase 2: 코어 컨텍스트 재정비
- [ ] `CLAUDE.md`를 순수하게 "AI 코딩 가이드라인"으로 개편 (에러 처리, Zod 검증, RLS 규칙 등)
- [ ] `HANDOFF.md`를 "현재 상태와 다음 목표" 중심으로 경량화
- [ ] 프로젝트 루트에 `TODO.md` 생성 (앞으로의 작업은 여기에 체크리스트로 관리)

### Phase 3: 테스트 인프라 강화
- [ ] 현재 `tests/e2e/`에 있는 Playwright 테스트들이 실제로 CI/CD에서 도는지 확인
- [ ] AI가 코드를 짜기 전에 `tests/e2e/`에 실패하는 테스트(Red)를 먼저 추가하는 워크플로 연습

### Phase 4: On-Demand 문서 생성 스킬(Skill) 구축
- [ ] AI에게 "현재 코드베이스를 분석해서 최신 개발명세서를 `docs/snapshot/`에 마크다운으로 뽑아줘"라는 프롬프트를 템플릿화하여 저장 (필요할 때만 사용)

---

## 5. 결론

"완벽한 문서"는 개발 과정 내내 유지해야 하는 짐이 아닙니다. 코드가 완벽하다면, AI는 언제든 그 코드를 읽고 완벽한 문서를 1분 만에 써낼 수 있습니다. 

문서 유지보수에 쓰던 AI의 지능을 **보안 취약점 탐지, 예외 처리, 테스트 코드 작성**으로 돌리십시오. 그것이 1인 창업자가 AI를 레버리지하여 가장 빠르고 안전하게 프로덕트를 완성하는 길입니다.

---

### References
[1] Addy Osmani, "My LLM coding workflow going into 2026", Medium, Dec 19, 2025. https://medium.com/@addyosmani/my-llm-coding-workflow-going-into-2026-52fe1681325e
