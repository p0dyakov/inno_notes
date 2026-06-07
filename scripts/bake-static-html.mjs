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
const siteDir = path.resolve(
	process.env.QUARTO_PROJECT_OUTPUT_DIR || process.argv[2] || path.join(repoRoot, '_site'),
);

if (!fs.existsSync(siteDir)) {
	console.warn(`[bake-static-html] skip: output dir not found: ${siteDir}`);
	process.exit(0);
}

const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);
const tex = new TeX({ packages: AllPackages });
const chtml = new CHTML({
	fontURL: 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/output/chtml/fonts/woff-v2',
});
const mjDoc = mathjax.document('', { InputJax: tex, OutputJax: chtml });

const MATH_TAG_RE = /<(?:span|div)\b[^>]*\bclass=["'][^"']*\bmath(?:\s+(?:inline|display)|\b)[^"']*["'][^>]*>([\s\S]*?)<\/(?:span|div)>/gi;
const MATH_SCRIPT_RE = /<script\b[^>]*type=["']math\/tex[^"']*["'][^>]*>([\s\S]*?)<\/script>/gi;

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

const convertTex = (tex, display) => {
	const node = mjDoc.convert(tex, { display });
	return adaptor.outerHTML(node);
};

const bakeMathInHtml = (html) => {
	let mathCount = 0;
	const replaceMath = (full, inner, displayHint) => {
		if (full.includes('mjx-container')) return full;
		const { tex, display } = unwrapTex(inner, displayHint);
		if (!tex) return full;
		try {
			mathCount += 1;
			return convertTex(tex, display);
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

const stripRuntimeScripts = (html) => html
	.replace(/<script\b[^>]*\bsrc=["'][^"']*mathjax[^"']*["'][^>]*>\s*<\/script>\s*/gi, '')
	.replace(/<script\b[^>]*\bsrc=["'][^"']*quarto-diagram\/mermaid[^"']*["'][^>]*>\s*<\/script>\s*/gi, '')
	.replace(/<link\b[^>]*\bhref=["'][^"']*quarto-diagram\/mermaid\.css[^"']*["'][^>]*>\s*/gi, '');

const markBaked = (html) => (/\bdata-inn-baked=/.test(html)
	? html
	: html.replace(/<html\b/i, '<html data-inn-baked="true"'));

const htmlFiles = globSync('**/*.html', {
	cwd: siteDir,
	absolute: true,
	ignore: ['**/site_libs/**'],
});

let totalMath = 0;
let updated = 0;
let bakedCount = 0;

for (const filePath of htmlFiles) {
	const before = fs.readFileSync(filePath, 'utf8');
	const { html: baked, mathCount } = bakeMathInHtml(before);
	let after = stripRuntimeScripts(baked);
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
if (totalMath === 0 && bakedCount < htmlFiles.length * 0.5) {
	console.warn('[bake-static-html] run full `quarto render` once so all lessons are baked (preview alone only refreshes changed files)');
}
