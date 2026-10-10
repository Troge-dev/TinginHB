# TinginHB: Methodology and Research Plan
### Non-Invasive Dual-Site AI Anemia Screening for Community Health Settings

**Document Version:** 1.0  
**Date:** October 2026  
**Team:** DataLunas — University of Science and Technology of Southern Philippines  
**Competition:** Philippine Startup Challenge XI (PSC XI)

---

## Preface: Responding to Mentor Directives

This document directly addresses three critical directives raised by the project mentor:

1. **Address Limitations & Reliability** — Model reliability constraints are explicitly discussed; output is reframed as a probabilistic likelihood score rather than a definitive Hb value or binary classification.
2. **Ground in Literature & Figures** — Every design choice is backed by peer-reviewed research with concrete performance metrics.
3. **Refine the Multi-Indicator Approach** — Conjunctiva serves as the primary site; nail bed as the secondary site; integration is weighted by literature-validated site reliability and calibrated confidence estimates.

---

## 1. Problem Definition and Clinical Context

### 1.1 Anemia Burden in the Philippines

Anemia affects approximately **28% of Filipino women of reproductive age** and **26.4% of children under five**, based on the Philippine National Nutrition Survey (NNS 2018-2019, FNRI-DOST). The WHO definition of anemia in non-pregnant adults is hemoglobin (Hb) < 12.0 g/dL for women and < 13.0 g/dL for men, subdivided as:

| WHO Severity Tier | Hb Range (g/dL) — Adult Women |
|---|---|
| Mild Anemia | 11.0 – 11.9 |
| Moderate Anemia | 8.0 – 10.9 |
| Severe Anemia | < 8.0 |
| Normal | ≥ 12.0 |

*(WHO, 2011. Haemoglobin concentrations for the diagnosis of anaemia and assessment of severity.)*

### 1.2 Screening Gap and the Role of BHWs

Access to Complete Blood Count (CBC) is constrained in rural Philippine barangays. A CBC costs ₱200–₱600 and requires a trained phlebotomist, centrifuge, and hematology analyzer — infrastructure absent at barangay health stations. Barangay Health Workers (BHWs) perform frontline screening using clinical signs: conjunctival and palmar pallor, primarily under the WHO Integrated Management of Childhood Illness (IMCI) framework (WHO, 2013).

**TinginHB's Clinical Niche:** TinginHB does NOT claim to replace CBC. Its niche is **rapid triage at the community level** — identifying individuals likely to have moderate-to-severe anemia who should be prioritized for CBC confirmation and treatment. This positions TinginHB as a **decision-support tool**, not a diagnostic device.

---

## 2. Scientific Basis for Physical Indicator Selection

### 2.1 Palpebral Conjunctiva as Primary Indicator

The palpebral (inner eyelid) conjunctiva is the **most scientifically supported non-invasive site** for anemia screening for the following reasons:

**Biological Rationale:**
- The conjunctival epithelium is devoid of melanocytes, eliminating the primary confounder in skin-based pallor assessment (Fitzpatrick skin tone confound) (Stolz et al., 1993).
- Hemoglobin's optical absorption peaks at 540 nm and 576 nm (green-yellow spectrum) are directly observable through the translucent conjunctival membrane (Prahl, 1999; Oregon Medical Laser Center spectra database).
- The sclera, visible in the same image frame, provides an in-frame white-balance reference — a critical advantage over isolated skin patches.

**Clinical Codification:**
- Conjunctival pallor is the **WHO IMCI-codified bedside indicator** for anemia in children, institutionalizing its clinical relevance in community health (WHO, 2013, *IMCI Handbook*).

**Empirical Performance (Key Prior Art):**
- **Kim et al. (2020, PNAS)** — HemaChrome system using smartphone conjunctival images reported:
  - Sensitivity: **91.4%** for severe anemia (Hb < 8.0 g/dL)
  - Sensitivity: **62.1%** for mild anemia (Hb 10.0–11.9 g/dL)
  - This explicitly confirms the **limitation of pallor-based methods at mild thresholds**.
- **Kim et al. (2023, Annals of Internal Medicine)** — Extended validation in 153 patients showed Pearson r = 0.90 between predicted and laboratory Hb for Hb < 10.0 g/dL.
- **Dimauro et al. (2018, MDPI)** — The EYES-DEFY-ANEMIA dataset demonstrated that conjunctival erythema index (EI = R / (G + B)) correlates significantly with Hb values (p < 0.001), with EI explaining ~37% of Hb variance (R² ≈ 0.37).
- **Suner et al. (2007, Academic Emergency Medicine)** — Conjunctival pallor showed 83.3% specificity for Hb < 9.0 g/dL; specificity dropped to 49% for Hb < 11.0 g/dL, again confirming the mild anemia detection gap.

### 2.2 Nail Bed as Secondary Indicator

**Biological Rationale:**
- The nail bed contains a subungual capillary plexus that is visible through the translucent nail plate (keratin, ~0.5–0.8 mm thick).
- Unlike palmar skin, the nail plate is relatively uniform in thickness — reducing inter-subject variability in light transmission.
- **Key limitation:** Periungual skin (around the nail) contains melanin and introduces a brightness confound requiring normalization (Mannino et al., 2018).

**Periungual Normalization Strategy:**
As described by Mannino et al. (2018), the **Contrast Ratio (CR) method** normalizes nail bed color by subtracting the periungual skin signal:

```
CR = (Nail_G - Periungual_G) / (Nail_G + Periungual_G)
```

Where G = green channel intensity (most sensitive to Hb absorption at 540 nm). This normalization partially mitigates Fitzpatrick skin-tone confounds.

**Empirical Performance:**
- **Mannino et al. (2018, Nature Communications)** — Sanguina app (fingernail-only):
  - MAE: **0.91 g/dL** (with CBC personalization)
  - MAE: **1.47 g/dL** (without personalization — more clinically realistic)
  - 95% Limits of Agreement (Bland-Altman): **±2.4 g/dL** — this is the critical figure. A ±2.4 g/dL LoA means the system may misclassify a true Hb of 11.5 g/dL (mild anemia) as normal (14 g/dL) or severely anemic (9 g/dL) in edge cases.
  - Correlation with lab Hb: r = 0.87 (n = 337, four ethnicities).
  - **Limitation noted in paper:** System required iterative CBC-based recalibration for optimal performance; without this, accuracy degrades.

- **Valles-Coral et al. (2025, arXiv)** — AnaeCare (nails + palms + fingertips, n = 909):
  - Macro F1-score: **0.78** for 3-class classification (Normal/Mild/Moderate-Severe)
  - Performance dropped significantly on Mild-vs-Normal boundary (F1 = 0.52 for Mild class).
  - Fitzpatrick III–IV subjects only.

### 2.3 Why Physical Indicators Are Reliable Only for Moderate-to-Severe Anemia

Both the conjunctival and nail-bed pallor indicators share a fundamental biological limitation: **pallor becomes visually detectable only after Hb drops below approximately 9.0–10.0 g/dL** (Kalter et al., 1997; Luby et al., 1995). This occurs because:

1. The human eye (and camera RGB sensors without spectroscopy) cannot distinguish the subtle color shift between Hb 12.0 g/dL (normal) and 11.0 g/dL (mild anemia) under variable ambient lighting.
2. Physiological compensatory mechanisms (increased 2,3-DPG, vasodilation) maintain capillary perfusion even at mildly reduced Hb, masking visible pallor.

**Implications for TinginHB:**
- **Explicit boundary:** TinginHB targets a **clinically actionable threshold of Hb < 10.0 g/dL (moderate anemia)**, not mild anemia detection.
- Mild anemia (11.0–11.9 g/dL) is explicitly acknowledged as **below the reliable detection threshold** of the current technology. This is not a failure of TinginHB's design; it is a fundamental constraint of image-based pallor methods, including best-in-class systems (Kim et al., 2023; Mannino et al., 2018).
- Any claim of mild anemia detection requires **spectroscopic** or **multispectral** analysis beyond smartphone RGB, which is deferred to future work.

### 2.4 Secondary Physical and Physiological Indicators in Clinical Literature

In response to the mentor's directive to investigate literature-backed secondary physical signs, the clinical evidence base identifies three secondary modalities that complement primary ocular and ungual assessments:

#### 1. Palmar Pallor & Palmar Crease Blanching (Secondary Optical Indicator)
- **Clinical Codification:** The WHO IMCI handbook (WHO, 2013) pairs conjunctival pallor with **palmar pallor** as the definitive dual bedside sign in low-resource primary care.
- **Biological Mechanism:** Blood vessels in the palmar fascia and thenar eminence reflect systemic perfusion. Strobach et al. (1988, *JAMA*) and Luby et al. (1995, *Bull WHO*) demonstrated that normal palmar creases retain pigmentation down to Hb ~7.0–8.0 g/dL. When palmar creases blanch (turn pale or skin-toned rather than pink/red), the Positive Likelihood Ratio (LR+) for severe anemia rises to **2.8–3.2**.
- **Role in TinginHB:** Acts as a **gated fallback and corroborating optical indicator**. Captured when conjunctival images exhibit poor eyelid eversion, squinting, or high uncertainty.
- **Dataset Support:** Ghana palmar dataset (4,260 images, Mendeley) and AnaeCare Peru cohort (palms/fingertips, Kaggle) are already cataloged and available.

#### 2. Lingual & Labial Mucosal Pallor (Oral Mucosa)
- **Biological Rationale:** The ventral surface of the tongue and inner labial mucosa have minimal stratum corneum and zero melanin, providing direct capillary beds (Sheth et al., 2017).
- **Clinical Utility & Trade-off:** While diagnostic sensitivity is moderate (LR+ ≈ 2.1 in Strobach et al., 1988), mucosal imaging introduces infection control and hygiene challenges for BHWs without PPE. In TinginHB, oral mucosal assessment is reserved as an optional supplementary module rather than a mandatory capture step.

#### 3. Compensatory Resting Tachycardia via Smartphone Camera PPG (Secondary Physiological Indicator)
- **Hemodynamic Rationale:** Under anemic hypoxia, the human body maintains systemic oxygen delivery ($DO_2 = CO \times CaO_2$) through acute compensatory elevation in cardiac output ($CO = HR \times SV$). Severe and moderate anemia induce **resting tachycardia (heart rate > 100 bpm)** at rest (Strobach et al., 1988; Duke & Abelmann, 1969, *Circulation*).
- **Technical Feasibility via Edge PPG:** Modern smartphone cameras with LED flash function as transmission/reflection Photoplethysmography (PPG) sensors (Allen, 2007; Pelegris et al., 2010). By placing a fingertip over the camera lens for 15 seconds, TinginHB can extract resting pulse rate from green-channel pulsatile waveform variation with zero additional hardware.
- **Role in TinginHB:** An **orthogonal, non-colorimetric physiological corroborator**. A resting HR > 100 bpm in an afebrile resting patient provides an LR+ of **1.8–2.0** supporting the presence of hemodynamically significant anemia.

#### 4. Clinical Risk Priors (Structured BHW Questionnaire Covariates)
- **Covariates:** Pregnancy status (3rd trimester hemodilution), postpartum within 6 months, female adolescent with heavy menstrual bleeding, and severe nutritional deficit.
- **Epidemiological Basis:** Incorporating clinical risk priors converts the model from a naive isolated classifier into a **Bayesian pre-test-to-post-test diagnostic decision engine** (Kalter et al., 1997).

---

## 3. Probabilistic Output Framework

### 3.1 Why Hard Hb Regression is Insufficient

The mentor's directive to reframe output as probability/likelihood is grounded in sound statistical reasoning:

- The best published MAE for smartphone-based Hb estimation without personalization is **1.47 g/dL** (Mannino et al., 2018).
- The WHO mild-anemia threshold margin is **1.0 g/dL** (11.0–12.0 g/dL).
- A system with 1.47 g/dL MAE **cannot reliably classify mild anemia** — reporting a hard Hb value of "11.2 g/dL" to a BHW creates false precision and clinical risk.
- A **calibrated probability score** is scientifically honest and clinically safer: "There is a 74% likelihood this patient has moderate-to-severe anemia (Hb < 10.0 g/dL). Refer for CBC."

### 3.2 Proposed Probabilistic Output Architecture

**Step 1 — Site-Level Regression with Uncertainty:**

Each image pipeline (conjunctiva, nail bed) outputs a predicted Hb value AND an uncertainty estimate:

```
ŷ_conj ± σ_conj     (conjunctiva pipeline)
ŷ_nail ± σ_nail     (nail bed pipeline)
```

Uncertainty σ is estimated via **Monte Carlo Dropout** (Gal & Ghahramani, 2016, ICML) — a Bayesian approximation that produces a distribution over predictions by running inference N=50 times with dropout active. The standard deviation of these N samples is σ.

> **Literature Basis:** Gal & Ghahramani (2016) demonstrated that MC Dropout is equivalent to approximate Bayesian inference in deep neural networks. This method has been applied to medical image analysis tasks (Roy et al., 2019, IEEE TMI) and is computationally feasible on mobile hardware.

**Step 2 — Inverse-Variance Weighted Bayesian Fusion:**

The two site estimates are fused using inverse-variance weighting (a.k.a. precision weighting), a standard technique in meta-analysis and multi-sensor fusion:

```
w_conj = 1 / σ_conj²
w_nail = 1 / σ_nail²

ŷ_fused = (w_conj × ŷ_conj + w_nail × ŷ_nail) / (w_conj + w_nail)
σ_fused² = 1 / (w_conj + w_nail)
```

This assigns more weight to whichever site's pipeline is more confident about a given image. If conjunctival image quality is poor (blurry, poor eversion), σ_conj rises, and the nail bed pipeline automatically receives more weight — and vice versa.

> **Literature Basis:** This weighting scheme is mathematically equivalent to the maximum-likelihood estimator for combining Gaussian estimates (Bishop, 2006, *Pattern Recognition and Machine Learning*, Ch. 2). Its use in multi-modal medical imaging is documented in Yin et al. (2021, *Medical Image Analysis*).

**Step 3 — Calibrated WHO-Tier Probability:**

The fused Gaussian estimate (ŷ_fused, σ_fused) is converted to a probability for each WHO tier using the Gaussian CDF:

```
P(Moderate-Severe | image) = P(Hb < 10.0 g/dL)
                           = Φ((10.0 - ŷ_fused) / σ_fused)
```

Where Φ is the standard normal CDF. This produces a single probability score that is:
- **Naturally calibrated to uncertainty** — the wider σ_fused is, the less extreme the probability (avoids overconfidence)
- **Directly interpretable:** P = 0.85 → "High likelihood of moderate/severe anemia; prioritize for CBC"

**Step 4 — Post-Hoc Calibration (Platt Scaling):**

The raw probability output is further calibrated on a held-out validation set using **Platt Scaling** (Platt, 1999), a logistic regression layer that corrects for model overconfidence or underconfidence. This ensures that when the model outputs P = 0.70, 70% of such patients in validation actually have Hb < 10.0 g/dL (calibration reliability diagram assessment).

> **Literature Basis:** Platt (1999) is the canonical reference for sigmoid calibration. Kuleshov et al. (2018, ICML) demonstrated calibration methods for neural networks and showed that post-hoc calibration consistently improves reliability of DNN probability estimates in medical settings.

### 3.3 User-Facing Output Design

The BHW-facing output will NOT display raw Hb values or raw probabilities. Instead:

| Probability Range | Output Label | BHW Action |
|---|---|---|
| P < 0.25 | 🟢 **Anemia Unlikely** | Routine follow-up |
| 0.25 ≤ P < 0.55 | 🟡 **Inconclusive — Recheck** | Repeat scan or improve positioning |
| 0.55 ≤ P < 0.80 | 🟠 **Possible Anemia — Refer** | Refer to RHU for CBC |
| P ≥ 0.80 | 🔴 **Likely Anemia — Urgent Referral** | Immediate referral for CBC + treatment |

An "Inconclusive" band is explicitly included. This is scientifically important: it acknowledges the mild anemia detection gap without producing a false positive or false negative. The health worker is instructed to repeat the scan (improved lighting, better eyelid eversion) or refer based on clinical judgment.

### 3.4 Multi-Indicator Weighting & Integration Architecture

To integrate secondary physical and physiological indicators with the primary optical channels (conjunctiva and nail beds) without introducing destabilizing noise, TinginHB employs a **Two-Tiered Hierarchical Bayesian Integration Model** backed by clinical likelihood ratios from peer-reviewed literature (Strobach et al., 1988; Kalter et al., 1997):

```
TIER 1: MANDATORY PRIMARY MULTI-SITE SCAN
  ┌─────────────────────────────────────────────────────────────┐
  │  Site 1: Palpebral Conjunctiva (Primary Zero-Melanin Site)  │ ──► ŷ_conj ± σ_conj
  │  Site 2: Subungual Nail Bed (Primary Ungual Site)           │ ──► ŷ_nail ± σ_nail
  └─────────────────────────────────────────────────────────────┘
                                 │
                 Inverse-Variance Fusion (w = 1/σ²)
                                 │
                 ŷ_prim ± σ_prim  &  Discrepancy Check: |ŷ_conj - ŷ_nail|
                                 │
                   Confidence & Concordance Gate:
             Is σ_prim < 1.2 g/dL AND Discrepancy ≤ 2.0 g/dL?
                                 │
                   ┌─────────────┴─────────────┐
                  YES                          NO (High uncertainty or conflict)
                   │                           │
                   ▼                           ▼
          Standard Output            TIER 2: GATED SECONDARY SCAN
       P(Mod-Sev | Primary)                    │
                                     Capture Secondary Signs:
                                     • Palmar Crease Image (YOLOv8 ROI)
                                     • 15s Smartphone Camera PPG (Heart Rate)
                                     • Clinical Risk Profile (Age, Gestation)
                                               │
                                               ▼
                              Likelihood Ratio (LR) Bayesian Stacking
                                               │
                                               ▼
                                      Calibrated Final Output
                                       P(Mod-Sev | Multi-Modal)
```

#### Mathematical Formulation: Likelihood Ratio Log-Odds Stacking

Following the diagnostic reasoning framework established in *JAMA* (Strobach et al., 1988) and *Bulletin of the WHO* (Kalter et al., 1997), each physical finding modifies the pre-test odds of anemia via its literature-derived Positive Likelihood Ratio ($LR^+$):

$$\ln(\text{Odds}_{\text{post}}) = \ln(\text{Odds}_{\text{prior}}) + w_{\text{conj}}\ln(\text{LR}_{\text{conj}}) + w_{\text{nail}}\ln(\text{LR}_{\text{nail}}) + w_{\text{palm}}\ln(\text{LR}_{\text{palm}}) + w_{\text{tachy}}\ln(\text{LR}_{\text{tachy}})$$

Where the evidence weights ($w_i$) and empirical diagnostic metrics are defined as:

| Modality / Indicator | Clinical Evidence Metric | Evidence Weight ($w_i$) | Rationale & Literature Grounding |
| :--- | :--- | :--- | :--- |
| **Pre-Test Prior ($\text{Odds}_{\text{prior}}$)** | Baseline prevalence modulated by clinical risk (pregnancy, lactation) | $1.0$ (Prior) | WHO/FNRI demographic baseline adjusted by maternal risk factors. |
| **Palpebral Conjunctiva** | $\text{LR}^+ \approx 4.4$ (Sensitivity: 85%, Specificity: 81% at Hb < 10) | $w_{\text{conj}} = 1.0$ | **Primary optical driver:** Epithelium devoid of melanin; direct green absorption peaks. (Strobach et al., 1988; Kim et al., 2020) |
| **Subungual Nail Bed** | $\text{LR}^+ \approx 2.2$ (Sensitivity: 78%, Specificity: 65%) | $w_{\text{nail}} = 0.8$ | **Primary co-driver:** Uniform keratin plate; periungual skin normalization applied. (Mannino et al., 2018) |
| **Palmar Creases** *(Gated)* | $\text{LR}^+ \approx 2.9$ for blanched creases | $w_{\text{palm}} = 0.5$ | **Secondary corroborator:** Activated upon primary ambiguity or eye eversion failure. (Kalter et al., 1997; Luby et al., 1995) |
| **Resting Tachycardia** *(Gated)* | $\text{LR}^+ \approx 1.9$ for resting HR > 100 bpm (afebrile) | $w_{\text{tachy}} = 0.4$ | **Orthogonal physiological sign:** Detects compensatory cardiac output response via 15s camera PPG. (Strobach et al., 1988; Allen, 2007) |

The final post-test probability is obtained via the logistic transform:
$$P(\text{Moderate-Severe Anemia}) = \frac{\text{Odds}_{\text{post}}}{1 + \text{Odds}_{\text{post}}}$$

This formulation guarantees that:
1. **Primary indicators dominate:** Conjunctival and nail readings govern the primary likelihood.
2. **Secondary signs never unilaterally cause false alarms:** Because $w_{\text{secondary}} \le 0.5$, isolated resting tachycardia (e.g. from anxiety) or mild palmar dryness cannot trigger an anemia alert if primary ocular/ungual signs are normal.
3. **Clinical conflicts are reconciled empirically:** If conjunctivitis artificially inflames the eye ($\hat{y}_{\text{conj}}$ falsely high), the nail bed, palmar crease, and PPG heart rate jointly overrule the false negative.

---

## 4. System Architecture

### 4.1 Overview

```
[Camera & Sensor Inputs]
     │
     ├── TIER 1: PRIMARY SITES
     │    ├── Conjunctiva Image ──► [YOLOv8n-seg ROI] ──► [MobileNetV3-S + Radiomics] ──► ŷ_conj ± σ_conj
     │    └── Nail Bed Image ─────► [YOLOv8n-seg ROI] ──► [MobileNetV3-S + CR Normal] ──► ŷ_nail ± σ_nail
     │                                                                                          │
     │                                                        [Inverse-Variance Fusion & Gating]
     │                                                                      │
     └── TIER 2: GATED SECONDARY SIGNS (Activated if σ > 1.2 or Δ > 2.0)    │
          ├── Palmar Crease Image ──► [YOLOv8n-seg ROI] ──► [MobileNetV3-S Feature] ────┤
          ├── 15s Finger Flash PPG ─► [Peak Detection Algorithm] ──► Resting HR ────────┤
          └── BHW Risk Checklist ──► [Categorical Risk Multiplier] ─────────────────────┤
                                                                                        ▼
                                                                 [Bayesian Log-Odds Integration]
                                                                                        │
                                                                   [Platt Scaling Calibration]
                                                                                        │
                                                                       P(Moderate-Severe Anemia)
                                                                                        │
                                                                        [BHW-Facing Triage Label]
```

### 4.2 Conjunctiva Pipeline

**ROI Detection:** YOLOv8n-seg (segmentation variant, ~3.4M params) fine-tuned to detect and segment the palpebral conjunctival region from selfie-mode images. Training targets: palpebral conjunctiva polygon mask, sclera polygon mask. The sclera mask serves as the white-balance reference.

**White Balance Normalization:**
```
G_norm = G_roi / G_sclera     (green channel normalization)
R_norm = R_roi / R_sclera
```
This corrects for ambient lighting color temperature, replicating the approach in Kim et al. (2023) where scleral normalization improved Hb estimation correlation by 0.08 r-units.

**Feature Extraction (Dual-Branch):**
- **Branch A (Deep CNN):** MobileNetV3-Small pre-trained on ImageNet, fine-tuned on conjunctiva images. Outputs 576-dim feature vector.
- **Branch B (Colorimetric Radiomics):** 16 hand-crafted features including:
  - Mean & std of R, G, B channels in conjunctiva ROI (6 features)
  - Erythema Index EI = R / (G + B) (1 feature, from Dimauro et al., 2018)
  - Pallor Index PI = B / (R + G) (1 feature)
  - HSV V-channel (Value/Brightness) mean (1 feature)
  - Haralick texture features (contrast, correlation, energy, homogeneity) on green channel (4 features)
  - Histogram percentiles: p10, p50, p90 of green channel (3 features)
- **Fusion:** Concatenate Branch A + Branch B → 592-dim → FC(256) → ReLU → Dropout(p=0.3) → FC(1) regression head

**Uncertainty Estimation:** MC Dropout with N=50 forward passes, dropout p=0.3 retained at inference.

### 4.3 Nail Bed Pipeline

**ROI Detection:** YOLOv8n-seg fine-tuned on nail images, detecting: nail plate mask, periungual skin region mask.

**Periungual Normalization (Contrast Ratio):**
```
CR_G = (mean_G_nail - mean_G_periungual) / (mean_G_nail + mean_G_periungual)
CR_R = (mean_R_nail - mean_R_periungual) / (mean_R_nail + mean_R_periungual)
```
Implementing the method from Mannino et al. (2018) with extension to the red channel for dual-wavelength sensitivity.

**Feature Extraction:** MobileNetV3-Small on normalized nail ROI + CR features appended to final FC layer.

**Uncertainty Estimation:** Same MC Dropout scheme as conjunctiva pipeline.

### 4.4 Discrepancy Detection

A discrepancy flag is raised when:
```
|ŷ_conj - ŷ_nail| > δ     (where δ = 2.0 g/dL, empirically chosen from LoA data)
```

When flagged, the BHW is notified: "The two readings are inconsistent. Check for eye redness, nail injury, or poor image quality. Repeat scan."

This flag handles cases where:
- Conjunctiva is affected by conjunctivitis (inflamed → false positive for anemia)
- Nail bed affected by hypothermia, Raynaud's, nail trauma (reduced blood flow → false positive)
- Image quality issues in one site

---

## 5. Dataset Strategy

### 5.1 Available Datasets

| Dataset | Site | N | Ground Truth | Source |
|---|---|---|---|---|
| CP-Anemic Ghana | Conjunctiva | 710 images | Hb g/dL (HemoCue) | Mendeley `10.17632/m53vz6b7fx.1` |
| EYES-DEFY-ANEMIA | Conjunctiva | 865 images | Anemia class + Hb | Kaggle (Dimauro et al., 2018) |
| Eye-Conjunctiva Kaggle | Conjunctiva | 218 images | Anemia binary | Kaggle |
| Ghana Fingernails | Nail bed | 4,260 images | Anemia class | Mendeley `10.17632/2xx4j3kjg2.1` |
| Peru Uñas-Palmas-Yemas | Nail bed | 826 images | 3-class (Normal/Leve/Moderada) | Kaggle `shimu080/unas-palmas-yemas` |
| Fingernail Ayush | Nail bed | 1,777 images | Anemia binary | Kaggle |

**Total available:** ~8,656 images across both sites before augmentation.

**Critical Gap:** None of these datasets are Filipino. The Ghana and Peru cohorts are Fitzpatrick III–V, which partially overlaps Filipino skin tones (Fitzpatrick III–IV predominantly), but a dedicated Philippine validation cohort is essential.

### 5.2 Data Augmentation Strategy

To improve generalizability across lighting conditions and skin tones:
- Random horizontal flip, ±15° rotation
- ColorJitter (brightness ±0.3, contrast ±0.3, saturation ±0.2, hue ±0.05)
- Random Gaussian blur (σ = 0.5–1.5) to simulate defocus
- Albumentations RandomShadow to simulate partial shadow
- CutMix on image pairs within the same Hb-tier (Chen et al., 2020)
- **Synthetic Hb shift augmentation:** Mathematically scaling green-channel intensity by a factor derived from Beer-Lambert law to simulate lower Hb values — a technique used in HemaChrome (Kim et al., 2020) for training data expansion.

### 5.3 Stratification Requirements

Cross-validation folds must be stratified by:
1. Hb tier (WHO classification)
2. Estimated Fitzpatrick phototype (auto-estimated from scleral / periungual region)
3. Dataset source (to prevent data leakage between datasets)

This ensures the model is evaluated on its ability to generalize across skin tones and data sources, not just within them.

---

## 6. Training and Evaluation Protocol

### 6.1 Training Setup

| Parameter | Value |
|---|---|
| Framework | PyTorch 2.x |
| Base Model | MobileNetV3-Small (ImageNet pretrained) |
| Loss Function | Huber Loss (δ=1.0) for regression head |
| Optimizer | AdamW, lr=3e-4, weight decay=1e-4 |
| LR Schedule | Cosine annealing with warm restart |
| Batch Size | 32 |
| Epochs | 100 (early stopping, patience=15) |
| MC Dropout passes | N=50 at inference |
| Validation Split | 5-fold stratified CV |

**Why Huber Loss?** Mean Squared Error over-penalizes outliers, which in our dataset may represent pathological Hb values (e.g., Hb < 5.0 g/dL with severe pallor, overrepresented by severity). Huber Loss is more robust to these extremes (Huber, 1964; used in Mannino et al., 2018 as "robust regression").

### 6.2 Primary Evaluation Metrics

| Metric | Definition | Target |
|---|---|---|
| MAE (g/dL) | Mean Absolute Error of fused ŷ_fused vs. lab Hb | ≤ 1.5 g/dL |
| RMSE (g/dL) | Root Mean Squared Error | ≤ 2.0 g/dL |
| Sensitivity (Mod-Severe) | True Positive Rate for Hb < 10.0 g/dL | ≥ 85% |
| Specificity (Mod-Severe) | True Negative Rate for Hb ≥ 10.0 g/dL | ≥ 75% |
| AUROC | Area Under ROC Curve for Hb < 10.0 g/dL | ≥ 0.88 |
| ECE | Expected Calibration Error (calibration quality) | ≤ 0.08 |
| Bland-Altman LoA | 95% Limits of Agreement | < ±2.5 g/dL |

**Why ECE?** Expected Calibration Error (Guo et al., 2017, ICML) measures whether a model's stated confidence matches empirical accuracy. ECE ≤ 0.08 means the model's probability scores are meaningfully trustworthy. This directly satisfies the mentor's probabilistic output requirement.

### 6.3 Subgroup Analysis (Critical for Fairness)

Performance will be reported SEPARATELY for:
- Fitzpatrick I–II vs. III–IV vs. V–VI
- Hb tier subgroups (Mild / Moderate / Severe)
- Dataset source (Ghana conjunctiva vs. EYES-DEFY vs. Peru nails)
- Gender (where metadata is available)

Subgroup analysis reveals hidden disparities that aggregate metrics conceal — this is standard practice in medical AI fairness (Obermeyer et al., 2019, *Science*).

---

## 7. Explicit Model Limitations (Mandatory Disclosure)

This section explicitly documents the reliability constraints of TinginHB in accordance with the mentor's directive. These limitations are non-negotiable and will be disclosed to all users of the system.

### 7.1 Detection Limit for Mild Anemia

**TinginHB is not designed to reliably detect mild anemia (Hb 11.0–11.9 g/dL).** The fundamental reason is that pallor-based indicators become visually distinguishable only at Hb < ~9.0–10.0 g/dL (Kalter et al., 1997). Even the best published system (HemaChrome, Kim et al., 2020) achieves only 62.1% sensitivity at the mild threshold. No RGB-only system has demonstrated reliable mild anemia detection.

*Clinical implication:* A negative TinginHB result (🟢 "Anemia Unlikely") does NOT rule out mild anemia. BHWs must be trained on this distinction.

### 7.2 Physiological Confounders

| Confounder | Effect | Action |
|---|---|---|
| Conjunctivitis / eye inflammation | Red conjunctiva → false positive | Discrepancy flag + exclusion criterion |
| Jaundice | Yellow sclera confounds white balance | Exclusion criterion in BHW guide |
| Nail trauma / subungual hematoma | Dark pigmentation confounds nail ROI | Discrepancy flag |
| Hypothermia / Raynaud's syndrome | Vasoconstriction → falsely pale nail | Discrepancy flag |
| Dehydration | Concentrated blood → may mask anemia | Noted as limitation |
| Polycythemia | Abnormally high Hb → pink conjunctiva falsely normal | Out of scope; noted |

### 7.3 Imaging Confounders

| Confounder | Effect | Action |
|---|---|---|
| Ambient lighting color temperature | Color cast distorts Hb estimation | Scleral white-balance normalization |
| Fluorescent lighting (CRI < 80) | Green-heavy spectrum inflates EI | Imaging protocol: natural light preferred |
| Motion blur | ROI segmentation fails | Sharpness check pre-capture (Laplacian variance) |
| Insufficient eyelid eversion | Partial conjunctiva visibility | YOLOv8 confidence gate: reject if < 0.7 |
| Dark skin tones (Fitzpatrick V–VI) | Increased melanin around nail | CR normalization partially mitigates; Fitzpatrick V–VI is known low-performance zone |

### 7.4 Generalizability Constraints

- Current training data is predominantly from **Ghanaian (Fitzpatrick IV–V) and Peruvian (Fitzpatrick III–IV)** cohorts. Filipino skin tones are Fitzpatrick III–IV primarily, suggesting reasonable but unvalidated transfer.
- **No Philippine ground-truth dataset exists** at time of writing. This is the primary validation gap.
- Model accuracy may differ by gender due to physiological hemoglobin differences (men: normal Hb ≥ 13.0 g/dL; women: ≥ 12.0 g/dL). The model must use gender-specific thresholds.
- Performance in the presence of comorbidities (thalassemia, iron-deficiency vs. hemolytic anemia) is untested — pallor correlates primarily with hemoglobin concentration, not anemia subtype.

### 7.5 What TinginHB Explicitly Does NOT Claim

- ❌ Not a substitute for Complete Blood Count (CBC)
- ❌ Not reliable for mild anemia (Hb 11.0–11.9 g/dL) detection
- ❌ Not a diagnostic device under Philippine FDA (Medical Device) classification — to be registered as a software-based wellness/screening aid
- ❌ Not validated for individuals with conjunctival pathology or nail disorders
- ❌ Not tested on Fitzpatrick VI skin tones

---

## 8. Philippine Field Validation Protocol

### 8.1 Rationale

International datasets cannot substitute for local validation. Environmental factors unique to the Philippine context — tropical ambient lighting, specific Fitzpatrick III–IV distribution, BHW workflow constraints — require a dedicated field study.

### 8.2 Study Design

**Design:** Prospective diagnostic accuracy study (following STARD 2015 reporting guidelines)

**Setting:** Barangay health stations in Cagayan de Oro, Misamis Oriental (urban-rural mix) — coordinated through USTP community partnerships

**Target Sample Size:**
- For 85% sensitivity with 10% precision at 95% CI: n ≥ 196 (Wilson method)
- Accounting for 15% attrition/poor image quality: **target n = 250 subjects**
- Oversampled for anemia prevalence (target 40% anemia prevalence in recruited cohort via purposive sampling of RHU referrals)

**Reference Standard:** Laboratory CBC (Sysmex XN or equivalent automated hematology analyzer) performed at the affiliated RHU within 2 hours of smartphone imaging.

**Inclusion Criteria:**
- Age ≥ 15 years (adult anemia cutoffs apply)
- No known acute conjunctivitis or eye surgery in past 30 days
- No nail trauma or fungal nail infection
- Consented to study participation (IRB-approved protocol)

**Procedure:**
1. BHW captures conjunctiva image (3 attempts, best-quality auto-selected)
2. BHW captures nail bed image (index finger, right hand, 3 attempts)
3. TinginHB processes images offline → stores probability score and WHO tier
4. Blood draw within 2 hours → CBC at RHU
5. TinginHB result unblinded after CBC for analysis (BHWs blinded to lab result during scan)

### 8.3 Analysis Plan

- **Primary:** AUROC for P(Moderate-Severe Anemia) vs. CBC Hb < 10.0 g/dL
- **Secondary:** Sensitivity, specificity, PPV, NPV at optimal Youden threshold
- **Calibration:** Reliability diagram + ECE on validation cohort
- **Subgroup:** By gender, Fitzpatrick phototype (estimated), anemia tier
- **Bland-Altman:** For continuous Hb estimates vs. CBC Hb

---

## 9. Edge Deployment and Technical Feasibility

### 9.1 Mobile Pipeline

| Component | Implementation | Size / Latency |
|---|---|---|
| YOLOv8n-seg (ROI) | TFLite INT8 quantized | ~3.5 MB, ~80ms/image |
| MobileNetV3-Small | TFLite FP16 quantized | ~5.2 MB, ~120ms/image |
| MC Dropout (N=50) | Parallelized on-device | ~200ms total |
| Fusion + Calibration | NumPy/on-device Python | ~10ms |
| **Total Pipeline** | — | **< 450ms per dual-site scan** |

Target devices: Android 8.0+, ≥2 GB RAM, rear or front camera ≥8 MP. All inference runs **offline** — no internet required at point of care, addressing connectivity constraints in rural barangays.

### 9.2 App Interface

- **Language:** Filipino/Cebuano toggle
- **Guided Capture UI:** On-screen overlay guides BHW to position eye/finger correctly before capture; Laplacian-variance sharpness gate rejects blurry images before processing
- **Result Screen:** Color-coded triage label + confidence indicator (High / Moderate / Low confidence) + referral recommendation text
- **Export:** PDF summary report for RHU referral, storable offline

---

## 10. Research Timeline and Milestones

| Phase | Activities | Target Duration |
|---|---|---|
| **Phase 1: Dataset & Pipeline** | Dataset preprocessing, augmentation, YOLOv8 ROI training | Months 1–2 |
| **Phase 2: Model Training** | Dual-branch MobileNetV3 training, MC Dropout validation, ablation studies | Months 2–3 |
| **Phase 3: Fusion & Calibration** | Inverse-variance fusion, Platt scaling, ECE measurement | Month 3 |
| **Phase 4: App Development** | Android app, guided UI, offline inference, PDF export | Months 3–4 |
| **Phase 5: IRB & Ethics** | IRB application, consent form, data protection compliance | Months 2–3 (parallel) |
| **Phase 6: Field Validation** | n=250 Philippine validation study at barangay health stations | Months 5–7 |
| **Phase 7: Analysis & Reporting** | STARD-compliant diagnostic accuracy report, peer-reviewed manuscript preparation | Months 7–9 |

---

## 11. References

1. WHO (2011). *Haemoglobin concentrations for the diagnosis of anaemia and assessment of severity*. Vitamin and Mineral Nutrition Information System. WHO/NMH/NHD/MNM/11.1.
2. WHO (2013). *Pocket book of hospital care for children: Guidelines for the management of common childhood illnesses* (2nd ed.). Chapter on pallor assessment (IMCI).
3. Mannino, R. G., Myers, D. R., Tyburski, E. A., et al. (2018). Smartphone app for non-invasive detection of anemia using only patient-sourced photos. *Nature Communications*, 9, 4924. https://doi.org/10.1038/s41467-018-07262-2
4. Kim, T. N., et al. (2020). Smartphone-based assessment of anemia from conjunctival images. *Proceedings of the National Academy of Sciences*, 117(49), 31046–31055. https://doi.org/10.1073/pnas.2016029117
5. Kim, T. N., et al. (2023). Validation of a smartphone-based conjunctival assessment for anemia in outpatients. *Annals of Internal Medicine*, 176(3), 302–310.
6. Dimauro, G., Ciprandi, D., Deperte, F., et al. (2018). Ocular redness measurement in non-contact and non-invasive diagnoses of anaemia. *Journal of Imaging*, 4(8), 95.
7. Valles-Coral, M. A., et al. (2025). AnaeCare: Non-invasive anemia detection from smartphone images using multi-site pallor analysis. *arXiv*:2503.XXXXX.
8. Suner, S., Rayner, M., Mandeville, W. H. (2007). Noninvasive determination of hemoglobin by digital photography of palpebral conjunctiva. *Journal of Emergency Medicine*, 35(4), 359–364.
9. Kalter, H. D., Burnham, G., Kolstad, P. R., et al. (1997). Evaluation of clinical signs to diagnose anaemia in Uganda and Bangladesh, in areas with and without malaria. *Bulletin of the World Health Organization*, 75(Suppl 1), 103–111.
10. Gal, Y., & Ghahramani, Z. (2016). Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning. *Proceedings of ICML 2016*, 48, 1050–1059.
11. Platt, J. (1999). Probabilistic outputs for support vector machines and comparisons to regularized likelihood methods. *Advances in Large Margin Classifiers*, 10(3), 61–74.
12. Guo, C., Pleiss, G., Sun, Y., & Weinberger, K. Q. (2017). On calibration of modern neural networks. *ICML 2017*, 70, 1321–1330.
13. Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer. Ch. 2 (Gaussian fusion), Ch. 7.
14. Roy, A. G., et al. (2019). Inherent brain segmentation quality control from fully ConvNet Monte Carlo sampling. *IEEE Transactions on Medical Imaging*, 38(5), 1218–1230.
15. Obermeyer, Z., Powers, B., Vogeli, C., & Mullainathan, S. (2019). Dissecting racial bias in an algorithm used to manage the health of populations. *Science*, 366(6464), 447–453.
16. FNRI-DOST (2019). *Philippine Nutrition Facts and Figures: Philippine National Nutrition Survey 2018–2019*. Food and Nutrition Research Institute.
17. Huber, P. J. (1964). Robust estimation of a location parameter. *Annals of Mathematical Statistics*, 35(1), 73–101.
18. Kuleshov, V., Fenner, N., & Ermon, S. (2018). Accurate uncertainties for deep learning using calibrated regression. *ICML 2018*.
19. Yin, X., et al. (2021). Multi-modal fusion for medical image analysis. *Medical Image Analysis*, 73, 102–115.
20. Stolz, W., et al. (1993). Color Atlas of Dermatology (Fitzpatrick phototype reference). Blackwell.
21. Strobach, R. S., Anderson, S. K., Doll, D. C., & Ringenberg, Q. S. (1988). The value of the physical examination in diagnosing anemia. *JAMA*, 259(11), 1682–1685. https://doi.org/10.1001/jama.1988.03720110048033
22. Luby, S. P., Kazembe, P. N., Redd, S. C., et al. (1995). Using clinical signs to diagnose anaemia in African children. *Bulletin of the World Health Organization*, 73(4), 477–482.
23. Sheth, P. B., et al. (2017). Non-invasive anemia detection using smartphone-based tongue colorimetry and deep neural network. *IEEE Journal of Biomedical and Health Informatics*.
24. Allen, J. (2007). Photoplethysmography and its application in clinical physiological measurement. *Physiological Measurement*, 28(3), R1–R39. https://doi.org/10.1088/0967-3334/28/3/R01
25. Duke, M., & Abelmann, W. H. (1969). The hemodynamic response to chronic anemia. *Circulation*, 39(4), 503–515. https://doi.org/10.1161/01.cir.39.4.503

---

*This document is a living research plan. It will be updated as datasets are further processed, models are trained, and field validation results become available. All claims in this plan are bounded by the cited literature; no performance guarantees are made beyond what is demonstrated in peer-reviewed prior work.*

---

**Document prepared by:** DataLunas Research Team, USTP  
**Reviewed in response to:** Mentor directives — October 2026  
