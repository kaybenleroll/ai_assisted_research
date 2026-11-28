'use strict';
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const { pathToFileURL } = require('url');
const assert = require('assert').strict;

async function check(file, browser) {
  const isMathml = file.endsWith('.mathml.html');
  const mathml = isMathml ? file : file.replace(/(?:\.mathjax)?\.html$/, '.mathml.html');
  const rendererTarget = isMathml ? file.replace(/\.mathml\.html$/, '.mathjax.html') : mathml;
  const hasMathml = !isMathml && fs.existsSync(mathml);
  if (hasMathml) {
    const context = await browser.newContext({ javaScriptEnabled: false });
    try {
      const page = await context.newPage();
      page.setDefaultTimeout(5000);
      page.setDefaultNavigationTimeout(5000);
      await page.goto(pathToFileURL(file).href);
      const fallback = page.getByRole('link', { name: 'Read the MathML version' });
      assert(await fallback.isVisible(), 'MathML fallback is not visible');
      let reached = false;
      for (let i = 0; i < 300; i++) {
        await page.keyboard.press('Tab');
        if (await fallback.evaluate(el => el === document.activeElement)) { reached = true; break; }
      }
      assert(reached, 'MathML fallback was not reached by Tab');
      await page.keyboard.press('Enter');
      await page.waitForURL(url => url.pathname === pathToFileURL(mathml).pathname);
      assert(await page.locator('math').count() > 0, 'MathML destination contains no maths');
      console.log('  PASS JavaScript off: Tab and Enter to MathML');
    } finally { await context.close(); }
  } else console.log(isMathml
    ? '  SKIP JavaScript-off MathML fallback: selected output is already MathML'
    : '  SKIP JavaScript-off MathML fallback: no sibling MathML output');

  const page = await browser.newPage();
  page.setDefaultTimeout(5000);
  page.setDefaultNavigationTimeout(5000);
  try {
    await page.goto(pathToFileURL(file).href);
    await page.waitForSelector('#TOC.collapsible-ready', { timeout: 15000 });
    const nav = page.getByRole('navigation', { name: 'Table of contents' });
    const main = page.getByRole('main');
    assert.equal(await nav.count(), 1, 'named contents navigation missing');
    assert.equal(await main.count(), 1, 'main landmark missing');
    const skip = page.getByRole('link', { name: 'Skip to main content' });
    await page.keyboard.press('Tab');
    assert(await skip.evaluate(el => el === document.activeElement), 'skip link is not first focus');
    await page.keyboard.press('Enter');
    assert(await main.evaluate(el => el === document.activeElement), 'skip link did not focus main');
    await page.reload();
    await page.waitForSelector('#TOC.collapsible-ready', { timeout: 15000 });
    const toggle = nav.getByRole('button').first();
    await tabTo(page, toggle, 'contents toggle');
    const before = await toggle.getAttribute('aria-expanded');
    const id = await toggle.getAttribute('aria-controls');
    assert(id, 'contents toggle lacks aria-controls');
    const controlled = page.locator(`#${CSSescape(id)}`);
    assert.equal(await controlled.count(), 1, 'controlled list missing or duplicated');
    const wasHidden = await controlled.evaluate(el => el.hidden);
    assert.equal(before, String(!wasHidden), 'contents initial aria-expanded disagrees with visibility');
    await page.keyboard.press('Enter');
    const after = await toggle.getAttribute('aria-expanded');
    const hidden = await controlled.evaluate(el => el.hidden);
    assert.equal(after, String(!hidden), 'contents aria-expanded disagrees with visibility');
    assert.notEqual(after, before, 'contents aria-expanded did not change');
    assert.notEqual(hidden, wasHidden, 'contents list did not toggle');
    const link = nav.locator('a[href^="#"]').first();
    const href = await link.getAttribute('href');
    await tabTo(page, link, 'contents link');
    await page.keyboard.press('Enter');
    assert.equal(new URL(page.url()).hash, href, 'contents link did not navigate');
    assert(await page.evaluate(id => !!document.getElementById(id), decodeURIComponent(href.slice(1))), 'contents target missing');
    const tree = await page.locator('body').ariaSnapshot();
    assert(tree.includes('navigation "Table of contents"') && tree.includes('main'), 'landmarks absent from accessibility snapshot');
    console.log('  PASS JavaScript on: skip focus, landmarks, first contents toggle and link');
    if (!hasMathml && !file.endsWith('.mathml.html') && await page.locator('#math-mode-toggle').count()) {
      throw Error('renderer control exists but sibling MathML output is missing');
    }
    if (hasMathml || isMathml) {
      assert(fs.existsSync(rendererTarget), 'renderer destination is missing');
      await page.goto(pathToFileURL(file).href);
      await tabTo(page, page.locator('#math-mode-toggle'), 'renderer control');
      await page.keyboard.press('Enter');
      await page.waitForURL(url => url.pathname === pathToFileURL(rendererTarget).pathname);
      console.log(`  PASS renderer control: Tab and Enter to ${isMathml ? 'MathJax' : 'MathML'}`);
    } else console.log('  SKIP renderer control: no sibling MathML output');
  } finally { await page.close(); }
}
async function tabTo(page, target, label) {
  for (let i = 0; i < 300; i++) {
    await page.keyboard.press('Tab');
    if (await target.evaluate(el => el === document.activeElement)) return;
  }
  throw Error(`${label} was not reached by Tab`);
}
function CSSescape(id) { return id.replace(/[^a-zA-Z0-9_-]/g, c => `\\${c.codePointAt(0).toString(16)} `); }
(async () => {
  if (!process.argv.slice(2).length) throw Error('Select at least one repository-relative HTML output');
  const browser = await chromium.launch({ headless: true, args: ['--no-sandbox'] });
  let failures = 0;
  console.log(`Playwright ${require('playwright/package.json').version}; Chromium ${browser.version()}`);
  for (const arg of process.argv.slice(2)) {
    console.log(`CHECK ${arg}`);
    try { await check(path.resolve('/repo', arg), browser); }
    catch (error) { failures++; console.log(`  FAIL ${error.message}`); }
  }
  await browser.close();
  console.log(`Failures: ${failures}`);
  process.exitCode = failures ? 1 : 0;
})().catch(error => { console.error(error); process.exitCode = 1; });
