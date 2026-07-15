#!/usr/bin/env python3
"""generate-graph-viz 데이터 주입·렌더 단위 테스트 (의존성 없음).

레이아웃은 브라우저에서 dagre 가 계산하므로(신뢰 라이브러리), 파이썬 쪽은
데이터 주입 정합성·번들 인라인·자리표시자 치환을 검증한다.

  python3 tests/test_graph_viz.py
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location(
    "graph_viz", ROOT / "60_tools" / "generate-graph-viz.py")
gv = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gv)

GRAPH = gv.load_graph(gv.GRAPH_JSON)
NODES = GRAPH["nodes"]


def test_js_nodes_cover_all_without_coords() -> None:
    jn = gv.js_nodes(NODES)
    assert len(jn) == len(NODES)
    assert {n["id"] for n in jn} == {n["id"] for n in NODES}
    keys = set(jn[0].keys())
    assert keys == {"id", "lb", "cat", "path", "role"}, keys
    # 레이아웃은 dagre 몫 — 파이썬이 좌표를 넣으면 안 된다.
    assert "x" not in keys and "y" not in keys


def test_js_edges_classify_primary() -> None:
    je = gv.js_edges(GRAPH["edges"])
    assert len(je) == len(GRAPH["edges"])
    prod = [e for e in je if e["k"] == "produces"]
    assert prod and all(e["prim"] for e in prod)
    tmpl = [e for e in je if e["k"] == "templates-for"]
    assert not tmpl or all(not e["prim"] for e in tmpl)


def test_js_life_marks_single_loop() -> None:
    life = gv.js_life(GRAPH.get("lifecycle", {}))
    assert life
    assert len([s for s in life if s["loop"]]) == 1


def test_dagre_source_inlined() -> None:
    src = gv.dagre_source()
    assert len(src) > 10000, "dagre 번들이 비었거나 너무 작음"
    assert "graphlib" in src
    # sourceMappingURL 주석은 제거돼야(아티팩트 404 방지).
    assert "sourceMappingURL" not in src


def test_render_injects_everything() -> None:
    html = gv.render(GRAPH)
    assert "/*__" not in html, "치환 안 된 자리표시자"
    assert "dagre.layout(g)" in html, "dagre 레이아웃 호출 없음"
    assert "graphlib" in html, "dagre 번들 미인라인"
    assert GRAPH["version"] in html
    assert "CLAUDE.md" in html
    assert 'id="graph"' in html


def test_dashboard_co_build_writes_viz() -> None:
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
        txt = f.read_text(encoding="utf-8")
        assert "<svg" in txt and "dagre.layout" in txt


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
