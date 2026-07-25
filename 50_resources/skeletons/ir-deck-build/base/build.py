# -*- coding: utf-8 -*-
"""IR 덱 빌드 오케스트레이터 (지침 22 P3~P4).

파이프라인: 차트 재생성(xlsx→PNG) → pptx 빌드 → geometry check → soffice 렌더 → PDF 동기화.
슬라이드 함수는 이 파일 하단(또는 slides/ 분리)에 1슬라이드=1함수로 원자적으로 추가한다.

실행:  python3 build.py
필요:  pip install python-pptx ;  LibreOffice(soffice) PATH; 렌더 서체(Pretendard) 설치.
"""
import os
import subprocess as sp
from pptx import Presentation
from pptx.util import Inches
from contract import *  # noqa: 디자인 계약 + 헬퍼

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_PPTX = os.path.join(HERE, "deck.pptx")
DATA = os.path.join(HERE, "_data")
CHART_GEN = os.path.join(HERE, "charts.py")  # xlsx 정본 → PNG (있을 때만)

# ── P0: 차트 데이터 정본(xlsx) → PNG 자동 재생성 ────────────────
if os.path.exists(CHART_GEN):
    sp.run(["python3", CHART_GEN], check=True)

# ── P2/P3: 프레젠테이션 초기화 + 슬라이드 주입 ─────────────────
prs = Presentation(); prs.slide_width = Inches(SW); prs.slide_height = Inches(SH)


def s01_cover():
    s = slide(prs, NAVY)
    txt(s, 0, 1.95, SW, 2.0, [("BRAND", {'size': 104, 'bold': True, 'color': TXT_HI, 'font': HEAD})],
        align=PP_ALIGN.CENTER)
    txt(s, 0, 4.25, SW, 0.45, [("한 줄 태그라인.", {'size': 16, 'color': TXT_MID})], align=PP_ALIGN.CENTER)
    txt(s, 0, SH - 0.62, SW, 0.3,
        [("㈜회사  ·  2026.MM  ·  Strictly Private & Confidential", {'size': T_FOOT, 'color': TXT_LOW})],
        align=PP_ALIGN.CENTER)


def s02_market():
    s = slide(prs, NAVY)
    title(s, [("시장은 이렇게 움직이고 있습니다 — 완결 주장문으로", {'size': T_HEAD, 'bold': True, 'color': TXT_HI, 'font': HEAD})],
          kicker="시장 기회")
    foot(s, "출처: (기관, 2026)")


# 슬라이드 등록 — 텍스트본(P1) 순서대로. 1슬라이드=1함수, 원자적 수정.
SLIDES = [s01_cover, s02_market]
for fn in SLIDES:
    fn()

prs.save(OUT_PPTX)
print(f"[ok] {OUT_PPTX}  ({len(SLIDES)} slides)")

# ── P4: geometry check — 하단 겹침 가드 (§7) ──────────────────
# soffice 렌더 육안만으론 footer 침범을 놓친다. 하단 요소 y+h ≤ FOOT_LINE 검산.
warns = []
for i, s in enumerate(prs.slides, 1):
    for shp in s.shapes:
        try:
            top = shp.top / 914400
            bottom = (shp.top + shp.height) / 914400  # EMU→inch
            # 전면 배경(top≈0 & 슬라이드 전체 높이)은 정당한 full-bleed — 제외
            is_full_bleed = top < 0.05 and bottom >= SH - 0.05
            if not is_full_bleed and bottom > FOOT_LINE + 0.35:  # footer 밴드 초과
                warns.append(f"  S{i:02d}: {shp.shape_type} bottom={bottom:.2f} > {FOOT_LINE}")
        except (TypeError, AttributeError):
            pass
if warns:
    print("[warn] 하단 겹침 후보 (§7 y+h≤7.05):")
    print("\n".join(warns))
else:
    print("[ok] geometry: 하단 겹침 없음")

# ── P4: soffice 렌더 → PDF 동기화 ─────────────────────────────
try:
    sp.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", HERE, OUT_PPTX],
           check=True, capture_output=True)
    print("[ok] PDF 동기화 완료 (스크린샷 자기검토 → 실사 패널로)")
except (sp.CalledProcessError, FileNotFoundError) as e:
    print(f"[skip] soffice 렌더 불가: {e}. 서체 임베드는 pdffonts로 검증할 것.")
