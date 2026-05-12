# 60_meta/catalog/ — 메타-Catalog (방법론 자체의 반복 마찰)

> 본 저장소 운영에서 반복되는 *방법론·프로세스·문서* 차원의 마찰.
> 외부 프로젝트에 주입되지 **않습니다** (`60_meta/_README.md` §2 이중 안전망).

## 도메인 Catalog와의 결정적 차이

| 항목 | `40_resources/catalog/` | `60_meta/catalog/` (본 폴더) |
|---|---|---|
| ID 접두 | `C-NNN` | **`MC-NNN`** |
| 대상 | 기술/구현 마찰 | 방법론 운영 마찰 |
| 주입 | ✅ 외부 복사됨 | ❌ 본 저장소만 |
| 솔루션 레벨 | 코드·아키텍처 | 프로세스·문서·CLI 규칙 |

## 파일명·스키마

[`40_resources/catalog/_README.md`](../../40_resources/catalog/_README.md) 와 **동일**. 단:
- `id`: `MC-NNN` (3자리 제로패딩)
- `domain`: `meta-methodology` 고정

## 디렉터리 구조

```
60_meta/catalog/
├── README.md               ← 본 문서
├── _pending/               ← N=1 Pending Lesson + L3 승급 후보 (MP-NNN)
├── archived/               ← 6개월 hit 0회 자동 아카이브
└── MC-NNN_<slug>.md        ← 활성 엔트리
```

## 승급·아카이브 규칙

도메인 Catalog와 동일:
- N≥2 목격 시 active 승급 (사람 머지)
- 사람 명시 승인 시 N=1에서도 승급 가능 (PR/ADR에 이유 명시)
- 6개월 hit 0 → 자동 archived

## 예시 (예상) 메타 마찰 후보

> 아래는 *시드 후보 예시*. 실제 N≥2 목격 후에만 정식 엔트리 신설.

- "RFC 작성 시 부록 C 매번 검색 — 색인 부재"
- "L1 관찰 누락 — 세션 종료 hook 미가동 환경에서 빈번"
- "백서·CLAUDE.md·HANDOFF가 표현 불일치"
- "신규 폴더 추가 시 MANIFEST excluded_paths 갱신 누락"

## CLI (예정)

`methodology meta-catalog ...` 또는 기존 `catalog` 서브커맨드에 `--scope meta` 플래그. 결정 보류 (현 시점 수동 운영).
