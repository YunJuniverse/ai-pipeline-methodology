#!/usr/bin/env python3
"""generate-graph-viz — methodology-graph.json 을 문서 역할 지식그래프 HTML 로 렌더.

정본 `60_tools/methodology-graph.json` 을 읽어 라이프사이클 파이프라인 + 노드/엣지
지식그래프를 self-contained HTML 로 뽑는다. 레이아웃은 벤더링한 **dagre**(계층 DAG
레이아웃)를 인라인해 브라우저에서 계산한다 — 손 배치 격자의 엣지 교차(스파게티)를
없애고, 노드 순서·엣지 라우팅을 교차 최소화로 자동 배치한다.

  python3 60_tools/generate-graph-viz.py [--out PATH] [--standalone]

기본 출력은 Artifact 게시용 body-content(스타일+본문+스크립트, doctype/html/head/body
없음). --standalone 이면 바로 브라우저로 열 수 있는 완전 문서로 감싼다.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GRAPH_JSON = ROOT / "60_tools" / "methodology-graph.json"
VENDOR_DAGRE = ROOT / "60_tools" / "vendor" / "dagre.min.js"
DEFAULT_OUT = ROOT / "_start" / ".cache" / "methodology-graph-viz.html"

# 생산·서열·라우팅 흐름 = 실선(primary). 나머지(부팅·참조·템플릿 등) = 점선.
# primary 는 dagre 랭킹에서 가중치를 높여 흐름 축을 곧게 편다.
PRIMARY_KINDS = {
    "produces", "routes-to", "sequences", "sequenced-by", "drives",
    "expands-to", "phased-by", "gate-catalog-applied-by",
    "gate-catalog-instantiated-by", "decisions-go-to", "parent-of",
    "promotes-to", "bakes-into", "writes-to",
}


def load_graph(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dagre_source() -> str:
    """벤더링한 dagre 번들. 아티팩트에서 404 나지 않게 sourceMappingURL 주석 제거."""
    src = VENDOR_DAGRE.read_text(encoding="utf-8")
    return re.sub(r"\n//# sourceMappingURL=.*$", "", src).rstrip()


def js_nodes(nodes: list[dict]) -> list[dict]:
    """레이아웃은 dagre 가 하므로 좌표 없이 식별·표시 정보만 넘긴다."""
    return [{"id": n["id"], "lb": n["label"], "cat": n["category"],
             "path": n["path"], "role": n["role"]} for n in nodes]


def js_edges(edges: list[dict]) -> list[dict]:
    return [{"f": e["from"], "t": e["to"], "k": e["kind"],
             "lb": e.get("label", ""), "prim": e["kind"] in PRIMARY_KINDS}
            for e in edges]


def js_cat(categories: list[dict]) -> dict:
    """category id → CSS 변수명 + 라벨 (CSS 의 --{id}-bg/bd/tx 규약)."""
    return {c["id"]: {"bg": f"--{c['id']}-bg", "bd": f"--{c['id']}-bd",
                      "tx": f"--{c['id']}-tx", "label": c["label"]}
            for c in categories}


def js_life(lifecycle: dict) -> list[dict]:
    stages = lifecycle.get("stages", [])
    ids = [s["id"] for s in stages]
    out = []
    for i, s in enumerate(stages):
        nxt = s.get("next")
        loops = bool(nxt) and (i + 1 >= len(stages) or nxt != ids[i + 1])
        gate = s.get("human_gate")
        out.append({"id": s["id"], "lb": s["label"],
                    "out": s.get("produces", []),
                    "gate": gate if gate else None, "loop": loops})
    return out


def render(graph: dict) -> str:
    data = {
        "CAT": js_cat(graph["categories"]),
        "NODES": js_nodes(graph["nodes"]),
        "EDGES": js_edges(graph["edges"]),
        "LIFE": js_life(graph.get("lifecycle", {})),
        "VERSION": graph.get("version", "?"),
        "NCOUNT": len(graph["nodes"]), "ECOUNT": len(graph["edges"]),
    }
    body = _TEMPLATE.replace("/*__DAGRE__*/", dagre_source())
    for key, val in data.items():
        body = body.replace(f"/*__{key}__*/", json.dumps(val, ensure_ascii=False))
    return body


def wrap_standalone(body: str) -> str:
    return ("<!doctype html><html><head><meta charset=utf8>"
            "<meta name=viewport content=\"width=device-width,initial-scale=1\">"
            "<style>:root{color-scheme:light}body{margin:0;background:#faf9f5}</style>"
            "</head><body>\n" + body + "\n</body></html>")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="methodology-graph.json → 지식그래프 HTML")
    p.add_argument("--out", help=f"출력 경로 (기본: {DEFAULT_OUT})")
    p.add_argument("--standalone", action="store_true",
                   help="완전 HTML 문서로 감싼다 (브라우저 직접 열기용)")
    args = p.parse_args(argv)

    graph = load_graph(GRAPH_JSON)
    body = render(graph)
    html = wrap_standalone(body) if args.standalone else body
    out = Path(args.out) if args.out else DEFAULT_OUT
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"[ok] {out}  (nodes={len(graph['nodes'])}, edges={len(graph['edges'])}, "
          f"version={graph.get('version')}, layout=dagre)")
    return 0


# ─── HTML/CSS/JS 템플릿 (데이터는 /*__KEY__*/ 자리표시자로 주입) ─────────────
_TEMPLATE = r"""<title>방법론 문서 파이프라인 · 지식그래프</title>
<style>
  *{box-sizing:border-box;}
  :root{
    --bg:#F4F6F9; --surface:#FFFFFF; --surface-2:#F7F9FC;
    --ink:#1A2130; --muted:#586173; --faint:#8B94A6; --line:#E3E8F0; --line-strong:#C9D1DE;
    --accent:#0E9F6E; --accent-soft:#E3F3EC; --edge:#AEB7C6; --edge-strong:#54607A;
    --meta-bg:#EAEDF3; --meta-bd:#7C8AA6; --meta-tx:#2A3450;
    --guides-bg:#DBEFE6; --guides-bd:#2A9D78; --guides-tx:#0A5942;
    --planning-bg:#F6E4D9; --planning-bd:#C76A42; --planning-tx:#7A2C11;
    --dev-bg:#F4E7CE; --dev-bd:#BA8824; --dev-tx:#6B390E;
    --resources-bg:#E1E9F8; --resources-bd:#4C77C8; --resources-tx:#1C3C86;
    --font:-apple-system,BlinkMacSystemFont,"Segoe UI","Apple SD Gothic Neo","Noto Sans KR",system-ui,sans-serif;
    --mono:ui-monospace,"SF Mono","JetBrains Mono","Cascadia Code",Menlo,Consolas,monospace;
  }
  @media (prefers-color-scheme:dark){
    :root{
      --bg:#0E1117; --surface:#161B22; --surface-2:#1B212B;
      --ink:#E8ECF3; --muted:#9BA5B6; --faint:#6E7889; --line:#262D39; --line-strong:#39424F;
      --accent:#35C89B; --accent-soft:#123329; --edge:#4C5768; --edge-strong:#8F9DB2;
      --meta-bg:#252D3A; --meta-bd:#63728C; --meta-tx:#C4CEDD;
      --guides-bg:#123228; --guides-bd:#2E9E78; --guides-tx:#79E6BC;
      --planning-bg:#39240F; --planning-bd:#C05F38; --planning-tx:#F0B79A;
      --dev-bg:#362D11; --dev-bd:#B4841D; --dev-tx:#EBC981;
      --resources-bg:#17263F; --resources-bd:#5981CE; --resources-tx:#A7C2EF;
    }
  }
  :root[data-theme="light"]{
    --bg:#F4F6F9; --surface:#FFFFFF; --surface-2:#F7F9FC;
    --ink:#1A2130; --muted:#586173; --faint:#8B94A6; --line:#E3E8F0; --line-strong:#C9D1DE;
    --accent:#0E9F6E; --accent-soft:#E3F3EC; --edge:#AEB7C6; --edge-strong:#54607A;
    --meta-bg:#EAEDF3; --meta-bd:#7C8AA6; --meta-tx:#2A3450;
    --guides-bg:#DBEFE6; --guides-bd:#2A9D78; --guides-tx:#0A5942;
    --planning-bg:#F6E4D9; --planning-bd:#C76A42; --planning-tx:#7A2C11;
    --dev-bg:#F4E7CE; --dev-bd:#BA8824; --dev-tx:#6B390E;
    --resources-bg:#E1E9F8; --resources-bd:#4C77C8; --resources-tx:#1C3C86;
  }
  :root[data-theme="dark"]{
    --bg:#0E1117; --surface:#161B22; --surface-2:#1B212B;
    --ink:#E8ECF3; --muted:#9BA5B6; --faint:#6E7889; --line:#262D39; --line-strong:#39424F;
    --accent:#35C89B; --accent-soft:#123329; --edge:#4C5768; --edge-strong:#8F9DB2;
    --meta-bg:#252D3A; --meta-bd:#63728C; --meta-tx:#C4CEDD;
    --guides-bg:#123228; --guides-bd:#2E9E78; --guides-tx:#79E6BC;
    --planning-bg:#39240F; --planning-bd:#C05F38; --planning-tx:#F0B79A;
    --dev-bg:#362D11; --dev-bd:#B4841D; --dev-tx:#EBC981;
    --resources-bg:#17263F; --resources-bd:#5981CE; --resources-tx:#A7C2EF;
  }
  body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--font);line-height:1.6;-webkit-font-smoothing:antialiased;}
  .wrap{max-width:1180px;margin:0 auto;padding:32px 24px 64px;}
  header.top{margin-bottom:28px;}
  .eyebrow{font-family:var(--mono);font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);margin:0 0 8px;}
  h1{font-size:27px;font-weight:600;letter-spacing:-.01em;margin:0 0 8px;text-wrap:balance;}
  .lede{font-size:15px;color:var(--muted);margin:0;max-width:64ch;}
  h2{font-size:18px;font-weight:600;margin:40px 0 4px;letter-spacing:-.01em;display:flex;align-items:baseline;gap:10px;}
  h2 .n{font-family:var(--mono);font-size:13px;color:var(--accent);font-weight:500;}
  .sub{font-size:13.5px;color:var(--muted);margin:0 0 18px;}
  .legend{display:flex;flex-wrap:wrap;gap:8px 16px;margin:18px 0 6px;align-items:center;}
  .lg{display:inline-flex;align-items:center;gap:7px;font-size:12.5px;color:var(--muted);}
  .sw{width:13px;height:13px;border-radius:4px;border:1.5px solid;}
  .sw.meta{background:var(--meta-bg);border-color:var(--meta-bd);}
  .sw.guides{background:var(--guides-bg);border-color:var(--guides-bd);}
  .sw.planning{background:var(--planning-bg);border-color:var(--planning-bd);}
  .sw.dev{background:var(--dev-bg);border-color:var(--dev-bd);}
  .sw.resources{background:var(--resources-bg);border-color:var(--resources-bd);}
  .lg .ln{width:20px;height:0;border-top:2px solid var(--edge-strong);}
  .lg .ln.dash{border-top:2px dashed var(--edge);}
  .flow-scroll{overflow-x:auto;padding:4px 2px 12px;}
  .flow{display:flex;align-items:stretch;gap:0;min-width:940px;}
  .stage{position:relative;flex:1 1 0;min-width:96px;padding:14px 12px 13px;background:var(--surface);border:1px solid var(--line);border-radius:10px;margin-right:22px;}
  .stage:last-child{margin-right:0;}
  .stage::after{content:"";position:absolute;right:-19px;top:50%;width:16px;height:16px;transform:translateY(-50%) rotate(45deg);border-top:2px solid var(--edge);border-right:2px solid var(--edge);}
  .stage:last-child::after{display:none;}
  .stage.loop{border-color:var(--accent);border-style:dashed;}
  .st-id{font-family:var(--mono);font-size:11px;color:var(--faint);letter-spacing:.05em;}
  .st-lb{font-size:13.5px;font-weight:600;margin:3px 0 8px;letter-spacing:-.01em;}
  .st-out{display:flex;flex-direction:column;gap:4px;}
  .chip{font-family:var(--mono);font-size:10.5px;line-height:1.35;padding:2px 6px;border-radius:5px;background:var(--surface-2);border:1px solid var(--line);color:var(--muted);word-break:break-all;}
  .gate{margin-top:9px;display:inline-flex;align-items:center;gap:5px;font-size:11px;font-weight:500;color:var(--planning-tx);background:var(--planning-bg);border:1px solid var(--planning-bd);padding:2px 7px 2px 5px;border-radius:20px;}
  .gate svg{width:11px;height:11px;}
  .loopnote{margin-top:10px;font-size:12.5px;color:var(--muted);display:flex;align-items:center;gap:8px;}
  .loopnote b{color:var(--accent);font-weight:600;font-family:var(--mono);font-size:12px;}
  .loopnote svg{width:16px;height:16px;display:block;}
  .graph-scroll{overflow:auto;background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:6px;max-height:78vh;}
  svg.graph{display:block;}
  .gnode{cursor:pointer;}
  .gnode rect{stroke-width:1.5;transition:opacity .16s;}
  .gnode text{font-family:var(--font);font-size:11.5px;font-weight:500;pointer-events:none;}
  .gnode .path{font-family:var(--mono);font-size:8.5px;font-weight:400;opacity:.7;}
  .gedge{fill:none;transition:opacity .16s;}
  .dim{opacity:.1;}
  .dim-e{opacity:.04;}
  .hint{font-size:12.5px;color:var(--faint);margin:10px 2px 0;font-family:var(--mono);}
  .detail{margin-top:16px;padding:18px 20px;background:var(--surface);border:1px solid var(--line);border-radius:12px;min-height:120px;}
  .detail .ph{color:var(--faint);font-size:14px;}
  .d-head{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:6px;}
  .d-cat{font-size:11px;font-weight:600;font-family:var(--mono);letter-spacing:.04em;text-transform:uppercase;padding:2px 9px;border-radius:20px;border:1.5px solid;}
  .d-title{font-size:18px;font-weight:600;letter-spacing:-.01em;}
  .d-path{font-family:var(--mono);font-size:12px;color:var(--muted);margin:0 0 12px;}
  .d-role{font-size:14.5px;color:var(--ink);margin:0 0 14px;max-width:70ch;}
  .d-conns{display:grid;grid-template-columns:1fr 1fr;gap:14px;}
  @media(max-width:640px){.d-conns{grid-template-columns:1fr;}}
  .d-col h4{font-size:11.5px;font-family:var(--mono);text-transform:uppercase;letter-spacing:.06em;color:var(--faint);margin:0 0 7px;font-weight:600;}
  .d-col ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:5px;}
  .d-col li{font-size:13px;color:var(--muted);display:flex;gap:7px;align-items:baseline;}
  .d-col li b{color:var(--ink);font-weight:500;}
  .d-col .k{font-family:var(--mono);font-size:10.5px;color:var(--accent);white-space:nowrap;}
  .d-col .none{color:var(--faint);font-size:12.5px;}
  .foot{margin-top:34px;padding-top:16px;border-top:1px solid var(--line);font-size:12.5px;color:var(--faint);}
  .foot code{font-family:var(--mono);font-size:11.5px;color:var(--muted);}
</style>

<div class="wrap">
  <header class="top">
    <p class="eyebrow">Methodology · Document Pipeline</p>
    <h1>산출물이 나오기까지 — 문서 파이프라인 & 역할 지식그래프</h1>
    <p class="lede">레포가 스스로 인코딩한 <code style="font-family:var(--mono);font-size:13px">60_tools/methodology-graph.json</code> 을 정본으로 자동 렌더 — <b id="counts"></b>. 레이아웃은 dagre 계층 배치로 교차를 최소화한다.</p>
  </header>

  <h2><span class="n">A</span> 라이프사이클 파이프라인</h2>
  <p class="sub">입력에서 환류까지의 단일 사이클. 각 단계가 무엇을 <b>낳는지(produces)</b>와 사람의 <b>승인 게이트</b>를 표시. 마지막 단계는 개발로 순환한다.</p>
  <div class="flow-scroll"><div class="flow" id="flow"></div></div>
  <div class="loopnote" id="loopnote"></div>

  <h2><span class="n">B</span> 문서 역할 지식그래프</h2>
  <p class="sub">왼쪽(입력·지침)에서 오른쪽(산출물)으로 흐른다. <b>실선</b> = 생산·라우팅 흐름, <b>점선</b> = 부팅·참조·템플릿 등 보조 연결. 노드를 클릭하면 역할과 연결을 아래에 펼친다.</p>
  <div class="legend" id="legend">
    <span class="lg"><span class="sw meta"></span>메타 / 라이브 상태</span>
    <span class="lg"><span class="sw guides"></span>지침서</span>
    <span class="lg"><span class="sw planning"></span>기획 산출물</span>
    <span class="lg"><span class="sw dev"></span>개발 산출물</span>
    <span class="lg"><span class="sw resources"></span>재사용 자원</span>
    <span class="lg"><span class="ln"></span>생산·흐름</span>
    <span class="lg"><span class="ln dash"></span>보조·참조</span>
  </div>
  <div class="graph-scroll"><svg class="graph" id="graph" role="img" aria-label="방법론 문서 역할 지식그래프"></svg></div>
  <p class="hint">← 스크롤 · 노드 클릭 → 상세 · 배경 클릭 → 초기화</p>

  <div class="detail" id="detail"><span class="ph">노드를 클릭하면 그 문서의 역할과 들어오고 나가는 연결을 보여줍니다.</span></div>

  <p class="foot">출처: <code>60_tools/methodology-graph.json</code> (<span id="ver"></span>) — <code>60_tools/generate-graph-viz.py</code> 가 자동 렌더. 레이아웃 = dagre(계층 DAG). 인터랙션 = 노드 클릭 상세.</p>
</div>

<script>/*__DAGRE__*/</script>
<script>
const CAT=/*__CAT__*/;
const NODES=/*__NODES__*/;
const EDGES=/*__EDGES__*/;
const LIFE=/*__LIFE__*/;
const VERSION=/*__VERSION__*/, NCOUNT=/*__NCOUNT__*/, ECOUNT=/*__ECOUNT__*/;
const NW=158,NH=46;
const byId=Object.fromEntries(NODES.map(n=>[n.id,n]));
document.getElementById('counts').textContent=NCOUNT+' 노드 · '+ECOUNT+' 엣지 · '+VERSION;
document.getElementById('ver').textContent=VERSION;

// ---- lifecycle pipeline ----
const lock='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><rect x="4.5" y="10.5" width="15" height="10" rx="2"/><path d="M8 10.5V7a4 4 0 0 1 8 0v3.5"/></svg>';
const loopIcon='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 11.5a8 8 0 0 0-14.3-4.6M4 4v3.5h3.5"/><path d="M4 12.5a8 8 0 0 0 14.3 4.6M20 20v-3.5h-3.5"/></svg>';
const flow=document.getElementById('flow');
LIFE.forEach(s=>{
  const d=document.createElement('div');
  d.className='stage'+(s.loop?' loop':'');
  d.innerHTML='<div class="st-id">'+s.id+'</div><div class="st-lb">'+s.lb+'</div>'+
    '<div class="st-out">'+s.out.map(o=>'<span class="chip">'+o+'</span>').join('')+'</div>'+
    (s.gate?'<div class="gate">'+lock+s.gate+'</div>':'');
  flow.appendChild(d);
});
const looper=LIFE.find(s=>s.loop);
if(looper){
  document.getElementById('loopnote').innerHTML='<span style="color:var(--accent);display:inline-flex;width:16px;height:16px">'+loopIcon+'</span>'+
    '<span><b>'+looper.id+' → 개발</b> 로 순환 — 환류가 다음 배치를 다시 개발 단계로 되돌린다.</span>';
}

// ---- dagre layout ----
const cs=getComputedStyle(document.documentElement);
function v(t){return cs.getPropertyValue(t).trim();}
const g=new dagre.graphlib.Graph({multigraph:true});
g.setGraph({rankdir:'LR',nodesep:22,ranksep:64,edgesep:14,marginx:18,marginy:18});
g.setDefaultEdgeLabel(()=>({}));
NODES.forEach(n=>g.setNode(n.id,{width:NW,height:NH}));
EDGES.forEach((e,i)=>{
  if(byId[e.f]&&byId[e.t]) g.setEdge(e.f,e.t,{weight:e.prim?4:1,minlen:1,data:e},'e'+i);
});
dagre.layout(g);
const gInfo=g.graph();

const NS='http://www.w3.org/2000/svg';
const svg=document.getElementById('graph');
const W=Math.ceil(gInfo.width)+36, H=Math.ceil(gInfo.height)+36;
svg.setAttribute('width',W); svg.setAttribute('height',H);
svg.setAttribute('viewBox','0 0 '+W+' '+H);

const defs=document.createElementNS(NS,'defs');
defs.innerHTML='<marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="context-stroke"/></marker>';
svg.appendChild(defs);
const eLayer=document.createElementNS(NS,'g');
const nLayer=document.createElementNS(NS,'g');
svg.appendChild(eLayer); svg.appendChild(nLayer);

function smoothPath(pts){
  if(pts.length<2) return '';
  let d='M'+pts[0].x.toFixed(1)+' '+pts[0].y.toFixed(1);
  for(let i=1;i<pts.length-1;i++){
    const xc=(pts[i].x+pts[i+1].x)/2, yc=(pts[i].y+pts[i+1].y)/2;
    d+=' Q'+pts[i].x.toFixed(1)+' '+pts[i].y.toFixed(1)+' '+xc.toFixed(1)+' '+yc.toFixed(1);
  }
  const last=pts[pts.length-1];
  d+=' L'+last.x.toFixed(1)+' '+last.y.toFixed(1);
  return d;
}
const edgeEls=[];
g.edges().forEach(eo=>{
  const ed=g.edge(eo); const e=ed.data;
  const path=document.createElementNS(NS,'path');
  path.setAttribute('d',smoothPath(ed.points));
  path.setAttribute('class','gedge');
  path.setAttribute('stroke', e.prim?v('--edge-strong'):v('--edge'));
  path.setAttribute('stroke-width', e.prim?'1.7':'1.2');
  if(!e.prim) path.setAttribute('stroke-dasharray','4 4');
  path.setAttribute('opacity', e.prim?'0.6':'0.4');
  path.setAttribute('marker-end','url(#ah)');
  eLayer.appendChild(path);
  edgeEls.push({el:path,f:e.f,t:e.t,prim:e.prim});
});

function truncate(s,n){return s.length>n?s.slice(0,n-1)+'…':s;}
const nodeEls={};
g.nodes().forEach(id=>{
  const n=byId[id]; if(!n) return;
  const nd=g.node(id);
  const x=nd.x-NW/2, y=nd.y-NH/2;
  const grp=document.createElementNS(NS,'g');
  grp.setAttribute('class','gnode');
  grp.setAttribute('transform','translate('+x.toFixed(1)+','+y.toFixed(1)+')');
  const c=CAT[n.cat];
  const rect=document.createElementNS(NS,'rect');
  rect.setAttribute('width',NW);rect.setAttribute('height',NH);rect.setAttribute('rx','8');
  rect.setAttribute('fill',v(c.bg));rect.setAttribute('stroke',v(c.bd));rect.setAttribute('stroke-width','1.5');
  const t1=document.createElementNS(NS,'text');
  t1.setAttribute('x',NW/2);t1.setAttribute('y',20);t1.setAttribute('text-anchor','middle');
  t1.setAttribute('fill',v(c.tx));t1.setAttribute('class','lbl');t1.textContent=truncate(n.lb,16);
  const t2=document.createElementNS(NS,'text');
  t2.setAttribute('x',NW/2);t2.setAttribute('y',34);t2.setAttribute('text-anchor','middle');
  t2.setAttribute('fill',v(c.tx));t2.setAttribute('class','path');t2.textContent=truncate(n.path,28);
  grp.appendChild(rect);grp.appendChild(t1);grp.appendChild(t2);
  grp.addEventListener('click',ev=>{ev.stopPropagation();select(id);});
  nLayer.appendChild(grp);
  nodeEls[id]=grp;
});

function select(id){
  const nb=new Set([id]);
  edgeEls.forEach(e=>{if(e.f===id||e.t===id){nb.add(e.f);nb.add(e.t);}});
  Object.keys(nodeEls).forEach(k=>nodeEls[k].classList.toggle('dim',!nb.has(k)));
  edgeEls.forEach(e=>{
    const on=(e.f===id||e.t===id);
    e.el.classList.toggle('dim-e',!on);
    e.el.setAttribute('opacity', on?'0.95':(e.prim?'0.6':'0.4'));
    e.el.setAttribute('stroke-width', on?(e.prim?'2.4':'2'):(e.prim?'1.7':'1.2'));
  });
  renderDetail(id);
}
function reset(){
  Object.keys(nodeEls).forEach(k=>nodeEls[k].classList.remove('dim'));
  edgeEls.forEach(e=>{e.el.classList.remove('dim-e');e.el.setAttribute('opacity',e.prim?'0.6':'0.4');e.el.setAttribute('stroke-width',e.prim?'1.7':'1.2');});
  document.getElementById('detail').innerHTML='<span class="ph">노드를 클릭하면 그 문서의 역할과 들어오고 나가는 연결을 보여줍니다.</span>';
}
svg.addEventListener('click',reset);

function renderDetail(id){
  const n=byId[id], c=CAT[n.cat];
  const outs=EDGES.filter(e=>e.f===id).map(e=>({node:byId[e.t],k:e.k,lb:e.lb}));
  const ins=EDGES.filter(e=>e.t===id).map(e=>({node:byId[e.f],k:e.k,lb:e.lb}));
  const li=o=>'<li><span class="k">'+o.k+(o.lb?' · '+o.lb:'')+'</span><b>'+(o.node?o.node.lb:'?')+'</b></li>';
  const outHtml=outs.length?outs.map(li).join(''):'<li class="none">없음 — 최종/말단 산출물</li>';
  const inHtml=ins.length?ins.map(li).join(''):'<li class="none">없음 — 사이클의 입력</li>';
  document.getElementById('detail').innerHTML=
    '<div class="d-head"><span class="d-cat" style="color:'+v(c.tx)+';border-color:'+v(c.bd)+';background:'+v(c.bg)+'">'+c.label+'</span>'+
    '<span class="d-title">'+n.lb+'</span></div>'+
    '<p class="d-path">'+n.path+'</p>'+
    '<p class="d-role">'+n.role+'</p>'+
    '<div class="d-conns"><div class="d-col"><h4>← 들어오는 연결 (input)</h4><ul>'+inHtml+'</ul></div>'+
    '<div class="d-col"><h4>나가는 연결 (output) →</h4><ul>'+outHtml+'</ul></div></div>';
}
const mo=new MutationObserver(()=>{
  Object.keys(nodeEls).forEach(id=>{const c=CAT[byId[id].cat],grp=nodeEls[id];
    grp.querySelector('rect').setAttribute('fill',v(c.bg));
    grp.querySelector('rect').setAttribute('stroke',v(c.bd));
    grp.querySelectorAll('text').forEach(t=>t.setAttribute('fill',v(c.tx)));});
  edgeEls.forEach(e=>e.el.setAttribute('stroke',e.prim?v('--edge-strong'):v('--edge')));
});
mo.observe(document.documentElement,{attributes:true,attributeFilter:['data-theme']});
</script>
"""


if __name__ == "__main__":
    raise SystemExit(main())
