// Kullanım: node render.js <timeline.json> <kare_dir> <cikti.mp4|--kareler t1,t2,...> [baslangic_kare] [bitis_kare]
// sahne.html'i Chromium'da açar, her kareyi render(t) ile çizer, JPEG olarak ffmpeg'e aktarır.
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const fs = require('fs'); const path = require('path');

(async () => {
  const [tlPath, kareDir, out, a0, a1] = process.argv.slice(2);
  const TL = JSON.parse(fs.readFileSync(tlPath, 'utf8'));
  const html = 'file://' + path.join(__dirname, 'sahne.html');
  const asset = 'file://' + path.resolve(__dirname, '..', 'assets');
  const browser = await chromium.launch({ args: ['--allow-file-access-from-files', '--disable-web-security'] });
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  page.on('pageerror', e => console.error('SAYFA HATASI:', e.message));
  await page.addInitScript(([tl, k, a]) => { window.__TL__ = tl; window.__KARE__ = k; window.__ASSET__ = a; },
    [TL, 'file://' + path.resolve(kareDir), asset]);
  await page.goto(html);
  await page.waitForFunction(() => window.__ready === true);
  await page.evaluate(() => document.fonts.ready);

  if (out === '--kareler') {  // önizleme kareleri
    for (const ts of a0.split(',')) {
      await page.evaluate(t => window.render(t), parseFloat(ts));
      await page.screenshot({ path: path.join(a1, `onizleme_${ts}.jpg`), type: 'jpeg', quality: 85 });
    }
    await browser.close(); return;
  }
  const fps = TL.fps, N = Math.ceil(TL.total * fps);
  const s = a0 ? parseInt(a0) : 0, e = a1 ? parseInt(a1) : N;
  const ff = spawn('ffmpeg', ['-v', 'error', '-y', '-f', 'image2pipe', '-framerate', String(fps), '-c:v', 'mjpeg', '-i', '-',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '16', '-pix_fmt', 'yuv420p', '-r', String(fps), out], { stdio: ['pipe', 'inherit', 'inherit'] });
  const t0 = Date.now();
  for (let f = s; f < e; f++) {
    await page.evaluate(t => window.render(t), f / fps);
    const buf = await page.screenshot({ type: 'jpeg', quality: 93 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if ((f - s) % 300 === 0) console.log(`[${s}-${e}] kare ${f} (${((Date.now() - t0) / 1000).toFixed(0)} sn)`);
  }
  ff.stdin.end(); await new Promise(r => ff.on('close', r));
  await browser.close();
})();
