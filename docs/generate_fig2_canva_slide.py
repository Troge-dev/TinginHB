"""
generate_fig2_canva_slide.py
Renders Figure 2 in 16:9 widescreen (1920 x 1080 px) matching Canva's
minimalist light-mode presentation design system.
Outputs: docs/figures/canva/fig2_canva.png
"""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch

OUT_DIR = os.path.join(os.path.dirname(__file__), "figures", "canva")
os.makedirs(OUT_DIR, exist_ok=True)
OUT_FILE = os.path.join(OUT_DIR, "fig2_canva.png")

# ─── COLOR PALETTE ───────────────────────────────────────────────────────────
CANVAS_BG     = "#FFFFFF"
CARD_BG       = "#FFFFFF"
TEAL_PRIMARY  = "#0E4D64"
TEAL_MID      = "#1B6B8A"
TEAL_LIGHT    = "#E0F2FE"
TEAL_BORDER   = "#BAE6FD"
ROSE_BG       = "#FFF5F5"
ROSE_BORDER   = "#FECACA"
RED_PRIMARY   = "#DC2626"
RED_DARK      = "#991B1B"
RED_BORDER    = "#FECACA"
GREEN_BAND_BG = "#DCFCE7"
GREEN_BORDER  = "#86EFAC"
GREEN_TEXT    = "#166534"
SLATE_DARK    = "#1E293B"
SLATE_BODY    = "#334155"
SLATE_MUTED   = "#64748B"
BORDER_LIGHT  = "#E2E8F0"
GOLD_ACCENT   = "#D97706"

# Font selection
plt.rcParams['font.sans-serif'] = ['Segoe UI', 'DejaVu Sans', 'Arial', 'sans-serif']
plt.rcParams['font.family'] = 'sans-serif'

def build_fig2_slide():
    # 1920 x 1080 px at 120 DPI -> 16.0 x 9.0 inches
    fig = plt.figure(figsize=(16.0, 9.0), dpi=120, facecolor=CANVAS_BG)
    
    # Base canvas coordinate system: [0, 1] in x and y
    ax_bg = fig.add_axes([0, 0, 1, 1])
    ax_bg.axis('off')
    ax_bg.set_xlim(0, 1)
    ax_bg.set_ylim(0, 1)

    # ═════════════════════════════════════════════════════════════════════════
    # 1. HEADER SECTION
    # ═════════════════════════════════════════════════════════════════════════
    # Category Eyebrow Pill
    eyebrow_box = FancyBboxPatch((0.04, 0.925), 0.32, 0.032, boxstyle="round,pad=0.005,rounding_size=0.01",
                                 fc=TEAL_LIGHT, ec=TEAL_BORDER, lw=1)
    ax_bg.add_patch(eyebrow_box)
    ax_bg.text(0.048, 0.941, "OPTICAL BIOPHYSICS & ANATOMICAL MECHANISMS", 
               fontsize=8.5, fontweight='bold', color=TEAL_MID, va='center')

    # Status / Spec Pill (Top Right)
    spec_box = FancyBboxPatch((0.68, 0.925), 0.28, 0.032, boxstyle="round,pad=0.005,rounding_size=0.01",
                              fc="#F1F5F9", ec=BORDER_LIGHT, lw=1)
    ax_bg.add_patch(spec_box)
    ax_bg.text(0.82, 0.941, "CMOS Green Band (520–585 nm)  •  0-Melanin Mucosa", 
               fontsize=8.5, fontweight='bold', color=SLATE_MUTED, va='center', ha='center')

    # Main Title
    ax_bg.text(0.04, 0.885, "Figure 2: Microvascular Optical Anatomy & Spectral Absorption Bases",
               fontsize=18, fontweight='bold', color=TEAL_PRIMARY, va='center')

    # Subtitle
    ax_bg.text(0.04, 0.852, "Hemoglobin spectral extinction mechanics and multi-site microvascular signal pathways for non-invasive hemoglobin estimation",
               fontsize=10.5, color=SLATE_MUTED, va='center')

    # Thin Divider
    ax_bg.plot([0.04, 0.96], [0.835, 0.835], color=BORDER_LIGHT, lw=1.2)

    # ═════════════════════════════════════════════════════════════════════════
    # 2. LEFT PANEL: SPECTRAL ABSORPTION PLOT & CMOS SENSITIVITY
    # ═════════════════════════════════════════════════════════════════════════
    left_card = FancyBboxPatch((0.04, 0.095), 0.46, 0.725, boxstyle="round,pad=0.01,rounding_size=0.015",
                               fc=CARD_BG, ec=BORDER_LIGHT, lw=1.5)
    ax_bg.add_patch(left_card)

    # Card Title
    ax_bg.text(0.055, 0.795, "A. Hemoglobin Optical Absorption Spectrum & CMOS Band", 
               fontsize=12, fontweight='bold', color=TEAL_PRIMARY, va='center')
    ax_bg.text(0.055, 0.772, "Molar extinction coefficient (ε) curves and camera Bayer filter SNR alignment", 
               fontsize=9, color=SLATE_MUTED, va='center')

    # Subplot for Spectral Curve inside Left Card
    # Normalized position: [left, bottom, width, height]
    ax_plot = fig.add_axes([0.075, 0.25, 0.40, 0.48], facecolor="#FFFFFF")
    
    wavelengths = np.linspace(450, 650, 500)
    # Calibrated extinction modeling matching Prahl (1999) & Zijlstra (2000)
    ext_hbo2 = (0.58 * np.exp(-((wavelengths - 540)/12.5)**2) + 
                0.64 * np.exp(-((wavelengths - 576)/13.5)**2) + 
                0.32 * np.exp(-((wavelengths - 500)/32.0)**2) + 
                0.12 * np.exp(-((wavelengths - 635)/45.0)**2))
    ext_hb = (0.52 * np.exp(-((wavelengths - 555)/26.0)**2) + 
              0.28 * np.exp(-((wavelengths - 485)/35.0)**2) + 
              0.16 * np.exp(-((wavelengths - 620)/35.0)**2))

    idx_540 = np.argmin(np.abs(wavelengths - 540))
    idx_576 = np.argmin(np.abs(wavelengths - 576))
    idx_555 = np.argmin(np.abs(wavelengths - 555))
    val_540 = ext_hbo2[idx_540]
    val_576 = ext_hbo2[idx_576]
    val_555 = ext_hb[idx_555]

    # Green Bayer band shaded region (520nm - 585nm)
    ax_plot.axvspan(520, 585, color=GREEN_BAND_BG, alpha=0.75, zorder=1)
    ax_plot.axvline(520, color=GREEN_BORDER, linestyle=':', lw=1.2, zorder=2)
    ax_plot.axvline(585, color=GREEN_BORDER, linestyle=':', lw=1.2, zorder=2)
    
    # Label for Green Band
    ax_plot.text(552.5, 0.98, "Green Sensor Band\n(Optimal CMOS SNR)", 
                 ha='center', va='top', fontsize=8, fontweight='bold', color=GREEN_TEXT,
                 bbox=dict(boxstyle="round,pad=0.25", fc="#FFFFFF", ec=GREEN_BORDER, lw=0.8), zorder=4)

    # Plot lines
    l1, = ax_plot.plot(wavelengths, ext_hbo2, color=RED_PRIMARY, lw=2.6, label=r'Oxyhemoglobin ($HbO_2$)', zorder=3)
    l2, = ax_plot.plot(wavelengths, ext_hb, color=TEAL_MID, lw=2.0, linestyle='--', label=r'Deoxyhemoglobin ($Hb$)', zorder=3)

    # Marker Pins for Twin Peaks directly on the curve
    # 540nm
    ax_plot.scatter([540], [val_540], color=RED_PRIMARY, s=45, zorder=5, edgecolor='#FFFFFF', lw=1.5)
    ax_plot.annotate('Primary Peak\n540 nm', xy=(540, val_540), xytext=(505, 0.85),
                     arrowprops=dict(arrowstyle="->", color=RED_DARK, lw=1.2),
                     fontsize=8, fontweight='bold', color=RED_DARK, ha='center',
                     bbox=dict(boxstyle="round,pad=0.2", fc="#FFF5F5", ec=RED_PRIMARY, lw=0.7))

    # 576nm
    ax_plot.scatter([576], [val_576], color=RED_PRIMARY, s=45, zorder=5, edgecolor='#FFFFFF', lw=1.5)
    ax_plot.annotate('Secondary Peak\n576 nm', xy=(576, val_576), xytext=(615, 0.85),
                     arrowprops=dict(arrowstyle="->", color=RED_DARK, lw=1.2),
                     fontsize=8, fontweight='bold', color=RED_DARK, ha='center',
                     bbox=dict(boxstyle="round,pad=0.2", fc="#FFF5F5", ec=RED_PRIMARY, lw=0.7))

    # Single broad peak 555nm
    ax_plot.scatter([555], [val_555], color=TEAL_MID, s=35, zorder=5, edgecolor='#FFFFFF', lw=1.2)
    ax_plot.annotate('Hb Peak\n555 nm', xy=(555, val_555), xytext=(555, 0.36),
                     arrowprops=dict(arrowstyle="->", color=TEAL_MID, lw=1.0),
                     fontsize=7.5, fontweight='bold', color=TEAL_MID, ha='center',
                     bbox=dict(boxstyle="round,pad=0.2", fc="#F0F9FF", ec=TEAL_BORDER, lw=0.6))

    ax_plot.set_xlim(450, 650)
    ax_plot.set_ylim(0, 1.05)
    ax_plot.set_xlabel("Optical Wavelength (nm)", fontsize=8.5, fontweight='bold', color=SLATE_DARK)
    ax_plot.set_ylabel("Molar Extinction Coefficient (Relative)", fontsize=8.5, fontweight='bold', color=SLATE_DARK)
    ax_plot.tick_params(colors=SLATE_DARK, labelsize=8)
    ax_plot.grid(True, linestyle='--', alpha=0.35, color=BORDER_LIGHT)
    
    # Modern clean spines
    ax_plot.spines['top'].set_visible(False)
    ax_plot.spines['right'].set_visible(False)
    ax_plot.spines['left'].set_color(BORDER_LIGHT)
    ax_plot.spines['bottom'].set_color(BORDER_LIGHT)
    ax_plot.legend(loc='lower left', fontsize=7.8, framealpha=0.95, edgecolor=BORDER_LIGHT)

    # Physics Callout Box at bottom of Left Card
    phys_box = FancyBboxPatch((0.055, 0.115), 0.43, 0.105, boxstyle="round,pad=0.008,rounding_size=0.01",
                              fc="#F8FAFC", ec=BORDER_LIGHT, lw=1)
    ax_bg.add_patch(phys_box)
    
    ax_bg.text(0.065, 0.198, "BEER-LAMBERT ATTENUATION & ERYTHEMA FORMULATION:", 
               fontsize=8, fontweight='bold', color=TEAL_PRIMARY, va='center')
    ax_bg.text(0.065, 0.168, "• Attenuation Model:  A(λ) = ln(I₀ / I) = ε(λ) · c · d   [c = [Hb], d = optical path length]",
               fontsize=7.8, color=SLATE_BODY, va='center')
    ax_bg.text(0.065, 0.140, "• Erythema Index (EI):  EI = log₁₀(1 / R_red) - log₁₀(1 / R_green)   (Calibrated against Sysmex CBC)",
               fontsize=7.8, color=SLATE_BODY, va='center')

    # ═════════════════════════════════════════════════════════════════════════
    # 3. RIGHT PANEL: DUAL ANATOMICAL MICROVASCULAR SIGNAL PATHWAYS
    # ═════════════════════════════════════════════════════════════════════════
    
    # ─── TOP RIGHT CARD: PALPEBRAL CONJUNCTIVA (PRIMARY SITE) ───────────────
    card_eye = FancyBboxPatch((0.52, 0.470), 0.44, 0.350, boxstyle="round,pad=0.01,rounding_size=0.015",
                              fc=ROSE_BG, ec=ROSE_BORDER, lw=1.5)
    ax_bg.add_patch(card_eye)

    # Site Header Badges
    eye_badge = FancyBboxPatch((0.535, 0.778), 0.195, 0.028, boxstyle="round,pad=0.004,rounding_size=0.008",
                               fc="#FEE2E2", ec=RED_PRIMARY, lw=1)
    ax_bg.add_patch(eye_badge)
    ax_bg.text(0.632, 0.792, "PRIMARY SITE: INNER EYELID", fontsize=8, fontweight='bold', color=RED_DARK, ha='center', va='center')

    # Stat Badges
    stat_eye1 = FancyBboxPatch((0.745, 0.778), 0.095, 0.028, boxstyle="round,pad=0.004,rounding_size=0.008",
                               fc="#FFFFFF", ec=RED_BORDER, lw=0.8)
    ax_bg.add_patch(stat_eye1)
    ax_bg.text(0.792, 0.792, "LR+ ≈ 4.4", fontsize=8, fontweight='bold', color=RED_DARK, ha='center', va='center')

    stat_eye2 = FancyBboxPatch((0.85, 0.778), 0.095, 0.028, boxstyle="round,pad=0.004,rounding_size=0.008",
                               fc="#FFFFFF", ec=GREEN_BORDER, lw=0.8)
    ax_bg.add_patch(stat_eye2)
    ax_bg.text(0.897, 0.792, "SNR: OPTIMAL", fontsize=8, fontweight='bold', color=GREEN_TEXT, ha='center', va='center')

    # Card Title
    ax_bg.text(0.535, 0.744, "Palpebral Conjunctiva & Scleral White Balance", fontsize=12, fontweight='bold', color=SLATE_DARK, va='center')
    ax_bg.text(0.535, 0.723, "Non-invasive vascular inspection site with 0-melanin mucosal epithelial barrier", fontsize=8.5, color=SLATE_MUTED, va='center')

    # Eye Bullets
    ax_bg.text(0.535, 0.682, "1. Zero Melanocyte Epithelium (Fitzpatrick I–VI Invariance):", 
               fontsize=8.5, fontweight='bold', color=RED_DARK, va='center')
    ax_bg.text(0.552, 0.660, "Non-keratinized mucosal epithelium contains zero melanocytes. Eliminates skin pigmentation confounding", 
               fontsize=8, color=SLATE_BODY, va='center')
    ax_bg.text(0.552, 0.642, "and racial bias across all skin tones without algorithmic melanin correction factor.", 
               fontsize=8, color=SLATE_BODY, va='center')

    ax_bg.text(0.535, 0.605, "2. Superficial Microvascular Plexus (<100 µm depth):", 
               fontsize=8.5, fontweight='bold', color=SLATE_DARK, va='center')
    ax_bg.text(0.552, 0.583, "Dense capillary loops lie immediately beneath transparent tissue, directly exposing intravascular", 
               fontsize=8, color=SLATE_BODY, va='center')
    ax_bg.text(0.552, 0.565, "hemoglobin to incident smartphone flash/ambient illumination with minimal light scattering.", 
               fontsize=8, color=SLATE_BODY, va='center')

    ax_bg.text(0.535, 0.528, "3. Organic In-Scene Scleral White Balance Reference:", 
               fontsize=8.5, fontweight='bold', color=TEAL_PRIMARY, va='center')
    ax_bg.text(0.552, 0.506, "Adjacent avascular white sclera provides a natural, co-located neutral reference (R ≈ G ≈ B) in every", 
               fontsize=8, color=SLATE_BODY, va='center')
    ax_bg.text(0.552, 0.488, "single frame, completely eliminating the need for physical calibration cards (X-Rite / Teflon tiles).", 
               fontsize=8, color=SLATE_BODY, va='center')

    # ─── BOTTOM RIGHT CARD: SUBUNGUAL NAIL BED (SECONDARY SITE) ────────────
    card_nail = FancyBboxPatch((0.52, 0.095), 0.44, 0.355, boxstyle="round,pad=0.01,rounding_size=0.015",
                               fc="#F0F9FF", ec=TEAL_BORDER, lw=1.5)
    ax_bg.add_patch(card_nail)

    # Site Header Badges
    nail_badge = FancyBboxPatch((0.535, 0.407), 0.205, 0.03, boxstyle="round,pad=0.004,rounding_size=0.008",
                                fc=TEAL_LIGHT, ec=TEAL_MID, lw=1)
    ax_bg.add_patch(nail_badge)
    ax_bg.text(0.637, 0.422, "SECONDARY SITE: SUBUNGUAL NAIL", fontsize=8, fontweight='bold', color=TEAL_PRIMARY, ha='center', va='center')

    # Stat Badges
    stat_nail1 = FancyBboxPatch((0.755, 0.407), 0.095, 0.03, boxstyle="round,pad=0.004,rounding_size=0.008",
                                fc="#FFFFFF", ec=TEAL_BORDER, lw=0.8)
    ax_bg.add_patch(stat_nail1)
    ax_bg.text(0.802, 0.422, "LR+ ≈ 2.2", fontsize=8, fontweight='bold', color=TEAL_PRIMARY, ha='center', va='center')

    stat_nail2 = FancyBboxPatch((0.86, 0.407), 0.085, 0.03, boxstyle="round,pad=0.004,rounding_size=0.008",
                                fc="#FFFFFF", ec=BORDER_LIGHT, lw=0.8)
    ax_bg.add_patch(stat_nail2)
    ax_bg.text(0.902, 0.422, "KERATIN: 0.6mm", fontsize=7.5, fontweight='bold', color=SLATE_MUTED, ha='center', va='center')

    # Card Title
    ax_bg.text(0.535, 0.373, "Subungual Nail Bed & Contrast Ratio Melanin Normalization", fontsize=12, fontweight='bold', color=SLATE_DARK, va='center')
    ax_bg.text(0.535, 0.350, "Uniform keratin optical transmission window paired with periungual melanin subtraction", fontsize=8.5, color=SLATE_MUTED, va='center')

    # Nail Bullets
    ax_bg.text(0.535, 0.307, "1. Translucent Keratin Window (0.5–0.8 mm Thickness):", 
               fontsize=8.5, fontweight='bold', color=TEAL_PRIMARY, va='center')
    ax_bg.text(0.552, 0.283, "Compact translucent nail plate transmits incident light directly into the subungual vascular bed,", 
               fontsize=8, color=SLATE_BODY, va='center')
    ax_bg.text(0.552, 0.265, "avoiding thick epidermal stratum corneum scattering present in palmar skin.", 
               fontsize=8, color=SLATE_BODY, va='center')

    ax_bg.text(0.535, 0.227, "2. Contrast Ratio (CR) Melanin Subtraction Formula:", 
               fontsize=8.5, fontweight='bold', color=GOLD_ACCENT, va='center')
    ax_bg.text(0.552, 0.203, "Normalized ratio:  CR = (G_nail - G_skin) / (G_nail + G_skin)   (Mannino et al., Nature Comm. 2018)", 
               fontsize=8, fontweight='bold', color=SLATE_DARK, va='center')
    ax_bg.text(0.552, 0.185, "Subtracts individualized periungual skin pigmentation baseline directly from the vascular reading.", 
               fontsize=8, color=SLATE_BODY, va='center')

    ax_bg.text(0.535, 0.147, "3. Gentle Pediatric & Geriatric Fallback Modality:", 
               fontsize=8.5, fontweight='bold', color=SLATE_DARK, va='center')
    ax_bg.text(0.552, 0.125, "Provides a distress-free, motion-tolerant screening pathway for infants (6–11 mos) and agitated", 
               fontsize=8, color=SLATE_BODY, va='center')
    ax_bg.text(0.552, 0.107, "patients where manual eyelid retraction is clinically inadvisable or triggers reflex tears.", 
               fontsize=8, color=SLATE_BODY, va='center')

    # ═════════════════════════════════════════════════════════════════════════
    # 4. BOTTOM EDGE INTEGRATION STRIP
    # ═════════════════════════════════════════════════════════════════════════
    foot_box = FancyBboxPatch((0.04, 0.022), 0.92, 0.052, boxstyle="round,pad=0.005,rounding_size=0.01",
                              fc=TEAL_PRIMARY, ec=TEAL_PRIMARY, lw=1)
    ax_bg.add_patch(foot_box)
    
    ax_bg.text(0.50, 0.048, "EDGE-AI FUSION RULE:  Conjunctiva (35%) + Nail (25%) + Palm (15%) + Prior Survey (15%) + BP (10%)  |  Dynamic Rescaling: w'_i = w_i / Σ(w_avail)  |  100% Offline (<450ms)",
               fontsize=8.5, fontweight='bold', color="#FFFFFF", ha='center', va='center')

    # Save output
    plt.savefig(OUT_FILE, dpi=120, facecolor=CANVAS_BG)
    plt.close()
    print(f"[SUCCESS] Figure 2 Canva slide generated at: {OUT_FILE}")

if __name__ == "__main__":
    build_fig2_slide()
