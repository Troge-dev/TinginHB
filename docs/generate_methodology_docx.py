"""
generate_methodology_docx.py
Generates TinginHB_Methodology_and_Research_Plan.docx from the markdown source.
Run with: py generate_methodology_docx.py
"""

from docx import Document
from docx.shared import Pt, Cm, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import copy
import re
import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "TinginHB_Methodology_and_Research_Plan.docx")

# ─── Color Palette ───────────────────────────────────────────────────────────
COLOR_TITLE   = RGBColor(0x1A, 0x56, 0x76)   # deep teal
COLOR_H1      = RGBColor(0x1A, 0x56, 0x76)
COLOR_H2      = RGBColor(0x24, 0x76, 0x9A)
COLOR_H3      = RGBColor(0x35, 0x8E, 0xBE)
COLOR_TABLE_H = RGBColor(0x1A, 0x56, 0x76)
COLOR_ALT_ROW = RGBColor(0xE8, 0xF4, 0xF8)

def set_cell_bg(cell, rgb: RGBColor):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    hex_color = f"{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}"
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_color)
    tcPr.append(shd)

def add_run_bold(para, text, size=11, color=None):
    run = para.add_run(text)
    run.bold = True
    run.font.size = Pt(size)
    if color:
        run.font.color.rgb = color
    return run

def add_run_normal(para, text, size=11, italic=False):
    run = para.add_run(text)
    run.font.size = Pt(size)
    run.italic = italic
    return run

def set_para_spacing(para, before=0, after=4):
    para.paragraph_format.space_before = Pt(before)
    para.paragraph_format.space_after = Pt(after)

def add_heading(doc, text, level=1):
    para = doc.add_paragraph()
    set_para_spacing(para, before=14 if level==1 else 10, after=4)
    if level == 1:
        run = para.add_run(text)
        run.bold = True
        run.font.size = Pt(14)
        run.font.color.rgb = COLOR_H1
    elif level == 2:
        run = para.add_run(text)
        run.bold = True
        run.font.size = Pt(12)
        run.font.color.rgb = COLOR_H2
    elif level == 3:
        run = para.add_run(text)
        run.bold = True
        run.font.size = Pt(11)
        run.font.color.rgb = COLOR_H3
    return para

def add_body(doc, text, italic=False):
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.font.size = Pt(10.5)
    run.italic = italic
    set_para_spacing(para, before=2, after=4)
    para.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    return para

def add_bullet(doc, text, level=0):
    para = doc.add_paragraph(style="List Bullet")
    run = para.add_run(text)
    run.font.size = Pt(10.5)
    set_para_spacing(para, before=1, after=1)
    return para

def add_code_block(doc, text):
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.font.name = "Courier New"
    run.font.size = Pt(9)
    para.paragraph_format.left_indent = Cm(1.0)
    para.paragraph_format.space_before = Pt(4)
    para.paragraph_format.space_after = Pt(4)
    # Light gray background
    pPr = para._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), "F0F0F0")
    pPr.append(shd)
    return para

def add_table(doc, headers, rows, col_widths=None):
    n_cols = len(headers)
    table = doc.add_table(rows=1 + len(rows), cols=n_cols)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = "Table Grid"

    # Header row
    hdr_row = table.rows[0]
    for i, h in enumerate(headers):
        cell = hdr_row.cells[i]
        set_cell_bg(cell, COLOR_TABLE_H)
        para = cell.paragraphs[0]
        run = para.add_run(h)
        run.bold = True
        run.font.size = Pt(9.5)
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        para.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Data rows
    for r_idx, row_data in enumerate(rows):
        row = table.rows[r_idx + 1]
        bg = COLOR_ALT_ROW if r_idx % 2 == 1 else RGBColor(0xFF, 0xFF, 0xFF)
        for c_idx, cell_text in enumerate(row_data):
            cell = row.cells[c_idx]
            set_cell_bg(cell, bg)
            para = cell.paragraphs[0]
            run = para.add_run(str(cell_text))
            run.font.size = Pt(9.5)

    # Column widths
    if col_widths:
        for i, w in enumerate(col_widths):
            for row in table.rows:
                row.cells[i].width = Cm(w)

    doc.add_paragraph()  # spacing after table
    return table

# ─── BUILD DOCUMENT ──────────────────────────────────────────────────────────

doc = Document()

# Margins
for section in doc.sections:
    section.top_margin    = Cm(2.5)
    section.bottom_margin = Cm(2.5)
    section.left_margin   = Cm(3.0)
    section.right_margin  = Cm(2.5)

# Default font
doc.styles["Normal"].font.name = "Calibri"
doc.styles["Normal"].font.size = Pt(10.5)

# ─── TITLE PAGE ──────────────────────────────────────────────────────────────
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("TinginHB")
run.bold = True
run.font.size = Pt(28)
run.font.color.rgb = COLOR_TITLE

p2 = doc.add_paragraph()
p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
run2 = p2.add_run("Methodology and Research Plan")
run2.bold = True
run2.font.size = Pt(16)
run2.font.color.rgb = COLOR_H2

doc.add_paragraph()
meta = doc.add_paragraph()
meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
meta.add_run("Non-Invasive Dual-Site AI Anemia Screening for Community Health Settings\n").font.size = Pt(11)

meta2 = doc.add_paragraph()
meta2.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = meta2.add_run("DataLunas  |  University of Science and Technology of Southern Philippines\nPhilippine Startup Challenge XI  |  October 2026")
r.font.size = Pt(10)
r.italic = True
r.font.color.rgb = COLOR_H3

doc.add_page_break()

# ─── PREFACE ─────────────────────────────────────────────────────────────────
add_heading(doc, "Preface: Responding to Mentor Directives", 1)
add_body(doc, "This document directly addresses three critical directives raised by the project mentor:")
for item in [
    "Address Limitations & Reliability — Model reliability constraints are explicitly discussed; output is reframed as a probabilistic likelihood score rather than a definitive Hb value or binary classification.",
    "Ground in Literature & Figures — Every design choice is backed by peer-reviewed research with concrete performance metrics.",
    "Refine the Multi-Indicator Approach — Conjunctiva serves as the primary site; nail bed as the secondary site; integration is weighted by literature-validated site reliability and calibrated confidence estimates.",
]:
    add_bullet(doc, item)

# ─── SECTION 1 ───────────────────────────────────────────────────────────────
add_heading(doc, "1. Problem Definition and Clinical Context", 1)

add_heading(doc, "1.1 Anemia Burden in the Philippines", 2)
add_body(doc, "Anemia affects approximately 28% of Filipino women of reproductive age and 26.4% of children under five, based on the Philippine National Nutrition Survey (NNS 2018–2019, FNRI-DOST). The WHO definition of anemia in non-pregnant adults is hemoglobin (Hb) < 12.0 g/dL for women and < 13.0 g/dL for men, subdivided as follows:")

add_table(doc,
    ["WHO Severity Tier", "Hb Range (g/dL) — Adult Women"],
    [
        ["Mild Anemia",      "11.0 – 11.9"],
        ["Moderate Anemia",  "8.0 – 10.9"],
        ["Severe Anemia",    "< 8.0"],
        ["Normal",           "≥ 12.0"],
    ],
    col_widths=[8, 8]
)
add_body(doc, "(WHO, 2011. Haemoglobin concentrations for the diagnosis of anaemia and assessment of severity.)", italic=True)

add_heading(doc, "1.2 Screening Gap and the Role of BHWs", 2)
add_body(doc, "Access to Complete Blood Count (CBC) is constrained in rural Philippine barangays. A CBC costs ₱200–₱600 and requires a trained phlebotomist, centrifuge, and hematology analyzer — infrastructure absent at barangay health stations. Barangay Health Workers (BHWs) perform frontline screening using clinical signs: conjunctival and palmar pallor, primarily under the WHO Integrated Management of Childhood Illness (IMCI) framework (WHO, 2013).")
add_body(doc, "TinginHB's Clinical Niche: TinginHB does NOT claim to replace CBC. Its niche is rapid triage at the community level — identifying individuals likely to have moderate-to-severe anemia who should be prioritized for CBC confirmation and treatment. This positions TinginHB as a decision-support tool, not a diagnostic device.")

# ─── SECTION 2 ───────────────────────────────────────────────────────────────
add_heading(doc, "2. Scientific Basis for Physical Indicator Selection", 1)

add_heading(doc, "2.1 Palpebral Conjunctiva as Primary Indicator", 2)
add_body(doc, "The palpebral (inner eyelid) conjunctiva is the most scientifically supported non-invasive site for anemia screening.")

add_heading(doc, "Biological Rationale", 3)
for b in [
    "The conjunctival epithelium is devoid of melanocytes, eliminating the primary confounder in skin-based pallor assessment (Fitzpatrick skin tone confound) (Stolz et al., 1993).",
    "Hemoglobin's optical absorption peaks at 540 nm and 576 nm (green-yellow spectrum) are directly observable through the translucent conjunctival membrane (Prahl, 1999).",
    "The sclera, visible in the same image frame, provides an in-frame white-balance reference — a critical advantage over isolated skin patches.",
]:
    add_bullet(doc, b)

add_heading(doc, "Empirical Performance (Key Prior Art)", 3)
add_table(doc,
    ["Study", "Finding", "Key Metric"],
    [
        ["Kim et al. (2020, PNAS)", "HemaChrome — conjunctiva only", "Sensitivity 91.4% (Hb < 8.0 g/dL); 62.1% mild (10–11.9 g/dL)"],
        ["Kim et al. (2023, Ann Intern Med)", "Extended validation, n=153", "Pearson r = 0.90 for Hb < 10.0 g/dL"],
        ["Dimauro et al. (2018)", "EYES-DEFY-ANEMIA dataset", "EI explains ~37% of Hb variance (R² ≈ 0.37)"],
        ["Suner et al. (2007)", "Conjunctival pallor specificity", "83.3% specificity at Hb < 9.0 g/dL; 49% at Hb < 11.0 g/dL"],
    ],
    col_widths=[5, 6, 7]
)

add_heading(doc, "2.2 Nail Bed as Secondary Indicator", 2)
add_body(doc, "The nail bed contains a subungual capillary plexus visible through the translucent nail plate. Unlike palmar skin, the nail plate is relatively uniform in thickness, reducing inter-subject variability in light transmission. Key limitation: periungual skin contains melanin and requires normalization (Mannino et al., 2018).")

add_heading(doc, "Periungual Normalization — Contrast Ratio Method", 3)
add_code_block(doc, "CR = (Nail_G - Periungual_G) / (Nail_G + Periungual_G)\n\nwhere G = green channel intensity (most sensitive to Hb absorption at 540 nm)")

add_heading(doc, "Empirical Performance", 3)
add_table(doc,
    ["Study", "System", "Key Metric"],
    [
        ["Mannino et al. (2018, Nat. Commun.)", "Sanguina — fingernail only", "MAE 1.47 g/dL (no personalization); 95% LoA ±2.4 g/dL; r = 0.87"],
        ["Valles-Coral et al. (2025, arXiv)", "AnaeCare — nails+palms+fingertips", "Macro F1 = 0.78; Mild-class F1 = 0.52 (n=909)"],
    ],
    col_widths=[5.5, 5.5, 7]
)

add_heading(doc, "2.3 Why Physical Indicators Are Reliable Only for Moderate-to-Severe Anemia", 2)
add_body(doc, "Both conjunctival and nail-bed pallor indicators share a fundamental biological limitation: pallor becomes visually detectable only after Hb drops below approximately 9.0–10.0 g/dL (Kalter et al., 1997; Luby et al., 1995). This occurs because (1) RGB camera sensors cannot distinguish the subtle color shift between Hb 12.0 g/dL and 11.0 g/dL under variable ambient lighting, and (2) physiological compensatory mechanisms (increased 2,3-DPG, vasodilation) maintain capillary perfusion at mildly reduced Hb, masking visible pallor.")
add_body(doc, "Explicit boundary: TinginHB targets a clinically actionable threshold of Hb < 10.0 g/dL (moderate anemia). Mild anemia (11.0–11.9 g/dL) is explicitly acknowledged as below the reliable detection threshold of the current technology — consistent with best-in-class systems (Kim et al., 2023; Mannino et al., 2018).")

add_heading(doc, "2.4 Secondary Physical and Physiological Indicators in Clinical Literature", 2)
add_body(doc, "In response to the mentor's directive to explore literature-backed secondary physical signs, the clinical evidence base highlights three secondary modalities that complement ocular and ungual inspection:")
for b in [
    "Palmar Pallor & Crease Blanching (WHO IMCI, 2013): Blood vessels in the palmar fascia and thenar eminence reflect systemic perfusion. Normal palmar creases retain pigmentation down to Hb ~7.0–8.0 g/dL; blanching of the creases provides an LR+ of 2.8–3.2 for severe anemia (Strobach et al., 1988; Luby et al., 1995).",
    "Lingual & Oral Mucosal Pallor: Devoid of stratum corneum and melanin, oral mucosa provides direct capillary beds (Sheth et al., 2017; LR+ ≈ 2.1). Reserved as an optional module due to field infection control/hygiene constraints.",
    "Compensatory Resting Tachycardia via Smartphone Camera PPG: Anemic hypoxia induces compensatory elevation in cardiac output via resting tachycardia (HR > 100 bpm; LR+ ≈ 1.8–2.0) (Strobach et al., 1988; Duke & Abelmann, 1969). A smartphone camera with LED flash acts as a 15-second Photoplethysmography (PPG) pulse sensor without extra hardware (Allen, 2007).",
    "Clinical Risk Covariates: Structured questionnaire covering pregnancy, lactation, menorrhagia, and dietary history, establishing the Bayesian prior probability P(Anemia) (Kalter et al., 1997).",
]:
    add_bullet(doc, b)

# ─── SECTION 3 ───────────────────────────────────────────────────────────────
add_heading(doc, "3. Probabilistic Output Framework", 1)

add_heading(doc, "3.1 Why Hard Hb Regression is Insufficient", 2)
add_body(doc, "The best published MAE for smartphone-based Hb estimation without personalization is 1.47 g/dL (Mannino et al., 2018). The WHO mild-anemia threshold margin is 1.0 g/dL (11.0–12.0 g/dL). A system with 1.47 g/dL MAE cannot reliably classify mild anemia. Reporting a hard Hb value of '11.2 g/dL' to a BHW creates false precision and clinical risk. A calibrated probability score is scientifically honest and clinically safer: 'There is a 74% likelihood this patient has moderate-to-severe anemia (Hb < 10.0 g/dL). Refer for CBC.'")

add_heading(doc, "3.2 Proposed Probabilistic Output Architecture", 2)

add_heading(doc, "Step 1 — Site-Level Regression with Uncertainty (MC Dropout)", 3)
add_body(doc, "Each image pipeline outputs a predicted Hb value AND an uncertainty estimate, using Monte Carlo Dropout (Gal & Ghahramani, 2016, ICML) with N=50 forward passes:")
add_code_block(doc, "ŷ_conj ± σ_conj     (conjunctiva pipeline)\nŷ_nail ± σ_nail     (nail bed pipeline)")

add_heading(doc, "Step 2 — Inverse-Variance Weighted Bayesian Fusion", 3)
add_code_block(doc,
"w_conj = 1 / σ_conj²\n"
"w_nail = 1 / σ_nail²\n\n"
"ŷ_fused = (w_conj × ŷ_conj + w_nail × ŷ_nail) / (w_conj + w_nail)\n"
"σ_fused² = 1 / (w_conj + w_nail)"
)
add_body(doc, "This assigns more weight to whichever site's pipeline is more confident. If conjunctival image quality is poor, σ_conj rises, and the nail bed pipeline automatically receives more weight — and vice versa. (Bishop, 2006, Pattern Recognition and Machine Learning, Ch. 2.)")

add_heading(doc, "Step 3 — Calibrated WHO-Tier Probability", 3)
add_code_block(doc,
"P(Moderate-Severe | image) = P(Hb < 10.0 g/dL)\n"
"                           = Φ((10.0 - ŷ_fused) / σ_fused)\n\n"
"Where Φ = standard normal CDF"
)
add_body(doc, "The wider σ_fused is, the less extreme the probability — the model avoids overconfidence automatically.")

add_heading(doc, "Step 4 — Post-Hoc Calibration (Platt Scaling)", 3)
add_body(doc, "The raw probability output is calibrated on a held-out validation set using Platt Scaling (Platt, 1999), ensuring that when the model outputs P = 0.70, 70% of such patients in validation actually have Hb < 10.0 g/dL. This satisfies the Expected Calibration Error (ECE) requirement (Guo et al., 2017, ICML).")

add_heading(doc, "3.3 User-Facing Output Design", 2)
add_table(doc,
    ["Probability Range", "Output Label", "BHW Action"],
    [
        ["P < 0.25",          "🟢 Anemia Unlikely",              "Routine follow-up"],
        ["0.25 ≤ P < 0.55",  "🟡 Inconclusive — Recheck",       "Repeat scan or improve positioning"],
        ["0.55 ≤ P < 0.80",  "🟠 Possible Anemia — Refer",      "Refer to RHU for CBC"],
        ["P ≥ 0.80",          "🔴 Likely Anemia — Urgent Referral", "Immediate referral for CBC + treatment"],
    ],
    col_widths=[4.5, 5.5, 8]
)

add_heading(doc, "3.4 Multi-Indicator Weighting & Integration Architecture", 2)
add_body(doc, "To integrate secondary physical and physiological indicators with the primary optical channels without introducing noise, TinginHB employs a Two-Tiered Hierarchical Bayesian Integration Model backed by clinical likelihood ratios (Strobach et al., 1988; Kalter et al., 1997):")
add_code_block(doc,
"ln(Odds_post) = ln(Odds_prior) + w_conj*ln(LR_conj) + w_nail*ln(LR_nail) + w_palm*ln(LR_palm) + w_tachy*ln(LR_tachy)"
)
add_table(doc,
    ["Modality / Indicator", "Diagnostic Metric", "Weight (w_i)", "Literature Grounding"],
    [
        ["Palpebral Conjunctiva", "LR+ ≈ 4.4 (Sens: 85%, Spec: 81%)", "w = 1.0", "Primary optical driver; zero melanin (Strobach 1988; Kim 2020)"],
        ["Subungual Nail Bed",    "LR+ ≈ 2.2 (Sens: 78%, Spec: 65%)", "w = 0.8", "Primary co-driver; CR-normalized (Mannino 2018)"],
        ["Palmar Creases (Gated)","LR+ ≈ 2.9 (blanched creases)",      "w = 0.5", "Secondary corroborator upon ambiguity (Kalter 1997; Luby 1995)"],
        ["Resting Tachycardia",   "LR+ ≈ 1.9 (HR > 100 bpm, resting)","w = 0.4", "Compensatory cardiac output via 15s camera PPG (Allen 2007)"],
    ],
    col_widths=[4.5, 5.5, 2.5, 6.5]
)
add_body(doc, "Tier 2 Gating Rule: Secondary checks (Palmar Crease scan, 15s camera PPG) are only activated if primary uncertainty σ_prim > 1.2 g/dL or if primary discrepancy |ŷ_conj - ŷ_nail| > 2.0 g/dL. This preserves fast BHW workflow while providing clinical resilience.")

# ─── SECTION 4 ───────────────────────────────────────────────────────────────
add_heading(doc, "4. System Architecture", 1)
add_heading(doc, "4.1 Pipeline Overview", 2)
add_code_block(doc,
"[Camera & Sensor Inputs]\n"
"  ├── TIER 1: PRIMARY SITES\n"
"  │    ├── Conjunctiva Image ──► YOLOv8n-seg ROI ──► MobileNetV3-S + Radiomics ──► ŷ_conj ± σ_conj\n"
"  │    └── Nail Bed Image ─────► YOLOv8n-seg ROI ──► MobileNetV3-S + CR Norm  ──► ŷ_nail ± σ_nail\n"
"  │                                                                                  │\n"
"  │                                                [Inverse-Variance Fusion & Gating Rule]\n"
"  │                                                                                  │\n"
"  └── TIER 2: GATED SECONDARY SIGNS (Activated if σ > 1.2 or Δ > 2.0)                │\n"
"       ├── Palmar Crease Image ──► YOLOv8n-seg ROI ──► MobileNetV3-S Feature ────────┤\n"
"       ├── 15s Finger Flash PPG ─► [Peak Detection Algorithm] ──► Resting HR ────────┤\n"
"       └── BHW Risk Checklist ──► [Categorical Risk Multiplier] ─────────────────────┤\n"
"                                                                                      ▼\n"
"                                                               [Bayesian Log-Odds Integration]\n"
"                                                                                      │\n"
"                                                                 [Platt Scaling Calibration]\n"
"                                                                                      │\n"
"                                                                     P(Moderate-Severe Anemia)\n"
"                                                                                      │\n"
"                                                                      [BHW-Facing Triage Label]"
)

add_heading(doc, "4.2 Conjunctiva Pipeline", 2)
for b in [
    "ROI Detection: YOLOv8n-seg fine-tuned to detect and segment the palpebral conjunctival region. Sclera mask serves as white-balance reference.",
    "White Balance Normalization: G_norm = G_roi / G_sclera (green channel). Replicates Kim et al. (2023) scleral normalization approach.",
    "Branch A (Deep CNN): MobileNetV3-Small → 576-dim feature vector.",
    "Branch B (Colorimetric Radiomics): 16 features including Erythema Index (R/(G+B), from Dimauro et al., 2018), Haralick texture, HSV brightness, histogram percentiles.",
    "Fusion: Concatenate → FC(256) → ReLU → Dropout(0.3) → FC(1) regression head.",
    "Uncertainty: MC Dropout N=50 passes at inference.",
]:
    add_bullet(doc, b)

add_heading(doc, "4.3 Nail Bed Pipeline", 2)
for b in [
    "ROI Detection: YOLOv8n-seg detecting nail plate mask and periungual skin region mask.",
    "Periungual Normalization: Contrast Ratio method (Mannino et al., 2018) on G and R channels.",
    "Feature Extraction: MobileNetV3-Small on normalized nail ROI + CR features appended to FC.",
    "Uncertainty: Same MC Dropout scheme as conjunctiva pipeline.",
]:
    add_bullet(doc, b)

add_heading(doc, "4.4 Discrepancy Detection", 2)
add_code_block(doc, "Flag raised when: |ŷ_conj - ŷ_nail| > δ   (δ = 2.0 g/dL)")
add_body(doc, "When flagged, BHW is notified to re-check for conjunctivitis, nail injury, or image quality issues. This handles pathological confounders (jaundice, Raynaud's, nail trauma) that would otherwise bias one site's estimate.")

# ─── SECTION 5 ───────────────────────────────────────────────────────────────
add_heading(doc, "5. Dataset Strategy", 1)
add_heading(doc, "5.1 Available Datasets", 2)
add_table(doc,
    ["Dataset", "Site", "N", "Ground Truth", "Source"],
    [
        ["CP-Anemic Ghana",          "Conjunctiva", "710",  "Hb g/dL (HemoCue)", "Mendeley 10.17632/m53vz6b7fx.1"],
        ["EYES-DEFY-ANEMIA",         "Conjunctiva", "865",  "Class + Hb",         "Kaggle (Dimauro et al., 2018)"],
        ["Eye-Conjunctiva Kaggle",   "Conjunctiva", "218",  "Binary",             "Kaggle"],
        ["Ghana Fingernails",        "Nail bed",    "4,260","Anemia class",       "Mendeley 10.17632/2xx4j3kjg2.1"],
        ["Peru Uñas-Palmas-Yemas",  "Nail bed",    "826",  "3-class",            "Kaggle shimu080"],
        ["Fingernail Ayush",         "Nail bed",    "1,777","Binary",             "Kaggle"],
    ],
    col_widths=[4, 2.5, 1.8, 3.5, 4.5]
)
add_body(doc, "Total: ~8,656 images across both sites before augmentation. Critical Gap: No Filipino ground-truth dataset exists. Philippine field validation is essential.")

add_heading(doc, "5.2 Data Augmentation", 2)
for b in [
    "Geometric: Random flip, ±15° rotation",
    "Photometric: ColorJitter (brightness ±0.3, contrast ±0.3, saturation ±0.2, hue ±0.05)",
    "Blur: Random Gaussian blur σ = 0.5–1.5 (defocus simulation)",
    "Shadow: Albumentations RandomShadow (lighting condition simulation)",
    "Synthetic Hb Shift: Beer-Lambert-derived green-channel scaling to simulate lower Hb values (Kim et al., 2020 method)",
]:
    add_bullet(doc, b)

# ─── SECTION 6 ───────────────────────────────────────────────────────────────
add_heading(doc, "6. Training and Evaluation Protocol", 1)
add_heading(doc, "6.1 Training Setup", 2)
add_table(doc,
    ["Parameter", "Value"],
    [
        ["Framework",          "PyTorch 2.x"],
        ["Base Model",         "MobileNetV3-Small (ImageNet pretrained)"],
        ["Loss Function",      "Huber Loss (δ=1.0) — robust to outlier Hb extremes (Huber, 1964)"],
        ["Optimizer",          "AdamW, lr=3e-4, weight decay=1e-4"],
        ["LR Schedule",        "Cosine annealing with warm restart"],
        ["Batch Size",         "32"],
        ["Epochs",             "100 (early stopping, patience=15)"],
        ["MC Dropout passes",  "N=50 at inference"],
        ["Validation",         "5-fold stratified CV (stratified by Hb tier, Fitzpatrick, dataset source)"],
    ],
    col_widths=[7, 11]
)

add_heading(doc, "6.2 Primary Evaluation Metrics", 2)
add_table(doc,
    ["Metric", "Definition", "Target"],
    [
        ["MAE (g/dL)",      "Mean Absolute Error — fused ŷ vs. lab Hb",         "≤ 1.5 g/dL"],
        ["RMSE (g/dL)",     "Root Mean Squared Error",                           "≤ 2.0 g/dL"],
        ["Sensitivity",     "True Positive Rate — Hb < 10.0 g/dL",              "≥ 85%"],
        ["Specificity",     "True Negative Rate — Hb ≥ 10.0 g/dL",             "≥ 75%"],
        ["AUROC",           "Area Under ROC Curve for Hb < 10.0 g/dL",          "≥ 0.88"],
        ["ECE",             "Expected Calibration Error (calibration quality)",  "≤ 0.08"],
        ["Bland-Altman LoA","95% Limits of Agreement",                           "< ±2.5 g/dL"],
    ],
    col_widths=[3.5, 8, 3.5]
)

add_heading(doc, "6.3 Subgroup Analysis", 2)
add_body(doc, "Performance reported SEPARATELY for: Fitzpatrick I–II vs. III–IV vs. V–VI; Hb tier (Mild/Moderate/Severe); dataset source; gender. Subgroup analysis reveals hidden disparities that aggregate metrics conceal (Obermeyer et al., 2019, Science).")

# ─── SECTION 7 ───────────────────────────────────────────────────────────────
add_heading(doc, "7. Explicit Model Limitations (Mandatory Disclosure)", 1)
add_body(doc, "The following limitations are non-negotiable and will be disclosed to all users of the system, per mentor directive and responsible AI practice.")

add_heading(doc, "7.1 Detection Limit for Mild Anemia", 2)
add_body(doc, "TinginHB is not designed to reliably detect mild anemia (Hb 11.0–11.9 g/dL). Pallor-based indicators become visually distinguishable only at Hb < ~9.0–10.0 g/dL (Kalter et al., 1997). Even HemaChrome (Kim et al., 2020) achieves only 62.1% sensitivity at the mild threshold. A negative TinginHB result does NOT rule out mild anemia.")

add_heading(doc, "7.2 Physiological Confounders", 2)
add_table(doc,
    ["Confounder", "Effect", "Mitigation"],
    [
        ["Conjunctivitis / eye inflammation", "Red conjunctiva → false positive", "Discrepancy flag + exclusion criterion"],
        ["Jaundice",                           "Yellow sclera distorts white balance", "Exclusion criterion in BHW guide"],
        ["Nail trauma / subungual hematoma",   "Dark pigmentation confounds ROI",  "Discrepancy flag"],
        ["Hypothermia / Raynaud's",            "Vasoconstriction → false pallor",  "Discrepancy flag"],
        ["Dehydration",                        "May mask anemia (concentrated blood)", "Noted as limitation"],
    ],
    col_widths=[5, 5.5, 5.5]
)

add_heading(doc, "7.3 Imaging Confounders", 2)
add_table(doc,
    ["Confounder", "Effect", "Mitigation"],
    [
        ["Ambient lighting color temperature", "Color cast distorts Hb estimation", "Scleral white-balance normalization"],
        ["Fluorescent lighting (CRI < 80)",    "Green-heavy spectrum inflates EI",  "Protocol: natural light preferred"],
        ["Motion blur",                         "ROI segmentation fails",            "Laplacian variance sharpness gate"],
        ["Insufficient eyelid eversion",        "Partial conjunctiva visible",       "YOLOv8 confidence gate < 0.7 → reject"],
        ["Fitzpatrick V–VI skin",               "High melanin around nail",          "CR normalization partial; known gap"],
    ],
    col_widths=[5, 5.5, 5.5]
)

add_heading(doc, "7.4 What TinginHB Explicitly Does NOT Claim", 2)
for b in [
    "NOT a substitute for Complete Blood Count (CBC)",
    "NOT reliable for mild anemia (Hb 11.0–11.9 g/dL) detection",
    "NOT a diagnostic device — to be registered as a software-based wellness/screening aid",
    "NOT validated for individuals with conjunctival pathology or nail disorders",
    "NOT tested on Fitzpatrick VI skin tones",
]:
    add_bullet(doc, b)

# ─── SECTION 8 ───────────────────────────────────────────────────────────────
add_heading(doc, "8. Philippine Field Validation Protocol", 1)
add_heading(doc, "8.1 Study Design", 2)
add_table(doc,
    ["Parameter", "Details"],
    [
        ["Design",          "Prospective diagnostic accuracy study (STARD 2015 reporting guidelines)"],
        ["Setting",         "Barangay health stations, Cagayan de Oro, Misamis Oriental"],
        ["Target N",        "n = 250 subjects (Wilson method: 196 for 85% sensitivity, 10% precision, 15% attrition)"],
        ["Reference Std.",  "Laboratory CBC (Sysmex XN) at affiliated RHU within 2 hours of imaging"],
        ["Recruitment",     "Purposive sampling — 40% target anemia prevalence via RHU referrals"],
        ["Blinding",        "BHWs blinded to CBC result during scan; unblinded for analysis only"],
    ],
    col_widths=[4, 13]
)

add_heading(doc, "8.2 Analysis Plan", 2)
for b in [
    "Primary: AUROC for P(Moderate-Severe Anemia) vs. CBC Hb < 10.0 g/dL",
    "Secondary: Sensitivity, specificity, PPV, NPV at optimal Youden threshold",
    "Calibration: Reliability diagram + ECE on validation cohort",
    "Subgroup: By gender, estimated Fitzpatrick phototype, anemia tier",
    "Bland-Altman: Continuous Hb estimates vs. CBC Hb",
]:
    add_bullet(doc, b)

# ─── SECTION 9 ───────────────────────────────────────────────────────────────
add_heading(doc, "9. Edge Deployment and Technical Feasibility", 1)
add_table(doc,
    ["Component", "Implementation", "Size / Latency"],
    [
        ["YOLOv8n-seg (ROI)",       "TFLite INT8 quantized",                    "~3.5 MB, ~80 ms/image"],
        ["MobileNetV3-Small",       "TFLite FP16 quantized",                    "~5.2 MB, ~120 ms/image"],
        ["MC Dropout (N=50)",       "Parallelized on-device",                   "~200 ms total"],
        ["Fusion + Calibration",    "NumPy / on-device Python",                 "~10 ms"],
        ["Total Pipeline",          "—",                                        "< 450 ms per dual-site scan"],
    ],
    col_widths=[5, 6, 5.5]
)
add_body(doc, "Target devices: Android 8.0+, ≥2 GB RAM, ≥8 MP camera. All inference runs offline — no internet required at point of care.")

# ─── SECTION 10 ──────────────────────────────────────────────────────────────
add_heading(doc, "10. Research Timeline and Milestones", 1)
add_table(doc,
    ["Phase", "Activities", "Duration"],
    [
        ["Phase 1: Dataset & Pipeline",    "Preprocessing, augmentation, YOLOv8 ROI training",                   "Months 1–2"],
        ["Phase 2: Model Training",        "Dual-branch MobileNetV3, MC Dropout, ablation studies",              "Months 2–3"],
        ["Phase 3: Fusion & Calibration",  "Inverse-variance fusion, Platt scaling, ECE measurement",            "Month 3"],
        ["Phase 4: App Development",       "Android app, guided UI, offline inference, PDF export",              "Months 3–4"],
        ["Phase 5: IRB & Ethics",          "IRB application, consent form, data protection compliance",          "Months 2–3 (parallel)"],
        ["Phase 6: Field Validation",      "n=250 Philippine validation at barangay health stations",             "Months 5–7"],
        ["Phase 7: Analysis & Reporting",  "STARD report, peer-reviewed manuscript preparation",                  "Months 7–9"],
    ],
    col_widths=[4.5, 8.5, 3.5]
)

# ─── REFERENCES ──────────────────────────────────────────────────────────────
add_heading(doc, "References", 1)
refs = [
    "WHO (2011). Haemoglobin concentrations for the diagnosis of anaemia and assessment of severity. WHO/NMH/NHD/MNM/11.1.",
    "WHO (2013). Pocket book of hospital care for children (2nd ed.). IMCI pallor assessment chapter.",
    "Mannino, R. G., et al. (2018). Smartphone app for non-invasive detection of anemia using only patient-sourced photos. Nature Communications, 9, 4924.",
    "Kim, T. N., et al. (2020). Smartphone-based assessment of anemia from conjunctival images. PNAS, 117(49), 31046–31055.",
    "Kim, T. N., et al. (2023). Validation of a smartphone-based conjunctival assessment for anemia in outpatients. Annals of Internal Medicine, 176(3), 302–310.",
    "Dimauro, G., et al. (2018). Ocular redness measurement in non-contact diagnoses of anaemia. Journal of Imaging, 4(8), 95.",
    "Valles-Coral, M. A., et al. (2025). AnaeCare: Non-invasive anemia detection from multi-site pallor analysis. arXiv.",
    "Suner, S., et al. (2007). Noninvasive determination of hemoglobin by digital photography of palpebral conjunctiva. Journal of Emergency Medicine, 35(4), 359–364.",
    "Kalter, H. D., et al. (1997). Evaluation of clinical signs to diagnose anaemia in Uganda and Bangladesh. Bulletin of the World Health Organization, 75(Suppl 1), 103–111.",
    "Gal, Y., & Ghahramani, Z. (2016). Dropout as a Bayesian Approximation. ICML 2016, 48, 1050–1059.",
    "Platt, J. (1999). Probabilistic outputs for SVMs and regularized likelihood methods. Advances in Large Margin Classifiers.",
    "Guo, C., et al. (2017). On calibration of modern neural networks. ICML 2017, 70, 1321–1330.",
    "Bishop, C. M. (2006). Pattern Recognition and Machine Learning. Springer. Ch. 2 & 7.",
    "Roy, A. G., et al. (2019). Monte Carlo sampling for segmentation quality control. IEEE Trans. Medical Imaging, 38(5), 1218–1230.",
    "Obermeyer, Z., et al. (2019). Dissecting racial bias in an algorithm used to manage health. Science, 366(6464), 447–453.",
    "FNRI-DOST (2019). Philippine National Nutrition Survey 2018–2019.",
    "Huber, P. J. (1964). Robust estimation of a location parameter. Annals of Mathematical Statistics, 35(1), 73–101.",
    "Kuleshov, V., et al. (2018). Accurate uncertainties for deep learning using calibrated regression. ICML 2018.",
    "Stolz, W., et al. (1993). Color Atlas of Dermatology (Fitzpatrick phototype reference). Blackwell.",
    "Strobach, R. S., et al. (1988). The value of the physical examination in diagnosing anemia. JAMA, 259(11), 1682–1685.",
    "Luby, S. P., et al. (1995). Using clinical signs to diagnose anaemia in African children. Bulletin of the World Health Organization, 73(4), 477–482.",
    "Sheth, P. B., et al. (2017). Non-invasive anemia detection using smartphone-based tongue colorimetry. IEEE JBHI.",
    "Allen, J. (2007). Photoplethysmography and its application in clinical physiological measurement. Physiological Measurement, 28(3), R1–R39.",
    "Duke, M., & Abelmann, W. H. (1969). The hemodynamic response to chronic anemia. Circulation, 39(4), 503–515.",
]
for i, ref in enumerate(refs, 1):
    para = doc.add_paragraph()
    para.paragraph_format.left_indent = Cm(0.6)
    para.paragraph_format.first_line_indent = Cm(-0.6)
    run = para.add_run(f"{i}. {ref}")
    run.font.size = Pt(9.5)
    set_para_spacing(para, before=1, after=2)

# ─── FOOTER NOTE ─────────────────────────────────────────────────────────────
doc.add_paragraph()
disclaimer = doc.add_paragraph()
disclaimer.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = disclaimer.add_run("This document is a living research plan. All claims are bounded by the cited literature. No performance guarantees are made beyond what is demonstrated in peer-reviewed prior work.\n\nDataLunas Research Team, USTP  |  Reviewed in response to mentor directives — October 2026")
r.italic = True
r.font.size = Pt(9)
r.font.color.rgb = COLOR_H3

try:
    doc.save(OUTPUT_PATH)
    print(f"[OK] Document saved to:\n    {OUTPUT_PATH}")
except PermissionError:
    alt_path = OUTPUT_PATH.replace(".docx", "_v2.docx")
    doc.save(alt_path)
    print(f"[NOTE] '{os.path.basename(OUTPUT_PATH)}' is currently open in Word.")
    print(f"[OK] Saved updated version to:\n    {alt_path}")
