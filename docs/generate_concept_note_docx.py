"""
generate_concept_note_docx.py
Generates TinginHB_Revised_Concept_Note_PSCXI.docx
Run with: py docs/generate_concept_note_docx.py
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

# ─── BUILD DOCUMENT ──────────────────────────────────────────────────────────

doc = Document()

for section in doc.sections:
    section.top_margin    = Cm(2.2)
    section.bottom_margin = Cm(2.2)
    section.left_margin   = Cm(2.5)
    section.right_margin  = Cm(2.5)

doc.styles["Normal"].font.name = "Calibri"
doc.styles["Normal"].font.size = Pt(10)

# ─── TITLE HEADER ────────────────────────────────────────────────────────────
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("TinginHB")
run.bold = True
run.font.size = Pt(24)
run.font.color.rgb = COLOR_TITLE

p2 = doc.add_paragraph()
p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
run2 = p2.add_run("REVISED CONCEPT NOTE — PHILIPPINE STARTUP CHALLENGE XI")
run2.bold = True
run2.font.size = Pt(13)
run2.font.color.rgb = COLOR_H2

sub = doc.add_paragraph()
sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = sub.add_run("Non-Invasive Dual-Site Edge-AI Anemia Screening for Primary Care & Community Triage\n")
r.font.size = Pt(10.5)

meta = doc.add_paragraph()
meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
r2 = meta.add_run("Team DataLunas  |  University of Science and Technology of Southern Philippines (USTP)\nDepartment of Data Science  |  October 2026  |  Version 2.0 (Empirically Calibrated)")
r2.font.size = Pt(9)
r2.italic = True
r2.font.color.rgb = COLOR_MUTED

doc.add_paragraph()

# ─── SECTION I ───────────────────────────────────────────────────────────────
add_heading(doc, "I. EXECUTIVE SUMMARY", 1)
add_body(doc, "TinginHB (Tingin = 'to look/inspect'; HB = hemoglobin) is an offline-first, smartphone-based triage support system designed for Philippine Barangay Health Workers (BHWs) and rural primary care clinics. Rather than claiming to replace gold-standard Complete Blood Count (CBC) testing, TinginHB serves as a non-invasive, point-of-care triage engine that identifies individuals with a high probability of moderate-to-severe anemia (hemoglobin < 10.0 g/dL) who must be prioritized for confirmatory laboratory testing and clinical intervention.")
add_body(doc, "By capturing smartphone images of two complementary microvascular anatomical sites—the palpebral conjunctiva (primary, zero-melanin mucosal surface) and the subungual nail bed (secondary, translucent keratin plate)—TinginHB extracts optical and colorimetric features via quantized edge deep learning models (<10 MB, 100% offline). Crucially, acknowledging the biological and physical noise floor of ambient smartphone colorimetry, TinginHB rejects false precision: it does not output an absolute hemoglobin decimal. Instead, it outputs a statistically calibrated posterior probability score stratified into actionable WHO triage tiers (including an explicit 'Inconclusive / Recheck' buffer).")
add_body(doc, "TinginHB directly addresses the diagnostic desert in rural and Geographically Isolated and Disadvantaged Areas (GIDA), where over 200,000 BHWs currently rely on naked-eye pallor inspection—a method with an inter-observer agreement kappa of only κ = 0.20–0.45 (poor-to-fair agreement). By standardizing community triage at ₱0 consumable cost, TinginHB operationalizes early referral under the Universal Health Care Act (RA 11223) and the First 1,000 Days Law (RA 11148).")

# ─── SECTION II ──────────────────────────────────────────────────────────────
add_heading(doc, "II. BACKGROUND OF THE PROBLEM & THE CLINICAL SCREENING GAP", 1)

add_heading(doc, "1. The Public Health Burden in the Philippines", 2)
add_body(doc, "Anemia remains an intractable public health crisis in the Philippines:")
for b in [
    "Maternal Mortality: According to DOST-FNRI surveys, 21.8% to 28.0% of pregnant Filipino women are clinically anemic. Maternal anemia is a primary risk factor for Postpartum Hemorrhage (PPH)—responsible for ~30% of maternal deaths (~2,000+ deaths annually). Anemic mothers face up to a 4-fold increased risk of fatal PPH due to uterine atony.",
    "Infant Brain Development: 40% to 45% of Filipino infants aged 6–11 months suffer from iron deficiency anemia, leading to irreversible loss of 5–10 IQ points.",
    "Target Priority Populations: Under DOH and WHO guidelines, routine screening is mandated for pregnant mothers, infants, and adolescent females.",
]:
    add_bullet(doc, b)

add_heading(doc, "2. The Clinical Bottleneck: Access, Not Analytical Cost", 2)
add_body(doc, "A Complete Blood Count (CBC) is indeed an established, analytical gold standard and relatively inexpensive in urban laboratories (₱200–₱350). However, a CBC is only inexpensive if the patient can physically access a functioning laboratory:")
for b in [
    "In rural and GIDA barangays, there are no centrifuges, reagents, automated hematology analyzers, or medical technologists at the Barangay Health Station (BHS).",
    "Patients must travel 2 to 6 hours over rough terrain and pay ₱300–₱800 in round-trip transport fares—frequently exceeding their daily household income.",
    "Point-of-care digital hemoglobinometers (such as HemoCue Hb 301) cost ₱70,000–₱125,000 per device, and their microcuvettes cost ₱150 per fingerstick, creating chronic stockouts across rural LGUs.",
]:
    add_bullet(doc, b)

add_heading(doc, "3. The Current Frontline Reality: Subjective Naked-Eye Pallor", 2)
add_body(doc, "In the absence of point-of-care CBC, over 200,000 BHWs perform physical triage using naked-eye clinical pallor inspection under the WHO Integrated Management of Childhood Illness (IMCI) protocol. Peer-reviewed clinical evaluations (Strobach et al., 1988, JAMA; Kalter et al., 1997, Bull WHO) establish that naked-eye inspection has a wide sensitivity range of 10% to 60% for mild-to-moderate anemia, and inter-observer reliability between health workers is extremely low (κ = 0.20–0.45).")
add_body(doc, "TinginHB's Value Proposition is not analytical superiority over CBC; it is diagnostic accessibility and standardization over naked-eye triage.")

# ─── SECTION III ─────────────────────────────────────────────────────────────
add_heading(doc, "III. SCIENTIFIC GROUNDING & PRIOR ART ANALYSIS", 1)

add_heading(doc, "1. Biological and Optical Basis of Indicator Selection", 2)
for b in [
    "Primary Site — Palpebral Conjunctiva (Inner Lower Eyelid): Devoid of melanocytes, making it completely invariant to skin tone (Fitzpatrick I–VI). Oxygenated hemoglobin displays characteristic absorption peaks at 540 nm and 576 nm (green spectrum). The adjacent white sclera provides an in-scene white-balance anchor.",
    "Secondary Site — Subungual Nail Bed: Subungual capillary plexus viewed through a uniform 0.5–0.8 mm keratin plate, avoiding light scattering from calluses. Periungual skin melanin is normalized using the Contrast Ratio (CR) method (Mannino et al., 2018).",
]:
    add_bullet(doc, b)

add_heading(doc, "2. Prior Art Benchmarks", 2)
add_table(doc,
    ["Prior Art / Study", "Modality & Finding", "Documented Limitation"],
    [
        ["Mannino et al. (2018, Nature Comms)", "Sanguina / AnemoCheck — nail bed only; MAE = 1.47 g/dL; 95% LoA = ±2.4 g/dL", "Requires personalized CBC calibration; sensitive to skin tone without multi-site check."],
        ["Kim et al. (2020, PNAS; 2023, Annals)", "HemaChrome — conjunctiva only; Sens = 91.4% (severe); drops to 62.1% (mild)", "Confirms physical limit of mild pallor; single-site vulnerability to eye movement."],
        ["Valles-Coral et al. (2025, AnaeCare)", "AnaeCare — nails+palms+fingers; Macro F1 = 0.78; Mild class F1 = 0.52 (Peru)", "High capture friction (multiple images); lacks probabilistic uncertainty modeling."],
    ],
    col_widths=[5.5, 6.5, 5.0]
)

# ─── SECTION IV ──────────────────────────────────────────────────────────────
add_heading(doc, "IV. SYSTEM ARCHITECTURE & PROBABILISTIC REFRAMING", 1)

add_heading(doc, "1. Rejecting False Precision: The Bayesian Posterior Probability Framework", 2)
add_body(doc, "Best-in-class smartphone systems achieve an uncalibrated MAE of ≈ 1.5 g/dL. Because the WHO mild anemia threshold interval is only 1.0 g/dL wide (11.0–11.9 g/dL), predicting a single deterministic number (e.g., '11.2 g/dL') creates dangerous false confidence.")
add_body(doc, "TinginHB adopts a Probabilistic Bayesian Output Model:")
for b in [
    "Uncertainty Quantification (MC Dropout): N=50 stochastic passes extract epistemic uncertainty (σ).",
    "Inverse-Variance Bayesian Fusion: Combines eye and nail estimates weighted by precision (w = 1/σ²).",
    "Probability Transformation: Converts continuous Gaussian estimate into P(Moderate-Severe Anemia | features).",
    "Post-Hoc Calibration (Platt Scaling): Calibrates probabilities to achieve Expected Calibration Error ECE ≤ 0.08.",
]:
    add_bullet(doc, b)

add_heading(doc, "2. Actionable Triage Tiers with Safety Buffering", 2)
add_table(doc,
    ["Probability Score", "Triage Classification", "Clinical Interpretation", "Action Protocol for BHW"],
    [
        ["P < 0.25",         "🟢 Anemia Unlikely",              "Normal perfusion",            "Routine follow-up; nutrition counseling"],
        ["0.25 ≤ P < 0.55", "🟡 Inconclusive — Recheck",       "Within noise floor / mild",   "Reposition under natural light, repeat scan, or refer"],
        ["0.55 ≤ P < 0.80", "🟠 Possible Anemia — Refer",      "Elevated probability of Hb < 10", "Schedule RHU visit for confirmatory laboratory CBC"],
        ["P ≥ 0.80",         "🔴 Likely Anemia — Urgent",       "High probability of mod-severe", "Priority referral to RHU/hospital; auto-generate Konsulta PDF"],
    ],
    col_widths=[3.0, 4.5, 4.5, 5.0]
)

# ─── SECTION V ───────────────────────────────────────────────────────────────
add_heading(doc, "V. DYNAMIC MULTI-INDICATOR WEIGHTING & EVIDENCE INTEGRATION", 1)
add_body(doc, "In frontline primary care, clinical data collection is inherently variable: an infant may resist eyelid eversion, or a BHW may conduct a house-to-house visit without their blood pressure cuff. TinginHB handles these conditions through a Dynamic Multi-Indicator Fusion Architecture that accounts for Missing Modalities (Baltrusaitis et al., 2019; Huang et al., 2020, npj Digital Medicine).")

add_heading(doc, "1. The 5-Modality Clinical Indicator Matrix", 2)
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

add_heading(doc, "2. Dynamic Weight Re-normalization for Missing Modalities", 2)
add_code_block(doc,
"w'_i = w_i / SUM(w_available)\n\n"
"• Full Clinic Check (All 5): Eye (35%) + Nail (25%) + Survey (15%) + Palm (15%) + BP (10%) = 100%\n"
"• Field Visit (Eye + Nail + Survey): Eye (46.7%) + Nail (33.3%) + Survey (20.0%) = 100%\n"
"• Pediatric Fallback (Nail + Palm + Survey): Nail (45.5%) + Palm (27.3%) + Survey (27.3%) = 100%"
)

add_heading(doc, "3. Bayesian Likelihood Ratio Log-Odds Stacking", 2)
add_code_block(doc,
"ln(Odds_post) = ln(Odds_prior(Survey)) + SUM(w'_i * ln(LR_i))\n\n"
"Omitted/missing tests contribute a neutral factor of LR = 1.0 (ln(1.0) = 0)."
)

# ─── SECTION VI ──────────────────────────────────────────────────────────────
add_heading(doc, "VI. EXPLICIT LIMITATIONS & RELIABILITY BOUNDS", 1)
add_body(doc, "TinginHB adopts an uncompromising stance on scientific honesty. The following constraints are formally acknowledged:")
for b in [
    "The Mild Anemia Detection Limit: Optical pallor is a physiological lagging indicator (Kalter et al., 1997). Under smartphone RGB cameras, physical pallor does not separate reliably from normal perfusion until hemoglobin drops below ~9.0–10.0 g/dL. TinginHB is explicitly NOT designed or marketed to detect mild anemia (11.0–11.9 g/dL). A green result does not rule out early-stage iron deficiency.",
    "Not a Diagnostic Replacement for CBC: TinginHB is a decision-support triage tool, not a diagnostic device. It identifies who needs urgent laboratory evaluation.",
    "Physiological Confounders: Active conjunctivitis (produces redness/false negatives), jaundice (distorts scleral reference), hypothermia (causes temporary nail vasoconstriction), and nail fungus (blocks nail plate).",
    "Generalizability: Training datasets originate from Ghana (Fitzpatrick IV–V) and Peru (Fitzpatrick III–IV). Local validation (n=250 cohort) paired with laboratory automated CBC is required.",
]:
    add_bullet(doc, b)

# ─── SECTION VII ─────────────────────────────────────────────────────────────
add_heading(doc, "VII. PRODUCT IMPLEMENTATION & EDGE SPECIFICATIONS", 1)
add_table(doc,
    ["Component", "Engine / Runtime", "Specification / Footprint"],
    [
        ["ROI Segmentation",      "YOLOv8n-seg (INT8)",     "~3.5 MB | 80ms inference"],
        ["Feature Extraction",    "MobileNetV3-S (FP16)",   "~5.2 MB | 120ms inference"],
        ["Radiomics Extractor",   "OpenCV Colorimetry",     "16 Handcrafted Features (EI, PI)"],
        ["Uncertainty Engine",    "Monte Carlo Dropout",    "N=50 stochastic passes (~200ms)"],
        ["Total System Footprint","Fully On-Device",        "< 10 MB total | < 450ms latency"],
        ["Minimum Hardware",      "Android 8.0 (Oreo)",     "2 GB RAM | 8 MP Rear Camera"],
        ["Operational Mode",      "100% Offline",           "Zero mobile data required"],
    ],
    col_widths=[4.5, 5.5, 7.0]
)

# ─── SECTION VIII ────────────────────────────────────────────────────────────
add_heading(doc, "VIII. BUSINESS MODEL & PUBLIC HEALTH SUSTAINABILITY", 1)
for b in [
    "FREE TIER FOR BHWs: Core screening, triage, and offline PDF referral generation are perpetually free for community health workers and rural barangay health stations.",
    "LGU & DOH ENTERPRISE LICENSING: Municipal and provincial health offices pay an annual SaaS license (₱500–₱1,000 / BHW / year) for centralized epidemiological dashboards, maternal tracking analytics, and PhilHealth Konsulta integration.",
    "NGO & DEVELOPMENT PARTNERSHIPS: Bulk enterprise deployment across maternal and child health programs (UNFPA, UNICEF, Zuellig Family Foundation).",
    "Macro-Economic Value: Replacing just one disposable HemoCue microcuvette (₱150) across 50,000 community screenings/month saves local government health budgets over ₱7.5 Million monthly in consumable waste.",
]:
    add_bullet(doc, b)

# ─── SECTION IX ──────────────────────────────────────────────────────────────
add_heading(doc, "IX. COMPETITIVE DIFFERENTIATION MATRIX", 1)
add_table(doc,
    ["Parameter", "TinginHB (DataLunas)", "HemoCue Hb 301", "AnemoCheck / Sanguina", "Naked-Eye Pallor"],
    [
        ["Cost per Test",       "₱0 (Zero Consumables)",  "₱150 / cuvette",      "~$5 USD / test",        "₱0"],
        ["Device Hardware",     "₱0 (Existing Phone)",     "₱70,000–₱125,000",    "Existing Phone",        "₱0"],
        ["Lab Calibration",     "Not Required",            "Factory Calibrated",  "Required (Prior CBC)",  "None"],
        ["Anatomical Sites",    "Dual: Conjunctiva + Nail","Blood (Fingerstick)", "Nail Bed Only",         "Subjective / Variable"],
        ["Skin Bias",           "Minimal (0-melanin eye)", "None (Invasive)",     "High (Skin sensitive)", "Severe"],
        ["Output Type",         "Calibrated Probability",  "Absolute Hb (g/dL)",  "Continuous Hb (g/dL)",  "Subjective Guess"],
        ["Offline Ready",       "100% Offline",            "100% Offline",        "Requires Cloud Sync",   "Offline"],
        ["PhilHealth Aligned",  "Konsulta PDF Generated",  "None",                "None",                  "Manual Paper Logs"],
    ],
    col_widths=[3.5, 3.8, 3.5, 3.5, 2.7]
)

# ─── SECTION X ───────────────────────────────────────────────────────────────
add_heading(doc, "X. CONCLUSION", 1)
add_body(doc, "TinginHB demonstrates that responsible AI in healthcare is not about making unsubstantiated claims of replacing laboratory medicine, but about scientifically bounding algorithms to solve concrete frontline bottlenecks. By transforming entry-level smartphones into zero-consumable, dual-site triage tools with calibrated probabilistic outputs and dynamic missing-modality weighting, TinginHB empowers 200,000 Filipino Barangay Health Workers to detect severe maternal and infant anemia months before catastrophic clinical complications arise—turning every routine barangay visit into a life-saving health intervention.")

# ─── SECTION XI ──────────────────────────────────────────────────────────────
add_heading(doc, "XI. REFERENCES & ACADEMIC GROUNDING", 1)
refs = [
    "World Health Organization (2011). Haemoglobin concentrations for the diagnosis of anaemia and assessment of severity. WHO/NMH/NHD/MNM/11.1.",
    "World Health Organization (2013). Pocket book of hospital care for children (2nd ed.). Section: Assessment of palmar and conjunctival pallor (IMCI).",
    "World Health Organization (2016). WHO recommendations on antenatal care for a positive pregnancy experience.",
    "Strobach, R. S., et al. (1988). The value of the physical examination in diagnosing anemia. JAMA, 259(11), 1682–1685.",
    "Kalter, H. D., et al. (1997). Evaluation of clinical signs to diagnose anaemia in Uganda and Bangladesh. Bulletin of the WHO, 75(Suppl 1), 103–111.",
    "Luby, S. P., et al. (1995). Using clinical signs to diagnose anaemia in African children. Bulletin of the WHO, 73(4), 477–482.",
    "Duke, M., & Abelmann, W. H. (1969). The hemodynamic response to chronic anemia. Circulation, 39(4), 503–515.",
    "Varat, M. A., Adolph, R. J., & Fowler, N. O. (1972). Cardiovascular effects of severe anemia. American Heart Journal, 83(3), 415–426.",
    "Kim, T. N., et al. (2020). Smartphone-based assessment of anemia from conjunctival images. PNAS, 117(49), 31046–31055.",
    "Kim, T. N., et al. (2023). Validation of a smartphone-based conjunctival assessment for anemia in outpatients. Annals of Internal Medicine, 176(3), 302–310.",
    "Mannino, R. G., et al. (2018). Smartphone app for non-invasive detection of anemia using only patient-sourced photos. Nature Communications, 9(1), 4924.",
    "Dimauro, G., et al. (2018). Ocular redness measurement in non-contact and non-invasive diagnoses of anaemia. Journal of Imaging, 4(8), 95.",
    "Valles-Coral, M. A., et al. (2025). AnaeCare: Non-invasive anemia detection from smartphone images using multi-site pallor analysis. arXiv.",
    "Baltrusaitis, T., Ahuja, C., & Morency, L. P. (2019). Multimodal machine learning: A survey and taxonomy. IEEE TPAMI, 41(2), 423–443.",
    "Huang, S. C., et al. (2020). Fusion of medical imaging and electronic health records using deep learning. npj Digital Medicine, 3(1), 136.",
    "Gal, Y., & Ghahramani, Z. (2016). Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning. ICML, 48, 1050–1059.",
    "Platt, J. (1999). Probabilistic outputs for support vector machines and comparisons to regularized likelihood methods. Advances in Large Margin Classifiers.",
    "Food and Nutrition Research Institute (DOST-FNRI, 2020). Expanded National Nutrition Survey.",
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
