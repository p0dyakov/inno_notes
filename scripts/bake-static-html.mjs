#!/usr/bin/env node
/**
 * Post-render: bake MathJax CHTML into each page and remove client math/mermaid JS.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { globSync } from 'glob';
import { mathjax } from 'mathjax-full/js/mathjax.js';
import { TeX } from 'mathjax-full/js/input/tex.js';
import { CHTML } from 'mathjax-full/js/output/chtml.js';
import { liteAdaptor } from 'mathjax-full/js/adaptors/liteAdaptor.js';
import { RegisterHTMLHandler } from 'mathjax-full/js/handlers/html.js';
import { AllPackages } from 'mathjax-full/js/input/tex/AllPackages.js';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(__dirname, '..');
// Optional per-file mode: `node bake-static-html.mjs <a.html> [<b.html> ...]`
// (paths absolute or relative to the site dir). No args = whole site (legacy,
// where argv[2] may additionally be an output dir).
const rawArgs = process.argv.slice(2).filter((a) => a !== '--');
const fileArgs = rawArgs.filter((a) => a.toLowerCase().endsWith('.html'));
const perFileMode =
	fileArgs.length > 0 && fileArgs.length === rawArgs.filter((a) => !a.startsWith('-')).length;
const siteDir = path.resolve(
	process.env.QUARTO_PROJECT_OUTPUT_DIR ||
		(!perFileMode && process.argv[2] ? process.argv[2] : path.join(repoRoot, '_site')),
);

if (!fs.existsSync(siteDir)) {
	console.warn(`[bake-static-html] skip: output dir not found: ${siteDir}`);
	process.exit(0);
}

const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);

const MATHJAX_FONT_URL = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/output/chtml/fonts/woff-v2';

const createMjDoc = () => {
	const tex = new TeX({ packages: AllPackages });
	const chtml = new CHTML({ fontURL: MATHJAX_FONT_URL });
	const doc = mathjax.document('', { InputJax: tex, OutputJax: chtml });
	return { doc, chtml };
};

const MATH_TAG_RE = /<(?:span|div)\b[^>]*\bclass=["'][^"']*\bmath(?:\s+(?:inline|display)|\b)[^"']*["'][^>]*>([\s\S]*?)<\/(?:span|div)>/gi;
const MATH_SCRIPT_RE = /<script\b[^>]*type=["']math\/tex[^"']*["'][^>]*>([\s\S]*?)<\/script>/gi;
const SVG_MATH_RE = /<mjx-container\b[^>]*\bjax=["']SVG["'][^>]*>[\s\S]*?<\/mjx-container>/gi;

const decodeHtml = (value) => value
	.replace(/&lt;/g, '<')
	.replace(/&gt;/g, '>')
	.replace(/&amp;/g, '&')
	.replace(/&quot;/g, '"')
	.replace(/&#39;/g, "'");

const unwrapTex = (raw, displayHint) => {
	let tex = decodeHtml(String(raw || '').trim());
	if (!tex) return { tex: '', display: displayHint };
	if (tex.startsWith('\\(') && tex.endsWith('\\)')) {
		return { tex: tex.slice(2, -2).trim(), display: false };
	}
	if (tex.startsWith('\\[') && tex.endsWith('\\]')) {
		return { tex: tex.slice(2, -2).trim(), display: true };
	}
	if (tex.startsWith('$$') && tex.endsWith('$$')) {
		return { tex: tex.slice(2, -2).trim(), display: true };
	}
	if (tex.startsWith('$') && tex.endsWith('$') && !tex.startsWith('$$')) {
		return { tex: tex.slice(1, -1).trim(), display: false };
	}
	return { tex, display: displayHint };
};

// CHTML glyphs are rendered via mjx-c::before in the injected stylesheet.
// Text nodes inside mjx-c would duplicate those glyphs in the browser.
const stripMjxText = (html) => html.replace(
	/<mjx-c\b([^>]*)>[\s\S]*?<\/mjx-c>/gi,
	(full, attrs) => `<mjx-c${attrs}></mjx-c>`,
);

const patchChtmlLineHeight = (css) => css.replace(
	/mjx-container\[jax="CHTML"\]\s*\{\s*line-height:\s*0;?\s*\}/g,
	'mjx-container[jax="CHTML"] {\n  line-height: normal;\n}',
);

const convertTex = (mj, tex, display) => {
	const node = mj.doc.convert(tex, { display });
	return adaptor.outerHTML(node);
};

const bakeMathInHtml = (html, mj) => {
	let mathCount = 0;
	const replaceMath = (full, inner, displayHint) => {
		if (full.includes('mjx-container')) return full;
		const { tex, display } = unwrapTex(inner, displayHint);
		if (!tex) return full;
		try {
			mathCount += 1;
			return convertTex(mj, tex, display);
		} catch (err) {
			console.warn(`[bake-static-html] tex error: ${tex.slice(0, 80)}… (${err.message})`);
			return full;
		}
	};

	let out = html.replace(MATH_TAG_RE, (full, inner) => {
		const display = /\bdisplay\b/.test(full);
		return replaceMath(full, inner, display);
	});
	out = out.replace(MATH_SCRIPT_RE, (full, inner) => {
		const display = /mode=display/i.test(full);
		return replaceMath(full, inner, display);
	});
	return { html: out, mathCount };
};

const MERMAID_SVG_OPEN_RE = /<svg\b([^>]*\b(?:id=["']mermaid-figure-|class=["'][^"']*(?:flowchart|Diagram)[^"']*)[^>]*)>/gi;
const SVG_FONT_SPRITE_RE = /<svg\b[^>]*\bid=["']inn-mathjax-svg-fonts["'][^>]*>[\s\S]*?<\/svg>\s*/gi;

const siteRelativePrefix = (filePath) => {
	const relDir = path.relative(siteDir, path.dirname(filePath));
	if (!relDir || relDir === '.') return '';
	const depth = relDir.split(path.sep).filter(Boolean).length;
	return '../'.repeat(depth);
};

const injectHeadLink = (html, linkTag) => html.replace(/<\/head>/i, `  ${linkTag}\n</head>`);

const injectMathJaxStyles = (html, mj, mathCount) => {
	if (!html.includes('mjx-container')) return html;
	if (mathCount === 0 && html.includes('inn-mathjax-chtml-styles')) {
		return patchChtmlLineHeight(html);
	}
	let out = html
		.replace(/<style\b[^>]*\bid=["']inn-mathjax-chtml-styles["'][^>]*>[\s\S]*?<\/style>\s*/gi, '')
		.replace(/<link\b[^>]*\bhref=["'][^"']*chtml\.css[^"']*["'][^>]*>\s*/gi, '');
	const styleTag = patchChtmlLineHeight(
		adaptor.outerHTML(mj.chtml.styleSheet(mj.doc))
			.replace(/\bid=["']MJX-CHTML-styles["']/, 'id="inn-mathjax-chtml-styles"'),
	);
	return injectHeadLink(out, styleTag);
};

const injectMermaidCss = (html, filePath) => {
	if (!/\bid=["']mermaid-figure-|\bclass=["'][^"']*flowchart/.test(html)) return html;
	if (/<link\b[^>]*\bhref=["'][^"']*quarto-diagram\/mermaid\.css[^"']*["'][^>]*>/i.test(html)) {
		return html;
	}
	const href = `${siteRelativePrefix(filePath)}site_libs/quarto-diagram/mermaid.css`;
	return injectHeadLink(html, `<link rel="stylesheet" href="${href}">`);
};

const fixMermaidSvgOpenTag = (attrs) => {
	let fixed = attrs.replace(/\bviewbox=/gi, 'viewBox=');
	const viewBoxMatch = fixed.match(/\bviewBox=["']([^"']+)["']/i);
	if (!viewBoxMatch) return fixed;
	const parts = viewBoxMatch[1].trim().split(/\s+/).map(Number);
	if (parts.length !== 4 || parts.some((n) => Number.isNaN(n))) return fixed;
	fixed = fixed.replace(/\bwidth=["'][^"']*["']/gi, '');
	fixed = fixed.replace(/\bheight=["'][^"']*["']/gi, '');
	if (!/\bpreserveAspectRatio=/i.test(fixed)) {
		fixed += ' preserveAspectRatio="xMidYMid meet"';
	}
	const [, , vbW, vbH] = parts;
	// Keep Mermaid's natural size from viewBox; CSS max-width scales down on narrow viewports.
	return `${fixed} width="${vbW}" height="${vbH}"`;
};

const fixMermaidSvgs = (html) => html.replace(
	MERMAID_SVG_OPEN_RE,
	(full, attrs) => `<svg${fixMermaidSvgOpenTag(attrs)}>`,
);

const sanitizeMermaidForeignObjects = (html) => html.replace(
	/<foreignobject([^>]*)>([\s\S]*?)<\/foreignobject>/gi,
	(full, attrs, inner) => {
		const clean = inner
			.replace(/<\/?p>/gi, '')
			.replace(/<\/?ul>/gi, '')
			.replace(/<li>/gi, '<div>')
			.replace(/<\/li>/gi, '</div>');
		return `<foreignObject${attrs}>${clean}</foreignObject>`;
	},
);

const fixMermaidLayout = (html) => {
	let out = html.replace(/<p>::+[ \t]*<\/p>\s*/gi, '');
	out = out.replace(
		/(<div class="cell"[^>]*>\s*<div class="cell-output-display">(?:(?!<\/div>\s*<\/div>)[\s\S])*?<\/svg>[\s\S]*?<\/figure>\s*<\/div>)(?!\s*<\/div>\s*<\/div>)/gi,
		'$1\n</div>\n</div>\n',
	);
	return out;
};

const stripRuntimeScripts = (html) => html
	.replace(/<script\b[^>]*\bsrc=["'][^"']*mathjax[^"']*["'][^>]*>\s*<\/script>\s*/gi, '')
	.replace(/<script\b[^>]*\bsrc=["'][^"']*quarto-diagram\/mermaid[^"']*["'][^>]*>\s*<\/script>\s*/gi, '');

const TCS_PAGE_RE = /^semester-2\/Theoretical Computer Science\/\d+(\.ru)?\.html$/i;

// Pre-paint language redirect: runs synchronously in <head> before first
// paint. If the stored lecture-language preference points at the sibling
// (EN<->RU, TCS only), jump instantly via location.replace — no post-load
// SPA navigation, no progress-bar flash, no content swap after paint.
const LANG_REDIRECT_JS = `(function(){try{var p='en';try{p=localStorage.getItem('inn_lang_preference')==='ru'?'ru':'en';}catch(e){}var isRu=/\.ru\.html$/i.test(location.pathname);if((p==='ru')===isRu)return;var l=document.querySelector('link[rel="alternate"][hreflang="'+p+'"]');if(!l)return;var t=new URL(l.getAttribute('href'),location.href);if(t.pathname===location.pathname&&t.search===location.search)return;location.replace(t.href);}catch(e){}})();`;

const stripLangAlternates = (html) => html
	.replace(/<link\b[^>]*\bdata-inn-alternate=["']true["'][^>]*>\s*/gi, '')
	.replace(/<script\b[^>]*\bid=["']inn-lang-redirect["'][^>]*>[\s\S]*?<\/script>\s*/gi, '');

const injectLangAlternates = (html, filePath) => {
	const rel = path.relative(siteDir, filePath).split(path.sep).join('/');
	if (!TCS_PAGE_RE.test(rel)) return stripLangAlternates(html);
	const isRu = /\.ru\.html$/i.test(rel);
	const sibling = isRu ? rel.replace(/\.ru\.html$/i, '.html') : rel.replace(/\.html$/i, '.ru.html');
	if (!fs.existsSync(path.join(siteDir, sibling))) return stripLangAlternates(html);
	// Stable: never move already-injected tags (keeps re-bakes byte-identical).
	if (html.includes('data-inn-alternate="true"') && html.includes('id="inn-lang-redirect"')) return html;
	let out = stripLangAlternates(html);
	const siblingFile = sibling.split('/').pop();
	const tags = `<link rel="alternate" data-inn-alternate="true" hreflang="${isRu ? 'en' : 'ru'}" href="${siblingFile}">\n  <script id="inn-lang-redirect">${LANG_REDIRECT_JS}</script>`;
	return injectHeadLink(out, tags);
};

// Defer render-blocking classic scripts in <head>: our inline scripts only
// touch these libs behind guards (`window.bootstrap?.Collapse`) or on
// DOMContentLoaded (quarto init), which always runs after deferred scripts.
// Sync survivors: module scripts (deferred by default), async (gtag),
// inn-lang-redirect (must run pre-paint), inline code.
const DEFER_SCRIPT_SUBSTR = [
	'quarto-nav/quarto-nav.js',
	'quarto-nav/headroom.min.js',
	'clipboard/clipboard.min.js',
	'quarto-search/autocomplete.umd.js',
	'quarto-search/fuse.min.js',
	'quarto-search/quarto-search.js',
	'quarto-html/popper.min.js',
	'quarto-html/tippy.umd.min.js',
	'quarto-html/anchor.min.js',
	'bootstrap/bootstrap.min.js',
];
const deferHeadScripts = (html) => html.replace(
	/<script\b([^>]*\bsrc=["']([^"']+)["'][^>]*)>/gi,
	(full, attrs, src) => {
		if (/\bdefer\b/i.test(attrs) || /\basync\b/i.test(attrs) || /\btype=["']module["']/i.test(attrs)) return full;
		if (!DEFER_SCRIPT_SUBSTR.some((s) => src.includes(s))) return full;
		return `<script defer${attrs}>`;
	},
);

// Dead weight: es6 polyfill from cdnjs (render-blocking, third-party).
// The site already requires modern JS (`?.` in head scripts), MathJax
// runtime is stripped at bake, so nothing needs it.
const stripPolyfill = (html) => html.replace(
	/<script\b[^>]*\bsrc=["'][^"']*polyfill[^"']*["'][^>]*>\s*<\/script>\s*/gi,
	'',
);

// Warm up third-party connections discovered during parse. Idempotent.
const injectPreconnect = (html) => {
	let out = html;
	if (!out.includes('href="https://www.googletagmanager.com"')) {
		out = injectHeadLink(out, '<link rel="preconnect" href="https://www.googletagmanager.com">');
	}
	if (!out.includes('href="https://cdn.jsdelivr.net"')) {
		out = injectHeadLink(out, '<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>');
	}
	return out;
};

// Below-the-fold media must not compete with first paint. First <img> in
// document order stays eager; the rest lazy-load. Idempotent.
const lazyMedia = (html) => {
	let first = true;
	let out = html.replace(/<img\b[^>]*>/gi, (tag) => {
		if (/\bloading=/i.test(tag)) return tag;
		if (first) {
			first = false;
			return tag;
		}
		return tag.replace(/<img\b/i, '<img loading="lazy" decoding="async"');
	});
	out = out.replace(/<video\b([^>]*)>/gi, (full, attrs) => (
		/\bpreload=/i.test(attrs) ? full : `<video preload="none"${attrs}>`
	));
	return out;
};

// Videos are banned from pages (owner decision): strip any <video> block
// that slipped through (e.g. a regenerated article). Files stay in repo,
// nothing is fetched or rendered. Idempotent.
const stripVideos = (html) => html.replace(
	/<video\b[^>]*>[\s\S]*?<\/video\s*>/gi,
	'',
);

const markBaked = (html) => (/\bdata-inn-baked=/.test(html)
	? html
	: html.replace(/<html\b/i, '<html data-inn-baked="true"'));

const htmlFiles = perFileMode
	? fileArgs
			.map((f) => (path.isAbsolute(f) ? f : path.resolve(siteDir, f)))
			.filter((f) => fs.existsSync(f))
		: globSync('**/*.html', {
				cwd: siteDir,
				absolute: true,
				ignore: ['**/site_libs/**'],
			});

const WS_CHARS = [32, 9, 10, 13, 12].map((c) => String.fromCharCode(c));

const isSafeFigId = (id) => {
  if (!id || id.length > 64) return false;
  for (const ch of id) {
    const ok = (ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z') ||
      (ch >= '0' && ch <= '9') || ch === '-' || ch === '_';
    if (!ok) return false;
  }
  return true;
};

const svgAttr = (tag, name) => {
  const key = name + '="';
  const i = tag.indexOf(key);
  if (i < 0) return '';
  const j = tag.indexOf('"', i + key.length);
  return j < 0 ? '' : tag.slice(i + key.length, j);
};

const collapseWs = (s) => {
  const words = [];
  let cur = '';
  for (const ch of s) {
    if (WS_CHARS.includes(ch)) {
      if (cur) { words.push(cur); cur = ''; }
    } else {
      cur += ch;
    }
  }
  if (cur) words.push(cur);
  return words.join(' ');
};

const escAttr = (s) => s.split('&').join('&amp;').split('"').join('&quot;').split('<').join('&lt;');

const diagramAlt = (svg) => {
  const bits = [];
  const opens = ['<span', '<div', '<p>', '<tspan', '<text'];
  const closeFor = (o) => {
    if (o === '<span') return '</span>';
    if (o === '<div') return '</div>';
    if (o === '<p>') return '</p>';
    if (o === '<tspan') return '</tspan>';
    return '</text>';
  };
  let pos = 0;
  let guard = 0;
  while (guard++ < 80) {
    let best = -1;
    let bestTag = '';
    for (const o of opens) {
      const k = svg.indexOf(o, pos);
      if (k >= 0 && (best < 0 || k < best)) { best = k; bestTag = o; }
    }
    if (best < 0) break;
    const gt = svg.indexOf('>', best);
    if (gt < 0) break;
    const end = svg.indexOf(closeFor(bestTag), gt);
    if (end < 0) { pos = gt + 1; continue; }
    const inner = svg.slice(gt + 1, end);
    if (!inner.includes('<')) {
      const s = collapseWs(inner);
      if (s) bits.push(s);
      pos = end + 1;
      if (bits.length >= 12) break;
    } else {
      pos = gt + 1;
    }
  }
  let alt = bits.join(' | ');
  if (alt.length > 180) alt = alt.slice(0, 177) + '...';
  return escAttr(alt) || 'Diagram';
};

// Forced-darkening-proof diagrams. Browser auto-darkeners (Chrome "Auto Dark
// Mode for Web Contents" and kin) treat inline SVG fills as image (preserved)
// but rewrite HTML text inside <foreignObject> as page text (inverted): light
// boxes survive while labels flip to white — unreadable. An SVG loaded via
// <img> is one atomic image (preserved or inverted as a whole), readable
// either way. Vanilla rendering is pixel-identical: the same markup (styles
// included) travels into the .svg file. No mermaid interactions exist
// repo-wide (no `click` directives), so nothing is lost. Idempotent: re-runs
// find no inline mermaid svg and skip; stale diagram-*.svg files left by
// removed figures are purged per page (strict prefix, own dir only).
// Standalone .svg files are parsed as strict XML, but mermaid emits HTML-style
// void elements (<br>) inside <foreignObject> labels. Self-close them so the
// extracted file stays well-formed (inline HTML parsing tolerates <br>).
const closeVoidTags = (svg) => {
  const voids = ['br', 'hr', 'wbr', 'img', 'input', 'link', 'meta', 'source', 'col', 'base'];
  let out = svg;
  for (const v of voids) {
    let pos = 0;
    for (;;) {
      const s = out.indexOf('<' + v, pos);
      if (s < 0) break;
      const after = s + 1 + v.length;
      const c = out.charAt(after);
      if (c !== ' ' && c !== '>' && c !== '/') { pos = after; continue; }
      const e = out.indexOf('>', after);
      if (e < 0) break;
      if (out.charAt(e - 1) === '/') { pos = e + 1; continue; }
      out = out.slice(0, e) + '/' + out.slice(e);
      pos = e + 2;
    }
  }
  return out;
};

// In a standalone .svg file the HTML inside <foreignObject> needs an explicit
// XHTML namespace, otherwise the XML parser places <div>/<span> in the SVG
// namespace and labels silently vanish. Tag every <div> once (guard keeps
// re-bakes byte-identical).
const xmlnsHtmlDivs = (svg) => {
  const NS = 'http://www.w3.org/1999/xhtml';
  let out = svg;
  let pos = 0;
  for (;;) {
    const s = out.indexOf('<div', pos);
    if (s < 0) break;
    const e = out.indexOf('>', s);
    if (e < 0) break;
    if (!out.slice(s, e).includes(' xmlns=')) {
      out = out.slice(0, s + 4) + ' xmlns="' + NS + '"' + out.slice(s + 4);
      pos = e + NS.length + 9;
    } else {
      pos = e + 1;
    }
  }
  return out;
};

// Mermaid emits label HTML with leading/trailing newlines inside <div>/<span>
// ("<div>\n<span>\n\nText\n\n</span>\n</div>"). Label divs use
// white-space:break-spaces, so each stray newline becomes a real line box
// that pushes content out of the fixed-height foreignObject viewport:
// clipped (invisible) labels. Trim edge whitespace of label runs only;
// interior breaks (explicit <br/>, CJK wrapping) are intentional and stay.
const trimWs = (s) => {
  let a = 0;
  let b = s.length;
  while (a < b && WS_CHARS.includes(s[a])) a += 1;
  while (b > a && WS_CHARS.includes(s[b - 1])) b -= 1;
  return s.slice(a, b);
};

const trimTagEdges = (block, tag) => {
  let out = '';
  let pos = 0;
  const open = '<' + tag;
  const close = '</' + tag + '>';
  for (;;) {
    const s = block.indexOf(open, pos);
    if (s < 0) break;
    const gt = block.indexOf('>', s);
    if (gt < 0) break;
    const c = block.charAt(s + 1 + tag.length);
    if (c !== '>' && c !== '/' && !WS_CHARS.includes(c)) { out += block.slice(pos, gt + 1); pos = gt + 1; continue; }
    const e = block.indexOf(close, gt);
    if (e < 0) { out += block.slice(pos, gt + 1); pos = gt + 1; continue; }
    const inner = block.slice(gt + 1, e);
    const edge = inner.match(/^([ \t\n\r\f]*)([\s\S]*?)([ \t\n\r\f]*)$/);
    out += block.slice(pos, gt + 1) + (edge ? edge[2] : inner);
    pos = e;
  }
  return out + block.slice(pos);
};

const trimForeignLabelText = (html) => {
  let out = '';
  let pos = 0;
  for (;;) {
    const f = html.indexOf('<foreignObject', pos);
    if (f < 0) break;
    const fEnd = html.indexOf('</foreignObject>', f);
    if (fEnd < 0) break;
    out += html.slice(pos, f);
    let block = html.slice(f, fEnd + 16);
    block = trimTagEdges(block, 'span');
    block = trimTagEdges(block, 'div');
    out += block;
    pos = fEnd + 16;
  }
  return out + html.slice(pos);
};

const externalizeDiagrams = (html, filePath) => {
  let count = 0;
  const written = new Set();
  let out = '';
  let pos = 0;
  for (;;) {
    const s = html.indexOf('<svg', pos);
    if (s < 0) break;
    const tagEnd = html.indexOf('>', s);
    if (tagEnd < 0) break;
    const tag = html.slice(s, tagEnd + 1);
    const figId = svgAttr(tag, 'id');
    const close = html.indexOf('</svg>', s);
    if (!figId.startsWith('mermaid-figure-') || !isSafeFigId(figId) || close < 0) {
      out += html.slice(pos, tagEnd + 1);
      pos = tagEnd + 1;
      continue;
    }
    const svg = html.slice(s, close + 6);
    let w = Math.round(Number(svgAttr(tag, 'width')) || 0);
    let h = Math.round(Number(svgAttr(tag, 'height')) || 0);
    if ((!w || !h) && svgAttr(tag, 'viewBox')) {
      const vb = collapseWs(svgAttr(tag, 'viewBox')).split(' ');
      if (vb.length === 4) {
        w = Math.round(Number(vb[2]) || 0);
        h = Math.round(Number(vb[3]) || 0);
      }
    }
    if (!w || !h) { out += html.slice(pos, tagEnd + 1); pos = tagEnd + 1; continue; }
    const dir = path.dirname(filePath);
    const stem = path.basename(filePath, path.extname(filePath));
    const filesDir = path.join(dir, stem + '_files');
    const name = 'diagram-' + figId + '.svg';
    fs.mkdirSync(filesDir, { recursive: true });
    fs.writeFileSync(path.join(filesDir, name), '<?xml version="1.0" encoding="UTF-8"?>' + String.fromCharCode(10) + xmlnsHtmlDivs(closeVoidTags(svg)), 'utf8');
    written.add(name);
    count += 1;
    out += html.slice(pos, s) + '<img src="' + stem + '_files/' + name + '" class="img-fluid figure-img" role="img" width="' + w + '" height="' + h + '" alt="' + diagramAlt(svg) + '">';
    pos = close + 6;
  }
  out += html.slice(pos);
  // Reconcile against BOTH newly written files and <img> references that
  // survived from previous bakes. (Purging on `written` alone would delete
  // every diagram on re-runs, when nothing is rewritten but imgs remain.)
  const kept = new Set(written);
  const needle = '_files/diagram-';
  let q = 0;
  for (;;) {
    const k = out.indexOf(needle, q);
    if (k < 0) break;
    const end = out.indexOf('"', k);
    if (end < 0) break;
    kept.add(out.slice(k + 7, end));
    q = end + 1;
  }
  try {
    const dir = path.dirname(filePath);
    const stem = path.basename(filePath, path.extname(filePath));
    const filesDir = path.join(dir, stem + '_files');
    for (const f of fs.readdirSync(filesDir)) {
      if (f.startsWith('diagram-') && f.endsWith('.svg') && !kept.has(f)) {
        fs.unlinkSync(path.join(filesDir, f));
      }
    }
  } catch (err) { void err; }
  return { html: out, diagrams: count };
};


let totalMath = 0;
let totalDiagrams = 0;
let updated = 0;
let bakedCount = 0;
let staleSvg = 0;

for (const filePath of htmlFiles) {
	const before = fs.readFileSync(filePath, 'utf8');
	if (SVG_MATH_RE.test(before) && !MATH_TAG_RE.test(before) && !MATH_SCRIPT_RE.test(before)) {
		staleSvg += 1;
	}
	MATH_TAG_RE.lastIndex = 0;
	MATH_SCRIPT_RE.lastIndex = 0;
	SVG_MATH_RE.lastIndex = 0;

	// Lazy MathJax init: creating the CHTML document is expensive, skip it
	// for pages without TeX (pure string transforms below don't need it).
	MATH_TAG_RE.lastIndex = 0;
	MATH_SCRIPT_RE.lastIndex = 0;
	const mayNeedMj =
		MATH_TAG_RE.test(before) || MATH_SCRIPT_RE.test(before) || before.includes('mjx-container');
	MATH_TAG_RE.lastIndex = 0;
	MATH_SCRIPT_RE.lastIndex = 0;
	const mj = mayNeedMj ? createMjDoc() : null;
	const { html: baked, mathCount } = bakeMathInHtml(before, mj);
	let after = baked.replace(SVG_FONT_SPRITE_RE, '');
	if (mathCount > 0) {
		after = after.replace(SVG_MATH_RE, '');
	}
	after = stripMjxText(after);
	after = stripRuntimeScripts(after);
	after = injectMathJaxStyles(after, mj, mathCount);
	after = fixMermaidSvgs(after);
	after = sanitizeMermaidForeignObjects(after);
	after = trimForeignLabelText(after);
	after = fixMermaidLayout(after);
	const ext = externalizeDiagrams(after, filePath);
	after = ext.html;
	totalDiagrams += ext.diagrams;
	after = injectMermaidCss(after, filePath);
	after = injectLangAlternates(after, filePath);
	after = deferHeadScripts(after);
	after = stripPolyfill(after);
	after = injectPreconnect(after);
	after = lazyMedia(after);
	after = stripVideos(after);
	after = markBaked(after);
	if (/\bdata-inn-baked=/.test(after)) bakedCount += 1;
	if (after !== before) {
		fs.writeFileSync(filePath, after, 'utf8');
		updated += 1;
	}
	totalMath += mathCount;
}

console.log(
	`[bake-static-html] ${siteDir}: ${totalMath} math expressions baked this run, ${bakedCount}/${htmlFiles.length} pages static, ${totalDiagrams} diagrams externalized, ${updated} files written`,
);
if (staleSvg > 0) {
	console.warn(
		`[bake-static-html] ${staleSvg} pages still have legacy SVG math without TeX source — run \`quarto render\` to regenerate from .qmd`,
	);
}
if (totalMath === 0 && bakedCount < htmlFiles.length * 0.5) {
	console.warn('[bake-static-html] run full `quarto render` once so all lessons are baked (preview alone only refreshes changed files)');
}
