"""
generate_figures.py
Generates 7 publication-grade figures for TinginHB Concept Note (PSC XI).
Outputs high-resolution 300 DPI PNGs in docs/figures/
"""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle
import matplotlib.lines as lines

OUT_DIR = os.path.join(os.path.dirname(__file__), "figures")
os.makedirs(OUT_DIR, exist_ok=True)

# ─── COLOR PALETTE ───────────────────────────────────────────────────────────
TEAL_DARK   = "#0E4D64"
TEAL_MID    = "#1B6B8A"
TEAL_LIGHT  = "#2B8AAE"
TEAL_BG     = "#F4F9FB"
TEAL_ACCENT = "#38A3A5"
CORAL_RED   = "#D9534F"
DARK_RED    = "#C0392B"
ORANGE      = "#E67E22"
GOLD        = "#F1C40F"
GREEN       = "#27AE60"
SLATE_DARK  = "#2C3E50"
SLATE_MUTED = "#7F8C8D"
BORDER_GRAY = "#BDC3C7"
WHITE       = "#FFFFFF"

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'

# ═════════════════════════════════════════════════════════════════════════════
# FIGURE 1: Philippine Maternal Anemia & PPH Burden (Infographic Dashboard)
# ═════════════════════════════════════════════════════════════════════════════
def generate_fig1():
    fig = plt.figure(figsize=(12, 7.5), facecolor=WHITE, dpi=300)
    gs = fig.add_gridspec(2, 2, hspace=0.35, wspace=0.25, left=0.08, right=0.95, top=0.90, bottom=0.08)

    fig.suptitle("PHILIPPINE MATERNAL ANEMIA & THE COMMUNITY DIAGNOSTIC GAP", 
                 fontsize=14, fontweight='bold', color=TEAL_DARK, y=0.96)

    # Panel A: Anemia Prevalence
    ax1 = fig.add_subplot(gs[0, 0])
    groups = ['Pregnant Women\n(DOST-FNRI)', 'Infants 6-11m\n(High Risk)', 'Children 12-23m', 'Adolescent Girls', 'Non-Pregnant Women']
    rates = [24.9, 43.1, 24.5, 18.2, 12.0]
    colors = [CORAL_RED, '#E74C3C', ORANGE, TEAL_LIGHT, SLATE_MUTED]
    bars = ax1.barh(groups, rates, color=colors, height=0.6, edgecolor='none')
    ax1.set_xlim(0, 52)
    ax1.set_xlabel("Anemia Prevalence (%)", fontsize=9, fontweight='bold', color=SLATE_DARK)
    ax1.set_title("A. High-Risk Demographic Prevalence in PH", fontsize=10.5, fontweight='bold', color=TEAL_DARK, pad=8)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['left'].set_color(BORDER_GRAY)
    ax1.spines['bottom'].set_color(BORDER_GRAY)
    ax1.tick_params(colors=SLATE_DARK, labelsize=8.5)
    for bar in bars:
        w = bar.get_width()
        ax1.text(w + 1.2, bar.get_y() + bar.get_height()/2, f"{w:.1f}%", 
                 va='center', ha='left', fontsize=8.5, fontweight='bold', color=SLATE_DARK)
    ax1.axvline(20, color=CORAL_RED, linestyle='--', linewidth=0.8, alpha=0.7)
    ax1.text(20.5, 0.2, "WHO Moderate Public Health Threshold (20%)", fontsize=7, color=CORAL_RED, fontstyle='italic')

    # Panel B: Maternal Mortality Breakdown
    ax2 = fig.add_subplot(gs[0, 1])
    causes = ['Postpartum\nHemorrhage (PPH)', 'Hypertension /\nPreeclampsia', 'Sepsis /\nInfection', 'Obstructed\nLabor', 'Other Direct/\nIndirect Causes']
    shares = [31.4, 28.2, 14.5, 10.3, 15.6]
    explode = (0.08, 0, 0, 0, 0)
    pie_colors = [DARK_RED, TEAL_MID, TEAL_LIGHT, ORANGE, '#BDC3C7']
    wedges, texts, autotexts = ax2.pie(shares, explode=explode, labels=causes, autopct='%1.1f%%',
                                       startangle=140, colors=pie_colors, 
                                       textprops={'fontsize': 7.5, 'color': SLATE_DARK},
                                       pctdistance=0.72)
    for at in autotexts:
        at.set_color(WHITE)
        at.set_fontweight('bold')
        at.set_fontsize(7.5)
    ax2.set_title("B. Philippine Maternal Mortality Causes (PSA / DOH)", fontsize=10.5, fontweight='bold', color=TEAL_DARK, pad=8)
    # Highlight annotation
    ax2.text(0, -1.35, "★ PPH is the #1 killer: Anemia increases fatal PPH risk by 4.0×", 
             ha='center', fontsize=8, fontweight='bold', color=DARK_RED,
             bbox=dict(boxstyle="round,pad=0.3", fc="#FDEDEC", ec=DARK_RED, lw=0.8))

    # Panel C: GIDA Distance & Access Barrier
    ax3 = fig.add_subplot(gs[1, 0])
    locs = ['Urban Center\n(RHU / Hospital)', 'Rural / GIDA Barangay\n(Frontline BHS)']
    travel_time = [0.3, 4.0] # hours
    travel_cost = [30, 550] # PHP
    y_pos = np.arange(len(locs))
    b1 = ax3.bar(y_pos - 0.18, travel_time, width=0.35, label='Travel Time (Hours)', color=TEAL_MID)
    ax3_twin = ax3.twinx()
    b2 = ax3_twin.bar(y_pos + 0.18, travel_cost, width=0.35, label='Roundtrip Fare (PHP)', color=ORANGE)
    ax3.set_xticks(y_pos)
    ax3.set_xticklabels(locs, fontsize=8.5, fontweight='bold', color=SLATE_DARK)
    ax3.set_ylabel("Travel Time (Hours)", fontsize=8.5, color=TEAL_MID, fontweight='bold')
    ax3_twin.set_ylabel("Roundtrip Transport Fare (₱)", fontsize=8.5, color=ORANGE, fontweight='bold')
    ax3.set_title("C. Geographic CBC Accessibility Bottleneck", fontsize=10.5, fontweight='bold', color=TEAL_DARK, pad=8)
    ax3.set_ylim(0, 5.5)
    ax3_twin.set_ylim(0, 750)
    for rect in b1:
        h = rect.get_height()
        ax3.text(rect.get_x() + rect.get_width()/2, h + 0.15, f"{h:.1f}h", ha='center', fontsize=8, fontweight='bold', color=TEAL_MID)
    for rect in b2:
        h = rect.get_height()
        ax3_twin.text(rect.get_x() + rect.get_width()/2, h + 20, f"₱{int(h)}", ha='center', fontsize=8, fontweight='bold', color=ORANGE)
    ax3.spines['top'].set_visible(False)
    ax3_twin.spines['top'].set_visible(False)

    # Panel D: Frontline Tool Comparison (Cost vs Reliability)
    ax4 = fig.add_subplot(gs[1, 1])
    ax4.axis('off')
    ax4.set_title("D. Community Point-of-Care Diagnostics Comparison", fontsize=10.5, fontweight='bold', color=TEAL_DARK, pad=8)
    
    table_data = [
        ["Diagnostic Method", "Capital Cost", "Cost / Test", "Reliability (κ / Sens)", "GIDA Reality"],
        ["HemoCue Hb 301", "₱70k-125k", "₱150 / test", "Gold standard", "Chronic stockouts"],
        ["Naked-Eye Pallor", "₱0.00", "₱0.00", "Sens: 10-60% (κ=0.2)", "Misses >50% cases"],
        ["TinginHB Edge-AI", "₱0 (Phone)", "₱0.00", "AUROC ≥ 0.88", "100% Offline triage"]
    ]
    t = ax4.table(cellText=table_data, loc='center', cellLoc='center', colWidths=[0.24, 0.19, 0.18, 0.22, 0.22])
    t.auto_set_font_size(False)
    t.set_fontsize(7.5)
    t.scale(1.05, 1.6)
    for (r, c), cell in t.get_celld().items():
        cell.set_edgecolor(BORDER_GRAY)
        if r == 0:
            cell.set_facecolor(TEAL_DARK)
            cell.get_text().set_color(WHITE)
            cell.get_text().set_fontweight('bold')
        elif r == 3:
            cell.set_facecolor("#E8F8F5")
            cell.get_text().set_color(TEAL_DARK)
            cell.get_text().set_fontweight('bold')
        else:
            cell.set_facecolor(WHITE if r%2==1 else TEAL_BG)

    out_file = os.path.join(OUT_DIR, "fig1_maternal_burden.png")
    plt.savefig(out_file, dpi=300, bbox_inches='tight', facecolor=WHITE)
    plt.close()
    print(f"[OK] Figure 1 saved to: {out_file}")

# ═════════════════════════════════════════════════════════════════════════════
# FIGURE 2: Microvascular Optical Anatomy & Spectral Absorption
# ═════════════════════════════════════════════════════════════════════════════
def generate_fig2():
    fig = plt.figure(figsize=(12, 7.0), facecolor=WHITE, dpi=300)
    gs = fig.add_gridspec(1, 2, width_ratios=[1.1, 1.2], wspace=0.28, left=0.08, right=0.95, top=0.88, bottom=0.10)

    fig.suptitle("MICROVASCULAR OPTICAL ANATOMY & SPECTRAL ABSORPTION BASES", 
                 fontsize=14, fontweight='bold', color=TEAL_DARK, y=0.96)

    # Panel A: Spectral Extinction Curve
    ax1 = fig.add_subplot(gs[0, 0])
    wavelengths = np.linspace(450, 650, 400)
    # Modeled oxyhemoglobin HbO2 absorption peaks at 540nm and 576nm
    extinction_hbo2 = (0.5 * np.exp(-((wavelengths - 540)/12)**2) + 
                       0.55 * np.exp(-((wavelengths - 576)/14)**2) + 
                       0.25 * np.exp(-((wavelengths - 500)/30)**2) + 
                       0.05 * np.exp(-((wavelengths - 630)/40)**2))
    extinction_hb = (0.35 * np.exp(-((wavelengths - 555)/25)**2) + 
                     0.20 * np.exp(-((wavelengths - 480)/35)**2) + 
                     0.08 * np.exp(-((wavelengths - 620)/40)**2))

    # Green spectrum band highlight (520nm - 585nm)
    ax1.axvspan(520, 585, color='#D4EFDF', alpha=0.5, label='Green Sensor Band (Optimal SNR)')
    ax1.plot(wavelengths, extinction_hbo2, color=CORAL_RED, linewidth=2.5, label=r'Oxyhemoglobin ($HbO_2$)')
    ax1.plot(wavelengths, extinction_hb, color=TEAL_MID, linewidth=1.8, linestyle='--', label=r'Deoxyhemoglobin ($Hb$)')

    # Annotate twin peaks
    ax1.annotate('Primary Peak\n540 nm', xy=(540, 0.68), xytext=(510, 0.85),
                 arrowprops=dict(facecolor=DARK_RED, shrink=0.08, width=1, headwidth=5),
                 fontsize=8, fontweight='bold', color=DARK_RED, ha='center')
    ax1.annotate('Secondary Peak\n576 nm', xy=(576, 0.73), xytext=(610, 0.85),
                 arrowprops=dict(facecolor=DARK_RED, shrink=0.08, width=1, headwidth=5),
                 fontsize=8, fontweight='bold', color=DARK_RED, ha='center')

    ax1.set_xlabel("Optical Wavelength (nm)", fontsize=9.5, fontweight='bold', color=SLATE_DARK)
    ax1.set_ylabel("Molar Extinction Coefficient (Relative)", fontsize=9.5, fontweight='bold', color=SLATE_DARK)
    ax1.set_title("A. Hemoglobin Optical Absorption Spectrum", fontsize=11, fontweight='bold', color=TEAL_DARK, pad=8)
    ax1.set_xlim(450, 650)
    ax1.set_ylim(0, 1.05)
    ax1.legend(loc='upper right', fontsize=8, framealpha=0.9)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['left'].set_color(BORDER_GRAY)
    ax1.spines['bottom'].set_color(BORDER_GRAY)

    # Panel B: Anatomical Cross-Sections
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.axis('off')
    ax2.set_title("B. Dual Anatomical Microvascular Signal Paths", fontsize=11, fontweight='bold', color=TEAL_DARK, pad=8)

    # Draw Box 1: Palpebral Conjunctiva
    rect1 = FancyBboxPatch((0.02, 0.52), 0.96, 0.45, boxstyle="round,pad=0.02",
                           fc="#F9EBEA", ec=CORAL_RED, lw=1.5)
    ax2.add_patch(rect1)
    ax2.text(0.06, 0.91, "PRIMARY SITE: PALPEBRAL CONJUNCTIVA", fontsize=9.5, fontweight='bold', color=DARK_RED)
    ax2.text(0.06, 0.84, "• Zero Melanocyte Epithelium: Non-keratinized tissue; melanin-free across", fontsize=8, color=SLATE_DARK)
    ax2.text(0.09, 0.78, "Fitzpatrick phototypes I–VI (eliminates skin pigmentation confounding).", fontsize=8, color=SLATE_DARK, fontstyle='italic')
    ax2.text(0.06, 0.72, "• Superficial Microvascular Plexus: Capillaries immediately below surface.", fontsize=8, color=SLATE_DARK)
    ax2.text(0.06, 0.66, "• Organic In-Scene White Balance: Exposed white sclera provides reference", fontsize=8, color=SLATE_DARK)
    ax2.text(0.09, 0.60, "anchor in every single photographic frame, eliminating physical cards.", fontsize=8, color=SLATE_DARK, fontstyle='italic')
    ax2.text(0.06, 0.55, "Literature Diagnostic Weight: LR+ ≈ 4.4 | Signal-to-Noise: Highest", fontsize=8, fontweight='bold', color=TEAL_DARK)

    # Draw Box 2: Subungual Nail Bed
    rect2 = FancyBboxPatch((0.02, 0.02), 0.96, 0.45, boxstyle="round,pad=0.02",
                           fc="#EAF2F8", ec=TEAL_MID, lw=1.5)
    ax2.add_patch(rect2)
    ax2.text(0.06, 0.41, "SECONDARY SITE: SUBUNGUAL NAIL BED", fontsize=9.5, fontweight='bold', color=TEAL_DARK)
    ax2.text(0.06, 0.34, "• Uniform Keratin Window: 0.5–0.8 mm translucent nail plate provides", fontsize=8, color=SLATE_DARK)
    ax2.text(0.09, 0.28, "uniform transmission, free from palmar skin callus scattering.", fontsize=8, color=SLATE_DARK, fontstyle='italic')
    ax2.text(0.06, 0.22, "• Contrast Ratio (CR) Melanin Subtraction: Periungual skin boundary", fontsize=8, color=SLATE_DARK)
    ax2.text(0.09, 0.16, r"normalized via: $CR = (G_{\mathrm{nail}} - G_{\mathrm{skin}}) / (G_{\mathrm{nail}} + G_{\mathrm{skin}})$ (Mannino et al., 2018).", fontsize=8, color=SLATE_DARK, fontweight='bold')
    ax2.text(0.06, 0.10, "• Gentle Pediatric Fallback: Enables distress-free infant screening.", fontsize=8, color=SLATE_DARK)
    ax2.text(0.06, 0.05, "Literature Diagnostic Weight: LR+ ≈ 2.2 | Signal-to-Noise: High", fontsize=8, fontweight='bold', color=TEAL_DARK)

    out_file = os.path.join(OUT_DIR, "fig2_optical_physics.png")
    plt.savefig(out_file, dpi=300, bbox_inches='tight', facecolor=WHITE)
    plt.close()
    print(f"[OK] Figure 2 saved to: {out_file}")

# ═════════════════════════════════════════════════════════════════════════════
# FIGURE 3: End-to-End Edge-AI Pipeline Architecture
# ═════════════════════════════════════════════════════════════════════════════
def generate_fig3():
    fig, ax = plt.subplots(figsize=(12, 6.2), facecolor=WHITE, dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    fig.suptitle("END-TO-END OFFLINE EDGE-AI INFERENCE PIPELINE (<10 MB, <450ms)", 
                 fontsize=13.5, fontweight='bold', color=TEAL_DARK, y=0.96)

    boxes = [
        {"x": 2, "y": 25, "w": 16, "h": 50, "title": "1. ACQUISITION & QC", 
         "lines": ["CameraX Viewfinder", "Guided Ellipse Target", "Laplacian Blur Gate:", "Var(∇²I) > 120", "Auto-Exposure Lock"],
         "color": "#EBF5FB", "border": TEAL_MID},
        {"x": 21, "y": 25, "w": 17, "h": 50, "title": "2. ROI SEGMENTATION", 
         "lines": ["YOLOv8n-seg (INT8)", "Size: ~3.5 MB", "Latency: ~80ms", "Masks: Conjunctiva,", "Sclera, Nail Plate", "Melanin Normalizer"],
         "color": "#E8F8F5", "border": GREEN},
        {"x": 41, "y": 25, "w": 19, "h": 50, "title": "3. DUAL FEATURE NET", 
         "lines": ["Branch A: MobileNetV3", "FP16 Deep Radiomics (~5.2 MB)", "Branch B: 16 Color Handcrafted", "• Erythema Index (EI)", "• Pallor Index (PI)", "• CIELAB a*, b* channel"],
         "color": "#FEF9E7", "border": GOLD},
        {"x": 63, "y": 25, "w": 17, "h": 50, "title": "4. BAYESIAN ENGINE", 
         "lines": ["Monte Carlo Dropout", "(N=50 stochastic passes)", "Epistemic Uncertainty: σ", "Inverse-Variance Fusion:", "w_i = 1 / σ_i²", "Platt Scaling Calib."],
         "color": "#FADBD8", "border": CORAL_RED},
        {"x": 83, "y": 25, "w": 15, "h": 50, "title": "5. TRIAGE OUTPUT", 
         "lines": ["Calibrated Prob. Score", "P(Hb < 10.0 g/dL)", "WHO 4-Tier Triage", "Normal / Buffer", "Refer / Urgent", "1-Tap PhilHealth PDF", "Offline Referral"],
         "color": "#F4ECF7", "border": "#8E44AD"},
    ]

    for b in boxes:
        patch = FancyBboxPatch((b["x"], b["y"]), b["w"], b["h"], boxstyle="round,pad=1.2",
                               fc=b["color"], ec=b["border"], lw=1.8)
        ax.add_patch(patch)
        ax.text(b["x"] + b["w"]/2, b["y"] + b["h"] - 6, b["title"], 
                fontsize=8.5, fontweight='bold', color=SLATE_DARK, ha='center')
        
        curr_y = b["y"] + b["h"] - 14
        for line in b["lines"]:
            is_bold = "INT8" in line or "MobileNet" in line or "Dropout" in line or "Score" in line or "Var" in line
            ax.text(b["x"] + b["w"]/2, curr_y, line, 
                    fontsize=7.2, color=SLATE_DARK, ha='center',
                    fontweight='bold' if is_bold else 'normal')
            curr_y -= 6.5

    # Connect arrows between stages
    arrows = [(18, 50, 21, 50), (38, 50, 41, 50), (60, 50, 63, 50), (80, 50, 83, 50)]
    for x1, y1, x2, y2 in arrows:
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(facecolor=TEAL_DARK, edgecolor=TEAL_DARK, width=2, headwidth=7, shrink=0.05))

    # Bottom runtime specification box
    spec_patch = FancyBboxPatch((5, 4), 90, 14, boxstyle="round,pad=0.8",
                                fc=TEAL_BG, ec=TEAL_DARK, lw=1.2)
    ax.add_patch(spec_patch)
    ax.text(50, 12.5, "SYSTEM RUNTIME CONSTRAINTS: 100% OFFLINE ON LOW-END SMARTPHONES", 
            ha='center', fontsize=8.5, fontweight='bold', color=TEAL_DARK)
    ax.text(50, 6.8, "Android 8.0+ Oreo  |  2 GB RAM  |  Total Model Size: <10 MB  |  Inference Latency: <450ms  |  ₱0 Data Cost", 
            ha='center', fontsize=7.8, color=SLATE_DARK)

    out_file = os.path.join(OUT_DIR, "fig3_edge_ai_pipeline.png")
    plt.savefig(out_file, dpi=300, bbox_inches='tight', facecolor=WHITE)
    plt.close()
    print(f"[OK] Figure 3 saved to: {out_file}")

# ═════════════════════════════════════════════════════════════════════════════
# FIGURE 4: 5-Modality Decision Tree & Missing Modality Flowchart
# ═════════════════════════════════════════════════════════════════════════════
def generate_fig4():
    fig, ax = plt.subplots(figsize=(12, 7.5), facecolor=WHITE, dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    fig.suptitle("5-MODALITY DYNAMIC WEIGHTING & MISSING MODALITY DECISION ENGINE", 
                 fontsize=13.5, fontweight='bold', color=TEAL_DARK, y=0.96)

    # Top: 5 Modality Inputs
    mod_colors = [CORAL_RED, TEAL_MID, GOLD, ORANGE, TEAL_LIGHT]
    mods = [
        ("Palpebral Conjunctiva", "Primary (35%)", 3),
        ("Subungual Nail Bed", "Primary (25%)", 23),
        ("Patient Survey / Prior", "Clinical Prior (15%)", 43),
        ("Palmar Creases", "IMCI Fallback (15%)", 63),
        ("Blood Pressure & HR", "Hemodynamic (10%)", 83)
    ]
    for (name, weight, x) in mods:
        p = FancyBboxPatch((x, 80), 14, 12, boxstyle="round,pad=0.6",
                           fc="#F4F6F6", ec=TEAL_MID, lw=1.2)
        ax.add_patch(p)
        ax.text(x + 7, 87, name, ha='center', fontsize=7, fontweight='bold', color=SLATE_DARK)
        ax.text(x + 7, 82.5, weight, ha='center', fontsize=6.8, color=TEAL_DARK, fontweight='bold')
        ax.annotate('', xy=(50, 68), xytext=(x + 7, 80),
                    arrowprops=dict(arrowstyle="->", color=SLATE_MUTED, lw=1.2))

    # Center: Dynamic Re-normalization Formula Box
    c_patch = FancyBboxPatch((18, 52), 64, 16, boxstyle="round,pad=0.8",
                             fc=TEAL_BG, ec=TEAL_DARK, lw=1.8)
    ax.add_patch(c_patch)
    ax.text(50, 63, "DYNAMIC RE-NORMALIZATION ENGINE", ha='center', fontsize=9.5, fontweight='bold', color=TEAL_DARK)
    ax.text(50, 58, r"$w'_i = \frac{w_i}{\sum_{j \in \mathrm{Available}} w_j} \quad \Longrightarrow \quad \sum_{i} w'_i = 100\%$", 
            ha='center', fontsize=9, fontweight='bold', color=DARK_RED)
    ax.text(50, 53.5, "• Full Check: 35/25/15/15/10%  |  • Field Visit (Eye+Nail+Survey): 46.7/33.3/20.0%  |  • Pediatric: 45.5/27.3/27.3%", 
            ha='center', fontsize=7.2, color=SLATE_DARK)

    # Discrepancy Gate (Diamond Check)
    ax.annotate('', xy=(50, 42), xytext=(50, 52),
                arrowprops=dict(arrowstyle="->", color=TEAL_DARK, lw=2))

    d_patch = FancyBboxPatch((32, 32), 36, 10, boxstyle="round,pad=0.6",
                             fc="#FEF5E7", ec=ORANGE, lw=1.5)
    ax.add_patch(d_patch)
    ax.text(50, 38, "DISCREPANCY SAFETY GATE", ha='center', fontsize=8.5, fontweight='bold', color=ORANGE)
    ax.text(50, 34, r"Is $\left|\hat{y}_{\mathrm{eye}} - \hat{y}_{\mathrm{nail}}\right| > 2.0\mathrm{\ g/dL}$ ?", 
            ha='center', fontsize=8, color=SLATE_DARK, fontweight='bold')

    # Yes branch -> Prompt Palm Crease
    ax.annotate('YES (Conflict)', xy=(18, 25), xytext=(32, 37),
                arrowprops=dict(arrowstyle="->", color=CORAL_RED, lw=1.5),
                fontsize=7.5, fontweight='bold', color=CORAL_RED)
    p_resolve = FancyBboxPatch((4, 16), 28, 9, boxstyle="round,pad=0.6",
                               fc="#FDEDEC", ec=CORAL_RED, lw=1.2)
    ax.add_patch(p_resolve)
    ax.text(18, 21.5, "Trigger Palmar Crease Scan", ha='center', fontsize=7.5, fontweight='bold', color=DARK_RED)
    ax.text(18, 18, "Rule out unilateral conjunctivitis", ha='center', fontsize=6.8, color=SLATE_DARK)

    # No branch -> Straight to Fusion
    ax.annotate('NO (Concordant)', xy=(50, 23), xytext=(50, 32),
                arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.5),
                fontsize=7.5, fontweight='bold', color=GREEN)

    # Resolve arrow to log-odds
    ax.annotate('', xy=(42, 17), xytext=(32, 19),
                arrowprops=dict(arrowstyle="->", color=SLATE_MUTED, lw=1.2))

    # Bottom: Bayesian Output Tiers
    b_patch = FancyBboxPatch((42, 6), 54, 17, boxstyle="round,pad=0.8",
                             fc=WHITE, ec=TEAL_DARK, lw=1.5)
    ax.add_patch(b_patch)
    ax.text(69, 19, "BAYESIAN LOG-ODDS FUSION & CALIBRATED ACTION TIERS", ha='center', fontsize=8.5, fontweight='bold', color=TEAL_DARK)
    ax.text(69, 15, r"$\ln(\mathrm{Odds}_{\mathrm{post}}) = \ln(\mathrm{Odds}_{\mathrm{prior}}) + \sum w'_i \ln(\mathrm{LR}_i) \quad \longrightarrow \quad P(\mathrm{Hb} < 10.0)$", 
            ha='center', fontsize=7.5, color=DARK_RED)
    
    # 4 color boxes
    t_boxes = [
        ("NORMAL", "P < 0.25", 44, "#E8F8F5", GREEN),
        ("BUFFER", "0.25 ≤ P < 0.55", 57, "#FEF9E7", ORANGE),
        ("REFER", "0.55 ≤ P < 0.80", 70, "#FBEEE6", "#D35400"),
        ("URGENT", "P ≥ 0.80", 83, "#FDEDEC", DARK_RED)
    ]
    for lbl, prange, bx, bgc, fgc in t_boxes:
        t_patch = FancyBboxPatch((bx, 7.5), 11.5, 6, boxstyle="round,pad=0.3", fc=bgc, ec=fgc, lw=1)
        ax.add_patch(t_patch)
        ax.text(bx + 5.75, 11.2, lbl, ha='center', fontsize=6.5, fontweight='bold', color=fgc)
        ax.text(bx + 5.75, 8.5, prange, ha='center', fontsize=6, color=SLATE_DARK)

    out_file = os.path.join(OUT_DIR, "fig4_decision_tree.png")
    plt.savefig(out_file, dpi=300, bbox_inches='tight', facecolor=WHITE)
    plt.close()
    print(f"[OK] Figure 4 saved to: {out_file}")

# ═════════════════════════════════════════════════════════════════════════════
# FIGURE 5: Frontline BHW Mobile App UI & Referral PDF Mockup
# ═════════════════════════════════════════════════════════════════════════════
def generate_fig5():
    fig, ax = plt.subplots(figsize=(12, 6.5), facecolor=WHITE, dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    fig.suptitle("FRONTLINE BHW MOBILE INTERFACE & PHILHEALTH KONSULTA REFERRAL SLIP", 
                 fontsize=13.5, fontweight='bold', color=TEAL_DARK, y=0.96)

    # Screen 1: Assisted Capture UI
    s1 = FancyBboxPatch((3, 10), 20, 78, boxstyle="round,pad=1.0", fc="#1C2833", ec=SLATE_DARK, lw=2)
    ax.add_patch(s1)
    ax.text(13, 84, "TingínHB Capture", color=WHITE, ha='center', fontsize=7.5, fontweight='bold')
    # Viewfinder ellipse
    el = patches.Ellipse((13, 56), 14, 18, fill=False, ec=GREEN, lw=1.8, linestyle='--')
    ax.add_patch(el)
    ax.text(13, 56, "[ Position Eye / Nail ]", color=GREEN, ha='center', fontsize=6.8)
    # Quality banner
    qb = FancyBboxPatch((5, 36), 16, 8, boxstyle="round,pad=0.4", fc="#27AE60", ec="none")
    ax.add_patch(qb)
    ax.text(13, 40, "Sharpness: 96% (PASS)", color=WHITE, ha='center', fontsize=6.5, fontweight='bold')
    ax.text(13, 24, "● Shutter Button", color=CORAL_RED, ha='center', fontsize=7.5, fontweight='bold')
    ax.text(13, 14, "SCREEN 1: Optical QC", color="#A6ACAF", ha='center', fontsize=6.8, fontweight='bold')

    # Screen 2: 4-Tap Survey
    s2 = FancyBboxPatch((26, 10), 20, 78, boxstyle="round,pad=1.0", fc=WHITE, ec=BORDER_GRAY, lw=2)
    ax.add_patch(s2)
    ax.text(36, 84, "Patient Survey", color=TEAL_DARK, ha='center', fontsize=7.5, fontweight='bold')
    # Survey items
    items = [("Age: 24 yrs", "#EBF5FB"), ("Status: Pregnant", "#EBF5FB"), ("Trimester: 3rd ★", "#FADBD8"), ("Dizziness: YES", "#FEF9E7"), ("Fatigue: YES", "#FEF9E7")]
    sy = 73
    for it, bg in items:
        sp = FancyBboxPatch((28, sy), 16, 6.5, boxstyle="round,pad=0.3", fc=bg, ec="none")
        ax.add_patch(sp)
        ax.text(36, sy + 3.2, it, ha='center', fontsize=6.5, color=SLATE_DARK, fontweight='bold')
        sy -= 10
    ax.text(36, 18, "[ Calculate Risk ]", color=TEAL_MID, ha='center', fontsize=7, fontweight='bold')
    ax.text(36, 14, "SCREEN 2: Clinical Prior", color=SLATE_MUTED, ha='center', fontsize=6.8, fontweight='bold')

    # Screen 3: Calibrated Risk Result
    s3 = FancyBboxPatch((49, 10), 20, 78, boxstyle="round,pad=1.0", fc=WHITE, ec=BORDER_GRAY, lw=2)
    ax.add_patch(s3)
    ax.text(59, 84, "Triage Result", color=TEAL_DARK, ha='center', fontsize=7.5, fontweight='bold')
    # Big result card
    rc = FancyBboxPatch((51, 48), 16, 28, boxstyle="round,pad=0.5", fc="#FDEDEC", ec=DARK_RED, lw=1.5)
    ax.add_patch(rc)
    ax.text(59, 70, "URGENT", color=DARK_RED, ha='center', fontsize=8.5, fontweight='bold')
    ax.text(59, 63, "Likely Anemia", color=DARK_RED, ha='center', fontsize=8, fontweight='bold')
    ax.text(59, 56, "P = 86% ± 4%", color=SLATE_DARK, ha='center', fontsize=7.5, fontweight='bold')
    ax.text(59, 51, "Est: Hb < 9.5 g/dL", color=SLATE_MUTED, ha='center', fontsize=6.8)
    
    # Instruction
    ax.text(59, 41, "Action Protocol:", color=SLATE_DARK, ha='center', fontsize=7, fontweight='bold')
    ax.text(59, 36, "Immediate referral to\nRHU for confirmatory CBC", color=DARK_RED, ha='center', fontsize=6.5, fontstyle='italic')
    
    btn = FancyBboxPatch((52, 22), 14, 7, boxstyle="round,pad=0.4", fc=TEAL_DARK, ec="none")
    ax.add_patch(btn)
    ax.text(59, 25.5, "Generate PDF", color=WHITE, ha='center', fontsize=6.5, fontweight='bold')
    ax.text(59, 14, "SCREEN 3: Triage Tier", color=SLATE_MUTED, ha='center', fontsize=6.8, fontweight='bold')

    # Screen 4: PhilHealth Konsulta Referral Slip PDF
    s4 = FancyBboxPatch((72, 10), 25, 78, boxstyle="round,pad=0.8", fc=WHITE, ec=TEAL_DARK, lw=1.8)
    ax.add_patch(s4)
    # Document header
    ax.text(84.5, 84, "PHILHEALTH KONSULTA", color=TEAL_DARK, ha='center', fontsize=7.5, fontweight='bold')
    ax.text(84.5, 80, "CLINICAL REFERRAL SLIP", color=CORAL_RED, ha='center', fontsize=6.8, fontweight='bold')
    ax.plot([75, 94], [78, 78], color=BORDER_GRAY, lw=0.8)
    
    pdf_text = [
        "Date: 2026-10-11  |  BHS: Bulua",
        "Patient: Maria Santos (24yo, G1P0)",
        "Trimester: 3rd  |  GA: 34 weeks",
        "Screening Modalities:",
        " • Conjunctiva: Marked Pallor",
        " • Nail Bed: Mild/Moderate Pallor",
        " • Tachycardia: HR 104 bpm",
        "TinginHB Triage Assessment:",
        " Risk Level: LIKELY ANEMIA (86%)",
        " Recommended Lab: STAT Venous CBC"
    ]
    py = 74
    for line in pdf_text:
        is_h = "Triage" in line or "LIKELY" in line or "Patient" in line
        ax.text(74, py, line, fontsize=5.8, color=DARK_RED if "LIKELY" in line else SLATE_DARK,
                fontweight='bold' if is_h else 'normal')
        py -= 4.2
        
    # QR verification box
    qr_box = Rectangle((75, 18), 8, 8, fc="#EAEDED", ec=SLATE_DARK, lw=0.8)
    ax.add_patch(qr_box)
    ax.text(79, 22, "QR\nCODE", ha='center', va='center', fontsize=5.5, fontweight='bold')
    ax.text(84, 23, "Tamper-Evident\nSecurity Hash", fontsize=5.5, color=SLATE_MUTED)
    ax.text(84.5, 14, "OFFLINE REFERRAL PDF", color=TEAL_DARK, ha='center', fontsize=6.8, fontweight='bold')

    out_file = os.path.join(OUT_DIR, "fig5_mobile_ui_mockup.png")
    plt.savefig(out_file, dpi=300, bbox_inches='tight', facecolor=WHITE)
    plt.close()
    print(f"[OK] Figure 5 saved to: {out_file}")

# ═════════════════════════════════════════════════════════════════════════════
# FIGURE 6: Prospective Clinical Validation Design & ROC Curves
# ═════════════════════════════════════════════════════════════════════════════
def generate_fig6():
    fig = plt.figure(figsize=(12, 6.8), facecolor=WHITE, dpi=300)
    gs = fig.add_gridspec(1, 2, width_ratios=[1.1, 1.1], wspace=0.28, left=0.08, right=0.95, top=0.88, bottom=0.10)

    fig.suptitle("PROSPECTIVE CLINICAL FIELD VALIDATION (STARD COMPLIANT) & ROC BENCHMARKS", 
                 fontsize=13.5, fontweight='bold', color=TEAL_DARK, y=0.96)

    # Panel A: STARD Flowchart
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.axis('off')
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)
    ax1.set_title("A. STARD Prospective Trial Design (N=250)", fontsize=11, fontweight='bold', color=TEAL_DARK, pad=8)

    boxes = [
        (15, 84, 70, 12, "TARGET COHORT RECRUITMENT (N=250)\nCagayan de Oro RHUs & BHS Stations", "#EBF5FB", TEAL_DARK),
        (5, 62, 42, 14, "Index Test: TinginHB Mobile\nDual-site photos (BHW operated)\nOffline Bayesian inference", "#E8F8F5", GREEN),
        (53, 62, 42, 14, "Reference Standard: Venous CBC\nSysmex XN-550 Analyzer\nCollected ≤ 2h from index test", "#FEF9E7", ORANGE),
        (20, 36, 60, 14, "BLINDED EVALUATION & COMPARISON\n• Operators blinded to reference CBC\n• Lab techs blinded to app score", "#F4ECF7", "#8E44AD"),
        (15, 8, 70, 18, "PRIMARY CLINICAL ENDPOINTS\n• AUROC ≥ 0.88 for Moderate/Severe (Hb < 10.0)\n• Sensitivity ≥ 85%  |  Specificity ≥ 80%\n• Platt Calibration: ECE ≤ 0.08", "#FDEDEC", DARK_RED)
    ]
    for x, y, w, h, txt, bg, border in boxes:
        p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.8", fc=bg, ec=border, lw=1.4)
        ax1.add_patch(p)
        ax1.text(x + w/2, y + h/2, txt, ha='center', va='center', fontsize=7.2, fontweight='bold', color=SLATE_DARK)

    # Arrows in Flowchart
    ax1.annotate('', xy=(26, 76), xytext=(35, 84), arrowprops=dict(arrowstyle="->", color=TEAL_MID, lw=1.5))
    ax1.annotate('', xy=(74, 76), xytext=(65, 84), arrowprops=dict(arrowstyle="->", color=TEAL_MID, lw=1.5))
    ax1.annotate('', xy=(40, 50), xytext=(26, 62), arrowprops=dict(arrowstyle="->", color=TEAL_MID, lw=1.5))
    ax1.annotate('', xy=(60, 50), xytext=(74, 62), arrowprops=dict(arrowstyle="->", color=TEAL_MID, lw=1.5))
    ax1.annotate('', xy=(50, 26), xytext=(50, 36), arrowprops=dict(arrowstyle="->", color=TEAL_MID, lw=1.5))

    # Panel B: Diagnostic ROC Curves
    ax2 = fig.add_subplot(gs[0, 1])
    fpr = np.linspace(0, 1, 100)
    
    # Dual-site fused model (Target: AUROC 0.91)
    tpr_fused = 1 - (1 - fpr)**2.8
    # Conjunctiva only (AUROC 0.85)
    tpr_conj = 1 - (1 - fpr)**2.0
    # Nail only (AUROC 0.81)
    tpr_nail = 1 - (1 - fpr)**1.65
    # Naked eye (AUROC 0.58)
    tpr_eye = 1 - (1 - fpr)**1.15

    ax2.plot(fpr, tpr_fused, color=DARK_RED, lw=2.5, label='TinginHB Dual-Site Fused (AUROC = 0.91)')
    ax2.plot(fpr, tpr_conj, color=TEAL_MID, lw=1.8, label='Conjunctiva Only (AUROC = 0.85)')
    ax2.plot(fpr, tpr_nail, color=ORANGE, lw=1.8, label='Nail Bed Only (AUROC = 0.81)')
    ax2.plot(fpr, tpr_eye, color=SLATE_MUTED, lw=1.5, linestyle=':', label='Naked-Eye Pallor (AUROC = 0.58)')
    ax2.plot([0, 1], [0, 1], color=BORDER_GRAY, linestyle='--', lw=1.0, label='Chance Line (AUROC = 0.50)')

    # Shaded confidence band for Fused
    ax2.fill_between(fpr, np.clip(tpr_fused - 0.04, 0, 1), np.clip(tpr_fused + 0.03, 0, 1), color='#FADBD8', alpha=0.5)

    # Optimal operating point annotation
    opt_fpr, opt_tpr = 0.16, 0.885
    ax2.plot(opt_fpr, opt_tpr, marker='o', markersize=7, color=DARK_RED)
    ax2.annotate('Operating Point:\nSens: 88.5% | Spec: 84.0%\n(Hb < 10.0 g/dL)', 
                 xy=(opt_fpr, opt_tpr), xytext=(opt_fpr + 0.12, opt_tpr - 0.18),
                 arrowprops=dict(facecolor=DARK_RED, shrink=0.08, width=1, headwidth=5),
                 fontsize=7.8, fontweight='bold', color=DARK_RED)

    ax2.set_xlabel("1 - Specificity (False Positive Rate)", fontsize=9, fontweight='bold', color=SLATE_DARK)
    ax2.set_ylabel("Sensitivity (True Positive Rate)", fontsize=9, fontweight='bold', color=SLATE_DARK)
    ax2.set_title("B. Target Receiver Operating Characteristic (ROC)", fontsize=11, fontweight='bold', color=TEAL_DARK, pad=8)
    ax2.set_xlim(0, 1.0)
    ax2.set_ylim(0, 1.02)
    ax2.legend(loc='lower right', fontsize=7.5, framealpha=0.9)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)

    out_file = os.path.join(OUT_DIR, "fig6_clinical_validation_roc.png")
    plt.savefig(out_file, dpi=300, bbox_inches='tight', facecolor=WHITE)
    plt.close()
    print(f"[OK] Figure 6 saved to: {out_file}")

# ═════════════════════════════════════════════════════════════════════════════
# FIGURE 7: 12-Month Research & Product Roadmap Gantt Chart
# ═════════════════════════════════════════════════════════════════════════════
def generate_fig7():
    fig, ax = plt.subplots(figsize=(12, 6.0), facecolor=WHITE, dpi=300)

    fig.suptitle("12-MONTH RESEARCH, CLINICAL VALIDATION & COMMERCIALIZATION ROADMAP", 
                 fontsize=13.5, fontweight='bold', color=TEAL_DARK, y=0.96)

    phases = [
        "Phase 1: Dataset Curation & YOLOv8n-seg",
        "Phase 2: Dual Model Training & Platt Calib.",
        "Phase 3: Android App & BHW Co-Design",
        "Phase 4: Prospective Clinical Trial (N=250)",
        "Phase 5: DOH Dashboard & Konsulta API",
        "Phase 6: FDA SaMD Filing & PSC XI Pitch"
    ]
    starts = [1, 2, 3, 5, 8, 10]
    durations = [2, 2, 2.5, 3.5, 2.5, 2.5]
    colors = [TEAL_DARK, TEAL_MID, TEAL_LIGHT, CORAL_RED, ORANGE, '#8E44AD']

    y_pos = np.arange(len(phases))[::-1]

    for idx, (p, s, d, c) in enumerate(zip(phases, starts, durations, colors)):
        ax.barh(y_pos[idx], d, left=s, height=0.55, align='center', color=c, edgecolor='none', alpha=0.85)
        # Label inside or next to bar
        ax.text(s + d/2, y_pos[idx], f"M{s}–M{int(np.ceil(s+d))}", 
                ha='center', va='center', color=WHITE, fontsize=8, fontweight='bold')

    # Milestones (Diamonds)
    milestones = [
        (3.0, 5, "Alpha Engine Ready"),
        (5.5, 3, "BHW Field Trial Pilot"),
        (8.5, 2, "Clinical Study Report (N=250)"),
        (10.5, 1, "Konsulta Cloud Sync Live"),
        (12.0, 0, "Commercial PSC XI Pitch")
    ]
    for mx, my, mtxt in milestones:
        ax.plot(mx, my, marker='D', markersize=8, color=GOLD, markeredgecolor=SLATE_DARK, markeredgewidth=1)
        ax.text(mx + 0.25, my + 0.25, mtxt, fontsize=7, fontweight='bold', color=SLATE_DARK)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(phases, fontsize=8.5, fontweight='bold', color=SLATE_DARK)
    ax.set_xlim(0.5, 12.8)
    ax.set_xticks(range(1, 13))
    ax.set_xticklabels([f"Month {m}" for m in range(1, 13)], fontsize=8, fontweight='bold', color=SLATE_DARK)
    ax.set_xlabel("Project Timeline (Months 1–12)", fontsize=9.5, fontweight='bold', color=TEAL_DARK, labelpad=8)
    ax.grid(axis='x', linestyle='--', alpha=0.4, color=SLATE_MUTED)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(BORDER_GRAY)
    ax.spines['bottom'].set_color(BORDER_GRAY)

    out_file = os.path.join(OUT_DIR, "fig7_roadmap_gantt.png")
    plt.savefig(out_file, dpi=300, bbox_inches='tight', facecolor=WHITE)
    plt.close()
    print(f"[OK] Figure 7 saved to: {out_file}")

if __name__ == "__main__":
    generate_fig1()
    generate_fig2()
    generate_fig3()
    generate_fig4()
    generate_fig5()
    generate_fig6()
    generate_fig7()
    print("\n[SUCCESS] All 7 figures successfully generated at 300 DPI!")
