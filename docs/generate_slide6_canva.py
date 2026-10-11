"""
generate_slide6_canva.py
Renders Slide 6 emphasizing the 6-step on-device Edge-AI pipeline in a clean,
modern 3x2 grid layout matching Canva's minimalist light-mode aesthetic.
Outputs: docs/figures/canva/slide6_canva.png
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT_DIR = os.path.join(os.path.dirname(__file__), "figures", "canva")
os.makedirs(OUT_DIR, exist_ok=True)
OUT_FILE = os.path.join(OUT_DIR, "slide6_canva.png")

# ─── COLOR PALETTE ───────────────────────────────────────────────────────────
CANVAS_BG     = "#FFFFFF"
CARD_BG       = "#FFFFFF"
CARD_STROKE   = "#E2E8F0"
TEAL_PRIMARY  = "#0E4D64"
TEAL_MID      = "#1B6B8A"
TEAL_LIGHT    = "#E0F2FE"
TEAL_BORDER   = "#BAE6FD"
SLATE_DARK    = "#1E293B"
SLATE_BODY    = "#334155"
SLATE_MUTED   = "#64748B"
BORDER_LIGHT  = "#E2E8F0"

GREEN_BG      = "#DCFCE7"
GREEN_BORDER  = "#86EFAC"
GREEN_TEXT    = "#166534"

GOLD_BG       = "#FEF3C7"
GOLD_BORDER   = "#FDE68A"
GOLD_TEXT     = "#92400E"

ROSE_BG       = "#FEE2E2"
ROSE_BORDER   = "#FECACA"
ROSE_TEXT     = "#991B1B"

PURPLE_BG     = "#F3E8FF"
PURPLE_BORDER = "#D8B4FE"
PURPLE_TEXT   = "#6B21A8"

BLUE_BG       = "#EFF6FF"
BLUE_BORDER   = "#BFDBFE"
BLUE_TEXT     = "#1D4ED8"

plt.rcParams['font.sans-serif'] = ['Segoe UI', 'DejaVu Sans', 'Arial', 'sans-serif']
plt.rcParams['font.family'] = 'sans-serif'

def build_slide6():
    # 1920 x 1080 px at 120 DPI -> 16.0 x 9.0 inches
    fig = plt.figure(figsize=(16.0, 9.0), dpi=120, facecolor=CANVAS_BG)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # ═════════════════════════════════════════════════════════════════════════
    # 1. HEADER SECTION
    # ═════════════════════════════════════════════════════════════════════════
    # Eyebrow Pill
    eyebrow = FancyBboxPatch((0.04, 0.932), 0.36, 0.030, boxstyle="round,pad=0.005,rounding_size=0.008",
                             fc=TEAL_LIGHT, ec=TEAL_BORDER, lw=1)
    ax.add_patch(eyebrow)
    ax.text(0.048, 0.947, "END-TO-END OFFLINE EDGE-AI ARCHITECTURE", 
            fontsize=8.5, fontweight='bold', color=TEAL_MID, va='center')

    # Status / Metric Pill (Top Right)
    spec_box = FancyBboxPatch((0.68, 0.932), 0.28, 0.030, boxstyle="round,pad=0.005,rounding_size=0.008",
                              fc="#F8FAFC", ec=BORDER_LIGHT, lw=1)
    ax.add_patch(spec_box)
    ax.text(0.82, 0.947, "<10 MB APK  •  <450ms Latency  •  100% Offline", 
            fontsize=8.5, fontweight='bold', color=SLATE_MUTED, va='center', ha='center')

    # Main Title
    ax.text(0.04, 0.892, "Engineering Features: The 6-Stage Edge Pipeline",
            fontsize=19, fontweight='bold', color=TEAL_PRIMARY, va='center')

    # Subtitle
    ax.text(0.04, 0.858, "Sequential on-device machine learning workflow delivering calibrated triage on low-cost ₱5,000 Android phones",
            fontsize=10.5, color=SLATE_MUTED, va='center')

    # Thin Divider Line
    ax.plot([0.04, 0.96], [0.838, 0.838], color=BORDER_LIGHT, lw=1.2)

    # ═════════════════════════════════════════════════════════════════════════
    # 2. 6-STAGE PIPELINE CARDS (3 COLUMNS x 2 ROWS)
    # ═════════════════════════════════════════════════════════════════════════
    col_w = 0.288
    row_h = 0.345
    gap_x = 0.028
    gap_y = 0.024

    cols_x = [0.04, 0.04 + col_w + gap_x, 0.04 + 2 * (col_w + gap_x)]
    rows_y = [0.472, 0.103]

    steps = [
        {
            "step": "STEP 01",
            "title": "Assisted Acquisition & QC",
            "tag": "STAGE 1 • 40ms",
            "tag_bg": GREEN_BG, "tag_border": GREEN_BORDER, "tag_text": GREEN_TEXT,
            "card_bg": "#FAFCFD", "card_border": GREEN_BORDER,
            "bullets": [
                ("CameraX Biometric Reticle:", "Guided elliptical targeting ensures proper distance, framing, and anatomical alignment."),
                ("Laplacian Blur Gate:", "Rejects unsteady hand tremor via variance threshold Var(Laplacian) > 120 before inference."),
                ("Exposure & Glare Lock:", "Auto-locks AE and AWB to prevent specular LED reflections on mucosal tissue.")
            ]
        },
        {
            "step": "STEP 02",
            "title": "Quantized ROI Segmentation",
            "tag": "STAGE 2 • 80ms",
            "tag_bg": TEAL_LIGHT, "tag_border": TEAL_BORDER, "tag_text": TEAL_MID,
            "card_bg": "#FAFCFD", "card_border": TEAL_BORDER,
            "bullets": [
                ("YOLOv8n-seg INT8 Model:", "Quantized to 8-bit integer weights with an ultra-compact ~3.5 MB storage footprint."),
                ("Multi-Anatomical Masks:", "Simultaneously segments palpebral conjunctiva, sclera, and nail bed (mAP@50 > 0.92)."),
                ("Pixel-Level Extraction:", "Isolates high-SNR capillary vascular regions from surrounding skin and eyelash noise.")
            ]
        },
        {
            "step": "STEP 03",
            "title": "Dual-Branch Radiomics",
            "tag": "STAGE 3 • 140ms",
            "tag_bg": GOLD_BG, "tag_border": GOLD_BORDER, "tag_text": GOLD_TEXT,
            "card_bg": "#FAFCFD", "card_border": GOLD_BORDER,
            "bullets": [
                ("Branch A (Deep Learning):", "MobileNetV3-Small FP16 (~5.2 MB) extracts invariant deep vascular feature maps."),
                ("Branch B (Color Radiomics):", "16 handcrafted physical traits: Erythema Index (EI), Pallor Index (PI), and CIELAB a*, b*."),
                ("Biophysical Grounding:", "Aligns camera Bayer green pixels with 540nm and 576nm oxyhemoglobin extinction peaks.")
            ]
        },
        {
            "step": "STEP 04",
            "title": "Epistemic Uncertainty",
            "tag": "STAGE 4 • 120ms",
            "tag_bg": BLUE_BG, "tag_border": BLUE_BORDER, "tag_text": BLUE_TEXT,
            "card_bg": "#FAFCFD", "card_border": BLUE_BORDER,
            "bullets": [
                ("Monte Carlo Dropout:", "Executes N=50 stochastic passes at test time to quantify predictive variance (σ²)."),
                ("Inverse-Variance Fusion:", "Dynamically weights modalities by reliability (w_i = 1/σ_i²), down-weighting noisy images."),
                ("Discrepancy Safety Alert:", "Flags differences >2.0 g/dL between eye and nail, triggering palmar confirmation.")
            ]
        },
        {
            "step": "STEP 05",
            "title": "Platt Scaling Calibration",
            "tag": "STAGE 5 • 35ms",
            "tag_bg": PURPLE_BG, "tag_border": PURPLE_BORDER, "tag_text": PURPLE_TEXT,
            "card_bg": "#FAFCFD", "card_border": PURPLE_BORDER,
            "bullets": [
                ("Probability Calibration:", "Post-hoc logistic Platt scaling minimizes Expected Calibration Error (ECE ≤ 0.08)."),
                ("WHO 4-Tier Stratification:", "Maps probabilities directly to WHO tiers: Normal, Mild Buffer, Refer, and Urgent."),
                ("Venous CBC Ground Truth:", "Calibrated against paired Sysmex XN-550 automated hematology reference testing.")
            ]
        },
        {
            "step": "STEP 06",
            "title": "Standardized Clinical Referral",
            "tag": "STAGE 6 • 15ms",
            "tag_bg": ROSE_BG, "tag_border": ROSE_BORDER, "tag_text": ROSE_TEXT,
            "card_bg": "#FAFCFD", "card_border": ROSE_BORDER,
            "bullets": [
                ("Pre-Filled Konsulta PDF:", "Auto-generates standardized referral endorsement slip matching PhilHealth Annex format."),
                ("Physician Gatekeeping:", "Empowers rural doctors to validate objective triage data without re-testing delays."),
                ("100% Offline Privacy:", "Zero patient imagery leaves device; all biometric processing runs locally on-chip.")
            ]
        }
    ]

    for idx, s in enumerate(steps):
        col_idx = idx % 3
        row_idx = idx // 3
        cx = cols_x[col_idx]
        cy = rows_y[row_idx]

        # Main Card Box
        card = FancyBboxPatch((cx, cy), col_w, row_h, boxstyle="round,pad=0.008,rounding_size=0.014",
                              fc="#FFFFFF", ec=s["card_border"], lw=1.5)
        ax.add_patch(card)

        # Step Pill Badge (Top Left of Card)
        step_box = FancyBboxPatch((cx + 0.014, cy + row_h - 0.046), 0.082, 0.026,
                                  boxstyle="round,pad=0.003,rounding_size=0.006",
                                  fc=TEAL_PRIMARY, ec=TEAL_PRIMARY, lw=1)
        ax.add_patch(step_box)
        ax.text(cx + 0.055, cy + row_h - 0.033, s["step"],
                fontsize=8.5, fontweight='bold', color="#FFFFFF", ha='center', va='center')

        # Tag Badge (Top Right of Card)
        tag_box = FancyBboxPatch((cx + col_w - 0.098, cy + row_h - 0.046), 0.084, 0.026,
                                 boxstyle="round,pad=0.003,rounding_size=0.006",
                                 fc=s["tag_bg"], ec=s["tag_border"], lw=0.8)
        ax.add_patch(tag_box)
        ax.text(cx + col_w - 0.056, cy + row_h - 0.033, s["tag"],
                fontsize=7.5, fontweight='bold', color=s["tag_text"], ha='center', va='center')

        # Card Title
        ax.text(cx + 0.014, cy + row_h - 0.078, s["title"],
                fontsize=11.5, fontweight='bold', color=SLATE_DARK, va='center')

        # Thin Internal Separator
        ax.plot([cx + 0.014, cx + col_w - 0.014], [cy + row_h - 0.096, cy + row_h - 0.096],
                color=BORDER_LIGHT, lw=0.8)

        # Bullets Section
        bullet_start_y = cy + row_h - 0.125
        bullet_spacing = 0.072

        for b_idx, (b_head, b_desc) in enumerate(s["bullets"]):
            by = bullet_start_y - b_idx * bullet_spacing
            
            # Bullet dot
            ax.scatter([cx + 0.018], [by], color=TEAL_PRIMARY, s=12, zorder=5)
            
            # Bullet header
            ax.text(cx + 0.028, by, b_head,
                    fontsize=8.2, fontweight='bold', color=TEAL_PRIMARY, va='center')
            
            # Bullet description (wrapped)
            ax.text(cx + 0.028, by - 0.022, b_desc,
                    fontsize=7.6, color=SLATE_BODY, va='center', wrap=True)

        # Connecting Flow Arrows between steps
        if col_idx < 2:
            arrow_x = cx + col_w + 0.006
            arrow_y = cy + row_h / 2
            ax.annotate('', xy=(arrow_x + 0.015, arrow_y), xytext=(arrow_x, arrow_y),
                        arrowprops=dict(arrowstyle="-|>", color=TEAL_MID, lw=1.5, mutation_scale=12))

    # ═════════════════════════════════════════════════════════════════════════
    # 3. BOTTOM HARDWARE GUARANTEES STRIP
    # ═════════════════════════════════════════════════════════════════════════
    foot_box = FancyBboxPatch((0.04, 0.022), 0.92, 0.054, boxstyle="round,pad=0.005,rounding_size=0.01",
                              fc="#0E4D64", ec="#0E4D64", lw=1)
    ax.add_patch(foot_box)
    
    ax.text(0.50, 0.049, "HARDWARE GUARANTEE:  ₱5,000 Budget Android (2GB RAM)  |  <10 MB Total Storage  |  <415ms Execution (<450ms Budget)  |  100% Offline Edge Sovereignty",
            fontsize=8.5, fontweight='bold', color="#FFFFFF", ha='center', va='center')

    # Save output
    plt.savefig(OUT_FILE, dpi=120, facecolor=CANVAS_BG)
    plt.close()
    print(f"[SUCCESS] Remade Slide 6 saved at: {OUT_FILE}")

if __name__ == "__main__":
    build_slide6()
