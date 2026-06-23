# Checkpoint — 2026-06-23 (METH-040 기획 craft 역주입: GambleScan 학습 → 방법론)

> ✅ METH-040: 적용 프로젝트 GambleScan의 실전 풀 기획 코퍼스를 방법론 업스트림으로 **역환류**
> (METH-039 ICONS 패턴의 GambleScan판). GambleScan은 전 기획 영역(사업·서비스·운영·마케팅·
> 브랜드·PM·개발명세·리서치)을 실제로 작성한 성숙 제품이라 ICONS보다 넓은 worked-example 코퍼스.
> ① **§19 없던 지침 12(운영)·14(브랜드) §19 신설 + 18(마스터플랜) §18 신설** + 기존 §19 보강
>   (10 사업·11 서비스·13 마케팅·15 PM). ② **개발명세 템플릿 4종 신설**(`50_resources/templates/`):
>   data-model·user-flow·wireframe-spec·functional-spec — 기획↔빌드 사이 빈 층.
> 관통 주제: **다면(N-sided) 시장 기획** + **거버넌스/추적 craft**. ICONS(METH-039)와 비중복.
> 모두 일반 craft만(GambleScan 도박/규제 도메인 특화 제외)+출처 명시. Class A(shared).
> 브랜치 `claude/inject-planning-craft-from-gamblescan`. **잔여**: PR 생성·대표 머지 → 다운스트림 sync.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: main checkout (branch `claude/inject-planning-craft-from-gamblescan`)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-040 GambleScan 기획 craft 역주입** (사용자: "기획문서 학습을 갬블스캔에서 진행했거든 …
까서 보고 너도 자료 찾아 학습하고 방법론 업데이트", 범위="전체 한 번에"):

1. **학습(까서 보기)**: GambleScan(`/Users/hayden/gamblescan`)의 실전 기획 코퍼스 확인 —
   `docs/archive/methodology-v1/planning/`(사업·서비스·운영·마케팅·브랜드·PM, 1,375줄),
   `.../development/`(data-model·user-flow·user-stories·wireframes·functional-spec·IA·requirements,
   2,034줄), `docs/planning/`(dev-specs·sprint-plan·task-registry, 5,455줄),
   `docs/archive/research/`(market·regulatory). 6개 영역을 병렬 서브에이전트로 정밀 학습 →
   *방법론에 아직 없는 일반화 가능 craft만* 추출(도메인 특화 제외, 기존 §19 대조해 중복 제외).
2. **갭의 핵심**: METH-039(ICONS)는 지침 10/11/13/15 §19만 채웠음 → GambleScan은
   **§19 없던 12·14·18을 실전본으로 신설**하고 **기획↔빌드 사이 개발명세 템플릿 층(전무)**을 채움.
3. **역주입(편집)**:
   - 지침 §19 보강: `10`(19.6~19.8 규제 게이팅·브리프 앵커드 리서치·다면+Phase 인덱싱),
     `11`(19.7~19.9 BR→UR→FR→NFR 4층·다면 권한/인계/피라미드·라벨링/MVP 제외),
     `13`(19.7 다면 콜드스타트·퍼널 밴드·90/9/1·검색의도), `15`(19.6~19.7 클래스×담당·
     인간 액션 레지스트리·게이트 SLA·전략폐기 도장).
   - §19/§18 신설: `12`(운영 — 독립성 4축·DoR/DoD·추적 매트릭스·의사결정 브리프·승인로그·
     5필드 프로세스), `14`(브랜드 — 인식맵·가치=실체·다면 메시지하우스·정량화 톤·역상황 규약·
     Surface 매트릭스), `18`(마스터플랜 §18 — 코드 베이스라인·페이즈 종료기준 이중화·동적
     스케줄/인라인 가드·게이트 라이프사이클·개발명세 4종 체계). 지침 18 변경이력 v4 추가.
   - 신규 템플릿 4종(`50_resources/templates/`): `data-model`·`user-flow`·`wireframe-spec`·
     `functional-spec` (공통: 기반문서 frontmatter + Change Log + Out-of-Scope + 3-state UI).
4. **검증**: 지침 7종 +122줄·템플릿 4종. manifest-check 통과(70_meta 격리 OK).
   shared_paths = `20_guides`/`50_resources`/`60_tools`(README:212) → 전부 다운스트림 전파 대상.
5. 라이브 파일 갱신: TODO(METH-040 InProgress), HANDOFF(Working on/Next/Recent 5건),
   본 checkpoint, observe 로그.

**METH-041 ICONS §19 압축 누락 보충** (이어서, 사용자 "icons 폴더에서도 역주입해야해
최근에 기획서 학습 진행했어 확인해봐"):

- 확인 결과: ICONS 기획 학습 코퍼스(`/Users/hayden/icons/40_dev/knowledge/` 01~05 +
  `40_dev/snapshots/ICONS-기획craft-학습보고서-2026-06-23.md`)는 **이미 METH-039
  (PR #30 머지)로 주입 완료된 바로 그 출처**. 학습보고서 §4가 knowledge 01~05와,
  그게 다시 방법론 지침 10/11/13/15 §19와 1:1. 타임라인도 일치(04·05는 03:34 UTC
  생성 → METH-039 머지 05:25 UTC 이전).
- 단, 서브에이전트 정밀 대조에서 **METH-039 압축 시 "이름만 남고 본문 증발"한 체크리스트
  6건**(중요 2 + 사소 4) 발견 → 보충:
  - 지침 10: §19.9 협업·커뮤니케이션(KJ법·블루캡·대화전환·개발/디자인 대화법),
    §19.10 Exec Summary 8칸.
  - 지침 11: §19.10 서비스정의 3종(측정가능 Target·Core/Support·출시유형 3)·
    ASIS UIUX 7루브릭·용어사전/페이퍼목업/신개념 온보딩.
  - 지침 15: §19.8 WBS 3계층(Step→Activity→Task)+Task 5요소·제안서 3 Style·
    품질검토 8항목.
  - 마케팅 13은 *완전 커버*라 제외. ICONS 도메인(서브컬처 IP·팝업) 특화 제외.
- **PR #31에 METH-040과 묶음**: METH-040과 METH-041이 같은 §19 섹션(지침 10/11/15)을
  편집 → 별도 PR이면 머지 충돌. 같은 브랜치에 ship.

## ⚠️ 다음 사람: 우선 처리 후보

- **METH-040 PR 생성·머지** (Human 승인 게이트). 브랜치 `claude/inject-planning-craft-from-gamblescan`
  → PR(대표 머지=승인 증빙). CLAUDE.md: no direct push to main.
- **머지 후 다운스트림 `sync --apply` 전파**: icons·ai-icons·gamblescan(템플릿 미수령),
  cafe24 경로 미확인(`/Users/hayden/cafe24` repo 부재 — 사용자 확인). **METH-039 다운스트림
  전파도 미수행 상태** → METH-040 머지 후 둘을 합쳐 1회 sync 로 처리하면 효율적.

## 다음 사람에게 (구체적 첫 행동)

1. METH-040 PR 생성(이미 ship 으로 push 됐으면 PR 만 열기) → 사용자 리뷰·머지 대기.
2. 머지되면 다운스트림 sync(METH-039+040 합산). cafe24 경로부터 사용자 확인.
3. 신규 작업은 사용자 지시 대기.

## 막혔던 지점 / 시도해봤지만 안 된 것

- 첫 추측 오류: 사용자의 "갬블스캔 역주입" 질문에 처음엔 `90_archive/evaluation/`의 manus
  외부감사 문서(방법론 원형의 출처)로 답했으나, 사용자가 정정 — *기획문서 학습*은 GambleScan
  실전 산출물(planning/development)을 의미. 코퍼스 위치 재탐색 후 정상 진행.
- GambleScan에 ICONS 같은 `40_dev/knowledge/` 라벨 폴더는 없음 — 학습 코퍼스 = 실제 작성된
  기획·개발명세 산출물 자체(docs/archive/methodology-v1/, docs/planning/).

## 미해결 결정사항 (Open Questions)

- 다운스트림 대상에 cafe24 포함 여부 — `/Users/hayden/cafe24` repo 부재. 경로/제외 사용자 확인.
- METH-040 분량이 커서(7지침+4템플릿) 머지 전 사용자 정독 권장. 도메인 특화 누출 0 의도했으나
  리뷰에서 일반성 재확인 바람.

## 환경 메모

- 본 작업 worktree: main checkout (branch `claude/inject-planning-craft-from-gamblescan`).
- 변경 파일: `20_guides/{10,11,12,13,14,15,18}` + `50_resources/templates/{data-model,
  user-flow,wireframe-spec,functional-spec}.md` + 라이브 4종 + observation 1건.
- 출처 프로젝트: GambleScan `/Users/hayden/gamblescan`(다면 시장 리뷰 플랫폼, Next.js, 16 Phase).
