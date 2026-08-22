# Skeleton: ir-deck-build

- Base version: `v1`
- Domain: IR·사업기획 덱 제작 (Deck as Code)
- 지침: `20_guides/22_IR_사업기획_덱_제작_지침.md`

## 무엇을 미리 깔아주나

지침 22 파이프라인을 *바로 실행 가능한* 형태로. **콘텐츠(텍스트 md=SSOT)와 디자인(테마 후보)을 분리**한 구조.

| 파일 | 역할 | 파이프라인 단계 |
|---|---|---|
| `base/deck.template.md` | **텍스트 SSOT** — 스토리라인 + 슬라이드 내 텍스트 구조 + 콘텐츠 승인 게이트 | **P1·P2 (콘텐츠)** |
| `base/contract.py` | 디자인 계약(색 3·타입 6·강조 예산) + **`THEMES` 후보 레지스트리** + 헬퍼 | **P3 (디자인)** |
| `base/build.py` | 빌드 오케스트레이터 — `--theme`/`--candidates`, 차트→pptx→geometry check→PDF | **P3·P4** |
| `base/panel-prompt.md` | 멀티에이전트 실사 패널 4렌즈 프롬프트 | **P4** |
| `base/_data/` | 차트 데이터 정본(xlsx) 위치 | **P0** |

## 사용 (Day-1, 지침 22 §8)

```bash
cp -R 50_resources/skeletons/ir-deck-build/base  <프로젝트>/40_dev/snapshots/IR/_build
cp <프로젝트>/.../base/deck.template.md  <프로젝트>/.../base/deck.md   # SSOT 사본
pip install python-pptx
# P0: _data/에 재무·차트 정본 xlsx 배치, README에 정본 판정 기록
# P1·P2 (콘텐츠 먼저): deck.md에 스토리라인+슬라이드 텍스트 채움 → 타이틀 테스트 → 사람 승인
# P3 (디자인 후보): contract.py THEMES에 2~3개 테마 → 후보 비교 → 선택
python3 <프로젝트>/.../build.py --candidates       # 대표 슬라이드를 테마별로 렌더(비교)
python3 <프로젝트>/.../build.py --theme A_darknavy # 고른 테마로 전체 빌드(+geometry check+PDF)
# P4: panel-prompt.md로 실사 패널(지침 08 팬아웃)
```

> **재편집 루프**: 텍스트는 `deck.md`, 디자인은 `THEMES`에서 고치고 리빌드. pptx를 직접 손대지 않는다(파생물).

## 미리 막는 함정 (지침 22 §7)
- 하단 겹침 → `build.py` geometry check(`y+h ≤ 7.05`)
- 서체 미임베드 → `pdffonts`로 검증(contract.py 주석)
- 색·타입 난립 → 계약 상단 고정(3단계·6단계)
- 강조색 남용 → 예산제(장당 1~2포인트)

> Catalog 엔트리(C-NNN)는 아직 없다 — IR 덱 마찰이 반복 검증(N≥2)되면 승급 후보. 현재는 base-only 스켈레톤.
