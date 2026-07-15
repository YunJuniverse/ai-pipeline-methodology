# 대시보드 슬림화 리서치 — 실용적 진행 모니터링 보드로

> 유형: Planning 리서치 스냅샷 (라이브 아님 · 승인 전 구현 금지)
> 날짜: 2026-07-15 · 작성: claude-opus-4-8
> 대상: `60_tools/generate-dashboard.py` (dashboard.html)
> 상태: **구현 완료(METH-112)** — 사용자 승인·결정(§5.1) 후 슬림 대시보드 구현. 이 문서는 그 리서치·설계 기록.

---

## 0. 목표와 결정 입력 (사용자 확인)

- **주 용도 = 진행 모니터링·공유.** 프로젝트 진척을 추적하고, 때로 남에게 보여줌.
  → 함의: 화면이 **깔끔·발표가능**해야 하고, 보는 사람이 맥락 없이도 "지금 어디까지 왔나"를 읽어야 함. **로컬 기계 전용 조작 UI는 공유 뷰에 부적합**.
- **꼭 남길 것 = 파일 전문 뷰어**(CLAUDE/HANDOFF/TODO 등 라이브 문서를 대시보드 안에서 읽기).
- **잘라도 됨 = dev 서버 제어 · 브랜치/대시보드 spawn · 커맨드 팔레트.**

---

## 1. 현행 대시보드 인벤토리 (감사)

**탭 5개:**

| # | 탭 | 담고 있는 것 | 성격 |
|---|-----|------------|------|
| 01 | 프로젝트 개요 | stat-row, stack-progress, **파일 뷰어**, 커맨드 팔레트, 로컬 대시보드 테이블(spawn/refresh), 브랜치·worktree spawn, **Dev 서버 start/kill**(3000–3099, cwd/cmd 입력), 기술스택 bento | 상태 + **운영 콘솔** 혼합 (과적재) |
| 02 | 가이드·백서 | 방법론 정적 설명(5영역·원칙·체인지클래스·sync정책) | 무시간적 레퍼런스 (프로젝트 상태 아님) |
| 03 | 관계 그래프 | 역할 지식그래프 (METH-111 후 dagre iframe) | 오리엔테이션/레퍼런스 |
| 04 | 칸반 보드 | TODO 칸반 (Backlog/Ready/InProgress/Blocked/Done) | **핵심 진행 상태** |
| 05 | 통합 뷰 | "quick scan" — stat-row + row2 + dashboards + branches **재렌더** | **01과 중복** |

**데이터 적재(assemble):** CLAUDE·AGENTS·HANDOFF·TODO·MASTER_PLAN 전문(각 ≤50KB) + `node_contents`(그래프 **모든 노드의 파일 전문**) + guides_readme + commands.json + stack.json + kanban + graph. → 상태 보드치고 페이로드 과다.

**서버 백엔드:** dev 서버 start/kill, 대시보드 spawn, worktree spawn, refresh 엔드포인트 — 파워유저 운영 기능이 앞면에 노출.

## 2. 진단 — "난잡"의 실체: 한 화면이 4가지 일을 겸함

1. **상태 파악** (지금 뭐가 진행 중인가) — HANDOFF 포커스·칸반·라이브파일 건강·브랜치/커밋. **← 진짜 핵심.**
2. **레퍼런스** (방법론 설명·역할 그래프) — 무시간적. 문서/README에 속함.
3. **운영 콘솔** (dev서버·spawn·worktree) — 드문 파워툴. CLI가 정본(`methodology dashboard list/stop` 이미 존재).
4. **파일 브라우징** (전문 뷰어) — 유지하되, 상태와 분리.

세 가지 구체적 문제:
- **중복**: 05 통합뷰 = 01 개요 재탕(stats·dashboards·branches). 그래프 노드 전문(`node_contents`)은 METH-111에서 그래프가 iframe이 되며 **죽은 데이터**(옛 d3 상세 패널만 쓰던 것).
- **공유 부적합**: dev서버 kill·localhost 포트 테이블·worktree spawn은 **내 기계 전용 조작** — 남에게 보여주는 진척 뷰에 노이즈이자 오해 소지.
- **무게**: 여러 문서 전문(50KB×N) + 전 노드 파일 전문 임베드 → 발표용으로 무겁고 느림.

## 3. 제안 — "진행 상태 보드" (모니터링 + 공유)

원칙: **한 가지 일(진행 상태)만 잘한다. 위→아래로 진척 리포트처럼 읽힌다. 로컬 조작 UI 제거.**

**탭 5 → 3으로 축소** (또는 단일 스크롤 + 그래프 1탭):

### 탭 1 · 상태 (기본, 단일 스크롤)
- **헤더/아이덴티티**: 프로젝트명 · 한 줄 목표(objective) · mode · 브랜치·커밋 · generated 시각. *(공유 시 맥락)*
- **지금(Now)**: HANDOFF *Working on* + *Recent Changes* 5건. 진척 서사.
- **진행(Progress)**: 칸반(5열) + 있으면 MASTER_PLAN 로드맵 진척(페이즈·MVP·게이트·마일스톤). **모니터링 코어.**
- **건강(Health) 스트립**: 라이브파일 사이즈 vs 한도(HANDOFF≤150·checkpoint≤200·Done건수) · wrap 신선도 · ADR/스냅샷 수 · 오픈이슈 수. "주의 필요"만 강조.

### 탭 2 · 문서 (유지 — 사용자 지정)
- 파일 전문 뷰어: CLAUDE · AGENTS · HANDOFF · TODO · MASTER_PLAN. 라이브 문서 열람.

### 탭 3 · 관계 그래프 (유지, lazy)
- dagre 지식그래프(METH-111 iframe). 오리엔테이션.

### 잘라냄
- **05 통합 뷰** (01 중복).
- **Dev 서버 제어 · 대시보드 spawn · 로컬 대시보드 테이블 · 브랜치 worktree spawn** (공유 부적합·CLI 정본).
- **커맨드 팔레트** (사용자 컷).
- **02 가이드·백서** → 대시보드에서 제거, WHITEPAPER 링크 한 줄로 대체(공유 뷰 상단 "about" 링크).
- **기술스택 bento** → **헤더에 "스택: …" 한 줄로 축약, bento 카드 제거** (확정).

### 페이로드 정리
- `node_contents`(전 노드 파일 전문) **제거** — METH-111 iframe 그래프는 미사용(죽은 데이터).
- 문서 전문은 "문서" 탭이 필요로 하는 것만(현행 5종 유지). Now/Health는 파싱 요약만 사용.

## 4. 슬림화 효과 (예상)

| 축 | 현행 | 슬림 후 |
|----|------|--------|
| 탭 | 5 | 3 |
| 앞면 카드/조작 UI | 8+ (스택·팔레트·dashboards·worktree·devservers…) | 3 블록(Now·Progress·Health) + 문서·그래프 |
| 서버 조작 엔드포인트 | dev서버·spawn·worktree | (제거) — 순수 뷰 |
| 임베드 페이로드 | 문서 전문×N + 전 노드 전문 | 문서 전문×5 (node_contents 제거) |
| 공유 적합성 | 낮음(로컬 조작 노출) | 높음(순수 진척 뷰) |

## 5. 리스크·열린 질문

- **R1. 운영 기능 실제 사용?** dev서버·spawn을 정말 안 쓰는지 최종 확인(쓴다면 별도 "ops" 뷰/CLI로 분리, 앞면엔 안 둠). — *사용자 답변상 컷.*
- **R2. 공유 방식?** 파일 열기(file://)로 보여주나, 서빙 URL을 공유하나? 서빙 조작 엔드포인트를 지우면 순수 정적 HTML로 배포 쉬워짐(공유에 유리).
- ~~Q1. 기술스택 카드~~ → **확정: 헤더 한 줄 축약, bento 제거.**
- ~~Q2. 단일 스크롤 vs 3탭~~ → **확정: 3탭 유지(상태/문서/그래프).**
- **Q3.** dashboards/worktree 관리가 필요하면 `methodology dashboard list/stop` CLI로 충분한지(대시보드 UI에서 뺄지). — 사용자 답변상 UI에서 컷.

## 5.1 확정 사항 (2026-07-15)
- 레이아웃 = **3탭**: 상태 / 문서 / 관계 그래프.
- 스택 = **헤더 한 줄 축약**, bento 카드 제거.
- 나머지 컷 목록·페이로드 정리(§3) 그대로 확정.
- **선행 의존**: METH-111(그래프 iframe화, PR #101) **머지 후** 이 위에서 구현 — `generate-dashboard.py` 충돌 방지 + node_contents 죽은 데이터 전제 성립.

## 6. 권고 다음 단계 (승인 후, Class A)

1. 이 제안 확정(탭 3안·컷 목록·스택 처리).
2. `generate-dashboard.py`에서 컷 대상 섹션·서버 엔드포인트·`node_contents` 제거, "상태" 탭 재구성(Now/Progress/Health), `parse_todo`·HANDOFF 파서·master_plan_meta 재활용.
3. 테스트: 빌드 HTML에 컷 대상 부재 + 핵심 블록 존재 + d3/죽은데이터 부재.
4. 다운스트림 sync로 10곳 전파.

> **게이트**: 이 스냅샷은 리서치 산출물. 사람의 "구현 시작" 지시 후 Dev Spec/Build로 넘어감.
