"""
generate_slide6_canva.py
Renders Slide 6 (Engineering Features & System Architecture) in 16:9 widescreen
(1920 x 1080 px) matching Canva's minimalist light-mode presentation design.
Outputs: docs/figures/canva/slide6_canva.png
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
OUT_FILE = os.path.join(OUT_DIR, "slide6_canva.png")

# ─── COLOR PALETTE ───────────────────────────────────────────────────────────
CANVAS_BG     = "#FFFFFF"
CARD_BG       = "#FFFFFF"
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

# Font selection
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
    eyebrow = FancyBboxPatch((0.04, 0.925), 0.35, 0.032, boxstyle="round,pad=0.005,rounding_size=0.01",
                             fc=TEAL_LIGHT, ec=TEAL_BORDER, lw=1)
    ax.add_patch(eyebrow)
    ax.text(0.048, 0.941, "TECHNICAL SPECIFICATIONS & ON-DEVICE PIPELINE", 
            fontsize=8.5, fontweight='bold', color=TEAL_MID, va='center')

    # Status / Metric Pill (Top Right)
    spec_box = FancyBboxPatch((0.66, 0.925), 0.30, 0.032, boxstyle="round,pad=0.005,rounding_size=0.01",
                              fc="#F1F5F9", ec=BORDER_LIGHT, lw=1)
    ax.add_patch(spec_box)
    ax.text(0.81, 0.941, "<10 MB APK  •  <450ms Latency  •  100% Offline", 
            fontsize=8.5, fontweight='bold', color=SLATE_MUTED, va='center', ha='center')

    # Main Title
    ax.text(0.04, 0.885, "Engineering Features & System Architecture",
            fontsize=20, fontweight='bold', color=TEAL_PRIMARY, va='center')

    # Subtitle
    ax.text(0.04, 0.852, "End-to-end offline Edge-AI pipeline for non-invasive hemoglobin estimation on low-cost Android smartphones",
            fontsize=10.5, color=SLATE_MUTED, va='center')

    # Thin Divider
    ax.plot([0.04, 0.96], [0.835, 0.835], color=BORDER_LIGHT, lw=1.2)

    # ═════════════════════════════════════════════════════════════════════════
    # 2. LEFT PANEL: 6 STRUCTURED ENGINEERING MODULES
    # ═════════════════════════════════════════════════════════════════════════
    card_w = 0.58
    card_h = 0.108
    gap_y  = 0.015
    start_y = 0.705

    features = [
        {
            "num": "01",
            "title": "Assisted Acquisition & Laplacian Quality Gate",
            "line1": "CameraX automated capture lock rejects motion blur via Var(Laplacian) > 120,",
            "line2": "verifies uniform LED flash illuminance, and locks exposure to eliminate glare.",
            "tag": "QC GATE",
            "tag_color": GREEN_TEXT,
            "tag_bg": GREEN_BG,
            "tag_border": GREEN_BORDER
        },
        {
            "num": "02",
            "title": "Quantized INT8 ROI Segmentation Network",
            "line1": "YOLOv8n-seg quantized to 8-bit integer weights (~3.5 MB footprint, ~80ms latency).",
            "line2": "Isolates palpebral conjunctiva, sclera, and nail bed boundaries (mAP@50 > 0.92).",
            "tag": "3.5 MB INT8",
            "tag_color": TEAL_MID,
            "tag_bg": TEAL_LIGHT,
            "tag_border": TEAL_BORDER
        },
        {
            "num": "03",
            "title": "Dual-Branch Deep Radiomic Feature Extractor",
            "line1": "Branch A: MobileNetV3-Small (FP16, ~5.2 MB) deep vascular representations.",
            "line2": "Branch B: 16 handcrafted color traits (Erythema Index, Pallor Index, CIELAB a*, b*).",
            "tag": "HYBRID NET",
            "tag_color": GOLD_TEXT,
            "tag_bg": GOLD_BG,
            "tag_border": GOLD_BORDER
        },
        {
            "num": "04",
            "title": "Bayesian Epistemic Uncertainty Estimation Engine",
            "line1": "Monte Carlo Dropout (N=50 stochastic passes at inference to quantify variance σ²).",
            "line2": "Inverse-variance evidence fusion (w_i = 1/σ_i²) guards against poor image quality.",
            "tag": "MC DROPOUT",
            "tag_color": TEAL_PRIMARY,
            "tag_bg": TEAL_LIGHT,
            "tag_border": TEAL_BORDER
        },
        {
            "num": "05",
            "title": "Platt Scaling Probability Calibration (ECE ≤ 0.08)",
            "line1": "Post-hoc logistic calibration aligning continuous predictions with clinical prevalence.",
            "line2": "Stratifies risk into World Health Organization (WHO) 4-tier clinical triage protocols.",
            "tag": "WHO TIERS",
            "tag_color": GREEN_TEXT,
            "tag_bg": GREEN_BG,
            "tag_border": GREEN_BORDER
        },
        {
            "num": "06",
            "title": "Standardized Clinical Referral & Offline Privacy",
            "line1": "100% on-device data sovereignty; zero patient imagery leaves the smartphone.",
            "line2": "Generates standardized referral endorsement sheets for attending RHU physicians.",
            "tag": "DOH / KONSULTA",
            "tag_color": TEAL_MID,
            "tag_bg": TEAL_LIGHT,
            "tag_border": TEAL_BORDER
        }
    ]

    for i, feat in enumerate(features):
        y_pos = start_y - i * (card_h + gap_y)
        
        # Outer Card Box
        card = FancyBboxPatch((0.04, y_pos), card_w, card_h, boxstyle="round,pad=0.006,rounding_size=0.012",
                              fc="#F8FAFC", ec=BORDER_LIGHT, lw=1.2)
        ax.add_patch(card)

        # Number Badge Circle
        num_circle = FancyBboxPatch((0.052, y_pos + 0.032), 0.042, 0.044, boxstyle="round,pad=0.003,rounding_size=0.01",
                                    fc=TEAL_PRIMARY, ec=TEAL_PRIMARY, lw=1)
        ax.add_patch(num_circle)
        ax.text(0.073, y_pos + 0.054, feat["num"], fontsize=10, fontweight='bold', color="#FFFFFF", ha='center', va='center')

        # Feature Title
        ax.text(0.105, y_pos + 0.075, feat["title"], fontsize=9.5, fontweight='bold', color=SLATE_DARK, va='center')

        # Tag Badge
        tag_box = FancyBboxPatch((0.505, y_pos + 0.064), 0.102, 0.024, boxstyle="round,pad=0.003,rounding_size=0.006",
                                 fc=feat["tag_bg"], ec=feat["tag_border"], lw=0.8)
        ax.add_patch(tag_box)
        ax.text(0.556, y_pos + 0.076, feat["tag"], fontsize=7.5, fontweight='bold', color=feat["tag_color"], ha='center', va='center')

        # Description Lines
        ax.text(0.105, y_pos + 0.045, feat["line1"], fontsize=7.8, color=SLATE_BODY, va='center')
        ax.text(0.105, y_pos + 0.023, feat["line2"], fontsize=7.8, color=SLATE_BODY, va='center')

    # ═════════════════════════════════════════════════════════════════════════
    # 3. RIGHT PANEL: ARCHITECTURE STACK & HARDWARE BENCHMARKS
    # ═════════════════════════════════════════════════════════════════════════
    right_x = 0.64
    right_w = 0.32
    right_h = 0.725
    right_y = 0.095

    right_box = FancyBboxPatch((right_x, right_y), right_w, right_h, boxstyle="round,pad=0.01,rounding_size=0.015",
                               fc="#FFFFFF", ec=TEAL_BORDER, lw=1.5)
    ax.add_patch(right_box)

    # Right Header
    ax.text(right_x + 0.02, right_y + right_h - 0.035, "OFFLINE EDGE INFERENCE STACK",
            fontsize=11.5, fontweight='bold', color=TEAL_PRIMARY, va='center')
    ax.text(right_x + 0.02, right_y + right_h - 0.058, "Sequential execution pipeline (<450ms total budget)",
            fontsize=8.5, color=SLATE_MUTED, va='center')

    # Pipeline Flow Visual
    pipe_steps = [
        ("STAGE 1: INPUT ACQUISITION", "CameraX Viewfinder • Auto-Exposure • Laplacian Gate", "40ms", TEAL_LIGHT, TEAL_MID),
        ("STAGE 2: ROI SEGMENTATION", "INT8 YOLOv8n-seg • Conjunctiva & Nail Masks", "80ms", GREEN_BG, GREEN_TEXT),
        ("STAGE 3: FEATURE EXTRACTION", "MobileNetV3 FP16 Deep Radiomics + 16 Color Traits", "140ms", GOLD_BG, GOLD_TEXT),
        ("STAGE 4: BAYESIAN INFERENCE", "Monte Carlo Dropout (N=50) • Epistemic Uncertainty", "120ms", TEAL_LIGHT, TEAL_PRIMARY),
        ("STAGE 5: WHO TRIAGE & REFERRAL", "Platt Scaling Calibration • Konsulta Endorsement", "35ms", "#FEE2E2", "#991B1B"),
    ]

    pipe_start_y = right_y + right_h - 0.125
    pipe_h = 0.055
    pipe_gap = 0.024

    for j, (p_title, p_sub, p_lat, p_bg, p_col) in enumerate(pipe_steps):
        cur_py = pipe_start_y - j * (pipe_h + pipe_gap)
        p_card = FancyBboxPatch((right_x + 0.02, cur_py), right_w - 0.04, pipe_h,
                                boxstyle="round,pad=0.005,rounding_size=0.008",
                                fc=p_bg, ec=BORDER_LIGHT, lw=1)
        ax.add_patch(p_card)

        # Title & Latency
        ax.text(right_x + 0.03, cur_py + 0.037, p_title, fontsize=8, fontweight='bold', color=p_col, va='center')
        ax.text(right_x + right_w - 0.03, cur_py + 0.037, p_lat, fontsize=8, fontweight='bold', color=p_col, ha='right', va='center')
        # Subtitle
        ax.text(right_x + 0.03, cur_py + 0.016, p_sub, fontsize=7.2, color=SLATE_BODY, va='center')

        # Down arrow between steps
        if j < len(pipe_steps) - 1:
            arrow_y = cur_py - 0.012
            ax.annotate('', xy=(right_x + right_w/2, arrow_y - 0.006), xytext=(right_x + right_w/2, arrow_y + 0.004),
                        arrowprops=dict(arrowstyle="->", color=TEAL_MID, lw=1.2))

    # Benchmark Summary Box at bottom of Right Card
    bench_y = right_y + 0.02
    bench_h = 0.14
    bench_box = FancyBboxPatch((right_x + 0.02, bench_y), right_w - 0.04, bench_h,
                               boxstyle="round,pad=0.005,rounding_size=0.008",
                               fc="#0E4D64", ec="#0E4D64", lw=1)
    ax.add_patch(bench_box)

    ax.text(right_x + right_w/2, bench_y + 0.118, "TARGET HARDWARE BENCHMARKS", 
            fontsize=8.5, fontweight='bold', color="#FFFFFF", ha='center', va='center')

    benchmarks = [
        ("Target Device", "₱5,000 Budget Android (2GB RAM)"),
        ("Model Size", "<10 MB Total Deployment APK"),
        ("End-to-End Latency", "<415ms Execution (<450ms Budget)"),
        ("Data Sovereignty", "100% Offline (Zero Cloud Telemetry)")
    ]

    for k, (label, val) in enumerate(benchmarks):
        by = bench_y + 0.088 - k * 0.024
        ax.text(right_x + 0.035, by, label + ":", fontsize=7.5, color="#94A3B8", va='center')
        ax.text(right_x + right_w - 0.035, by, val, fontsize=7.5, fontweight='bold', color="#FFFFFF", ha='right', va='center')

    # ═════════════════════════════════════════════════════════════════════════
    # 4. BOTTOM EDGE STRIP
    # ═════════════════════════════════════════════════════════════════════════
    foot_box = FancyBboxPatch((0.04, 0.022), 0.92, 0.052, boxstyle="round,pad=0.005,rounding_size=0.01",
                              fc="#F8FAFC", ec=BORDER_LIGHT, lw=1)
    ax.add_patch(foot_box)
    
    ax.text(0.50, 0.048, "CORE INNOVATION:  Quantized INT8 Multi-Task Edge-AI Pipeline Running 100% Offline on Frontline Rural Smartphones",
            fontsize=8.5, fontweight='bold', color=TEAL_PRIMARY, ha='center', va='center')

    # Save output
    plt.savefig(OUT_FILE, dpi=120, facecolor=CANVAS_BG)
    plt.close()
    print(f"[SUCCESS] Slide 6 Canva slide generated at: {OUT_FILE}")

if __name__ == "__main__":
    build_slide6()
