# -*- coding: utf-8 -*-
"""IR 덱 디자인 계약 + 헬퍼 라이브러리 (지침 22 §3).

기계가 읽는 계약: 색 3단계·타입 6단계·강조 예산제·마진.
슬라이드 코드(build.py)는 이 토큰만 부른다 — raw hex/pt 금지(지침 20 "이름=역할" 인스턴스화).
브랜드에 맞게 바꾸는 것은 *값*(색·서체)뿐, *구조*(3단계·6단계)는 유지한다.
"""
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn

# ============================================================
# DESIGN TOKENS — 콘텐츠는 이 블록을 수정하지 말 것
# ============================================================
# 색: 브랜드 값만 교체. 베이스(다크 프리미엄) + 강조 1색.
NAVY   = RGBColor(0x1A, 0x1F, 0x4B)   # 배경·잉크 베이스
NAVY2  = RGBColor(0x2A, 0x31, 0x70)   # 톤온톤 보조
CORAL  = RGBColor(0xFF, 0x5C, 0x7A)   # ★ 강조색 — 장당 1~2포인트 예산(§3.3)
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
MUTED  = RGBColor(0x6B, 0x72, 0x8F)

# 텍스트 색 3단계 위계 (§3.1) — 유사색 난립 금지
TXT_HI  = WHITE                       # 핵심
TXT_MID = RGBColor(0xD5, 0xDB, 0xF0)  # 본문
TXT_LOW = RGBColor(0x9A, 0xA2, 0xC8)  # 각주·라벨 (WCAG AA 4.5:1 검증 대상)

# 타입 스케일 6단계 (§3.2) — 표지/클로징 디스플레이는 예외
T_HEAD = 26   # 헤드라인(완결 주장문)
T_CARD = 14   # 카드·섹션 제목
T_SUB  = 12   # 소제목/키커
T_BODY = 10.5 # 본문
T_CAP  = 9.5  # 캡션
T_FOOT = 9    # 각주·푸터

HEAD = "Pretendard"; BODY = "Pretendard"  # 국내 표준·9굵기. 렌더 환경 설치 + pdffonts 임베드 검증 필수
SW, SH = 13.333, 7.5   # 16:9
MX = 0.7               # 좌우 마진
FOOT_LINE = 7.05       # 하단 요소 y+h ≤ 이 값 (§7 겹침 가드)

# ============================================================
# HELPERS — 슬라이드 코드가 부르는 원자적 프리미티브
# ============================================================
def slide(prs, bg=NAVY):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    r = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    r.fill.solid(); r.fill.fore_color.rgb = bg; r.line.fill.background(); r.shadow.inherit = False
    s.shapes._spTree.remove(r._element); s.shapes._spTree.insert(2, r._element)
    return s

def pic(s, path, l, t, w, h):
    return s.shapes.add_picture(path, Inches(l), Inches(t), Inches(w), Inches(h))

def rect(s, l, t, w, h, fill=None, line=None, lw=1.0, round=False, radius=0.08):
    shp = s.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE if round else MSO_SHAPE.RECTANGLE,
        Inches(l), Inches(t), Inches(w), Inches(h))
    if round:
        try: shp.adjustments[0] = radius
        except Exception: pass
    if fill is None: shp.fill.background()
    else: shp.fill.solid(); shp.fill.fore_color.rgb = fill
    if line is None: shp.line.fill.background()
    else: shp.line.color.rgb = line; shp.line.width = Pt(lw)
    shp.shadow.inherit = False
    return shp

def txt(s, l, t, w, h, runs, size=T_BODY, bold=False, color=TXT_MID,
        align=PP_ALIGN.LEFT, font=BODY, anchor=MSO_ANCHOR.TOP, sp=1.0, wrap=True):
    tb = s.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h)); tf = tb.text_frame
    tf.word_wrap = wrap
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = anchor
    if isinstance(runs, str): runs = [(runs, {})]
    def is_line_list(x): return isinstance(x, list) and x and isinstance(x[0], list)
    lines = runs if is_line_list(runs) else [runs]
    for i, ln in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align; p.line_spacing = sp
        if isinstance(ln, tuple): ln = [ln]
        for t_, o in ln:
            r = p.add_run(); r.text = t_
            r.font.size = Pt(o.get('size', size)); r.font.bold = o.get('bold', bold)
            r.font.name = o.get('font', font); r.font.color.rgb = o.get('color', color)
            if o.get('italic'): r.font.italic = True
    return tb

def title(s, head, kicker=None, color=TXT_HI):
    """헤드라인 = 완결 주장문(§3.4). 명사구 금지."""
    if kicker:
        txt(s, MX, 0.45, 12, 0.3, [(kicker, {'size': T_SUB, 'bold': True, 'color': CORAL, 'font': HEAD})])
    txt(s, MX, 0.72, SW - 2 * MX, 1.15, head, size=T_HEAD, bold=True, color=color, font=HEAD, sp=1.02)

def foot(s, text_):
    """각주·출처 — 전장 동일 위치·9pt·TXT_LOW (§3.1)."""
    txt(s, MX, SH - 0.42, SW - 2 * MX, 0.3, [(text_, {'size': T_FOOT, 'color': TXT_LOW})])
