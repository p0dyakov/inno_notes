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

let totalMath = 0;
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
	after = fixMermaidLayout(after);
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
	`[bake-static-html] ${siteDir}: ${totalMath} math expressions baked this run, ${bakedCount}/${htmlFiles.length} pages static, ${updated} files written`,
);
if (staleSvg > 0) {
	console.warn(
		`[bake-static-html] ${staleSvg} pages still have legacy SVG math without TeX source — run \`quarto render\` to regenerate from .qmd`,
	);
}
if (totalMath === 0 && bakedCount < htmlFiles.length * 0.5) {
	console.warn('[bake-static-html] run full `quarto render` once so all lessons are baked (preview alone only refreshes changed files)');
}
