#!/usr/bin/env python3
"""s117_draw_the_map_page.py

What it does, in plain words: for log S117, draws the relationship map page for the owner from the map's data file
(results/S117 The Avida work against the semantics - relationship map.json). The data is put inside the page, so the
page fetches nothing. The page shows, in order: the question and its short answer with a bar of all 284 units by
verdict; "What does not work, and why" (the main breaks); the map (the semantics' groups on the left, Avida's things on
the right, lines marked by verdict with colour and line style; choosing a group or a line shows what it holds); the
same map as a list, always visible (the only form on a phone); and what Avida shows that the semantics has no word for.
Writes: plain words/117 How the Avida work and the semantics relate - the map.html

  python3 -B Semantics/tools/s117_draw_the_map_page.py

Written 1 October 2026 by the one Opus 5.5 agent of log S117.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, 'results', 'S117 The Avida work against the semantics - relationship map.json')
OUT = os.path.join(ROOT, 'plain words', '117 How the Avida work and the semantics relate - the map.html')

PAGE = r'''<title>Avida and the Semantics</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&family=Source+Serif+4:opsz,wght@8..60,600;8..60,700&family=JetBrains+Mono:wght@400;500&display=swap">
<style>
/* Layout: one reading column; the map spans wider; the semantics on the left, Avida on the right, lines between. */
:root {
  --bg: #f4f6f8; --surface: #ffffff; --ink: #1b2430; --muted: #556170; --rule: #d5dbe2; --accent: #2f3f8f;
  --exact: #1f7a5a; --part: #a46a00; --not: #b23a3a; --none: #6b7684;
  --exact-bg: #e3f2ec; --part-bg: #f8eed9; --not-bg: #f8e3e3; --none-bg: #e9edf1;
  --focus: #2f3f8f;
  --display: "Source Serif 4", Georgia, "Times New Roman", serif;
  --body: "Atkinson Hyperlegible", "Segoe UI", Helvetica, Arial, sans-serif;
  --mono: "JetBrains Mono", ui-monospace, "SFMono-Regular", Menlo, Consolas, monospace;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #11151b; --surface: #1a2029; --ink: #e6eaf0; --muted: #a2adbb; --rule: #2e3846; --accent: #9fb0ff;
    --exact: #4fc39a; --part: #e0a540; --not: #f07a7a; --none: #9aa5b3;
    --exact-bg: #17332a; --part-bg: #3a2c10; --not-bg: #3c1d1f; --none-bg: #252d38;
    --focus: #9fb0ff; color-scheme: dark;
  }
}
:root[data-theme="dark"] {
  --bg: #11151b; --surface: #1a2029; --ink: #e6eaf0; --muted: #a2adbb; --rule: #2e3846; --accent: #9fb0ff;
  --exact: #4fc39a; --part: #e0a540; --not: #f07a7a; --none: #9aa5b3;
  --exact-bg: #17332a; --part-bg: #3a2c10; --not-bg: #3c1d1f; --none-bg: #252d38;
  --focus: #9fb0ff; color-scheme: dark;
}
body { background: var(--bg); color: var(--ink); font-family: var(--body); font-size: 17px; line-height: 1.55; }
.wrap { max-width: 1060px; margin: 0 auto; padding-inline: 20px; padding-block: 28px 64px; display: grid; gap: 48px; }
.col { max-width: 46rem; }
h1, h2, h3 { font-family: var(--display); line-height: 1.2; text-wrap: balance; margin: 0; color: var(--ink); }
h1 { font-size: clamp(1.8rem, 4.2vw, 2.6rem); font-weight: 700; }
h2 { font-size: 1.6rem; font-weight: 700; }
h3 { font-size: 1.15rem; font-weight: 600; }
p { margin: 0; }
.eyebrow { font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; color: var(--muted); font-weight: 700; }
.lede { font-size: 1.12rem; }
.stack { display: grid; gap: 14px; }
.small { font-size: .92rem; color: var(--muted); }
a { color: var(--accent); }
:focus-visible { outline: 3px solid var(--focus); outline-offset: 2px; }

/* verdict marks: colour and a symbol, never colour alone */
.mark { display: inline-flex; align-items: center; gap: 6px; font-weight: 700; white-space: nowrap; border-radius: 4px; padding: 1px 8px; font-size: .86rem; }
.mark .sym { font-family: var(--mono); font-weight: 500; }
.v-exact { color: var(--exact); background: var(--exact-bg); }
.v-part { color: var(--part); background: var(--part-bg); }
.v-not { color: var(--not); background: var(--not-bg); }
.v-none { color: var(--none); background: var(--none-bg); }

.bar { display: flex; height: 28px; border-radius: 4px; overflow: hidden; border: 1px solid var(--rule); }
.bar span { display: block; height: 100%; }
.bar .b-exact { background: var(--exact); } .bar .b-part { background: repeating-linear-gradient(135deg, var(--part) 0 6px, var(--part-bg) 6px 9px); }
.bar .b-not { background: repeating-linear-gradient(90deg, var(--not) 0 3px, var(--not-bg) 3px 6px); } .bar .b-none { background: var(--none-bg); border-left: 1px solid var(--none); }
.barkey { display: flex; flex-wrap: wrap; gap: 8px 16px; font-size: .92rem; }
.num { font-variant-numeric: tabular-nums; }

/* breaks */
.breaks { display: grid; gap: 18px; }
.break { background: var(--surface); border: 1px solid var(--rule); border-radius: 6px; padding: 18px 20px; display: grid; gap: 12px; min-width: 0; }
.break header { display: flex; gap: 10px; align-items: baseline; }
.break .tag { font-family: var(--mono); font-size: .8rem; color: var(--muted); }
.rows { display: grid; grid-template-columns: 11rem minmax(0, 1fr); gap: 8px 18px; margin: 0; }
.rows dt { font-size: .8rem; text-transform: uppercase; letter-spacing: .06em; color: var(--muted); font-weight: 700; padding-top: 3px; }
.rows dd { margin: 0; min-width: 0; }
.rows dd.why { font-weight: 700; }
@media (max-width: 640px) { .rows { grid-template-columns: minmax(0, 1fr); gap: 2px; } .rows dd { margin-bottom: 8px; } }

/* the map */
.legend { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 10px 18px; }
.legend .item { display: grid; grid-template-columns: 56px minmax(0, 1fr); gap: 10px; align-items: start; font-size: .93rem; }
.legend svg { width: 56px; height: 20px; }
.mapbox { overflow-x: auto; border: 1px solid var(--rule); border-radius: 6px; background: var(--surface); }
#mapsvg { display: block; width: 100%; min-width: 760px; height: auto; }
#mapsvg text { font-family: var(--body); fill: var(--ink); }
#mapsvg .side { font-size: 12px; fill: var(--muted); letter-spacing: .08em; font-weight: 700; }
#mapsvg .box rect { fill: var(--bg); stroke: var(--rule); }
#mapsvg .node { cursor: pointer; }
#mapsvg .node:focus { outline: none; }
#mapsvg .node:focus rect, #mapsvg .node.sel rect { stroke: var(--focus); stroke-width: 2.5; }
#mapsvg .counts { font-family: var(--mono); font-size: 11px; }
#mapsvg .line { fill: none; stroke-linecap: round; transition: opacity .15s; }
#mapsvg .hit { fill: none; stroke: transparent; stroke-width: 14; cursor: pointer; pointer-events: stroke; }
#mapsvg .hit:focus { outline: none; }
#mapsvg.dim .line { opacity: .12; }
#mapsvg.dim .line.on { opacity: 1; }
.l-exact { stroke: var(--exact); }
.l-part { stroke: var(--part); stroke-dasharray: 9 6; }
.l-not { stroke: var(--not); stroke-dasharray: 1.5 6; }
.l-none { stroke: var(--none); stroke-dasharray: 12 4 2 4; }
.c-exact { fill: var(--exact); } .c-part { fill: var(--part); } .c-not { fill: var(--not); } .c-none { fill: var(--none); }
.panel { background: var(--surface); border: 1px solid var(--rule); border-radius: 6px; padding: 16px 18px; display: grid; gap: 10px; min-width: 0; }
.wide-only { display: grid; gap: 16px; }
.narrow-note { display: none; }
@media (max-width: 760px) { .wide-only { display: none; } .narrow-note { display: block; } }

/* the map as a list */
.groups { display: grid; gap: 22px; }
.group { display: grid; gap: 10px; padding-top: 14px; border-top: 1px solid var(--rule); min-width: 0; }
.group.sel { border-top: 3px solid var(--focus); }
.chips { display: flex; flex-wrap: wrap; gap: 6px; }
.rels { list-style: none; margin: 0; padding: 0; display: grid; gap: 12px; }
.rel { display: grid; grid-template-columns: auto minmax(0, 1fr); gap: 4px 12px; align-items: start; }
.rel .to { font-weight: 700; }
.rel .ex { color: var(--muted); font-size: .95rem; }
.rel .open { font-size: .85rem; color: var(--part); font-weight: 700; }
@media (max-width: 520px) { .rel { grid-template-columns: minmax(0, 1fr); } }
details { font-size: .9rem; }
details summary { cursor: pointer; color: var(--accent); }
details .tech { display: grid; gap: 6px; margin-top: 8px; padding-left: 12px; border-left: 2px solid var(--rule); }
.mono { font-family: var(--mono); font-size: .82rem; }
.tech .u { overflow-wrap: anywhere; }
.reverse { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px 24px; }
.reverse div { display: grid; gap: 4px; min-width: 0; }
footer.notes { border-top: 1px solid var(--rule); padding-top: 18px; display: grid; gap: 8px; }
@media (prefers-reduced-motion: reduce) { #mapsvg .line { transition: none; } }
</style>

<div class="wrap">
  <header class="stack col">
    <p class="eyebrow">The Avida work against the semantics &middot; 1 October 2026</p>
    <h1>Does the Avida work line up with the semantics?</h1>
    <p class="lede">In part. Where the semantics describes things, their parts, changes and selection, Avida lines up with it, often exactly and with numbers to show it. Where the semantics describes explanation as something done (problems, arguments, criticism, building something new), Avida has nothing. And at the one point where the two meet, whether an evolved program counts as standing for its task, the semantics' own answer depends on a reading it has not yet made.</p>
    <div class="stack" aria-label="All 284 pieces of the semantics, by verdict">
      <div class="bar" id="bar"></div>
      <div class="barkey" id="barkey"></div>
      <p class="small">Each of the semantics' 284 pieces (its definitions, its claims and its named terms) was lined up with the Avida work. Of the pieces with nothing in Avida, 31 are the text's own worked examples and 18 are about the text's own wording; they say nothing about Avida either way.</p>
    </div>
  </header>

  <section class="stack" aria-labelledby="h-breaks">
    <div class="stack col">
      <h2 id="h-breaks">What does not work, and why</h2>
      <p>Eight places where the semantics and the Avida work part ways. Each gives the semantics' piece in plain words, what in Avida sits in its place, what happens, why it breaks, and one example.</p>
    </div>
    <div class="breaks" id="breaks"></div>
  </section>

  <section class="stack" aria-labelledby="h-map">
    <div class="stack col">
      <h2 id="h-map">The map</h2>
      <p>The semantics' fifteen groups of pieces are on the left, the things of the Avida work on the right. Each line joins a group to an Avida thing, or to "Nothing in Avida". A thicker line carries more pieces. Choose a group or a line to see what it holds; the same map is written out in full below.</p>
    </div>
    <div class="legend" id="legend"></div>
    <p class="narrow-note small">On a narrow screen the map is shown as the list below.</p>
    <div class="wide-only">
      <div class="mapbox"><svg id="mapsvg" role="group" aria-label="Map of the semantics' groups and the Avida things"></svg></div>
      <div class="panel" id="panel" aria-live="polite"><p class="small">Choose a group on the left, or a line, to see its pieces and why each lines up or not.</p></div>
    </div>
  </section>

  <section class="stack" aria-labelledby="h-list">
    <div class="stack col">
      <h2 id="h-list">The map in words</h2>
      <p>Every group, every line from it, and the plain reason for each. The technical references are inside "The pieces and references" under each group.</p>
    </div>
    <div class="groups" id="groups"></div>
  </section>

  <section class="stack" aria-labelledby="h-rev">
    <div class="stack col">
      <h2 id="h-rev">What Avida shows that the semantics has no word for</h2>
      <p>The other direction: things the Avida work found that no part of the semantics names. Three of them are your three properties of knowledge.</p>
    </div>
    <div class="reverse" id="reverse"></div>
  </section>

  <footer class="notes col small">
    <p><strong>How this was made.</strong> One Claude agent lined up each of the 284 pieces after writing down, before starting, how each would be judged. Where it could, it computed: on the Avida studies' own records, in Avida itself on saved program populations, and in a copy of the semantics' own program. No outside model checked it, as you asked. Nothing in the semantics was changed.</p>
    <p><strong>The open reading.</strong> <span id="readingA"></span> <span id="readingB"></span></p>
  </footer>
</div>

<script type="application/json" id="mapdata">__DATA__</script>
<script>
(function () {
  var M = JSON.parse(document.getElementById('mapdata').textContent);
  var V = {
    'LINES UP EXACTLY': { k: 'exact', sym: '=', label: 'Lines up exactly' },
    'LINES UP IN PART': { k: 'part', sym: '≈', label: 'Lines up in part' },
    'DOES NOT LINE UP': { k: 'not', sym: '≠', label: 'Does not line up' },
    'NOTHING IN AVIDA': { k: 'none', sym: '∅', label: 'Nothing in Avida' }
  };
  var ORDER = ['LINES UP EXACTLY', 'LINES UP IN PART', 'DOES NOT LINE UP', 'NOTHING IN AVIDA'];
  function h(tag, attrs, kids) {
    var e = document.createElement(tag);
    if (attrs) for (var a in attrs) { if (a === 'class') e.className = attrs[a]; else e.setAttribute(a, attrs[a]); }
    (kids || []).forEach(function (c) { if (c == null) return; e.appendChild(typeof c === 'string' ? document.createTextNode(c) : c); });
    return e;
  }
  var SVGNS = 'http://www.w3.org/2000/svg';
  function s(tag, attrs, kids) {
    var e = document.createElementNS(SVGNS, tag);
    for (var a in attrs) e.setAttribute(a, attrs[a]);
    (kids || []).forEach(function (c) { e.appendChild(typeof c === 'string' ? document.createTextNode(c) : c); });
    return e;
  }
  function mark(v, text) {
    var d = V[v];
    return h('span', { 'class': 'mark v-' + d.k }, [h('span', { 'class': 'sym', 'aria-hidden': 'true' }, [d.sym]), text || d.label]);
  }
  var G = {}; M.groups.forEach(function (g) { G[g.id] = g; });
  var A = {}; M.avida_things.forEach(function (a) { A[a.id] = a; });
  var R = {}; M.relations.forEach(function (r) { R[r.id] = r; });

  // the bar
  var total = 0; ORDER.forEach(function (v) { total += M.counts_by_verdict[v]; });
  var bar = document.getElementById('bar'), key = document.getElementById('barkey');
  ORDER.forEach(function (v) {
    var n = M.counts_by_verdict[v];
    bar.appendChild(h('span', { 'class': 'b-' + V[v].k, style: 'width:' + (100 * n / total) + '%', title: V[v].label + ': ' + n }));
    key.appendChild(h('span', null, [mark(v), ' ', h('span', { 'class': 'num' }, [String(n)])]));
  });

  // the breaks
  var bx = document.getElementById('breaks');
  M.main_breaks.forEach(function (b, i) {
    var rows = h('dl', { 'class': 'rows' }, [
      h('dt', null, ["The semantics' piece"]), h('dd', null, [b.semantics]),
      h('dt', null, ['In Avida']), h('dd', null, [b.avida]),
      h('dt', null, ['What happens']), h('dd', null, [b.happens]),
      h('dt', null, ['Why it breaks']), h('dd', { 'class': 'why' }, [b.why]),
      h('dt', null, ['Example']), h('dd', null, [b.example])
    ]);
    var tech = h('details', null, [h('summary', null, ['References']), h('div', { 'class': 'tech' }, [
      h('p', { 'class': 'mono u' }, ['Parts: ' + b.units.join(', ')]), h('p', { 'class': 'mono u' }, [b.refs])])]);
    bx.appendChild(h('article', { 'class': 'break' }, [h('header', null, [h('span', { 'class': 'tag' }, [String(i + 1)]), h('h3', null, [b.title])]), rows, tech]));
  });

  // legend
  var lg = document.getElementById('legend');
  M.verdicts.forEach(function (v) {
    var d = V[v.verdict];
    var sv = s('svg', { viewBox: '0 0 56 20', 'aria-hidden': 'true' }, [s('path', { d: 'M4 10 H52', 'class': 'line l-' + d.k, 'stroke-width': 3 })]);
    lg.appendChild(h('div', { 'class': 'item' }, [sv, h('div', null, [mark(v.verdict), ' ', v.meaning])]));
  });

  // the map
  var svg = document.getElementById('mapsvg');
  var W = 1000, top = 46, rowH = 44, boxW = 300, boxH = 34;
  // order the Avida things by the average position of the groups that join them (Nothing last)
  var bary = {};
  M.lines.forEach(function (l) {
    var gi = M.groups.findIndex(function (g) { return g.id === l.from_group; });
    var b = bary[l.to] || (bary[l.to] = { s: 0, n: 0 });
    b.s += gi * l.units; b.n += l.units;
  });
  var av = M.avida_things.slice().sort(function (a, b) {
    if (a.id === 'AV00') return 1; if (b.id === 'AV00') return -1;
    return bary[a.id].s / bary[a.id].n - bary[b.id].s / bary[b.id].n;
  });
  var rows = Math.max(M.groups.length, av.length);
  var H = top + rows * rowH + 10;
  svg.setAttribute('viewBox', '0 0 ' + W + ' ' + H);
  svg.appendChild(s('text', { x: 8, y: 24, 'class': 'side' }, ['THE SEMANTICS']));
  svg.appendChild(s('text', { x: W - 8, y: 24, 'class': 'side', 'text-anchor': 'end' }, ['THE AVIDA WORK']));
  var gy = {}, ay = {};
  M.groups.forEach(function (g, i) { gy[g.id] = top + i * rowH + boxH / 2; });
  var aStep = (rows * rowH) / av.length;
  av.forEach(function (a, i) { ay[a.id] = top + i * aStep + boxH / 2; });
  var lineLayer = s('g', {}), hitLayer = s('g', {}), nodeLayer = s('g', {});
  svg.appendChild(lineLayer); svg.appendChild(hitLayer); svg.appendChild(nodeLayer);
  var pairCount = {};
  M.lines.forEach(function (l) { var k = l.from_group + l.to; pairCount[k] = (pairCount[k] || 0) + 1; });
  var pairSeen = {};
  var lineEls = [];
  M.lines.forEach(function (l, i) {
    var k = l.from_group + l.to; var j = pairSeen[k] = (pairSeen[k] || 0) + 1; var off = (j - (pairCount[k] + 1) / 2) * 7;
    var x1 = 8 + boxW, y1 = gy[l.from_group] + off, x2 = W - 8 - boxW, y2 = ay[l.to] + off;
    var d = 'M' + x1 + ' ' + y1 + ' C' + (x1 + 150) + ' ' + y1 + ' ' + (x2 - 150) + ' ' + y2 + ' ' + x2 + ' ' + y2;
    var vk = V[l.verdict].k;
    var p = s('path', { d: d, 'class': 'line l-' + vk, 'stroke-width': (1.4 + Math.sqrt(l.units) * 0.9).toFixed(2) });
    lineLayer.appendChild(p);
    var label = G[l.from_group].name + ' to ' + A[l.to].name + ': ' + V[l.verdict].label + ', ' + l.units + (l.units === 1 ? ' piece' : ' pieces');
    var hp = s('path', { d: d, 'class': 'hit', tabindex: '0', role: 'button', 'aria-label': label }, [s('title', {}, [label])]);
    hitLayer.appendChild(hp);
    lineEls.push({ l: l, p: p });
    function act() { showLine(l, p); }
    hp.addEventListener('click', act);
    hp.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); act(); } });
  });
  function wrapText(t, n) { var w = t.split(' '), out = [], cur = ''; w.forEach(function (x) { if ((cur + ' ' + x).trim().length > n) { out.push(cur.trim()); cur = x; } else cur += ' ' + x; }); if (cur.trim()) out.push(cur.trim()); return out; }
  function nodeBox(x, y, label, sub, anchorRight) {
    var g = s('g', { 'class': 'box node', tabindex: '0', role: 'button' });
    g.appendChild(s('rect', { x: x, y: y - boxH / 2, width: boxW, height: boxH, rx: 4 }));
    var lines = wrapText(label, 44).slice(0, 2);
    var tx = anchorRight ? x + boxW - 10 : x + 10;
    var anchor = anchorRight ? 'end' : 'start';
    var fs = lines.length > 1 ? 11.5 : 13;
    lines.forEach(function (ln, i) { g.appendChild(s('text', { x: tx, y: y - (lines.length - 1) * 6.5 + i * 13 + 4, 'font-size': fs, 'text-anchor': anchor }, [ln])); });
    return g;
  }
  M.groups.forEach(function (g) {
    var y = gy[g.id];
    var node = nodeBox(8, y, g.name, null, false);
    node.setAttribute('aria-label', g.name + ': ' + ORDER.map(function (v) { return g.counts[v] + ' ' + V[v].label.toLowerCase(); }).join(', '));
    nodeLayer.appendChild(node);
    g._node = node;
    node.addEventListener('click', function () { showGroup(g); });
    node.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); showGroup(g); } });
  });
  av.forEach(function (a) {
    var node = nodeBox(W - 8 - boxW, ay[a.id], a.name, null, true);
    node.setAttribute('aria-label', a.name);
    nodeLayer.appendChild(node);
    node.addEventListener('click', function () { showThing(a, node); });
    node.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); showThing(a, node); } });
  });
  var panel = document.getElementById('panel');
  function clearSel() {
    svg.classList.add('dim');
    lineEls.forEach(function (x) { x.p.classList.remove('on'); });
    nodeLayer.querySelectorAll('.sel').forEach(function (n) { n.classList.remove('sel'); });
    document.querySelectorAll('.group.sel').forEach(function (n) { n.classList.remove('sel'); });
  }
  function relItem(r, showFrom) {
    var head = h('div', null, [mark(r.verdict)]);
    var body = h('div', { 'class': 'stack', style: 'gap:4px' }, [
      h('p', { 'class': 'to' }, [(showFrom ? G[r.from_group].name + ' → ' : '') + A[r.to].name + ' (' + r.units.length + (r.units.length === 1 ? ' piece)' : ' pieces)')]),
      h('p', null, [r.why || r.what_matches]),
      r.example ? h('p', { 'class': 'ex' }, ['Example: ' + r.example]) : null,
      r.turns_on_a_reading ? h('p', { 'class': 'open' }, ["The semantics' answer here flips on the open reading described at the foot of the page."]) : null
    ]);
    return h('li', { 'class': 'rel' }, [head, body]);
  }
  function fill(title, sub, rels, showFrom) {
    panel.textContent = '';
    panel.appendChild(h('h3', null, [title]));
    if (sub) panel.appendChild(h('p', { 'class': 'small' }, [sub]));
    panel.appendChild(h('ul', { 'class': 'rels' }, rels.map(function (r) { return relItem(r, showFrom); })));
  }
  function showGroup(g) {
    clearSel(); g._node.classList.add('sel');
    lineEls.forEach(function (x) { if (x.l.from_group === g.id) x.p.classList.add('on'); });
    var card = document.getElementById('grp-' + g.id); if (card) card.classList.add('sel');
    fill(g.name, g.plain, M.relations.filter(function (r) { return r.from_group === g.id; }), false);
  }
  function showLine(l, p) {
    clearSel(); p.classList.add('on');
    fill(G[l.from_group].name + ' → ' + A[l.to].name, null, l.relations.map(function (id) { return R[id]; }), false);
  }
  function showThing(a, node) {
    clearSel(); node.classList.add('sel');
    lineEls.forEach(function (x) { if (x.l.to === a.id) x.p.classList.add('on'); });
    fill(a.name, a.plain, M.relations.filter(function (r) { return r.to === a.id; }), true);
  }

  // the map in words
  var gl = document.getElementById('groups');
  M.groups.forEach(function (g) {
    var chips = h('div', { 'class': 'chips' }, ORDER.filter(function (v) { return g.counts[v] > 0; }).map(function (v) { return mark(v, V[v].label + ': ' + g.counts[v]); }));
    var rels = M.relations.filter(function (r) { return r.from_group === g.id; });
    var techKids = [];
    rels.forEach(function (r) {
      techKids.push(h('p', { 'class': 'mono u' }, [V[r.verdict].sym + ' ' + r.technical.units.map(function (u) {
        var w = u.formal_core_line ? ' (core line ' + u.formal_core_line + ')' : (u.claims_md_line ? ' (claims line ' + u.claims_md_line + ')' : '');
        var tl = u.text_lines && u.text_lines.length ? ' [text ' + u.text_lines.slice(0, 3).map(function (t) { return 'L' + t; }).join(', ') + ']' : '';
        return u.id + ' ' + u.name + w + tl;
      }).join('; ')]));
      techKids.push(h('p', { 'class': 'u' }, ['Evidence: ' + r.technical.evidence + (r.technical.alternatives_considered ? ' Alternatives considered: ' + r.technical.alternatives_considered : '')]));
    });
    gl.appendChild(h('article', { 'class': 'group', id: 'grp-' + g.id }, [
      h('h3', null, [g.name]), h('p', null, [g.plain]), chips,
      h('ul', { 'class': 'rels' }, rels.map(function (r) { return relItem(r, false); })),
      h('details', null, [h('summary', null, ['The pieces and references']), h('div', { 'class': 'tech' }, techKids)])
    ]));
  });

  // reverse list
  var rv = document.getElementById('reverse');
  M.reverse_list.forEach(function (r) { rv.appendChild(h('div', null, [h('h3', null, [r.name]), h('p', null, [r.what])])); });
  document.getElementById('readingA').textContent = 'Reading A: ' + M.readings.A;
  document.getElementById('readingB').textContent = 'Reading B: ' + M.readings.B + ' The text does not say which; which to take is yours.';
})();
</script>
'''


def main():
    data = json.load(open(DATA, encoding='utf-8'))
    for r in data['relations']:
        for u in r['technical']['units']:
            u.pop('note', None)
    js = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    open(OUT, 'w', encoding='utf-8').write(PAGE.replace('__DATA__', js))
    print(OUT, os.path.getsize(OUT))


if __name__ == '__main__':
    main()
