#!/usr/bin/env python3
"""generate-graph-viz 레이아웃·렌더 단위 테스트 (의존성 없음).

  python3 tests/test_graph_viz.py
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location(
    "graph_viz", ROOT / "60_tools" / "generate-graph-viz.py")
gv = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gv)

GRAPH = gv.load_graph(gv.GRAPH_JSON)
NODES = GRAPH["nodes"]
CAT_ORDER = [c["id"] for c in GRAPH["categories"]]


def test_columns_cover_all_nodes() -> None:
    cols = gv.build_columns(NODES, CAT_ORDER)
    placed = [n["id"] for col in cols for n in col]
    assert len(placed) == len(NODES), (len(placed), len(NODES))
    assert set(placed) == {n["id"] for n in NODES}


def test_guides_split_by_tier() -> None:
    cols = gv.build_columns(NODES, CAT_ORDER)
    guide_cols = [c for c in cols if c and c[0]["category"] == "guides"]
    # 각 guides 열은 단일 tier 로만 구성된다.
    for col in guide_cols:
        assert len({n["tier"] for n in col}) == 1, col
    # tier 종류 수 = guides 열 수.
    tiers = {n["tier"] for n in NODES if n["category"] == "guides"}
    assert len(guide_cols) == len(tiers)


def test_layout_positions_unique() -> None:
    cols = gv.build_columns(NODES, CAT_ORDER)
    pos = gv.layout(cols)
    assert len(pos) == len(NODES)
    assert len(set(pos.values())) == len(pos), "노드 좌표 중복"


def test_layout_columns_left_to_right() -> None:
    cols = gv.build_columns(NODES, CAT_ORDER)
    pos = gv.layout(cols)
    xs = [pos[col[0]["id"]][0] for col in cols if col]
    assert xs == sorted(xs) and len(set(xs)) == len(xs), xs


def test_no_intra_column_overlap() -> None:
    cols = gv.build_columns(NODES, CAT_ORDER)
    pos = gv.layout(cols)
    for col in cols:
        ys = sorted(pos[n["id"]][1] for n in col)
        for a, b in zip(ys, ys[1:]):
            assert b - a >= gv.NODE_H, (a, b)


def test_classify_edges_by_primary_kinds() -> None:
    # 정본의 모든 엣지 kind 는 primary 이거나 아니거나로 분류되며 예외 없음.
    kinds = {e["kind"] for e in GRAPH["edges"]}
    assert "produces" in gv.PRIMARY_KINDS
    assert "templates-for" not in gv.PRIMARY_KINDS  # 보조(점선)
    assert kinds, "엣지 없음"


def test_life_marks_loop_stage() -> None:
    life = gv.js_life(GRAPH.get("lifecycle", {}))
    assert life, "라이프사이클 비어있음"
    loops = [s for s in life if s["loop"]]
    assert len(loops) == 1, [s["id"] for s in loops]  # 마지막 순환 단계 1개


def test_render_injects_all_placeholders() -> None:
    html = gv.render(GRAPH)
    assert "/*__" not in html, "치환 안 된 자리표시자 존재"
    assert "<svg" in html and "id=\"graph\"" in html
    # 실제 노드/버전이 주입됐는지.
    assert GRAPH["version"] in html
    assert "CLAUDE.md" in html


def test_dashboard_co_build_writes_viz() -> None:
    # cmd_dashboard 이 부르는 _build_graph_viz 가 실제 파일을 생성하는지(통합).
    import tempfile
    _m = importlib.util.spec_from_file_location(
        "methodology_mod", ROOT / "60_tools" / "methodology.py")
    mod = importlib.util.module_from_spec(_m)
    _m.loader.exec_module(mod)
    with tempfile.TemporaryDirectory() as tmp:
        out_dir = Path(tmp)
        mod._build_graph_viz(ROOT, out_dir)
        f = out_dir / "methodology-graph-viz.html"
        assert f.exists(), "viz 파일 미생성"
        assert "<svg" in f.read_text(encoding="utf-8")


def main() -> int:
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    failed = 0
    for t in tests:
        try:
            t()
            print(f"  ok   {t.__name__}")
        except AssertionError as e:
            failed += 1
            print(f"  FAIL {t.__name__}: {e}")
        except Exception as e:  # noqa: BLE001
            failed += 1
            print(f"  ERR  {t.__name__}: {type(e).__name__}: {e}")
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
