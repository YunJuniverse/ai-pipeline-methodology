# Checkpoint — 2026-07-08 (METH-064 서비스기획서 = 부모(인덱스) 모델)

> ✅ METH-064: 문서별 심화 2번 = 서비스기획서. 사용자 통찰("여러 문서의 총합 아닌가")이 지침11 내부 모순
> (§2/§6=컨테이너 vs §19.2="12 중 한 장")을 드러냄. 웹리서치 → **컨테이너 아닌 index로 결정** → 부모=오케스트레이터로 재정의.
> 🏁 다음: PR 리뷰·머지 → 문서별 심화 계속(다음 대상 선정).
> ⚠️ 프로세스: stale local main 기준 브랜치 사고 → pull 후 재베이스로 복구(작업 손실 0). 앞으로 문서 심화는 머지 후 착수 or pull 먼저.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-064-service-plan-index-model` (main 기준, 063 머지 후 재베이스 — main 직접 PR)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-064 — 서비스기획서를 컨테이너 → 부모(인덱스)로 재정의** (사용자 통찰 발의):

- **발단**: 사용자가 "서비스기획서는 원래 여러 문서의 총합 아닌가"를 물음. 확인 결과 **지침11이 내부 모순**:
  §2.2/§6은 "구조·기능·정책의 *원본 컨테이너*"인데 §19.2는 "표준 12 산출물 중 *한 장*". 우리 카탈로그엔 이미
  `ia-spec·functional-spec·service-policy·user-flow·wireframe-spec·user-story` 자식 템플릿이 있어 단일출처 붕괴.
- **웹리서치**(서브에이전트): GitHub Spec Kit(spec.md=WHAT/WHY, HOW 배제; plan→tasks 하류 생성) · Cagan(고충실
  프로토타입이 화면 스펙) · Amazon PR/FAQ · Basecamp Shape Up(No-gos) · Atlassian/Figma(link-don't-embed) ·
  한국 실무(화면설계서 모놀리스 → Notion/Figma ID 인덱스 해체) → **결정적으로 index, not container**.
- **결정(사용자 확정 A)**: 부모=**의도·결정·경계** 소유 / 자식=**상세·열거** 소유. 상세가 전용 SSOT에 살 수 있으면 복사 말고 링크.
- **변경 (지침 `20_guides/11_서비스기획서_작성_지침.md`)**:
  - §2.2 위상 재정의(컨테이너→오케스트레이터) + [원본]/[인덱스] 소유표, §2.3/§2.4 정합.
  - §6 각 항목 **[원본]** vs **[인덱스 → 자식템플릿]** 재라벨 + 위임 노트(6.4→ia-spec·6.6→functional-spec·
    6.7→wireframe-spec·6.8→service-policy·6.9→functional-spec·6.10→ia-spec).
  - **§6.0 산출물 인덱스 신설**(부모의 척추: 자식 링크+상태+소유자 표) — §19.2 "12 산출물 현황"의 정본.
  - §8.1 목차를 인덱스 척추로 재정렬(의도·결정·경계 앞, 상세는 인덱스로 위임) + **비목표(Non-Goals) 1급화**(§6.11).
  - §16 인덱스 모델 체크(중복 없음·인덱스 최신·비목표·AI 품질bar) + §19.14 부모=인덱스 원칙 환류.
  - 스켈레톤 `30_planning/11_서비스기획서.md` 인덱스 척추로 재작성(§4에 산출물 인덱스 표).
- **동형성**: METH-062 "개발기획서=재번들 반대"의 기획 쪽 쌍둥이. 09/21 인덱스 패턴과 정합.

## 다음 사람에게 (구체적 첫 행동)

1. METH-064 PR 리뷰·머지.
2. **문서별 심화 계속** — 다음 대상 사용자와 합의(후보: 요구사항정의서·정책정의서). 패턴: 현행 고찰 → 웹리서치 → 제안 → 반영.
   **프로세스 교훈**: 다음 착수 전 `git pull` 또는 직전 PR 머지 확인(064에서 stale main 사고).
3. guide 09·21 + api-contract를 다음 다운스트림 sync 대상에 포함.
4. METH-060 잔여: ai-icons 번호 정리(별건 repo 세션) + cafe24·icons-invest clean 후 sync.

## 미해결 결정사항 (Open Questions)

- 서비스기획서 §6.0 산출물 인덱스를 *자동 생성*(자식 파일 존재→상태 채움) 도구화할지 — 현재 수동 표. 실사용 빈도 보고 판단.
- 문서별 심화 표준 산출물 = 지침 개정 + 스켈레톤 정합 + (필요 시) 위상 재정의. 063=포맷/척추, 064=위상/경계 — 문서마다 축이 다름.

## 환경 메모

- 브랜치: `claude/meth-064-service-plan-index-model` (fresh main 기준, 063 포함). main 직접 PR.
- 변경: `20_guides/11_서비스기획서_작성_지침.md`(§2·§6·§8·§16·§19) + `30_planning/11_서비스기획서.md`(재작성) + 라이브 4종.
- 선행 061·062·063 = PR #51·#52·#53 머지 완료(main 반영).
