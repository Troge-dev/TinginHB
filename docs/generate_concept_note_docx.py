"""
generate_concept_note_docx.py
Generates TinginHB_Revised_Concept_Note_PSCXI.docx adapted strictly to the
10-section Philippine Startup Challenge XI (PSC XI) concept note layout.
Includes 7 visual figure placeholder callout boxes, empirical clinical grounding,
dynamic 5-modality weighting matrix, and formal academic references.
"""

from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "TinginHB_Revised_Concept_Note_PSCXI.docx")

# ─── Color Palette ───────────────────────────────────────────────────────────
COLOR_TITLE   = RGBColor(0x0E, 0x4D, 0x64)   # deep teal
COLOR_H1      = RGBColor(0x0E, 0x4D, 0x64)
COLOR_H2      = RGBColor(0x1B, 0x6B, 0x8A)
COLOR_H3      = RGBColor(0x2B, 0x8A, 0xAE)
COLOR_TABLE_H = RGBColor(0x0E, 0x4D, 0x64)
COLOR_ALT_ROW = RGBColor(0xEA, 0xF4, 0xF8)
COLOR_MUTED   = RGBColor(0x55, 0x66, 0x77)
COLOR_FIG_BG  = RGBColor(0xF4, 0xF9, 0xFB)

def set_cell_bg(cell, rgb: RGBColor):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    hex_color = f"{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}"
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_color)
    tcPr.append(shd)

def set_para_spacing(para, before=2, after=4):
    para.paragraph_format.space_before = Pt(before)
    para.paragraph_format.space_after = Pt(after)

def add_heading(doc, text, level=1):
    para = doc.add_paragraph()
    set_para_spacing(para, before=14 if level==1 else (10 if level==2 else 6), after=3)
    run = para.add_run(text)
    run.bold = True
    if level == 1:
        run.font.size = Pt(13.5)
        run.font.color.rgb = COLOR_H1
    elif level == 2:
        run.font.size = Pt(11.5)
        run.font.color.rgb = COLOR_H2
    elif level == 3:
        run.font.size = Pt(10.5)
        run.font.color.rgb = COLOR_H3
    return para

def add_body(doc, text, italic=False):
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.font.size = Pt(10)
    run.italic = italic
    set_para_spacing(para, before=2, after=4)
    para.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    return para

def add_bullet(doc, text):
    para = doc.add_paragraph(style="List Bullet")
    run = para.add_run(text)
    run.font.size = Pt(10)
    set_para_spacing(para, before=1, after=1)
    return para

def add_code_block(doc, text):
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.font.name = "Courier New"
    run.font.size = Pt(8.5)
    para.paragraph_format.left_indent = Cm(0.8)
    set_para_spacing(para, before=3, after=3)
    pPr = para._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), "F4F6F8")
    pPr.append(shd)
    return para

def add_table(doc, headers, rows, col_widths=None):
    n_cols = len(headers)
    table = doc.add_table(rows=1 + len(rows), cols=n_cols)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = "Table Grid"

    hdr_row = table.rows[0]
    for i, h in enumerate(headers):
        cell = hdr_row.cells[i]
        set_cell_bg(cell, COLOR_TABLE_H)
        para = cell.paragraphs[0]
        run = para.add_run(h)
        run.bold = True
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        para.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

    for r_idx, row_data in enumerate(rows):
        row = table.rows[r_idx + 1]
        bg = COLOR_ALT_ROW if r_idx % 2 == 1 else RGBColor(0xFF, 0xFF, 0xFF)
        for c_idx, cell_text in enumerate(row_data):
            cell = row.cells[c_idx]
            set_cell_bg(cell, bg)
            para = cell.paragraphs[0]
            run = para.add_run(str(cell_text))
            run.font.size = Pt(9)

    if col_widths:
        for i, w in enumerate(col_widths):
            for row in table.rows:
                row.cells[i].width = Cm(w)

    doc.add_paragraph()
    return table

def add_figure_placeholder(doc, fig_num, title, suggested_visual, items, caption, data_sources):
    """
    Renders an elegant, shaded callout box for visual figure placeholders.
    """
    table = doc.add_table(rows=2, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = "Table Grid"
    table.autofit = False

    # Header cell
    hdr = table.rows[0].cells[0]
    hdr.width = Cm(16.0)
    set_cell_bg(hdr, COLOR_TITLE)
    p_hdr = hdr.paragraphs[0]
    set_para_spacing(p_hdr, before=4, after=4)
    p_hdr.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r_hdr = p_hdr.add_run(f"  [FIGURE {fig_num} PLACEHOLDER: {title.upper()}]")
    r_hdr.bold = True
    r_hdr.font.size = Pt(9.5)
    r_hdr.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    # Body cell
    body = table.rows[1].cells[0]
    body.width = Cm(16.0)
    set_cell_bg(body, COLOR_FIG_BG)

    p_sug = body.paragraphs[0]
    set_para_spacing(p_sug, before=4, after=2)
    r_sug_lbl = p_sug.add_run("Suggested Visual: ")
    r_sug_lbl.bold = True
    r_sug_lbl.font.size = Pt(9)
    r_sug_lbl.font.color.rgb = COLOR_H2
    r_sug_val = p_sug.add_run(suggested_visual)
    r_sug_val.font.size = Pt(9)

    for item in items:
        p_item = body.add_paragraph()
        set_para_spacing(p_item, before=1, after=1)
        p_item.paragraph_format.left_indent = Cm(0.5)
        r_bullet = p_item.add_run("• ")
        r_bullet.bold = True
        r_bullet.font.size = Pt(8.5)
        r_bullet.font.color.rgb = COLOR_H3
        r_txt = p_item.add_run(item)
        r_txt.font.size = Pt(8.5)

    p_cap = body.add_paragraph()
    set_para_spacing(p_cap, before=4, after=2)
    r_cap_lbl = p_cap.add_run("Caption: ")
    r_cap_lbl.bold = True
    r_cap_lbl.font.size = Pt(9)
    r_cap_val = p_cap.add_run(f"Figure {fig_num}. {caption}")
    r_cap_val.italic = True
    r_cap_val.font.size = Pt(9)

    p_src = body.add_paragraph()
    set_para_spacing(p_src, before=1, after=4)
    r_src_lbl = p_src.add_run("Data Sources / Theoretical Grounding: ")
    r_src_lbl.bold = True
    r_src_lbl.font.size = Pt(8.5)
    r_src_lbl.font.color.rgb = COLOR_MUTED
    r_src_val = p_src.add_run(data_sources)
    r_src_val.italic = True
    r_src_val.font.size = Pt(8.5)
    r_src_val.font.color.rgb = COLOR_MUTED

    p_spacer = doc.add_paragraph()
    set_para_spacing(p_spacer, before=0, after=4)
    return table

# ─── BUILD DOCUMENT ──────────────────────────────────────────────────────────

doc = Document()

for section in doc.sections:
    section.top_margin    = Cm(2.2)
    section.bottom_margin = Cm(2.2)
    section.left_margin   = Cm(2.5)
    section.right_margin  = Cm(2.5)

doc.styles["Normal"].font.name = "Calibri"
doc.styles["Normal"].font.size = Pt(10)

# ─── TITLE HEADER (PSC XI TEMPLATE LAYOUT) ───────────────────────────────────
p_track = doc.add_paragraph()
p_track.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_track = p_track.add_run("PHILIPPINE STARTUP CHALLENGE XI")
r_track.bold = True
r_track.font.size = Pt(13)
r_track.font.color.rgb = COLOR_H2

p_team = doc.add_paragraph()
p_team.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_team = p_team.add_run("DataLunas  |  University of Science and Technology of Southern Philippines (USTP)")
r_team.font.size = Pt(11)
r_team.font.color.rgb = COLOR_MUTED

p_app = doc.add_paragraph()
p_app.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_app = p_app.add_run("TingínHB")
r_app.bold = True
r_app.font.size = Pt(24)
r_app.font.color.rgb = COLOR_TITLE

p_note = doc.add_paragraph()
p_note.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_note = p_note.add_run("CONCEPT NOTE\nNon-Invasive Dual-Site Edge-AI Anemia Screening for Primary Care & Community Triage")
r_note.bold = True
r_note.font.size = Pt(11.5)
r_note.font.color.rgb = COLOR_H1

p_ver = doc.add_paragraph()
p_ver.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_ver = p_ver.add_run("Document Version 2.0 (Empirically Grounded & Probabilistically Calibrated)  |  October 2026")
r_ver.italic = True
r_ver.font.size = Pt(8.5)
r_ver.font.color.rgb = COLOR_MUTED

doc.add_paragraph()

# ─── SECTION I: SUMMARY ──────────────────────────────────────────────────────
add_heading(doc, "I. SUMMARY", 1)
add_body(doc, "Philippine maternal mortality is a solvable crisis — and TingínHB is the unlock. Every year, more than 2,000 Filipino mothers die from Postpartum Hemorrhage (PPH), the country's leading obstetric killer. The root cause hiding in plain sight: 21.8% to 28.0% of pregnant women enter labor severely anemic (DOST-FNRI, 2024), yet over 200,000 Barangay Health Workers (BHWs) — the frontline workforce that sees these mothers first — have no affordable, reliable tool to detect it.")
add_body(doc, "TingínHB (\"See\" + hemoglobin) is an offline-first, smartphone-based edge-AI hemoglobin triage support system designed for Philippine Barangay Health Workers and rural primary care clinics. Point the smartphone camera at two complementary microvascular sites—the palpebral conjunctiva (primary, zero-melanin mucosal surface with in-frame scleral white balance) and the subungual nail bed (secondary, translucent keratin plate with periungual melanin normalization)—and in under 2 seconds, with zero blood draw, zero disposable test strips, and zero internet connectivity, TingínHB delivers a calibrated statistical probability score stratified into actionable WHO triage tiers at ₱0.00 consumable cost.")
add_body(doc, "Crucially, acknowledging the biological noise floor of ambient smartphone colorimetry, TingínHB rejects false precision: it does not output an arbitrary hemoglobin decimal. Instead, it computes an epistemic uncertainty-weighted posterior likelihood of moderate-to-severe anemia (Hb < 10.0 g/dL). For patients flagged in high-risk tiers, TingínHB automatically generates a standardized PhilHealth Konsulta referral PDF ready for immediate clinical submission. Wired directly into Republic Act No. 11148 (First 1,000 Days Law) and Republic Act No. 11223 (Universal Health Care Act), TingínHB operationalizes frontline early detection where it matters most.")

# ─── SECTION II: BACKGROUND OF THE PROBLEM ──────────────────────────────────
add_heading(doc, "II. BACKGROUND OF THE PROBLEM", 1)

add_heading(doc, "1. The Public Health Burden in the Philippines", 2)
add_body(doc, "Anemia remains an intractable, inter-generational crisis across the Philippine archipelago:")
for b in [
    "Maternal Lethality: The Philippines loses over 2,000 mothers annually to Postpartum Hemorrhage (PPH)—accounting for ~30% of maternal deaths. DOST-FNRI Expanded National Nutrition Surveys reveal 21.8% to 28.0% of pregnant Filipino women are clinically anemic. Severe anemia strips the uterine myometrium of the oxygen and energetic reserve needed to contract post-delivery, multiplying fatal hemorrhage risk by 2.5- to 4.0-fold.",
    "Infant Cognitive Deprivation: 40% to 45% of Filipino infants aged 6–11 months suffer from iron deficiency anemia, causing irreversible loss of 5–10 IQ points during the critical first 1,000 days of life.",
    "Adolescent & Economic Toll: 15% to 20% of adolescent females are anemic, entering pregnancy depleted. The World Bank estimates iron deficiency anemia costs developing nations 1.5% to 4.0% of GDP annually in lost labor and cognitive productivity.",
]:
    add_bullet(doc, b)

add_heading(doc, "2. The Clinical Diagnostic Gap: Access Bottleneck vs. Analytical Cost", 2)
add_body(doc, "The diagnostic breakdown is not the laboratory cost of a Complete Blood Count (CBC, ₱200–₱350), but physical geographic accessibility:")
for b in [
    "Rural and GIDA Realities: Barangay Health Stations (BHS) lack centrifuges, reagents, automated hematology analyzers, and medical technologists. Patients in Geographically Isolated and Disadvantaged Areas (GIDA) face 2 to 6 hours of travel and ₱300 to ₱800 in round-trip transport fares—frequently exceeding total daily household income.",
    "HemoCue Stockout Paradox: Digital point-of-care analyzers (HemoCue Hb 301) carry a capital cost of ₱70,000–₱125,000 per unit, and their disposable microcuvettes cost ₱105–₱150 per fingerstick, leading to chronic municipal stockouts.",
    "Naked-Eye Subjectivity: Over 200,000 BHWs rely on naked-eye physical pallor inspection under WHO IMCI protocols. Peer-reviewed clinical literature (Strobach et al., 1988, JAMA; Kalter et al., 1997, Bull WHO) proves naked-eye sensitivity is only 10% to 60%, with an inter-observer agreement kappa of only κ = 0.20–0.45 (poor to slight agreement).",
]:
    add_bullet(doc, b)

add_figure_placeholder(
    doc,
    fig_num=1,
    title="Philippine Maternal Anemia & PPH Burden",
    suggested_visual="Infographic chart / map combining prevalence data, maternal mortality breakdown, and GIDA health access geography.",
    items=[
        "DOST-FNRI Anemia Prevalence: Bar chart highlighting 21.8% to 28.0% in pregnant women and 40%–45% in infants aged 6–11 months.",
        "Philippine Maternal Mortality: Pie chart showing Postpartum Hemorrhage (PPH) causing ~30% of maternal deaths (~2,000+ deaths/yr), with a 4-fold risk multiplier in anemic mothers.",
        "Geographic CBC Bottleneck: Accessibility map contrasting urban laboratory density (₱200–₱350 CBC) vs. rural GIDA barangays requiring 2–6 hours travel and ₱300–₱800 fare.",
        "HemoCue Stockout Paradox: Comparison showing ₱70k–₱125k capital cost and ₱150/test cuvette vs. ₱0 consumable smartphone triage.",
    ],
    caption="The Maternal Anemia and Diagnostic Desert in the Philippines.",
    data_sources="DOST-FNRI Expanded National Nutrition Survey (2020); DOH Maternal Health Statistics; Philippine Statistics Authority (PSA) Vital Statistics."
)

# ─── SECTION III: PROPOSED STARTUP SOLUTION ──────────────────────────────────
add_heading(doc, "III. PROPOSED STARTUP SOLUTION", 1)

add_heading(doc, "1. Biological & Optical Physics Grounding", 2)
add_body(doc, "TingínHB is strictly grounded in microvascular optical absorption physics across two complementary anatomical sites:")
for b in [
    "Primary Site — Palpebral Conjunctiva (Inner Lower Eyelid): The conjunctival epithelium is naturally devoid of melanocytes (Stolz et al., 1993), making optical evaluation completely invariant across Filipino skin tones (Fitzpatrick phototypes III–VI). Oxygenated hemoglobin displays characteristic absorption peaks at 540 nm and 576 nm (green spectrum). Crucially, the exposed sclera (white of the eye) serves as an in-frame white-balance anchor, eliminating physical calibration cards.",
    "Secondary Site — Subungual Nail Bed: Visualizes the subungual capillary plexus through a uniform 0.5–0.8 mm translucent keratin plate, avoiding light scattering from skin calluses. Periungual skin melanin is computationally normalized using the Contrast Ratio (CR) formula: CR = (G_nail - G_skin) / (G_nail + G_skin) (Mannino et al., 2018).",
]:
    add_bullet(doc, b)

add_figure_placeholder(
    doc,
    fig_num=2,
    title="Microvascular Optical Anatomy & Spectral Absorption",
    suggested_visual="Multi-panel optical physics diagram comparing conjunctiva and subungual nail bed signal paths.",
    items=[
        "Oxygenated Hemoglobin Absorption Curve: Spectral plot showing distinct extinction peaks at 540 nm and 576 nm within the green color spectrum.",
        "Palpebral Conjunctiva Cross-Section: Microvascular diagram illustrating non-keratinized epithelium with zero melanocytes (Fitzpatrick I–VI invariance) and adjacent white sclera anchor.",
        "Subungual Nail Bed Optical Transmission: Diagram showing 0.5–0.8 mm translucent keratin plate, subungual microvascular plexus, and periungual Contrast Ratio (CR) melanin subtraction zone.",
    ],
    caption="Optical Transmission and Chromophore Absorption in Primary Anatomical Sites.",
    data_sources="Prahl (1999); Kim et al. (2020, PNAS); Mannino et al. (2018, Nature Communications)."
)

add_heading(doc, "2. Edge-AI Architecture & Probabilistic Posterior Modeling", 2)
add_body(doc, "Rather than predicting an ungrounded continuous decimal (e.g. '11.2 g/dL'), TingínHB deploys an epistemic uncertainty-aware Bayesian framework:")
for b in [
    "ROI Segmentation: A quantized YOLOv8n-seg model (INT8, ~3.5 MB, 80ms) detects and crops the palpebral conjunctiva, sclera, and nail plate polygons.",
    "Dual-Branch Deep Radiomics: Combines deep convolutional features from MobileNetV3-Small (FP16, ~5.2 MB) with 16 handcrafted colorimetric radiomics (Erythema Index, Pallor Index, green-red channel ratios).",
    "Monte Carlo Dropout: Executes N=50 stochastic inference passes to estimate epistemic model uncertainty (σ).",
    "Post-Hoc Probability Calibration: Maps continuous estimates into a calibrated posterior probability of moderate-to-severe anemia (Hb < 10.0 g/dL) using Platt Scaling, maintaining Expected Calibration Error ECE ≤ 0.08.",
]:
    add_bullet(doc, b)

add_figure_placeholder(
    doc,
    fig_num=3,
    title="End-to-End Edge-AI Pipeline Architecture",
    suggested_visual="Neural network architecture schematic diagram illustrating offline edge inference.",
    items=[
        "Assisted Image Acquisition: Camera viewfinder with elliptical guide overlays and real-time Laplacian blur filtering.",
        "Region of Interest Segmentation: YOLOv8n-seg (INT8, ~3.5 MB, 80ms) generating polygon masks for conjunctiva, sclera, and nail plate.",
        "Dual-Branch Feature Extractor: Deep convolutional representations via MobileNetV3-Small (FP16, ~5.2 MB) parallel to 16 handcrafted colorimetric radiomics (Erythema Index, Pallor Index).",
        "Bayesian Uncertainty Engine: Monte Carlo Dropout (N=50 stochastic passes) generating Gaussian parameters (ŷ ± σ) followed by Platt Scaling probability calibration.",
    ],
    caption="Dual-Branch Deep Learning Pipeline and Bayesian Uncertainty Engine (<10 MB runtime footprint).",
    data_sources="Gal & Ghahramani (2016, ICML); Platt (1999); TinginHB Edge Software Specification."
)

add_heading(doc, "3. Dynamic 5-Modality Clinical Indicator Matrix & Missing Modalities", 2)
add_body(doc, "To ensure robustness when a child resists eyelid eversion or a BHW lacks a blood pressure cuff, TinginHB employs a dynamic multi-modal fusion architecture that gracefully handles missing inputs (Baltrusaitis et al., 2019; Huang et al., 2020):")

add_table(doc,
    ["Indicator / Modality", "Collection Method", "Weight", "Clinical Diagnostic Grounding"],
    [
        ["1. Palpebral Conjunctiva", "Camera macro crop (YOLOv8n-seg)", "35%", "Highest SNR: zero melanin; 540 & 576 nm absorption peaks; scleral white balance (Kim et al., 2020)."],
        ["2. Subungual Nail Bed",    "Camera macro with Contrast Ratio", "25%", "Uniform keratin transmission; periungual melanin subtracted (Mannino et al., 2018)."],
        ["3. Patient Survey / Risk", "4-tap UI: Age, Pregnancy, Symptoms", "15%", "Epidemiological Bayesian Prior: aligned with DOH Target Client List & WHO ANC (WHO, 2016)."],
        ["4. Palmar Creases",        "Open-hand photo (YOLOv8n-seg)",     "15%", "WHO IMCI Fallback: deep creases blanch only at severe anemia (Kalter et al., 1997)."],
        ["5. Blood Pressure & Pulse", "Input from standard DOH BP cuff", "10%", "Compensatory Tachycardia: detects resting HR > 100 bpm from chronic hypoxia (Duke & Abelmann, 1969)."],
    ],
    col_widths=[4.5, 4.0, 1.8, 6.7]
)

add_body(doc, "Missing Modality Re-normalization & Log-Odds Stacking:")
add_code_block(doc,
"w'_i = w_i / SUM(w_available)\n"
"ln(Odds_post) = ln(Odds_prior(Survey)) + SUM(w'_i * ln(LR_i))\n\n"
"• Full Clinic Check (All 5): Eye (35%) + Nail (25%) + Survey (15%) + Palm (15%) + BP (10%) = 100%\n"
"• Field Visit (Eye + Nail + Survey): Eye (46.7%) + Nail (33.3%) + Survey (20.0%) = 100%\n"
"• Pediatric Fallback (Nail + Palm + Survey): Nail (45.5%) + Palm (27.3%) + Survey (27.3%) = 100%\n"
"• Discrepancy Gate: If |Eye - Nail| > 2.0 g/dL, palmar crease scan is triggered to break ambiguity."
)

add_figure_placeholder(
    doc,
    fig_num=4,
    title="5-Modality Decision Tree & Missing Modality Flowchart",
    suggested_visual="Decision flow diagram / workflow tree illustrating graceful degradation across clinical scenarios.",
    items=[
        "Modality Acquisition Gate: Simultaneous check for active inputs: Conjunctiva (35%), Nail Bed (25%), Patient Survey (15%), Palmar Creases (15%), BP / Pulse (10%).",
        "Dynamic Weight Normalization Engine: Re-scaling formula w'_i = w_i / SUM(w_avail) adapting weights for Full Clinic (100%), Rapid Field Visit (75%), and Pediatric Fallback (55%).",
        "Discrepancy & Plausibility Checker: Automated check triggering palmar crease scan if |Eye - Nail| > 2.0 g/dL to rule out unilateral conjunctival inflammation.",
        "Bayesian Evidence Stacking: Likelihood ratio log-odds fusion yielding calibrated posterior probability mapped to 4-tier WHO Triage Action Protocols.",
    ],
    caption="5-Modality Dynamic Weighting Decision Tree and Missing-Modality Fallback Workflow.",
    data_sources="Baltrusaitis et al. (2019, IEEE TPAMI); Huang et al. (2020, npj Digital Medicine); Strobach et al. (1988, JAMA)."
)

add_heading(doc, "4. Calibrated Four-Tier Triage Classification", 2)
add_table(doc,
    ["Probability Score", "Triage Classification", "Clinical Interpretation", "Action Protocol for BHW"],
    [
        ["P < 0.25",         "🟢 NORMAL (Anemia Unlikely)",     "Normal perfusion",            "Continue standard ANC + Iron-Folic Acid Supplementation"],
        ["0.25 ≤ P < 0.55", "🟡 INCONCLUSIVE (Recheck Buffer)", "Within noise floor / mild",   "Reposition under natural light, repeat scan; review IFAS adherence"],
        ["0.55 ≤ P < 0.80", "🟠 MODERATE (Possible Anemia)",   "Elevated probability Hb < 10", "REFER to RHU for confirmatory CBC and clinical assessment"],
        ["P ≥ 0.80",         "🔴 SEVERE (Likely Anemia)",       "High probability mod-severe",  "URGENT referral to District Hospital; Auto-generate Konsulta PDF"],
    ],
    col_widths=[3.2, 4.5, 4.3, 5.0]
)

# ─── SECTION IV: OBJECTIVES & SCIENTIFIC RELIABILITY BOUNDS ──────────────────
add_heading(doc, "IV. OBJECTIVES", 1)
for b in [
    "Eliminate Consumable Cost Barriers: Deploy a ₱0-per-screening tool to replace ₱150/cuvette consumable methods across Barangay Health Stations and Rural Health Units.",
    "Dramatically Reduce Missed Diagnoses: Achieve AUROC ≥ 0.88 and ≥85% sensitivity for moderate-to-severe anemia (Hb < 10.0 g/dL), up from 10–60% sensitivity of naked-eye pallor.",
    "Accelerate High-Risk Patient Referrals: Reduce time-to-referral through one-tap automated generation of PhilHealth Konsulta referral PDF slips.",
    "Deploy in 100% Offline GIDA Settings: Operate completely on-device with a <10 MB AI footprint runnable on low-end ₱5,000 Android 8.0+ devices.",
    "Validate in Philippine Cohort: Execute a prospective STARD-compliant field validation study (n = 250, paired with laboratory automated CBC) within 12 months.",
]:
    add_bullet(doc, b)

add_heading(doc, "Explicit Scientific Reliability Bounds & Limitations", 2)
for b in [
    "The Mild Anemia Detection Limit: Optical pallor is a physiological lagging indicator (Kalter et al., 1997). Under smartphone RGB sensors, pallor does not reliably separate from normal perfusion until hemoglobin drops below ~9.0–10.0 g/dL. TinginHB is explicitly NOT designed or marketed to diagnose mild anemia (11.0–11.9 g/dL). A green result does not rule out early-stage iron deficiency.",
    "Triage Decision Support, Not Laboratory Diagnostic: TinginHB never issues a definitive medical diagnosis; it identifies individuals requiring urgent confirmatory CBC.",
    "Known Confounders: Active conjunctivitis (produces redness/false negatives), jaundice (distorts scleral reference), hypothermia (causes peripheral vasoconstriction), and onychomycosis (blocks nail bed transmission).",
]:
    add_bullet(doc, b)

# ─── SECTION V: TARGET MARKET / BENEFICIARIES ────────────────────────────────
add_heading(doc, "V. TARGET MARKET / BENEFICIARIES", 1)

add_heading(doc, "Primary Users (App Operators)", 2)
for b in [
    "~75,000–200,000 Barangay Health Workers (BHWs) conducting community house-to-house tracking.",
    "Rural Health Unit (RHU) nurses and midwives conducting antenatal care and Well-Baby checkups.",
]:
    add_bullet(doc, b)

add_heading(doc, "Primary Beneficiaries (Patients Screened)", 2)
for b in [
    "Pregnant Filipino women (~1.7 million deliveries/year; 21.8% to 28.0% entering labor anemic).",
    "Infants 6–24 months (~2.2 million; 40–45% anemic during the critical first 1,000 days).",
    "Adolescent females in DepEd Weekly Iron and Folic Acid Supplementation (WIFA) programs.",
]:
    add_bullet(doc, b)

add_heading(doc, "Institutional Customers (Procuring Bodies)", 2)
for b in [
    "Department of Health (DOH) and Local Government Units (LGUs) under Universal Health Care (RA 11223).",
    "PhilHealth Konsulta-accredited primary care provider networks.",
    "International NGOs: UNFPA, UNICEF, Helen Keller International, Zuellig Family Foundation.",
    "Geographic Launchpad: Northern Mindanao (Region X) rural LGUs, anchored by USTP Cagayan de Oro.",
]:
    add_bullet(doc, b)

# ─── SECTION VI: VALUE PROPOSITION ───────────────────────────────────────────
add_heading(doc, "VI. VALUE PROPOSITION", 1)
add_body(doc, "TingínHB delivers an unmatched combination of clinical accessibility, scientific honesty, and Philippine health policy integration:")

add_table(doc,
    ["Feature / Dimension", "TingínHB (DataLunas)", "HemoCue Hb 301", "AnemoCheck (US)", "Naked-Eye Pallor"],
    [
        ["Cost per Test",       "₱0.00 (Zero Consumables)", "₱105–₱150 / cuvette",  "~$5 USD + prior CBC",    "₱0.00"],
        ["Capital Equipment",   "₱0 (Existing Smartphone)", "₱70,000–₱125,000",     "Smartphone only",        "₱0.00"],
        ["Sites Assessed",      "Dual: Conjunctiva + Nail",  "Fingerstick (Blood)",  "Nail Bed Only",          "Variable / Subjective"],
        ["Requires Prior CBC",  "NO (Zero Personalization)", "No (Factory Calib.)",  "YES (Mandatory)",        "None"],
        ["Melanin-Independent", "YES (0-Melanin Mucosa)",    "Yes (Invasive)",       "NO (Skin Tone Bias)",    "NO (Severe Bias)"],
        ["Output Type",         "Calibrated Probability",   "Absolute Hb (g/dL)",   "Continuous Hb (g/dL)",   "Subjective Guess"],
        ["Offline Ready",       "100% Offline (<10 MB)",     "100% Offline",         "Requires Cloud Sync",    "Offline"],
        ["PH Policy Integration","Konsulta PDF Auto-Slip",   "None",                 "None",                   "Manual Paper Logs"],
        ["Biohazardous Waste",  "NONE (Non-Invasive)",       "Lancets & Cuvettes",   "None",                   "None"],
    ],
    col_widths=[3.5, 3.8, 3.5, 3.5, 2.7]
)

add_figure_placeholder(
    doc,
    fig_num=5,
    title="Frontline BHW Mobile App UI & Referral PDF Mockup",
    suggested_visual="High-fidelity 4-screen mobile user interface flow and printable referral document mockup.",
    items=[
        "Screen 1 (Assisted Capture): Viewfinder with green positioning guide, real-time focus validation, and auto-exposure lock.",
        "Screen 2 (4-Tap Clinical Survey): Minimalist questionnaire for patient age, pregnancy trimester, and acute symptoms (dizziness/fatigue).",
        "Screen 3 (Calibrated Triage Card): Actionable color-coded risk card displaying posterior probability band, clear Filipino/English directives, and auditory cues.",
        "Screen 4 (PhilHealth Konsulta Referral Letter): Automated 1-page PDF referral form with patient metadata, observed clinical cues, risk tier, and QR verification code for RHU doctor.",
    ],
    caption="TinginHB Frontline User Interface and Automated PhilHealth Konsulta Referral Workflow.",
    data_sources="DOH Telemedicine Guidelines; PhilHealth Circular 2022-0005 (Konsulta Package)."
)

# ─── SECTION VII: BUSINESS MODEL ─────────────────────────────────────────────
add_heading(doc, "VII. BUSINESS MODEL", 1)
add_body(doc, "TingínHB follows a freemium public-health B2G model. The BHW screening application is perpetually free—because neither the indigent mother nor the voluntary health worker is the financial buyer. Revenue flows from institutional health buyers whose procurement budgets achieve immediate cost savings:")

add_table(doc,
    ["Revenue Stream", "Description & Target Pricing", "Projected Timeline"],
    [
        ["DOH / LGU Enterprise SaaS", "Municipal/provincial annual license (₱500–₱1,000/BHW/yr) for maternal epidemiological dashboards and Konsulta API sync. 10% BHW adoption = ₱3.75M ARR.", "Year 3+"],
        ["NGO / Development Procurement", "Annual bulk deployment license to maternal programs (UNFPA, UNICEF, Zuellig Foundation) at ₱50,000–₱150,000 per program.", "Year 2+"],
        ["DICT / PSC XI Seed Grant", "Seed funding from PSC XI competition prize and DICT Startup Grant Fund (SGF) for prototype finalization and regulatory filings.", "Year 1"],
        ["Research / Clinical Partnerships", "Collaborative clinical validation grants with DOH tertiary hospitals and academic institutions.", "Year 1–2"],
    ],
    col_widths=[4.5, 9.0, 3.5]
)

add_body(doc, "Macro-Economic Cost Avoidance: Replacing just one single-use HemoCue microcuvette (₱150) across 50,000 monthly community screenings saves local government health budgets over ₱7.5 Million monthly in recurring procurement waste.")

# ─── SECTION VIII: MARKET ANALYSIS ───────────────────────────────────────────
add_heading(doc, "VIII. MARKET ANALYSIS", 1)

add_heading(doc, "Market Sizing", 2)
for b in [
    "Total Addressable Market (TAM): 75,000 BHWs × 12 antenatal screenings/BHW/month = ~900,000 screenings/month nationwide. At ₱150/avoided HemoCue cuvette, this represents ₱135M/month in quantifiable government cost avoidance at full national scale.",
    "Serviceable Addressable Market (SAM, Years 1–2): 5–10 GIDA municipalities in Northern Mindanao (1,500–3,000 BHWs, 18,000–36,000 screenings/month) acting as the primary regional evidence-building cohort.",
]:
    add_bullet(doc, b)

add_heading(doc, "Competitive Landscape & Market Drivers", 2)
for b in [
    "HemoCue Hb 301: The analytical point-of-care gold standard, but limited by device capital cost (₱125,000) and cuvette stockouts. TinginHB acts as a pre-filter, reserving HemoCue cuvettes for high-probability cases.",
    "AnemoCheck (Sanguina, US): Consumer-focused, nail-only, melanin-sensitive, requires lab CBC calibration, and is unavailable in the Philippines.",
    "Regulatory & Policy Tailwinds: DOH Digital Health Transformation Roadmap (2023–2028), Universal Health Care Act (RA 11223), and First 1,000 Days Law (RA 11148) mandate diagnostic coverage expansion to GIDAs.",
]:
    add_bullet(doc, b)

# ─── SECTION IX: OPERATIONS PLAN ─────────────────────────────────────────────
add_heading(doc, "IX. OPERATIONS PLAN", 1)
add_body(doc, "TingínHB executes a structured 12-month research and deployment roadmap across five workstreams:")

add_code_block(doc,
"[ Phase 1: Months 1–2 ]  Dataset Curation & Synthetic Augmentation\n"
"                         • Preprocess Ghana (710 eye, 4,260 nail, 4,260 palm) & Peru cohorts\n"
"                         • Train YOLOv8n-seg region proposal models\n\n"
"[ Phase 2: Months 2–3 ]  Dual-Branch Model Training & MC Dropout\n"
"                         • Train MobileNetV3-Small deep branch + 16-feature radiomics branch\n"
"                         • Implement Huber loss & Platt probability calibration (ECE ≤ 0.08)\n\n"
"[ Phase 3: Months 3–5 ]  Android Edge Integration & Usability Testing\n"
"                         • TFLite quantization, offline PDF referral generation\n"
"                         • Co-design usability trials with student and rural BHW volunteers\n\n"
"[ Phase 4: Months 5–8 ]  Prospective Clinical Field Validation (STARD Compliant)\n"
"                         • Target n = 250 subjects at Cagayan de Oro RHUs\n"
"                         • Paired with laboratory automated CBC (Sysmex XN-550) within 2 hours\n"
"                         • Primary Endpoint: AUROC ≥ 0.88 for Hb < 10.0 g/dL\n\n"
"[ Phase 5: Months 8–10]  PhilHealth Konsulta & DOH Maternal Dashboard Linking\n"
"                         • Cloud synchronization for municipal health officers\n\n"
"[ Phase 6: Months 10–12] Regulatory Filing & Academic Dissemination\n"
"                         • File for Philippine FDA Medical Device Classification (Software)\n"
"                         • Submit manuscript to peer-reviewed digital health journal"
)

add_figure_placeholder(
    doc,
    fig_num=6,
    title="Prospective Clinical Validation Design & ROC Curve",
    suggested_visual="Dual-panel clinical validation methodology schema and target diagnostic performance curve.",
    items=[
        "STARD Study Flowchart: Prospective recruitment schema of N=250 subjects at Cagayan de Oro City Health Centers (100 pregnant women, 75 infants/children, 75 general adults).",
        "Paired Reference Testing: Double-blinded evaluation between non-invasive TinginHB index test and automated venous complete blood count (Sysmex XN-550) within a 2-hour window.",
        "Target ROC / AUROC Curves: Expected Receiver Operating Characteristic curve displaying target AUROC >= 0.88 for moderate-to-severe anemia (Hb < 10.0 g/dL), with Sensitivity >= 85% and Specificity >= 80%.",
    ],
    caption="Prospective Clinical Field Validation Design (STARD Compliant) and Expected ROC Diagnostic Curves.",
    data_sources="Bossuyt et al. (2015, STARD 2015); Kim et al. (2020, PNAS); Mannino et al. (2018)."
)

add_figure_placeholder(
    doc,
    fig_num=7,
    title="12-Month Research & Product Roadmap Gantt Chart",
    suggested_visual="Horizontal Gantt Chart timeline spanning Months 1 through 12 across 5 core development workstreams.",
    items=[
        "Workstream 1 (Months 1–2): Dataset Curation & Synthetic Augmentation (Ghana & Peru cohorts, YOLOv8n-seg models).",
        "Workstream 2 (Months 2–3): Dual-Branch Model Training & MC Dropout (MobileNetV3-S + radiomics, Platt calibration ECE <= 0.08).",
        "Workstream 3 (Months 3–5): Android Edge App Development & Usability Testing (quantized TFLite, BHW co-design).",
        "Workstream 4 (Months 5–8): Prospective Clinical Trials (N=250) in Cagayan de Oro RHUs with Ethics Review Board (REC/IRB) approval.",
        "Workstream 5 (Months 8–10): DOH Maternal Dashboard & PhilHealth Konsulta API Integration.",
        "Workstream 6 (Months 10–12): Philippine FDA Class B Medical Device Software Notification & PSC XI Pitch Deployment.",
    ],
    caption="TinginHB 12-Month Multi-Phase Research, Clinical Validation, and Commercialization Roadmap.",
    data_sources="DOH Health Technology Assessment (HTA) Guidelines; Universal Health Care Act (RA 11223)."
)

add_heading(doc, "Team Roles & Responsibilities", 2)
for b in [
    "Rogelio Q. Mandamian III — Lead AI/ML Engineer: Model architecture, TFLite INT8 quantization, Monte Carlo Dropout uncertainty engine, dual-site Bayesian fusion.",
    "Kirsten Roise Moog — Mobile Application Developer: Flutter cross-platform UI, CameraX optical guided capture, offline SQLite patient registry, PhilHealth Konsulta PDF generation.",
    "[3rd Member — TBD] — Data Engineer & Field Liaison: Dataset curation, BHW field training, clinical pilot coordination.",
    "[Faculty Mentor — TBD] — Research & Clinical Adviser: Institutional endorsement, Ethics Review Committee (REC/IRB) supervision, hospital network liaison.",
]:
    add_bullet(doc, b)

# ─── SECTION X: FINANCIAL REQUIREMENT ────────────────────────────────────────
add_heading(doc, "X. FINANCIAL REQUIREMENT", 1)
add_body(doc, "TingínHB requests ₱280,000 in seed capital to cover prototype finalization, Philippine clinical validation, and initial field pilot deployment. This constitutes a one-time development investment—subsequent deployments carry ₱0 per-device or per-screening cost:")

add_table(doc,
    ["Budget Line Item", "Amount (PHP)", "Justification & Milestone"],
    [
        ["GPU Compute / Cloud Credits for AI Training", "₱ 80,000", "Model training, hyperparameter sweep, synthetic augmentation, INT8 quantization."],
        ["Mobile Test Devices (3× Low/Mid/High Tier)",  "₱ 30,000", "Cross-device camera sensor calibration, CameraX QA, low-end SoC latency testing."],
        ["Philippine Clinical Validation Study (n=250)", "₱ 80,000", "Paired Sysmex CBC testing fees, IRB review fees, travel to CDO health stations."],
        ["App Development Tools & PDF Deployment",      "₱ 20,000", "Flutter production build, offline SQLite encryption, PDF reporting libraries."],
        ["PFDA Regulatory Consultation & SaMD Filing",  "₱ 30,000", "Class B Medical Device Software regulatory pre-assessment consultation."],
        ["BHW Training Materials & Orientation Media",  "₱ 15,000", "Laminated quick-start pocket guides, video orientation modules."],
        ["Contingency Buffer (10%)",                     "₱ 25,000", "Unforeseen field logistics or technical adjustments."],
        ["TOTAL SEED BUDGET",                            "₱ 280,000", "Complete 12-Month Operational Milestone"],
    ],
    col_widths=[6.5, 3.2, 7.3]
)

add_heading(doc, "Proposed Funding Sources", 2)
for b in [
    "PSC XI Award Prize — Primary seed capital for prototyping and initial testing.",
    "DICT Startup Grant Fund (SGF) — Second-tranche application post-PSC competition.",
    "USTP Research Grant / Technology Transfer Office — Institutional co-funding and facility access.",
    "DOST-PCHRD Small Grant for Health Innovation — Clinical field validation phase support.",
]:
    add_bullet(doc, b)

# ─── SECTION XI: REFERENCES & ACADEMIC GROUNDING ─────────────────────────────
add_heading(doc, "XI. REFERENCES & ACADEMIC GROUNDING", 1)
refs = [
    "World Health Organization (2011). Haemoglobin concentrations for the diagnosis of anaemia and assessment of severity. WHO/NMH/NHD/MNM/11.1.",
    "World Health Organization (2013). Pocket book of hospital care for children (2nd ed.). Section: Assessment of palmar and conjunctival pallor (IMCI).",
    "World Health Organization (2016). WHO recommendations on antenatal care for a positive pregnancy experience. WHO Guidelines Approved by the Guidelines Review Committee.",
    "Strobach, R. S., Anderson, S. K., Doll, D. C., & Ringenberg, Q. S. (1988). The value of the physical examination in diagnosing anemia. JAMA, 259(11), 1682–1685.",
    "Kalter, H. D., Burnham, G., Kolstad, P. R., et al. (1997). Evaluation of clinical signs to diagnose anaemia in Uganda and Bangladesh. Bulletin of the WHO, 75(Suppl 1), 103–111.",
    "Luby, S. P., Kazembe, P. N., Redd, S. C., et al. (1995). Using clinical signs to diagnose anaemia in African children. Bulletin of the WHO, 73(4), 477–482.",
    "Duke, M., & Abelmann, W. H. (1969). The hemodynamic response to chronic anemia. Circulation, 39(4), 503–515.",
    "Varat, M. A., Adolph, R. J., & Fowler, N. O. (1972). Cardiovascular effects of severe anemia. American Heart Journal, 83(3), 415–426.",
    "Kim, T. N., et al. (2020). Smartphone-based assessment of anemia from conjunctival images. PNAS, 117(49), 31046–31055.",
    "Kim, T. N., et al. (2023). Validation of a smartphone-based conjunctival assessment for anemia in outpatients. Annals of Internal Medicine, 176(3), 302–310.",
    "Mannino, R. G., Myers, D. R., Tyburski, E. A., et al. (2018). Smartphone app for non-invasive detection of anemia using only patient-sourced photos. Nature Communications, 9(1), 4924.",
    "Dimauro, G., Ciprandi, D., Deperte, F., et al. (2018). Ocular redness measurement in non-contact and non-invasive diagnoses of anaemia. Journal of Imaging, 4(8), 95.",
    "Valles-Coral, M. A., et al. (2025). AnaeCare: Non-invasive anemia detection from smartphone images using multi-site pallor analysis. arXiv:2503.XXXXX.",
    "Baltrusaitis, T., Ahuja, C., & Morency, L. P. (2019). Multimodal machine learning: A survey and taxonomy. IEEE TPAMI, 41(2), 423–443.",
    "Huang, S. C., Pareek, A., Seyyedi, S., et al. (2020). Fusion of medical imaging and electronic health records using deep learning. npj Digital Medicine, 3(1), 136.",
    "Gal, Y., & Ghahramani, Z. (2016). Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning. ICML, 48, 1050–1059.",
    "Platt, J. (1999). Probabilistic outputs for support vector machines and comparisons to regularized likelihood methods. Advances in Large Margin Classifiers, 10(3), 61–74.",
    "Food and Nutrition Research Institute (DOST-FNRI, 2020). Expanded National Nutrition Survey: Nutritional Status of Filipino Children and Pregnant Women.",
    "Republic of the Philippines (2018). Republic Act No. 11148: Kalusugan at Nutrisyon ng Mag-Nanay Act (First 1,000 Days Law).",
    "Republic of the Philippines (2019). Republic Act No. 11223: Universal Health Care Act.",
]
for i, ref in enumerate(refs, 1):
    para = doc.add_paragraph()
    para.paragraph_format.left_indent = Cm(0.5)
    para.paragraph_format.first_line_indent = Cm(-0.5)
    run = para.add_run(f"{i}. {ref}")
    run.font.size = Pt(8.5)
    set_para_spacing(para, before=1, after=2)

# Footer
doc.add_paragraph()
f_para = doc.add_paragraph()
f_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
fr = f_para.add_run("Team DataLunas — University of Science and Technology of Southern Philippines (USTP)\nDepartment of Data Science | College of Information Technology and Computing | Cagayan de Oro City")
fr.italic = True
fr.font.size = Pt(8.5)
fr.font.color.rgb = COLOR_MUTED

try:
    doc.save(OUTPUT_PATH)
    print(f"[OK] Concept Note saved to:\n    {OUTPUT_PATH}")
except PermissionError:
    alt_path = OUTPUT_PATH.replace(".docx", "_v2.docx")
    doc.save(alt_path)
    print(f"[NOTE] '{os.path.basename(OUTPUT_PATH)}' is locked.")
    print(f"[OK] Saved version to:\n    {alt_path}")
