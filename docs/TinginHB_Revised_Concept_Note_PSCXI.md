# CONCEPT NOTE: TinginHB
## Non-Invasive Dual-Site Edge-AI Anemia Screening for Primary Care & Community Triage

**Competition Track:** Philippine Startup Challenge XI (PSC XI) — Student Category  
**Startup / Initiative Name:** TinginHB (DataLunas)  
**Academic Institution:** University of Science and Technology of Southern Philippines (USTP) — Cagayan de Oro  
**College / Department:** College of Information Technology and Computing (CITC) — Department of Data Science  
**Document Version:** 2.0 (Empirically Grounded & Probabilistically Calibrated)  
**Date:** October 2026  

---

## I. EXECUTIVE SUMMARY

**TinginHB** (*Tingin* = "to look/inspect"; *HB* = hemoglobin) is an offline-first, smartphone-based triage support system designed for Philippine Barangay Health Workers (BHWs) and rural primary care clinics. Rather than claiming to replace gold-standard Complete Blood Count (CBC) testing, TinginHB serves as a **non-invasive, point-of-care triage engine** that identifies individuals with a high probability of **moderate-to-severe anemia (hemoglobin < 10.0 g/dL)** who must be prioritized for confirmatory laboratory testing and clinical intervention.

By capturing smartphone images of two complementary microvascular anatomical sites—the **palpebral conjunctiva** (primary, zero-melanin mucosal surface) and the **subungual nail bed** (secondary, translucent keratin plate)—TinginHB extracts optical and colorimetric features via quantized edge deep learning models (<10 MB, 100% offline). Crucially, acknowledging the biological and physical noise floor of ambient smartphone colorimetry, TinginHB **rejects false precision**: it does not output an absolute hemoglobin decimal. Instead, it outputs a **statistically calibrated posterior probability score** stratified into actionable WHO triage tiers (including an explicit "Inconclusive / Recheck" buffer). 

TinginHB directly addresses the diagnostic desert in rural and Geographically Isolated and Disadvantaged Areas (GIDA), where over 200,000 BHWs currently rely on naked-eye pallor inspection—a method with an inter-observer agreement kappa of only $\kappa = 0.20–0.45$ (*poor-to-fair agreement*). By standardizing community triage at ₱0 consumable cost, TinginHB operationalizes early referral under the Universal Health Care Act (RA 11223) and the First 1,000 Days Law (RA 11148).

---

## II. BACKGROUND OF THE PROBLEM & THE CLINICAL SCREENING GAP

### 1. The Public Health Burden in the Philippines
Anemia remains an intractable public health crisis in the Philippines:
- **Maternal Health:** According to DOST-FNRI National Nutrition Surveys, **21.8% to 28.0% of pregnant Filipino women** are clinically anemic. Maternal anemia is a primary risk factor for Postpartum Hemorrhage (PPH)—the leading cause of maternal mortality in the country (accounting for ~30% of maternal deaths). Anemic mothers face up to a **4-fold increased risk of fatal PPH** due to myometrial uterine atony and depleted physiological reserve.
- **Infant Cognitive Development:** Approximately **40% to 45% of Filipino infants aged 6–11 months** suffer from iron deficiency anemia, leading to irreversible neurodevelopmental deficits and permanent loss of 5–10 IQ points.
- **Target Populations:** Under DOH and WHO guidelines, early detection is essential for pregnant mothers, infants, and adolescent females.

### 2. The Real Clinical Bottleneck: Access, Not Analytical Cost
A Complete Blood Count (CBC) is indeed an established, analytical gold standard and relatively inexpensive in urban laboratories (₱200–₱350). However, **a CBC is only inexpensive if the patient can physically access a functioning laboratory**:
- In rural and GIDA barangays, there are no centrifuges, reagents, automated hematology analyzers, or trained medical technologists at the Barangay Health Station (BHS).
- Patients must travel 2 to 6 hours over rough terrain and pay ₱300–₱800 in round-trip transport fares—frequently exceeding their daily household income. Consequently, asymptomatic and mildly symptomatic patients defer testing until acute crisis occurs.
- Point-of-care digital hemoglobinometers (such as HemoCue Hb 301) cost ₱70,000–₱125,000 per unit, and their single-use microcuvettes cost **₱150 per fingerstick**. This creates perpetual stockouts in rural local government units (LGUs).

### 3. The Current Frontline Reality: Subjective Naked-Eye Pallor
In the absence of point-of-care CBC, over 200,000 BHWs perform physical triage using naked-eye clinical pallor inspection under the WHO Integrated Management of Childhood Illness (IMCI) protocol. 

Peer-reviewed clinical evaluations (*Strobach et al., 1988, JAMA*; *Kalter et al., 1997, Bull WHO*) establish that:
- Naked-eye inspection has a wide sensitivity range of **10% to 60%** for mild-to-moderate anemia.
- Inter-observer reliability between health workers is extremely low, with a Cohen's kappa of **$\kappa = 0.20–0.45$** (*poor to slight agreement*).
- Variations in clinic illumination, examiner experience, and patient skin pigmentation lead to massive under-referral.

**TinginHB's Value Proposition is not analytical superiority over CBC; it is diagnostic accessibility and standardization over naked-eye triage.**

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ [FIGURE 1 PLACEHOLDER: PHILIPPINE MATERNAL ANEMIA & PPH BURDEN]                       │
│                                                                                        │
│ Suggested Visual: Infographic chart / map combining:                                  │
│ 1. DOST-FNRI Anemia Prevalence Bar Chart (Pregnant: 21.8%, Infants 6-11m: 43.1%).     │
│ 2. Philippine Maternal Mortality Breakdown showing PPH accounting for ~30% of deaths.  │
│ 3. Geographic Accessibility Map illustrating GIDA distance to laboratory CBC facilities.│
│                                                                                        │
│ Caption: Figure 1. The Maternal Anemia and Diagnostic Desert in the Philippines.       │
│ Data Sources: DOST-FNRI Expanded National Nutrition Survey (2020); DOH Maternal Health  │
│ Statistics; Philippine Statistics Authority (PSA) Civil Registration and Vital Stats.  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## III. SCIENTIFIC GROUNDING & PRIOR ART ANALYSIS

### 1. Biological and Optical Basis of Indicator Selection
The selection of anatomical sites is strictly grounded in microvascular anatomy and optical physics:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                             ANATOMICAL SIGNAL PATH                               │
├────────────────────────────────────────┬─────────────────────────────────────────┤
│    PRIMARY SITE: PALPEBRAL CONJUNCTIVA │   SECONDARY SITE: SUBUNGUAL NAIL BED    │
├────────────────────────────────────────┼─────────────────────────────────────────┤
│ • Zero melanocytes in epithelium       │ • Uniform 0.5–0.8 mm keratin nail plate │
│ • Hemoglobin absorption at 540 & 576nm │ • Direct view of subungual capillaries  │
│ • Sclera serves as white-balance card  │ • Periungual skin enables normalization │
│ • Literature LR+ ≈ 4.4                 │ • Literature LR+ ≈ 2.2                  │
└────────────────────────────────────────┴─────────────────────────────────────────┘
```

- **Primary Site — Palpebral Conjunctiva (Inner Lower Eyelid):**
  The palpebral conjunctival epithelium is naturally devoid of melanocytes (Stolz et al., 1993). This makes optical assessment completely **invariant to skin tone (Fitzpatrick phototypes I–VI)**. Furthermore, oxygenated hemoglobin displays characteristic absorption peaks at **540 nm and 576 nm** (green spectrum). Crucially, the exposed sclera (white of the eye) is captured in the identical photographic frame, serving as an organic, in-scene white-balance and illumination calibration reference.
- **Secondary Site — Subungual Nail Bed:**
  The subungual capillary plexus is visualized through the translucent dorsal and ventral nail plate (keratin). Unlike palmar skin, nail plate thickness is relatively uniform ($0.5–0.8\text{ mm}$), avoiding the severe light scattering caused by calluses. Periungual skin melanin is computationally subtracted using the **Contrast Ratio (CR) method** (Mannino et al., 2018).

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ [FIGURE 2 PLACEHOLDER: MICROVASCULAR OPTICAL ANATOMY & SPECTRAL ABSORPTION]            │
│                                                                                        │
│ Suggested Visual: Multi-panel optical physics diagram showing:                         │
│ 1. Hemoglobin Absorption Curve (peaks at 540 nm and 576 nm in green spectrum).         │
│ 2. Cross-section of Palpebral Conjunctiva highlighting zero-melanin epithelial layer   │
│    and adjacent sclera serving as the in-frame white balance anchor.                   │
│ 3. Cross-section of Subungual Nail Bed showing keratin transmission and periungual     │
│    melanin normalization zone (Contrast Ratio: CR = (Nail_G - Skin_G)/(Nail_G+Skin_G)).│
│                                                                                        │
│ Caption: Figure 2. Optical Transmission and Chromophore Absorption in Primary Sites.   │
│ Optical References: Prahl (1999); Kim et al. (2020, PNAS); Mannino et al. (2018).      │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 2. Prior Art & Performance Baselines
TinginHB builds upon peer-reviewed breakthroughs while addressing their commercial and clinical limitations:

1. **Mannino et al. (2018, Nature Communications) — *Sanguina / AnemoCheck* (US):**
   - Single-site nail bed colorimetry ($n=337$).
   - Reported Mean Absolute Error (MAE) of **$0.91\text{ g/dL}$** with personalized CBC calibration, but **$1.47\text{ g/dL}$** without personalization. Bland-Altman 95% Limits of Agreement were **$\pm 2.4\text{ g/dL}$**.
   - *Limitation:* Proprietary, consumer-oriented, requires CBC calibration for high accuracy, and is skin-pigmentation sensitive without multi-site corroboration.
2. **Kim et al. (2020, PNAS; 2023, Annals of Internal Medicine) — *HemaChrome* (Purdue Univ.):**
   - Single-site palpebral conjunctiva imaging using mobile super-resolution spectroscopy.
   - Reported **$91.4\%$ sensitivity** for severe anemia ($\text{Hb} < 8.0\text{ g/dL}$), but sensitivity dropped to **$62.1\%$** for mild anemia ($10.0–11.9\text{ g/dL}$).
   - *Limitation:* Hardware/computational overhead; single-site vulnerability to eye movement or localized inflammation.
3. **Valles-Coral et al. (2025, arXiv) — *AnaeCare* (Peru):**
   - Multi-site smartphone analysis (nails, palms, fingertips; $n=909$).
   - Achieved Macro F1 of **$0.78$**, but F1 fell to **$0.52$** along the Mild-vs-Normal boundary in Fitzpatrick III–IV cohorts.
   - *Limitation:* High workflow friction (multiple images required per subject); categorical classification without uncertainty quantification.

---

## IV. SYSTEM ARCHITECTURE & PROBABILISTIC REFRAMING

### 1. Rejecting False Precision: The Bayesian Posterior Probability Framework
Best-in-class non-invasive smartphone systems achieve an uncalibrated MAE of $\approx 1.5\text{ g/dL}$. Because the WHO mild anemia threshold interval is only $1.0\text{ g/dL}$ wide ($11.0–11.9\text{ g/dL}$), predicting a single deterministic number (e.g., "11.2 g/dL") creates dangerous false confidence.

TinginHB adopts a **Probabilistic Bayesian Output Model**:
1. **Uncertainty Quantification (MC Dropout):** Each neural network inference pass runs with active dropout ($N=50$ forward samples) to extract epistemic model uncertainty ($\sigma$).
2. **Inverse-Variance Bayesian Fusion:** The predicted estimates from the conjunctiva ($\hat{y}_{\text{conj}}, \sigma_{\text{conj}}$) and nail bed ($\hat{y}_{\text{nail}}, \sigma_{\text{nail}}$) are fused using precision weighting:
   $$w_i = \frac{1}{\sigma_i^2}, \quad \hat{y}_{\text{fused}} = \frac{w_{\text{conj}}\hat{y}_{\text{conj}} + w_{\text{nail}}\hat{y}_{\text{nail}}}{w_{\text{conj}} + w_{\text{nail}}}, \quad \sigma_{\text{fused}}^2 = \frac{1}{w_{\text{conj}} + w_{\text{nail}}}$$
3. **Probability Transformation:** The continuous Gaussian distribution is converted into a calibrated likelihood of moderate-to-severe anemia:
   $$P(\text{Moderate-Severe Anemia} \mid \text{Features}) = \Phi\left(\frac{10.0 - \hat{y}_{\text{fused}}}{\sigma_{\text{fused}}}\right)$$
4. **Post-Hoc Calibration (Platt Scaling):** Probabilities are calibrated on validation cohorts to achieve an Expected Calibration Error of **$\text{ECE} \le 0.08$**.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ [FIGURE 3 PLACEHOLDER: END-TO-END EDGE-AI PIPELINE ARCHITECTURE]                       │
│                                                                                        │
│ Suggested Visual: Neural architecture schematic diagram showing:                       │
│ 1. Image Acquisition: On-screen positioning overlay with Laplacian blur gate.         │
│ 2. ROI Segmentation: YOLOv8n-seg generating palpebral conjunctiva, sclera, and nail    │
│    polygon masks.                                                                      │
│ 3. Feature Extraction: Dual-branch processing combining deep MobileNetV3-Small features│
│    with 16 handcrafted colorimetric radiomics (Erythema Index, Pallor Index).          │
│ 4. Inference Engine: Monte Carlo Dropout (N=50 stochastic passes) generating Gaussian   │
│    estimates (ŷ ± σ) followed by Platt Scaling calibration layer.                      │
│                                                                                        │
│ Caption: Figure 3. Dual-Branch Deep Learning Pipeline and Bayesian Uncertainty Engine.│
│ Framework: PyTorch 2.x -> TFLite INT8 Quantized (<10 MB total runtime footprint).       │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 2. Actionable Triage Tiers with Safety Buffering
Rather than presenting confusing statistical decimals to community health workers, TinginHB maps calibrated probabilities to intuitive, standardized action protocols:

| Probability Score | Triage Classification | Clinical Interpretation | Action Protocol for BHW |
| :---: | :---: | :---: | :--- |
| **$P < 0.25$** | 🟢 **Anemia Unlikely** | High confidence normal perfusion | Routine antenatal/pediatric follow-up; reinforce nutrition |
| **$0.25 \le P < 0.55$** | 🟡 **Inconclusive — Recheck** | Signal within noise floor or mild zone | Reposition under natural light, repeat scan, or refer if symptomatic |
| **$0.55 \le P < 0.80$** | 🟠 **Possible Anemia — Refer** | Elevated probability of $\text{Hb} < 10.0\text{ g/dL}$ | Schedule routine RHU visit for confirmatory laboratory CBC |
| **$P \ge 0.80$** | 🔴 **Likely Anemia — Urgent** | High probability of moderate/severe anemia | Priority referral to RHU/hospital; auto-generate Konsulta PDF |

---

## V. DYNAMIC MULTI-INDICATOR WEIGHTING & EVIDENCE INTEGRATION

In frontline primary care, clinical data collection is inherently variable: a patient might be an uncooperative crying toddler whose eyelids cannot be pulled down, or a BHW might be conducting a rugged house-to-house visit without their blood pressure apparatus. To handle these real-world conditions without sacrificing mathematical rigor, TinginHB employs a **Dynamic Multi-Indicator Fusion Architecture** that accounts for **Missing Modalities** (Baltrusaitis et al., 2019; Huang et al., 2020, *npj Digital Medicine*).

### 1. The 5-Modality Clinical Indicator Matrix
TinginHB incorporates up to five clinical indicators, weighted by their empirical signal-to-noise ratio and clinical diagnostic yield:

| Indicator / Modality | Data Type & Collection Method | Default Weight ($w_i$) | Clinical Diagnostic Grounding |
| :--- | :--- | :---: | :--- |
| **1. Palpebral Conjunctiva** *(Primary Optical)* | High-resolution smartphone camera macro crop (YOLOv8n-seg) | **35%** | **Highest SNR:** Zero melanocytes in epithelium; direct green-channel hemoglobin absorption peaks (540 & 576 nm); scleral white-balance anchor. (Kim et al., 2020; Prahl, 1999) |
| **2. Subungual Nail Bed** *(Primary Optical)* | Smartphone macro photo with periungual Contrast Ratio (CR) | **25%** | **Uniform keratin transmission:** Translucent 0.5–0.8 mm plate; periungual skin melanin computationally subtracted. (Mannino et al., 2018) |
| **3. Patient Survey & Symptoms** *(Clinical Prior)* | 4-tap rapid UI: Age, Sex, Pregnancy/Trimester, Dizziness, Fatigue | **15%** | **Epidemiological Bayesian Prior:** Establishes pre-test odds. Aligned with DOH Target Client List (TCL) and WHO Antenatal Care guidelines. (WHO, 2016) |
| **4. Palmar Creases** *(Gated Optical Fallback)* | Open-hand smartphone photograph (YOLOv8n-seg) | **15%** | **WHO IMCI Fallback:** Deep creases retain pigmentation until severe anemia (<7–8 g/dL). Activated when eyelid capture is unfeasible. (Kalter et al., 1997; Luby et al., 1995) |
| **5. Blood Pressure & Pulse** *(Hemodynamic Check)* | Numerical input from standard DOH-issued digital/manual BP cuff | **10%** | **Compensatory Tachycardia:** Anemic hypoxia induces compensatory elevation in cardiac output (resting HR > 100 bpm; wide pulse pressure). (Duke & Abelmann, 1969; Varat et al., 1972) |
| **TOTAL (All Available)** | **Comprehensive Health Station Screening** | **100%** | **Maximum Diagnostic Confidence & Narrowest Credible Interval** |

---

### 2. Mathematical Handling of Missing Modalities (Dynamic Re-normalization)
Rather than failing or rejecting incomplete scans, TinginHB dynamically re-normalizes the active indicator weights so that the available evidence always sums to 100%:

$$w'_i = \frac{w_i}{\sum_{j \in \text{Available}} w_j}$$

- **Scenario 1 — Complete Clinic Screening (All 5 Present):**
  Full evaluation: Eye (35%) + Nail (25%) + Survey (15%) + Palm (15%) + BP (10%) = **100%**. Delivers the highest confidence score and narrowest uncertainty interval ($\sigma$).
- **Scenario 2 — Rapid Field Visit (Eye + Nail + Survey Only):**
  BP cuff is absent and palm is skipped. Sum of available weights = $35 + 25 + 15 = 75\%$.
  $$w'_{\text{eye}} = \frac{35}{75} \approx \mathbf{46.7\%}, \quad w'_{\text{nail}} = \frac{25}{75} \approx \mathbf{33.3\%}, \quad w'_{\text{survey}} = \frac{15}{75} \approx \mathbf{20.0\%} \quad (\Sigma = 100\%)$$
- **Scenario 3 — Pediatric / Eye-Infection Fallback (Nail + Palm + Survey Only):**
  Infant resists eyelid eversion or patient has acute conjunctivitis. Sum of available weights = $25 + 15 + 15 = 55\%$.
  $$w'_{\text{nail}} = \frac{25}{55} \approx \mathbf{45.5\%}, \quad w'_{\text{palm}} = \frac{15}{55} \approx \mathbf{27.3\%}, \quad w'_{\text{survey}} = \frac{15}{55} \approx \mathbf{27.3\%} \quad (\Sigma = 100\%)$$
  The system gracefully shifts optical weight to the extremity sites without code execution errors or false alarms.

---

### 3. Bayesian Evidence Formulation: Likelihood Ratio Log-Odds Stacking
For probabilistic risk scoring, the system computes the post-test log-odds of moderate-to-severe anemia using empirical Likelihood Ratios ($LR$) from clinical literature (Strobach et al., 1988; Kalter et al., 1997):

$$\ln(\text{Odds}_{\text{post}}) = \ln(\text{Odds}_{\text{prior}}(\text{Survey})) + \sum_{i \in \text{Available}} w'_i \cdot \ln(\text{LR}_i)$$

Where omitted or missing tests contribute a neutral multiplier of $\text{LR} = 1.0$ ($\ln(1.0) = 0$). The final calibrated probability is obtained via the standard logistic sigmoid:
$$P(\text{Moderate-Severe Anemia}) = \frac{\text{Odds}_{\text{post}}}{1 + \text{Odds}_{\text{post}}}$$

This guarantees that:
1. **Clinical priors govern baseline expectations:** A pregnant mother in her 3rd trimester starts at an elevated baseline prior (~28% prevalence), requiring less extreme pallor to trigger referral than a low-risk adult male.
2. **Missing data degrades gracefully:** Skipping an optional test widens the credible interval without corrupting the point estimate.
3. **Discrepancy safeguards remain active:** If the eye and nail predictions diverge by $>2.0\text{ g/dL}$, the discrepancy gate flags local pathology (e.g., conjunctivitis) and requests the palmar crease check to resolve ambiguity.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ [FIGURE 4 PLACEHOLDER: 5-MODALITY DECISION TREE & MISSING MODALITY FLOWCHART]          │
│                                                                                        │
│ Suggested Visual: Decision flow diagram / workflow tree showing:                       │
│ 1. Modality Acquisition Gate: Parallel capture check across available inputs:          │
│    Conjunctiva (35%), Nail Bed (25%), Survey (15%), Palmar Creases (15%), BP/HR (10%). │
│ 2. Dynamic Weight Normalization Engine: Re-scaling formula w'_i = w_i / SUM(w_avail)   │
│    demonstrating seamless adaptation for Full Clinic (100%), Rapid Field Visit (75%),  │
│    and Pediatric Fallback (55%).                                                       │
│ 3. Discrepancy & Plausibility Checker: If |Eye - Nail| > 2.0 g/dL, system triggers     │
│    automated Palmar Crease scan to break the tie and rule out local hyperemia.         │
│ 4. Output Calibration Layer: Bayesian log-odds aggregation mapped onto the 4-tier      │
│    WHO Triage Classification matrix (Green / Yellow / Orange / Red).                   │
│                                                                                        │
│ Caption: Figure 4. 5-Modality Dynamic Weighting Decision Tree and Missing Modality     │
│ Fallback Engine.                                                                       │
│ Theoretical Grounding: Baltrusaitis et al. (2019, IEEE TPAMI); Huang et al. (2020).    │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## VI. EXPLICIT LIMITATIONS & RELIABILITY BOUNDS

TinginHB adopts an uncompromising stance on scientific honesty. The following constraints are formally acknowledged in the system specification:

1. **The Mild Anemia Detection Limit:**
   Optical pallor is a physiological lagging indicator (*Kalter et al., 1997*). Under smartphone RGB cameras, physical pallor does not separate reliably from normal perfusion until hemoglobin drops below approximately **$9.0–10.0\text{ g/dL}$**. **TinginHB is explicitly NOT designed or marketed to detect mild anemia ($11.0–11.9\text{ g/dL}$).** A green result does not rule out early-stage iron deficiency.
2. **Not a Diagnostic Replacement for CBC:**
   TinginHB is a **decision-support triage tool**, not a diagnostic device. It never issues a definitive medical diagnosis; it identifies who needs urgent laboratory evaluation.
3. **Known Physiological Confounders & Exclusions:**
   - *Active Conjunctivitis / Eye Trauma:* Produces hyperemia (false negative).
   - *Severe Jaundice (Hyperbilirubinemia):* Yellow sclera corrupts the white-balance anchor.
   - *Hypothermia / Peripheral Vasoconstriction:* Induces temporary nail pallor.
   - *Fungal Onychomycosis / Subungual Hematoma:* Obstructs nail bed transmission.
4. **Generalizability & Ethnic Calibration:**
   Public training datasets originate from Ghana (Fitzpatrick IV–V) and Peru (Fitzpatrick III–IV). While this covers the pigmentation spectrum of Filipino populations (predominantly Fitzpatrick III–IV), a dedicated local validation cohort ($n=250$) paired with laboratory automated hematology analyzers is required.

---

## VII. PRODUCT IMPLEMENTATION & EDGE SPECIFICATIONS

TinginHB is engineered for extreme frugality and complete offline autonomy on entry-level Android devices:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                            EDGE SOFTWARE ARCHITECTURE                            │
├──────────────────────┬────────────────────────┬──────────────────────────────────┤
│ COMPONENT            │ ENGINE / RUNTIME       │ SPECIFICATION / FOOTPRINT        │
├──────────────────────┼────────────────────────┼──────────────────────────────────┤
│ ROI Segmentation     │ YOLOv8n-seg (INT8)     │ ~3.5 MB | 80ms inference         │
│ Feature Extraction   │ MobileNetV3-S (FP16)   │ ~5.2 MB | 120ms inference        │
│ Radiomics Extractor  │ OpenCV Colorimetry     │ 16 Handcrafted Features (EI, PI) │
│ Uncertainty Engine   │ Monte Carlo Dropout    │ N=50 stochastic passes (~200ms)  │
│ Total System Footprint│ Fully On-Device        │ < 10 MB total | < 450ms latency  │
└──────────────────────┴────────────────────────┴──────────────────────────────────┤
│ Minimum Hardware     │ Android 8.0 (Oreo)     │ 2 GB RAM | 8 MP Rear Camera      │
│ Operational Mode     │ 100% Offline           │ Zero mobile data required        │
└──────────────────────┴────────────────────────┴──────────────────────────────────┘
```

**BHW Workflow Experience:**
- **Zero-Consumable Screening:** ₱0 recurring cost per patient.
- **Assisted Capture UI:** Real-time on-screen bounding guide with an integrated Laplacian-variance sharpness gate that automatically rejects blurred or out-of-focus images before processing.
- **PhilHealth Konsulta Automation:** Generates a standardized offline referral PDF summary formatted for immediate submission to accredited Rural Health Units.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ [FIGURE 5 PLACEHOLDER: FRONTLINE BHW MOBILE APP UI & REFERRAL PDF MOCKUP]              │
│                                                                                        │
│ Suggested Visual: High-fidelity mobile screen UI flow and referral document mockup:    │
│ 1. Screen 1 (Assisted Capture): Camera viewfinder with elliptical eye/nail guides,     │
│    real-time Laplacian sharpness score indicator, and auto-exposure lock.              │
│ 2. Screen 2 (4-Tap Clinical Survey): Fast demographic toggles (Pregnancy Trimester,    │
│    Pediatric Age Bracket, Acute Pallor Symptoms: Dizziness/Lethargy).                  │
│ 3. Screen 3 (Calibrated Triage Card): Actionable color-coded risk tier card showing    │
│    posterior probability band, plain-language BHW action directive, and audio prompt.  │
│ 4. Screen 4 (PhilHealth Konsulta Referral Letter): Automated 1-page PDF referral slip   │
│    containing patient timestamp, observed anatomical cues, risk probability, and      │
│    tamper-evident QR code for RHU physician verification.                              │
│                                                                                        │
│ Caption: Figure 5. TinginHB Frontline User Interface and Automated PhilHealth Konsulta │
│ Referral Workflow.                                                                     │
│ Design Standards: DOH Telemedicine Guidelines; PhilHealth Circular 2022-0005.          │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## VIII. BUSINESS MODEL & PUBLIC HEALTH SUSTAINABILITY

TinginHB adopts a **B2G (Business-to-Government) and Institutional Freemium Model**:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                             PUBLIC-HEALTH B2G MODEL                              │
├──────────────────────────────────────────────────────────────────────────────────┤
│ • FREE TIER FOR BHWs: Core screening, triage, and offline PDF generation are     │
│   perpetually free for community health workers and rural barangay stations.     │
├──────────────────────────────────────────────────────────────────────────────────┤
│ • LGU & DOH ENTERPRISE LICENSING: Municipal and provincial health offices pay an │
│   annual SaaS license (₱500–₱1,000 / BHW / year) for centralized epidemiological │
│   analytics, maternal tracking dashboards, and PhilHealth Konsulta integration.  │
├──────────────────────────────────────────────────────────────────────────────────┤
│ • NGO & DEVELOPMENT PARTNERSHIPS: Bulk enterprise deployment across maternal     │
│   and child health programs (UNFPA, UNICEF, Zuellig Family Foundation).          │
└──────────────────────────────────────────────────────────────────────────────────┘
```

**Macro-Economic Value Creation:**
- If TinginHB replaces just one disposable HemoCue microcuvette (₱150) across 50,000 community screenings per month, it saves local government health budgets over **₱7.5 Million monthly in consumable procurement waste**.

---

## IX. RESEARCH TIMELINE & FIELD VALIDATION ROADMAP

```
[ Phase 1: Months 1–2 ]  Dataset Curation & Synthetic Augmentation
                         • Preprocess Ghana (710 eye, 4,260 nail, 4,260 palm) & Peru cohorts
                         • Train YOLOv8n-seg region proposal models

[ Phase 2: Months 2–3 ]  Dual-Branch Model Training & MC Dropout
                         • Train MobileNetV3-Small deep branch + 16-feature radiomics branch
                         • Implement Huber loss & Platt probability calibration (ECE ≤ 0.08)

[ Phase 3: Months 3–4 ]  Android Edge Integration & Usability Testing
                         • TFLite quantization, offline PDF referral generation
                         • Usability trials with student BHW volunteers

[ Phase 4: Months 5–7 ]  Prospective Clinical Field Validation (STARD Compliant)
                         • Target n = 250 subjects at Cagayan de Oro RHUs
                         • Paired with laboratory automated CBC (Sysmex XN) within 2 hours
                         • Primary Endpoint: AUROC ≥ 0.88 for Hb < 10.0 g/dL

[ Phase 5: Months 8–9 ]  Regulatory Filing & Academic Dissemination
                         • File for FDA Philippine Medical Device Classification (Software)
                         • Submit manuscript to peer-reviewed digital health journal
```

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ [FIGURE 6 PLACEHOLDER: PROSPECTIVE CLINICAL VALIDATION DESIGN & ROC CURVE]             │
│                                                                                        │
│ Suggested Visual: Dual-panel clinical validation methodology and diagnostic curve:     │
│ 1. STARD Study Flowchart: Prospective recruitment schema of N=250 subjects at Cagayan  │
│    de Oro City Health Centers (stratified: 100 pregnant women, 75 infants/children,    │
│    75 adults). Details paired, blinded evaluation between TinginHB index screening and │
│    gold-standard automated venous CBC (Sysmex XN-550) within a 2-hour window.          │
│ 2. Target ROC / AUROC Diagnostic Curves: Comparative Receiver Operating Characteristic │
│    plots illustrating target benchmark performance (AUROC >= 0.88 for moderate-to-    │
│    severe anemia Hb < 10.0 g/dL; Sensitivity >= 85%; Specificity >= 80%).              │
│                                                                                        │
│ Caption: Figure 6. Prospective Clinical Field Validation Design (STARD Compliant) and  │
│ Expected Receiver Operating Characteristic (ROC) Diagnostic Curves.                    │
│ Validation Standard: Bossuyt et al. (2015, STARD); Kim et al. (2020); Mannino (2018). │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ [FIGURE 7 PLACEHOLDER: 12-MONTH RESEARCH & PRODUCT ROADMAP GANTT CHART]                │
│                                                                                        │
│ Suggested Visual: Horizontal Gantt Chart timeline spanning Months 1 through 12:        │
│ • Phase 1 (M1–M2): Dataset curation, synthetic color augmentation, YOLOv8n-seg models. │
│ • Phase 2 (M2–M3): Dual-branch model training, MC Dropout, Platt calibration tuning.   │
│ • Phase 3 (M3–M5): Android edge integration, offline PDF builder, BHW UX field trials. │
│ • Phase 4 (M5–M8): Prospective clinical trials (N=250) in Cagayan de Oro RHUs with     │
│   Ethics Review Board (REC/IRB) approval & automated CBC comparison.                   │
│ • Phase 5 (M8–M10): DOH Central Maternal Dashboard, PhilHealth Konsulta API linking.   │
│ • Phase 6 (M10–M12): Philippine FDA Medical Device Software Notification & PSC XI Pitch│
│   commercialization rollout.                                                           │
│                                                                                        │
│ Caption: Figure 7. TinginHB 12-Month Multi-Phase Research, Clinical Validation, and    │
│ Deployment Roadmap.                                                                    │
│ Framework: DOH Health Technology Assessment (HTA) & RA 11223 Implementation Timeline.  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## X. COMPETITIVE DIFFERENTIATION MATRIX

| Parameter | TinginHB (DataLunas) | HemoCue Hb 301 | AnemoCheck / Sanguina | Naked-Eye Pallor |
| :--- | :---: | :---: | :---: | :---: |
| **Cost per Test** | **₱0 (Zero Consumables)** | ₱150 / cuvette | ~$5 USD / test | ₱0 |
| **Device Hardware Cost** | **₱0 (Existing Phone)** | ₱70,000–₱125,000 | Existing Phone | ₱0 |
| **Laboratory Calibration** | **Not Required** | Factory Calibrated | **Required (Prior CBC)** | None |
| **Anatomical Sites** | **Dual: Conjunctiva + Nail** | Blood (Fingerstick) | Nail Bed Only | Subjective / Variable |
| **Skin Pigmentation Bias** | **Minimal (0-melanin eye)** | None (Invasive) | High (Skin sensitive) | Severe |
| **Output Interpretation** | **Calibrated Probabilistic** | Absolute Hb (g/dL) | Continuous Hb (g/dL) | Subjective Guess |
| **Offline Functionality** | **100% Offline** | 100% Offline | Requires Cloud Sync | Offline |
| **Philippine Health Alignment** | **PhilHealth Konsulta PDF** | None | None | Manual Paper Logs |

---

## XI. CONCLUSION

TinginHB demonstrates that responsible AI in healthcare is not about making unsubstantiated claims of replacing laboratory medicine, but about **scientifically bounding algorithms to solve concrete frontline bottlenecks**. 

By transforming entry-level smartphones into zero-consumable, dual-site triage tools with calibrated probabilistic outputs and dynamic missing-modality weighting, TinginHB empowers 200,000 Filipino Barangay Health Workers to detect severe maternal and infant anemia months before catastrophic clinical complications arise—turning every routine barangay visit into a life-saving health intervention.

---

## XII. REFERENCES & ACADEMIC GROUNDING

1. **World Health Organization (2011).** *Haemoglobin concentrations for the diagnosis of anaemia and assessment of severity*. Vitamin and Mineral Nutrition Information System. WHO/NMH/NHD/MNM/11.1.
2. **World Health Organization (2013).** *Pocket book of hospital care for children: Guidelines for the management of common childhood illnesses* (2nd ed.). Section: Assessment of palmar and conjunctival pallor (IMCI).
3. **World Health Organization (2016).** *WHO recommendations on antenatal care for a positive pregnancy experience*. WHO Guidelines Approved by the Guidelines Review Committee.
4. **Strobach, R. S., Anderson, S. K., Doll, D. C., & Ringenberg, Q. S. (1988).** The value of the physical examination in diagnosing anemia. *JAMA*, 259(11), 1682–1685. https://doi.org/10.1001/jama.1988.03720110048033
5. **Kalter, H. D., Burnham, G., Kolstad, P. R., et al. (1997).** Evaluation of clinical signs to diagnose anaemia in Uganda and Bangladesh, in areas with and without malaria. *Bulletin of the World Health Organization*, 75(Suppl 1), 103–111.
6. **Luby, S. P., Kazembe, P. N., Redd, S. C., et al. (1995).** Using clinical signs to diagnose anaemia in African children. *Bulletin of the World Health Organization*, 73(4), 477–482.
7. **Duke, M., & Abelmann, W. H. (1969).** The hemodynamic response to chronic anemia. *Circulation*, 39(4), 503–515. https://doi.org/10.1161/01.cir.39.4.503
8. **Varat, M. A., Adolph, R. J., & Fowler, N. O. (1972).** Cardiovascular effects of severe anemia. *American Heart Journal*, 83(3), 415–426. https://doi.org/10.1016/0002-8703(72)90445-0
9. **Kim, T. N., et al. (2020).** Smartphone-based assessment of anemia from conjunctival images. *Proceedings of the National Academy of Sciences (PNAS)*, 117(49), 31046–31055. https://doi.org/10.1073/pnas.2016029117
10. **Kim, T. N., et al. (2023).** Validation of a smartphone-based conjunctival assessment for anemia in outpatients. *Annals of Internal Medicine*, 176(3), 302–310. https://doi.org/10.7326/M22-2624
11. **Mannino, R. G., Myers, D. R., Tyburski, E. A., et al. (2018).** Smartphone app for non-invasive detection of anemia using only patient-sourced photos. *Nature Communications*, 9(1), 4924. https://doi.org/10.1038/s41467-018-07262-2
12. **Dimauro, G., Ciprandi, D., Deperte, F., et al. (2018).** Ocular redness measurement in non-contact and non-invasive diagnoses of anaemia. *Journal of Imaging*, 4(8), 95. https://doi.org/10.3390/jimaging4080095
13. **Valles-Coral, M. A., et al. (2025).** AnaeCare: Non-invasive anemia detection from smartphone images using multi-site pallor analysis. *arXiv*:2503.XXXXX.
14. **Baltrusaitis, T., Ahuja, C., & Morency, L. P. (2019).** Multimodal machine learning: A survey and taxonomy. *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 41(2), 423–443. https://doi.org/10.1109/TPAMI.2018.2798607
15. **Huang, S. C., Pareek, A., Seyyedi, S., et al. (2020).** Fusion of medical imaging and electronic health records using deep learning: a systematic review and implementation guidelines. *npj Digital Medicine*, 3(1), 136. https://doi.org/10.1038/s41746-020-00341-z
16. **Gal, Y., & Ghahramani, Z. (2016).** Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning. *Proceedings of the 33rd International Conference on Machine Learning (ICML)*, 48, 1050–1059.
17. **Platt, J. (1999).** Probabilistic outputs for support vector machines and comparisons to regularized likelihood methods. *Advances in Large Margin Classifiers*, 10(3), 61–74.
18. **Food and Nutrition Research Institute (DOST-FNRI, 2020).** *Expanded National Nutrition Survey: Nutritional Status of Filipino Children and Pregnant Women*. Department of Science and Technology, Taguig City, Philippines.
19. **Republic of the Philippines (2018).** *Republic Act No. 11148: Kalusugan at Nutrisyon ng Mag-Nanay Act (First 1,000 Days Law)*. Official Gazette.
20. **Republic of the Philippines (2019).** *Republic Act No. 11223: Universal Health Care Act*. Official Gazette.

---

**Team DataLunas — University of Science and Technology of Southern Philippines**  
*Department of Data Science | College of Information Technology and Computing*  
*Cagayan de Oro City, Philippines*  
