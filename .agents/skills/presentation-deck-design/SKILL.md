---
name: presentation-deck-design
description: >-
  Expert system for creating high-impact, professional presentation decks, pitch decks,
  and keynote slide drafts. Covers 16:9 visual design systems, plain solid color styling
  (Light Mode & Dark Mode), Canva generation without decorative AI clutter, and interactive
  HTML/Keynote decks with pre-rendered 16:9 PDF export.
---

# Presentation Deck Design Skill

Use this skill whenever the user asks to create, outline, style, or generate a presentation deck, pitch deck, PowerPoint (PPT), keynote, or Canva slide draft.

This skill ensures that **every presentation draft looks exceptional, professional, and investor-ready** by following rigorous typography-first visual rules, strict background controls, and structured delivery pipelines.

---

## 1. Core Visual Principles: The "Looks Good" Standard

To prevent generic, cluttered, or amateur-looking slides, ALWAYS enforce these rules:

### A. Solid Plain Backgrounds Only (No AI Clutter)
* **Never use busy background images, decorative stock photos, or complex gradient meshes.**
* **Light Mode (Default & Clean)**: Pure Solid White (`#FFFFFF`) or Clinical Alabaster (`#F8FAFC`).
* **Dark Mode (Terminal / High Contrast)**: Solid Deep Slate/Navy (`#090D14` or `#0A1118`).
* **Why this matters in Canva**: When AI presentation generators parse words like "card", "container", "glow", or "box", they generate unwanted decorative vector art and textured background images. Explicitly commanding `Plain solid background only, zero background images, zero textures, pure typography` guarantees clean, crisp results.

### B. Universal 16:9 Widescreen Ratio
* All slides must use the modern **16:9 widescreen aspect ratio**:
  * Digital / Canvas: `1920 x 1080 px`
  * Print / PDF Export: `16in x 9in` or `1152 x 648 pt` (Aspect ratio: `1.778`)

### C. Modern Font Trio
Never use generic system fonts (Arial, Times New Roman, Calibri). Use this proven high-contrast stack:
1. **Display / Headings**: **Space Grotesk** (or Montserrat, Syne) — bold, geometric, confident.
2. **Body / Subtitles**: **Plus Jakarta Sans** (or Inter) — clean, highly readable, balanced.
3. **Eyebrows, Tags & Data Metrics**: **JetBrains Mono** (or Roboto Mono) — technical rigor, monospace precision.

### D. Typography Hierarchy Over Clutter
* **Hero Numbers**: Make primary metrics huge (`40pt – 56pt Bold`).
* **Category Kickers**: Place an uppercase monospace eyebrow tag above every slide title (e.g., `EPIDEMIOLOGICAL GROUNDING`).
* **Clean Hairline Dividers**: Use `1px solid #E2E8F0` (light) or `#1E293B` (dark) to delineate sections instead of bulky colored boxes.

---

## 2. Standard 10-Slide Pitch Deck Architecture

When creating an executive startup or innovation pitch deck, use this cohesive narrative arc:

| Slide # | Slide Title | Core Purpose & Required Elements |
| :---: | :--- | :--- |
| **01** | **Cover & Identity** | Venture Name, Bold Tagline, 2-line Value Proposition, Team/Institution metadata. |
| **02** | **Problem Description** | Macro statistics, fatal risk multiplier, current diagnostic/market bottleneck. |
| **03** | **SDG & Policy Alignment** | UN SDGs (e.g., 3.1, 3.2, 3.8, 10.3) + statutory national health/policy laws. |
| **04** | **Target Market & Sizing** | 3-tier stakeholders (Users vs Beneficiaries vs Buyers), TAM/SAM/SOM, cost avoidance. |
| **05** | **The Proposed Solution** | Core technological innovation, dual sensing, clinical workflow, automated referral. |
| **06** | **Engineering & Architecture** | 6 technical features: on-device model size, latency, calibration, data security. |
| **07** | **Business Model & Moat** | Revenue engines (SaaS/licensing), unit economics, 4-column competitor comparison. |
| **08** | **Progress & Traction** | Completed deliverables (left) + 12–18 month forward strategic roadmap (right). |
| **09** | **Asks & Resource Allocation** | Itemized budget breakdown table + 3 concrete strategic partnership asks. |
| **10** | **Closing Vision & Disclaimer** | High-impact call-to-action, contact details, formal regulatory/legal notice. |

---

## 3. Execution Workflows

### Workflow A: Generating in Canva via MCP
When using the Canva MCP tool (`create-design`):
1. **Craft the Brief with Strict Negative Constraints**:
   ```text
   Brief: 16:9 presentation for [Topic].
   THEME: LIGHT MODE (or DARK MODE).
   BACKGROUND: Plain solid white (#FFFFFF) background only.
   STRICT RULE: Absolutely NO background images, NO textures, NO photos, NO clip art, NO icons.
   FORMAT: Pure typography, structured numbers, and clean tables on a flat solid background.
   ```
2. **Poll the Job**: Respect `polling_policy.wait_seconds` (usually 10–15s).
3. **1-Click Canva Cleanup Instruction for User**:
   * Click canvas $\rightarrow$ Background Color tile $\rightarrow$ Select solid color $\rightarrow$ Click **"Apply to all pages"**.

### Workflow B: Interactive HTML Keynote Deck
When building an interactive web deck:
1. **Viewport Preservation**: Center `.keynote-stage` with `aspect-ratio: 16 / 9; max-width: calc(100vw - 2rem);`.
2. **Edge-Hover Drawers**: Hide header and footer navigation into subtle edge drawers (`transform: translateY(80%); opacity: 0.25;`) that expand on hover, so the presentation stage remains cinematic.
3. **Keyboard Shortcuts**: Support <kbd>ArrowLeft</kbd>/<kbd>ArrowRight</kbd>, <kbd>Space</kbd>, <kbd>T</kbd> (theme toggle), <kbd>F</kbd> (fullscreen), <kbd>P</kbd> (print).
4. **CSS Tokens**: Use CSS variables for instant Light/Dark switching:
   * Light: `--bg-canvas: #F8FAFC; --surface-card: #FFFFFF; --text-main: #0F172A;`
   * Dark: `--bg-canvas: #090D14; --surface-card: #111724; --text-main: #F8FAFC;`

### Workflow C: PDF Generation & Verification
1. **Print Stylesheet Requirement**:
   ```css
   @media print {
     *, *::before, *::after {
       animation: none !important;
       transition: none !important;
     }
     .slide {
       display: flex !important;
       width: 16in !important;
       height: 9in !important;
       opacity: 1 !important;
       visibility: visible !important;
       page-break-after: always !important;
       break-after: page !important;
       background: var(--surface-card) !important;
     }
   }
   ```
2. **Render Command (Windows PowerShell)**:
   ```powershell
   Start-Process -FilePath "C:\Program Files\Google\Chrome\Application\chrome.exe" -ArgumentList "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--print-to-pdf=`"output.pdf`"", "`"file:///absolute/path/deck.html`"" -Wait -PassThru
   ```
3. **Verify with Python (`pdfplumber`)**: Check that page count equals 10, aspect ratio is 1.778, and character count per page is $> 0$.
