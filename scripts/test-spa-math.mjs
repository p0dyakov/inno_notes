#!/usr/bin/env node
/**
 * End-to-end test: SPA navigation + baked CHTML math on local _site.
 */
import { chromium } from "playwright";

const BASE = "http://127.0.0.1:8080";
const PAGE1 =
  "/semester-2/Analytical%20Geometry%20and%20Linear%20Algebra%20II/1.html";
const PAGE2 =
  "/semester-2/Analytical%20Geometry%20and%20Linear%20Algebra%20II/2.html";

const failures = [];

function fail(msg) {
  failures.push(msg);
  console.error("FAIL:", msg);
}

async function main() {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  // --- Page 1: math quality ---
  await page.goto(BASE + PAGE1, { waitUntil: "networkidle" });

  const baked = await page.getAttribute("html", "data-inn-baked");
  if (baked !== "true") fail(`Page 1 not baked (data-inn-baked=${baked})`);

  const navFn = await page.evaluate(() => typeof window.__innNavigateInternal);
  if (navFn !== "function")
    fail(`__innNavigateInternal is ${navFn}, expected function`);

  const mathStats = await page.evaluate(() => {
    const containers = document.querySelectorAll('mjx-container[jax="CHTML"]');
    let badGlyphs = 0;
    let goodGlyphs = 0;
    let displayCount = 0;
    const isStretchy = (el) => {
      const p = el.parentElement?.tagName;
      return p === "MJX-BEG" || p === "MJX-EXT" || p === "MJX-MID" || p === "MJX-END";
    };
    const isInvisibleGlyph = (el) =>
      /\bmjx-c(?:2061|200B|FEFF|20|A0)\b/.test(el.className);
    const hasGlyph = (el) => {
      const before = getComputedStyle(el, "::before").content;
      return before && before !== "none" && before !== '""' && before !== "normal";
    };
    containers.forEach((c) => {
      if (c.getAttribute("display") === "true") displayCount++;
      c.querySelectorAll("mjx-c").forEach((el) => {
        if (isStretchy(el) || isInvisibleGlyph(el)) return;
        if (!/\bmjx-c[0-9A-Fa-f]+\b/.test(el.className)) return;
        if (hasGlyph(el)) goodGlyphs++;
        else badGlyphs++;
      });
    });
    const styleEl = document.getElementById("inn-mathjax-chtml-styles");
    return {
      containers: containers.length,
      badGlyphs,
      goodGlyphs,
      displayCount,
      hasStyles: !!styleEl && styleEl.textContent.length > 1000,
      styleLen: styleEl?.textContent?.length ?? 0,
    };
  });

  console.log("Math stats page 1:", mathStats);
  if (mathStats.containers === 0) fail("No mjx-container on page 1");
  if (mathStats.badGlyphs > 0)
    fail(`${mathStats.badGlyphs} letter glyphs missing ::before content on page 1`);
  if (!mathStats.hasStyles) fail("Missing inn-mathjax-chtml-styles on page 1");
  if (mathStats.displayCount === 0) fail("No display math on page 1");

  const h1Before = await page.textContent("main h1");
  const urlBefore = page.url();

  // --- SPA click to page 2 ---
  const linkSelector = `a[href="${PAGE2}"]`;
  const linkExists = await page.locator(linkSelector).count();
  if (linkExists === 0) {
    // try relative href
    const alt = await page.locator('a[href*="Linear Algebra II/2.html"]').first();
    if ((await alt.count()) === 0) fail("Sidebar link to page 2 not found");
    else {
      await alt.click();
    }
  } else {
    await page.click(linkSelector);
  }

  await page.waitForTimeout(800);

  const urlAfter = page.url();
  const h1After = await page.textContent("main h1");

  if (urlAfter === urlBefore) fail(`URL unchanged after nav: ${urlBefore}`);
  if (h1After === h1Before) fail(`H1 unchanged after nav: ${h1Before}`);

  console.log("Nav:", { urlBefore, urlAfter, h1Before, h1After });

  const mathStats2 = await page.evaluate(() => {
    const containers = document.querySelectorAll('mjx-container[jax="CHTML"]');
    let badGlyphs = 0;
    const isStretchy = (el) => {
      const p = el.parentElement?.tagName;
      return p === "MJX-BEG" || p === "MJX-EXT" || p === "MJX-MID" || p === "MJX-END";
    };
    const isInvisibleGlyph = (el) =>
      /\bmjx-c(?:2061|200B|FEFF|20|A0)\b/.test(el.className);
    const hasGlyph = (el) => {
      const before = getComputedStyle(el, "::before").content;
      return before && before !== "none" && before !== '""' && before !== "normal";
    };
    containers.forEach((c) => {
      c.querySelectorAll("mjx-c").forEach((el) => {
        if (isStretchy(el) || isInvisibleGlyph(el)) return;
        if (!/\bmjx-c[0-9A-Fa-f]+\b/.test(el.className)) return;
        if (!hasGlyph(el)) badGlyphs++;
      });
    });
    const styleEl = document.getElementById("inn-mathjax-chtml-styles");
    return {
      containers: containers.length,
      badGlyphs,
      hasStyles: !!styleEl && styleEl.textContent.length > 1000,
    };
  });

  console.log("Math stats page 2:", mathStats2);
  if (mathStats2.containers === 0) fail("No mjx-container after SPA nav");
  if (mathStats2.badGlyphs > 0)
    fail(`${mathStats2.badGlyphs} letter glyphs missing ::before after SPA nav`);
  if (!mathStats2.hasStyles)
    fail("Missing inn-mathjax-chtml-styles after SPA nav");

  // --- popstate back ---
  await page.goBack({ waitUntil: "networkidle" });
  await page.waitForTimeout(300);
  const urlBack = page.url();
  if (!urlBack.includes("1.html")) fail(`goBack wrong URL: ${urlBack}`);

  // --- Mermaid page ---
  await page.goto(
    BASE + "/semester-2/Software%20Systems%20Analysis%20and%20Design/1.html",
    { waitUntil: "networkidle" },
  );
  const mermaid = await page.evaluate(() => {
    const svgs = document.querySelectorAll(
      ".mermaid svg, svg.flowchart, svg[id^='mermaid']",
    );
    const pre = document.querySelectorAll("pre code, pre.sourceCode");
    return { svgCount: svgs.length, codeBlocks: pre.length };
  });
  console.log("SSAD page:", mermaid);
  if (mermaid.svgCount === 0 && mermaid.codeBlocks === 0)
    fail("SSAD page has no mermaid SVGs or code blocks");

  await browser.close();

  if (failures.length) {
    console.error("\n===", failures.length, "FAILURE(S) ===");
    process.exit(1);
  }
  console.log("\n=== ALL TESTS PASSED ===");
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
