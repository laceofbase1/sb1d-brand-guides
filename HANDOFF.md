# Smarter by 1 Degree — Brand System & Toolkit · HANDOFF

_Last updated: 29 June 2026_

This repo is a set of self-contained HTML pages (no build step) hosted on **GitHub Pages**. It holds four brand-direction guides, the chosen direction developed into a full system, a downloadable brand kit, a logo page, and an ambassador toolkit with an in-browser editor.

## Live links (public)
Base: **https://laceofbase1.github.io/sb1d-brand-guides/**

| Page | URL | What it is |
|---|---|---|
| Index | `/index.html` | Overview of 4 directions + banners to kit, logo, ambassador |
| 01 Cornerstone | `/01-cornerstone.html` | Current navy identity, documented |
| 02 Momentum ⭐ | `/02-momentum.html` | **CHOSEN direction** — full brand system + downloadable PDF |
| 03 The Better Way | `/03-better-way.html` | New direction concept (editorial) |
| 04 A Degree Ahead | `/04-one-degree.html` | New direction concept (premium) |
| 05 Brand kit | `/05-social.html` | Social templates (editable) + Logos + Icons downloads |
| 06 Logo | `/06-logo.html` | Logo assessment, refined-cap proposal, kit downloads |
| 07 Ambassador toolkit | `/07-ambassador.html` | "Smarter Together" — editable, downloadable posts for ambassadors |

## The chosen brand: "Momentum"
Lacey picked **Momentum**: the existing navy identity, kept, plus energy.
- **Colors:** Degree Navy `#1F497D` (primary) · Signal Azure `#2B86DB`/`oklch(0.64 0.155 244)` (action/motion, ~10% max) · Midnight/Deep Navy grounds · tinted-neutral grays. **No gold** (the old look used gold; we replaced it with azure).
- **Type:** **Archivo** (700–900) for display/headlines · **Hanken Grotesk** (400–700) for body.
- **Motif:** forward → arrow; navy→azure progress bars; motion always moves forward, eases out (`cubic-bezier(.16,1,.3,1)`), never bounces.
- **Voice:** confident, warm, forward. "Work smarter, get a degree ahead." Never fear-based or jargon.
- **Logo:** the real S+1 graduation mark. Always on white/light or on a **white chip** over dark. Never recolored/redrawn.

## Assets (`/assets/`)
- **Logo:** `sb1d-icon.(png|svg|pdf)`, `sb1d-icon-refined.(svg|pdf)` (deep-navy cap), `sb1d-logo-horizontal.(png|svg|pdf)`, `refine-onecolor.png` (1-color navy), `refine-reverse.png` (white), `sb1d-logo-kit.zip`. **SVG/PDF are true vector** (auto-traced).
- **Favicons:** `assets/favicon/` (16/32/180/192/512 png + `favicon.ico` + zip).
- **Icons:** `assets/icons/` — 6 line icons (degree, time-saved, debt-free, mastery, advised, forward) as SVG+PNG navy; `white/` subfolder; `sb1d-icons.zip`, `sb1d-icons-white.zip`.
- **Photos:** `assets/photos/students-1..3.jpg` (Unsplash, hosted locally — do NOT re-hotlink). **Stock placeholders** — swap for real SB1D student photos when available.
- **Social PNGs:** `assets/social/` (10 + zip).
- **Ambassador PNGs:** `assets/ambassador/` (23 + `sb1d-ambassador-templates.zip`).
- **Guide PDF:** `assets/sb1d-momentum-brand-guide.pdf`.

## How the in-browser editor works (05 + 07)
Templates are HTML (`.post`) sized with **CSS container queries (cqw units)**. Each carries `data-name`, `data-w`, `data-h`. Two modes:
- **Editor:** "✎ Edit & download" opens a modal, moves the `.post` in, makes text `contenteditable`, allows photo swap, then **html-to-image** (CDN) exports a PNG at native size (clones to an off-screen `data-w`×`data-h` stage so cqw computes at full res). `getFontEmbedCSS` embeds fonts.
- **`?only=N`** isolates the Nth template full-viewport — used to pre-render the static PNGs via headless Chrome.

## How to update & redeploy
1. Edit files in `~/Documents/Claude/sb1d-brand-guides/`.
2. Preview locally: `python3 -m http.server 4178` (or `serve.py`) → http://localhost:4178/
3. To re-render template PNGs: headless Chrome `--screenshot` against `?only=N` at the template's `data-w,data-h` (see git history commands).
4. `git add -A && git commit && git push origin main`. GitHub Pages rebuilds in ~1–4 min.
5. **Browser caches HTML for 10 min** — hard-refresh (`Cmd+Shift+R`) or use incognito to see changes immediately.

## Gotchas (learned)
- **Public repo:** the Claude auto-mode classifier blocks creating/flipping a repo to public — Lacey must explicitly authorize each time.
- **zsh arrays are 1-indexed** — a `names[$((n-1))]` loop misaligns filenames; use explicit mapping.
- **Don't hotlink Unsplash** — host photos locally (CDN/referrer/CORS broke on the live site). Photos with `crossorigin` need the attribute set in HTML before load for canvas export.
- **Logo vector tracing:** pure-python `potracer` (`pip install potracer`, imports as `potrace`). Pass a **boolean** mask (uint8 0/1 mis-thresholds), **invert** it (`~mask`, potracer fills the False region), navy mask = blue-dominant `B-R>18` to drop drop-shadows. Emit `fill-rule:evenodd`.

## Honest caveats to mention before any external share
- **Photos are stock placeholders** (esp. testimonials) — replace with real student photos/quotes.
- **Logo SVG/PDF are auto-traced from a raster** source — faithful and scalable, but a finer hand-cleanup of the laurels/tassel + an `.eps` export are available on request (see 06-logo.html).
- The **Smarter Together** program page (`smartertogether.smarterby1degree.com`) is JS-rendered (blank to fetch) — program details ($35/referral, $249/class, etc.) came from the original templates; verify against the live program.

## Open offers / next steps
- More ambassador template batches (myth-vs-fact, day-in-the-life, back-to-school/seasonal, multi-slide carousel).
- Voice rewrite of the original 9 ambassador posts toward the Momentum tone (kept original copy for now).
- The finer vector logo hand-cleanup + EPS.
- Apply Momentum to a real homepage or the student portal.
- White icon set exists; could add more icons.

## Original source (untouched)
Lacey's original chat-made ambassador templates: `~/Downloads/sb1d ambassador templates/` (navy+gold+serif, 2160×2700). These were rebranded into 07-ambassador.html; the originals are not modified.
