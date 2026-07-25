# Skeleton: ir-deck-build

- Base version: `v1`
- Domain: IR·사업기획 덱 제작 (Deck as Code)
- 지침: `20_guides/22_IR_사업기획_덱_제작_지침.md`

## 무엇을 미리 깔아주나

지침 22의 5단계 파이프라인을 *바로 실행 가능한* 형태로. 새 덱은 이 폴더를 프로젝트 IR 디렉터리로 복사하고 브랜드 값만 교체하면 시작된다.

| 파일 | 역할 | 파이프라인 단계 |
|---|---|---|
| `base/textbook.template.md` | 아웃라인/텍스트본 + 승인 게이트 체크 | **P1** |
| `base/contract.py` | 디자인 계약(색 3·타입 6·강조 예산) + 헬퍼 라이브러리 | **P2** |
| `base/build.py` | 빌드 오케스트레이터(차트→pptx→geometry check→PDF) | **P3·P4** |
| `base/panel-prompt.md` | 멀티에이전트 실사 패널 4렌즈 프롬프트 | **P4** |
| `base/_data/` | 차트 데이터 정본(xlsx) 위치 | **P0** |

## 사용 (Day-1, 지침 22 §8)

```bash
cp -R 50_resources/skeletons/ir-deck-build/base  <프로젝트>/40_dev/snapshots/IR/_build
pip install python-pptx
# 1) P0: _data/에 재무·차트 정본 xlsx 배치, README에 정본 판정 기록
# 2) P1: textbook.template.md 채우고 타이틀 테스트 → 사람 승인
# 3) P2: contract.py 토큰 블록에서 브랜드 색·서체 값만 교체(구조 유지)
# 4) P3: build.py에 1슬라이드=1함수로 텍스트본 주입
python3 <프로젝트>/.../build.py     # 5) P4: 렌더+PDF+geometry check
# 6) P4: panel-prompt.md로 실사 패널(지침 08 팬아웃)
```

## 미리 막는 함정 (지침 22 §7)
- 하단 겹침 → `build.py` geometry check(`y+h ≤ 7.05`)
- 서체 미임베드 → `pdffonts`로 검증(contract.py 주석)
- 색·타입 난립 → 계약 상단 고정(3단계·6단계)
- 강조색 남용 → 예산제(장당 1~2포인트)

> Catalog 엔트리(C-NNN)는 아직 없다 — IR 덱 마찰이 반복 검증(N≥2)되면 승급 후보. 현재는 base-only 스켈레톤.
