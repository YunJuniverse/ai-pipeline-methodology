---
doc_id: meta-readme
title: Meta-Methodology — 방법론을 진화시키는 방법론
version: v0.1.0
status: active
last_updated: 2026-05-12
ai_relevance: foundational
sync_policy: excluded
---

# 70_meta/ — Meta-Methodology

> **이 폴더는 본 저장소(methodology source)에만 존재합니다.**
> 외부 프로젝트에 `methodology init` / `sync` 로 주입되지 **않습니다**.
> 강제 메커니즘은 `60_tools/methodology.py` MANIFEST의 `excluded_paths`.
> 위상: [`10_foundation/WHITEPAPER.md`](../10_foundation/WHITEPAPER.md) §부록 C — 60 slot.

---

## 1. 왜 존재하는가

본 저장소는 두 역할을 동시에 갖는 *재귀 구조* 입니다:

1. **외부 프로젝트들이 적용하는 방법론의 원천** (외부에 주입되는 자산: `20_guides/`, `50_resources/`, `60_tools/`, `.ai/`, `10_foundation/`, root 마크다운)
2. **본 저장소 자체를 운영·진화시키는 메타-방법론** (`70_meta/` — 본 폴더)

본 폴더가 없으면, 본 저장소의 *방법론 자체에 대한* 관찰·실험·회고가 **외부 프로젝트들의 도메인 자산과 섞여 함께 주입되는 문제**가 발생합니다.
→ 분리는 *주입 안전성*과 *원천성 보존*을 위한 결정적(deterministic) 보장.

## 2. 주입 제외 보장 (이중 안전망)

| 계층 | 메커니즘 |
|---|---|
| **1차 (whitelist)** | `methodology.py` MANIFEST는 *명시된 경로만* 복사. `70_meta/`가 어디에도 명시되지 않으면 *애초에* 복사 안 됨. |
| **2차 (excluded_paths)** | MANIFEST에 `excluded_paths: ["70_meta"]` 명시. sync/init 시 안전망 검증. 실수로 다른 곳에 추가해도 차단됨. |

검증 명령:
```bash
python3 60_tools/methodology.py manifest-check   # 안전망 검증 (구현 시점에 따라)
```

## 3. 내부 구조

```
70_meta/
├── _README.md           ← 본 문서 (메타-방법론 운영 규칙)
├── rfc/                 ← 방법론 변경 제안 (RFC-NNN_<slug>.md)
├── retrospectives/      ← 분기 회고 (YYYY-QN_<slug>.md)
├── experiments/         ← 실험 (EXP-NNN_<slug>.md)
├── observations/        ← 메타-운영 관찰 (방법론 자체의 마찰)
└── catalog/             ← 메타-Catalog (방법론 운영의 반복 마찰)
    ├── _pending/        ← N=1 Pending Lesson + 승급 후보
    └── archived/        ← 6개월 hit 0회 자동 아카이브
```

식별자 컨벤션:
- **RFC**: `RFC-001`, `RFC-002` … (백서·헌법 변경의 *근거 문서*)
- **EXP** (실험): `EXP-001` … (예: 새 L3 마이닝 알고리즘 시도)
- **메타 Catalog ID**: `MC-NNN` (`M`eta `C`atalog) — `C-NNN` (도메인 카탈로그)와 충돌 회피
- **회고**: `YYYY-QN_<slug>.md` (예: `2026-Q2_methodology-review.md`)

## 4. 도메인 Catalog와의 차이 (가장 흔한 혼동 지점)

| 항목 | `50_resources/catalog/` (도메인) | `70_meta/catalog/` (메타) |
|---|---|---|
| **무엇** | 외부 프로젝트에서 반복되는 *기술/구현* 마찰 | 본 저장소 운영 중 발견되는 *방법론 자체의* 마찰 |
| **예시** | "Next.js + Supabase SSR auth hydration mismatch" | "HANDOFF.md가 분기마다 부패한다" / "L1 관찰 로그를 자주 깜빡한다" |
| **주입** | ✅ 외부 프로젝트에 복사됨 (`shared_paths`) | ❌ 본 저장소에만 |
| **ID** | `C-NNN` | `MC-NNN` |
| **솔루션 레벨** | 코드·아키텍처 | 프로세스·문서·CLI 규칙 |

판정 기준 한 줄: **"외부 프로젝트가 이 솔루션의 혜택을 받는가?"** Yes → 도메인 / No → 메타.

## 5. 각 디렉터리 운영 규칙

### 5.1 `rfc/`
- 백서·헌법·운영 규칙 변경 *제안*. 머지된 RFC는 `40_dev/adr/`에 ADR로 박힘.
- Class C 변경의 *논의 공간*.
- 폐기된 RFC도 삭제하지 않음 (`status: rejected`).

### 5.2 `retrospectives/`
- 분기마다 1회. 측정 지표(백서 §7) 대비 실측 + 다음 분기 우선순위.
- 자가발전 루프의 *사람 측 게이트*.

### 5.3 `experiments/`
- 검증되지 않은 아이디어의 *제한된 시도*. 성공·실패 모두 기록.
- 성공 시 RFC 또는 ADR로 승급.

### 5.4 `observations/`
- 본 저장소를 운영하면서 *AI가 자동 기록*하는 메타-관찰.
- 형식: [`20_guides/03_AI_관찰_로그_작성_규칙.md`](../20_guides/03_AI_관찰_로그_작성_규칙.md) 와 동일. 단 *대상이 방법론 운영*.
- 예: "RFC 작성 시 부록 C 매번 검색 필요 → 검색 효율 개선 후보".

### 5.5 `catalog/` (메타-Catalog)
- 형식: [`50_resources/catalog/_README.md`](../50_resources/catalog/_README.md) 의 스키마를 그대로 따름. 단 `id: MC-NNN`.
- 승급·아카이브 규칙도 동일 (N≥2 승급, 6개월 hit 0 아카이브).
- *주입 안 됨*이 결정적 차이.

## 6. 안티패턴

| 실수 | 결과 | 교정 |
|---|---|---|
| 도메인 마찰을 `70_meta/catalog/`에 넣음 | 외부 프로젝트가 그 솔루션의 혜택 못 받음 | 판정 기준(§4) 재적용 → `50_resources/catalog/`로 이동 |
| 메타 마찰을 `50_resources/catalog/`에 넣음 | 외부 프로젝트에 무관한 솔루션이 주입됨 | 제거 후 `70_meta/catalog/`에 재등록 |
| `70_meta/`를 MANIFEST `shared_paths`/`init_paths`에 추가 | 주입 격리 깨짐 | `excluded_paths` 검증 fail → CI 차단 |
| RFC 없이 백서 직접 수정 | Class C 게이트 우회 | 백서 §12 변경 절차 위반 — revert |

## 7. 첫 시드

본 폴더는 *Stage 1.5 — 메타-방법론 신설* 의 결과물. 초기 시드:
- `RFC-001`: (예정) 본 폴더 자체의 신설 결정 — ADR 후속화 대기
- `MC-001`: (대기) 첫 메타 마찰 N≥2 목격 시 추가

## 8. 자가 검증

분기 회고 시 본 폴더에 대해 다음을 확인:
- [ ] `70_meta/`의 어떤 경로도 MANIFEST `shared_paths`/`init_paths`에 들어 있지 않은가
- [ ] `excluded_paths` 검증이 통과하는가
- [ ] 메타-Catalog 엔트리 중 *도메인 마찰* 로 잘못 분류된 게 없는가
- [ ] RFC ≠ ADR 경계가 유지되는가 (논의 vs 결정)
