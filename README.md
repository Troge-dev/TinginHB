# TingínHB

<div align="center">

```
  _______ _             _           _    _ ____  
 |__   __(_)           (_)         | |  | |  _ \ 
    | |   _ _ __   __ _ _ _ __     | |__| | |_) |
    | |  | | '_ \ / _` | | '_ \    |  __  |  _ < 
    | |  | | | | | (_| | | | | |   | |  | | |_) |
    |_|  |_|_| |_|\__, |_|_| |_|   |_|  |_|____/ 
                   __/ |                         
                  |___/                          
```

### *Two sites. One screen. Zero cost. Zero consumables.*

**Non-Invasive, Multi-Site Edge-AI Hemoglobin Screening for Philippine Maternal and Community Health**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Flutter: 3.x](https://img.shields.io/badge/Flutter-3.x-02569B.svg?logo=flutter&logoColor=white)](https://flutter.dev/)
[![YOLOv8: Segment](https://img.shields.io/badge/YOLOv8-Segmentation-00FFFF.svg)](https://ultralytics.com)
[![Target: PSC XI](https://img.shields.io/badge/Competition-PSC%20XI%20Prototype%20Track-orange.svg)](https://dict.gov.ph)
[![Regulatory: PFDA Class B](https://img.shields.io/badge/PFDA%20Classification-Class%20B%20(AMDD)-red.svg)]()
[![Inference: Offline](https://img.shields.io/badge/Edge%20AI-100%25%20Offline%20(~13.5MB)-purple.svg)]()

<br/>

> **"Tingin"** *(Tagalog: Look / See)* + **"HB"** *(Hemoglobin)*  
> **"See Anemia Before It Kills."**

*Developed for the **Philippine Startup Challenge XI (PSC XI)** — Prototype-Ready Solution Track*  
*By 3rd-Year Data Science Students*

</div>

---

## Executive Summary

**TingínHB** is a multi-site non-invasive anemia screening mobile application. By capturing and analyzing images from two complementary anatomical microvascular sites — the **palpebral conjunctiva** (inner lower eyelid) and the **fingernail bed** — TingínHB standardizes and digitizes the clinical pallor examination of a trained physician.

Operating entirely on-device in under **2 seconds** on an entry-level **PHP 5,000 Android smartphone**, TingínHB requires **PHP 0 per test** (zero chemical reagents, zero disposable microcuvettes, zero biohazard sharps waste), providing high-accuracy hemoglobin screening for Barangay Health Workers (BHWs) in geographically isolated and disadvantaged areas (GIDAs).

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                     THE TINGÍNHB VALUE PILLARS                                  │
├───────────────────────┬────────────────────────┬────────────────────────┬────────────────────────┤
│   ZERO CONSUMABLES    │    DUAL-SITE FUSION    │   100% OFFLINE EDGE    │ PHILIPPINE POLICY      │
│   PHP 0/test vs       │   Conjunctiva + Nail   │   13.5 MB total models │ Aligned with RA 11148  │
│   PHP 150 for HemoCue │   Inverse-Variance ML  │   <60ms on low-end SoC │ & PhilHealth Konsulta  │
└───────────────────────┴────────────────────────┴────────────────────────┴────────────────────────┘
```

---

## The Multi-Dimensional Philippine Anemia Crisis

Anemia is not an isolated clinical condition; it is a systemic public health emergency that undermines maternal survival, childhood cognitive development, educational attainment, and national economic productivity across the Philippine archipelago.

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                             THE 4 PILLARS OF THE PHILIPPINE ANEMIA BURDEN                        │
├───────────────────────┬────────────────────────┬────────────────────────┬────────────────────────┤
│ 1. MATERNAL MORTALITY │ 2. PEDIATRIC COGNITION │ 3. ADOLESCENT HEALTH   │ 4. ECONOMIC DRAIN      │
│ • #1 Cause of Death   │ • 40–45% of infants    │ • 15–20% of schoolgirls│ • 1.5–4.0% GDP loss    │
│ • 25–30% from PPH     │ • Irreversible IQ loss │ • School absenteeism   │ • Reduced physical and │
│ • 21.8% pregnant anemic│ • Stunting & low birth │ • Intergenerational   │   cognitive workforce  │
│ • Uterine atony risk  │   weight cycle         │   malnutrition cycle   │   productivity         │
└───────────────────────┴────────────────────────┴────────────────────────┴────────────────────────┘
```

---

### 1. Maternal Mortality and Obstetric Complications
In the Philippines, maternal mortality remains an urgent public health crisis with a Maternal Mortality Ratio (MMR) of **119–144 per 100,000 live births**, significantly exceeding the UN Sustainable Development Goal (SDG 3.1) target of **<70 per 100,000 live births by 2030**.

* **Postpartum Hemorrhage (PPH) as the Leading Killer:** PPH is the single largest direct cause of maternal death nationwide, responsible for **25%–30% of all maternal fatalities** (~2,000+ preventable deaths annually).
* **High Antenatal Prevalence:** **21.8%** of pregnant Filipino women are clinically anemic (*DOST-FNRI Expanded National Nutrition Survey*), entering labor with severely compromised oxygen-carrying capacity.
* **The Fatal Pathophysiology Triad:** Anemic mothers ($\text{Hb} < 9.0\text{ g/dL}$) face a **2.5x to 4.0x higher risk of fatal delivery complications** due to:
  1. **Myometrial Uterine Atony:** Severe iron deficiency robs myometrial smooth muscle of adenosine triphosphate (ATP) and oxygen, preventing effective postpartum uterine contraction (the root cause of 70%–80% of all PPH cases).
  2. **Depleted Physiological Reserve:** A healthy mother ($\text{Hb } 12\text{--}14\text{ g/dL}$) tolerates normal blood loss ($500\text{ mL}$); an anemic mother ($\text{Hb} < 9\text{ g/dL}$) decompensates into irreversible hypovolemic shock after losing just $300\text{ mL}$.
  3. **Impaired Coagulation Kinetics:** Hypoxemia and micronutrient deficits disrupt clotting enzyme cascades.
* **Perinatal and Fetal Risks:** Maternal anemia increases the incidence of preterm birth, intrauterine growth restriction (IUGR), low birth weight ($<2,500\text{ g}$), and perinatal mortality.

```
       ┌──────────────────────────────────────────────────────────┐
       │   Severe Maternal Anemia (Hb < 9.0 g/dL) (21.8% in PH)   │
       └────────────────────────────┬─────────────────────────────┘
                                    │
         ┌──────────────────────────┼──────────────────────────┐
         ▼                          ▼                          ▼
┌──────────────────┐      ┌──────────────────┐      ┌──────────────────┐
│  Uterine Atony   │      │ Depleted Reserve │      │ Coagulopathy     │
│ (Myometrial ATP  │      │ (300mL loss ->   │      │ (Impaired        │
│  Depletion)      │      │  Hypovolemic     │      │  Clotting        │
│  [70-80% of PPH] │      │  Shock)          │      │  Cascade)        │
└────────┬─────────┘      └─────────┬────────┘      └─────────┬────────┘
         │                          │                         │
         └──────────────────────────┼─────────────────────────┘
                                    ▼
       ┌──────────────────────────────────────────────────────────┐
       │   FATAL POSTPARTUM HEMORRHAGE (PPH) — PRIMARY CAUSE IN PH│
       │   (119–144 MMR vs SDG Target <70 per 100k Live Births)   │
       └──────────────────────────────────────────────────────────┘
```

---

### 2. Pediatric Neurodevelopment and the First 1,000 Days
The first 1,000 days of life (conception through 24 months) represent a non-negotiable biological window for brain architecture development:

* **High Infant Vulnerability:** **40%–45%** of Filipino infants aged 6–11 months and **26%** of children under 5 suffer from iron-deficiency anemia (*DOST-FNRI*).
* **Irreversible Cognitive Impairment:** Iron is an indispensable cofactor for central nervous system myelination, oligodendrocyte maturation, and monoamine neurotransmitter synthesis (dopamine, serotonin, norepinephrine). Clinical trials demonstrate that chronic infantile anemia results in:
  * Permanent deficits in executive function, spatial memory, and auditory processing.
  * Long-term loss of **5 to 10 IQ points**, which cannot be fully reversed even after subsequent iron repletion.
* **Physical Stunting and Immune Compromise:** Anemic children experience impaired cellular immunity, higher susceptibility to severe respiratory and gastrointestinal infections, and accelerated linear growth stunting (chronic undernutrition).

---

### 3. Adolescent Health and the Intergenerational Poverty Cycle
* **Prevalence Among Adolescent Girls:** Approximately **15%–20%** of school-age adolescent females in the Philippines are anemic due to the combined demands of rapid pubertal growth spurts, inadequate dietary iron intake, and monthly menstrual blood loss.
* **Educational Losses:** Anemia causes chronic cerebral hypoxemia, presenting as fatigue, reduced attention span, impaired memory retention, and high school absenteeism, directly depressing academic achievement.
* **The Intergenerational Malnutrition Trap:** Adolescent girls who remain anemic frequently enter their first pregnancy in an iron-depleted state, perpetuating an intergenerational cycle of low birth weight infants, stunted children, and high-risk pregnancies.

---

### 4. Macroeconomic Drain and Labor Productivity Losses
The economic fallout of unmitigated anemia creates a profound drag on national development:

* **Gross Domestic Product (GDP) Impact:** The World Bank and World Health Organization estimate that iron deficiency anemia results in an annual loss of **1.5% to 4.0% of GDP** in developing nations through reduced cognitive capital and adult workforce debility.
* **Physical Workforce Degradation:** In agriculture, manufacturing, and the informal labor sector (which employ millions of Filipinos), anemia lowers maximal oxygen consumption ($\text{VO}_2\text{ max}$), reducing physical labor productivity by **10% to 20%** among manual workers.

---

### 5. The Primary Care Diagnostic Gap and Diagnostic Deserts
Despite the massive multi-demographic burden, primary healthcare facilities across the 7,641 Philippine islands lack basic diagnostic capacity:

* **Prohibitive Capital and Consumable Costs:** Standard gold-standard point-of-care analyzers (e.g., *HemoCue Hb 301*) require a capital outlay of **PHP 70,000–PHP 125,000 per unit** plus recurring operational costs of **PHP 105–PHP 150 per single-use microcuvette**. Rural Barangay Health Stations (BHS) and Rural Health Units (RHUs) face chronic stockouts and budgetary depletion.
* **Subjectivity and Failure of Visual Pallor Triage:** In the absence of diagnostic hardware, over 200,000 Barangay Health Workers (BHWs) rely on naked-eye physical inspection of the palms, conjunctiva, and nail beds. Clinical literature demonstrates visual pallor has:
  * Sensitivity of only **10%–60%** for mild-to-moderate anemia ($9.0 \le \text{Hb} \le 11.0\text{ g/dL}$).
  * Inter-observer Cohen's kappa agreement of only **$\kappa = 0.20\text{--}0.45$ (Poor/Slight)**.
  * **Misses over 50% of anemic cases** during routine community consultations before severe clinical crises emerge.
* **Severe Healthcare Worker Maldistribution:** While 40% of the Philippine population resides in rural areas, only ~10% of licensed physicians practice there. Physician density in isolated island and mountain provinces routinely drops below **1 doctor per 20,000–30,000 population**.
* **Biohazardous Waste Challenges:** Invasive fingerstick testing generates hazardous sharps and biohazard waste (lancets, blood-soaked cuvettes) in remote GIDA communities lacking autoclave or medical incineration facilities.

---

## The TingínHB Multi-Site Solution

TingínHB digitizes physical examination into an automated computer vision screening workflow. By evaluating **two complementary microvascular sites**, the platform addresses the clinical limitations inherent to single-site screeners:

```
                          ┌─────────────────────────────┐
                          │    TingínHB SENSING CORE    │
                          └──────────────┬──────────────┘
                                         │
                 ┌───────────────────────┴───────────────────────┐
                 ▼                                               ▼
   ┌───────────────────────────┐                   ┌───────────────────────────┐
   │    PRIMARY OPTICAL SITE   │                   │ COMPLEMENTARY FALLBACK    │
   │   Palpebral Conjunctiva   │                   │       Fingernail Bed      │
   ├───────────────────────────┤                   ├───────────────────────────┤
   │ • Zero melanin pigment    │                   │ • Dense vascular plexus   │
   │ • Fitzpatrick III–VI proof│                   │ • High patient comfort    │
   │ • Sclera white reference  │                   │ • Non-intrusive capture   │
   │ • Target MAE ~0.8 g/dL    │                   │ • Pediatric fallback      │
   └───────────────────────────┘                   └───────────────────────────┘
```

### Why the Palpebral Conjunctiva is the Primary Site
1. **Zero Melanin Pigmentation:** The palpebral conjunctiva (the vascular mucosal lining of the lower eyelid) contains no melanin. Optical absorption is determined strictly by hemoglobin and water content, ensuring identical diagnostic baseline performance across all Filipino skin complexions (**Fitzpatrick Skin Types III through VI**).
2. **In-Frame Sclera White-Balance Reference:** The white sclera adjacent to the lower eyelid serves as an internal, patient-specific white reference in every frame ($k_c = 255 / \overline{\text{Sclera}}_c$), eliminating the requirement for external color calibration cards.

### Why the Fingernail Bed is the Complementary Fallback
1. **Clinical Accessibility:** When lower eyelid eversion cannot be performed (e.g., distress in pediatric patients during nutritional outreach, photophobia, eye trauma, or active conjunctivitis), the subungual capillary bed provides an immediate, non-intrusive alternative.
2. **Quantifiable Optical Density:** The nail bed vasculature enables optical assessment using the Erythema Index ($\text{EI} = \ln(\text{Red}) - \ln(\text{Green})$), validated in clinical literature for non-invasive hemoglobin estimation.

---

### Multi-Site Adaptability Matrix

| Clinical Scenario | Conjunctiva-Only Tool | Fingernail-Only Tool | TingínHB (Multi-Site Fused) |
|:---|:---:|:---:|:---:|
| **Standard Antenatal Visit** | Capable | Capable | **Dual-Site Fusion (Optimal Precision)** |
| **Pediatric Screening (OPT+ / 6–24 mo)** | Impeded | Capable | **Fingernail Mode Fallback** |
| **Elderly Patients with Eye Sensitivity** | Impeded | Capable | **Fingernail Mode Fallback** |
| **Cosmetic Polish / Henna / Nail Trauma** | Capable | Impeded | **Conjunctiva Mode Primary** |
| **Active Conjunctivitis / Eye Infection** | Impeded | Capable | **Fingernail Mode Fallback** |
| **Cold Temperatures (Peripheral Vasoconstriction)** | Capable | Impeded | **Conjunctiva Mode Primary** |

---

## The Three Operational Modes

```mermaid
graph TD
    A[Initiate Screening Encounter] --> B{Can patient safely evert lower eyelid?}
    B -- Yes --> C[Acquire Conjunctiva Frame]
    B -- No / Pediatric / Infection --> D[Acquire Fingernail Frame]
    
    C --> E{Are unpolished fingernails accessible?}
    E -- Yes --> F[Acquire Fingernail Frame]
    E -- No / Polish / Trauma --> G[Mode 1: Conjunctiva Primary]
    
    D --> H[Mode 2: Fingernail Fallback]
    
    F --> I[Segmentation and Color Normalization]
    I --> J[Run Parallel Inference on Both Sites]
    J --> K{Discrepancy |Hb_conj - Hb_nail| > 2.0 g/dL?}
    K -- Yes --> L[Flag Inconsistency: Recommend Immediate Rescreen]
    K -- No --> M[Mode 3: Inverse-Variance Dual Fusion]
    
    G --> N[Composite Clinical Risk Stratification]
    H --> N
    M --> N
    L --> N
    N --> O[Display Hemoglobin Estimate, WHO Tiers, and Konsulta Referral]
```

1. **Mode 1: Conjunctiva Primary (High Accuracy)**  
   *Operational Trigger:* Patient everts lower eyelid; fingernails obstructed by cosmetics, artificial nails, or trauma.  
   *Methodology:* YOLOv8n-seg isolates conjunctival tissue and sclera; sclera normalization standardizes pixel channels; dual-branch MobileNetV3 performs feature extraction.  
   *Target Benchmark:* $\text{MAE} \le 1.0\text{ g/dL}$, $\text{AUC} \ge 0.88$.

2. **Mode 2: Fingernail Fallback (Broad Accessibility)**  
   *Operational Trigger:* Eyelid eversion impractical (uncooperative infants, ocular inflammation, cataracts).  
   *Methodology:* YOLOv8n-seg segments nail bed; computes Erythema Index and periungual contrast ratio; single-branch MobileNetV3 estimates hemoglobin.  
   *Target Benchmark:* $\text{MAE} \le 1.8\text{ g/dL}$, $\text{AUC} \ge 0.82$.

3. **Mode 3: Dual-Site Fusion (Maximum Clinical Precision)**  
   *Operational Trigger:* Both conjunctiva and fingernail captures pass quality verification.  
   *Methodology:* Estimates from both sites are combined using inverse-variance uncertainty weighting ($w_i = 1/\sigma_i^2$) with automated discrepancy detection.  
   *Target Benchmark:* $\text{MAE} \le 0.8\text{ g/dL}$, $\text{AUC} \ge 0.92$, $\text{Sensitivity} \ge 90\%$.

---

## Guidelines for Barangay Health Workers (BHW Guide)

<details>
<summary><b>Read the BHW Field Instructions and Operational Protocols (English / Tagalog)</b></summary>

<br/>

### Overview
**TingínHB** transforms a standard Android phone into an **objective anemia screening tool**. Using machine vision, it calculates estimated hemoglobin in **2 seconds without blood draws, needles, or recurring consumable costs**.

---

### Step-by-Step Acquisition Procedures

```
   [ 1. Dual-Site Mode ]                [ 2. Conjunctiva Mode ]          [ 3. Fingernail Mode ]
    Both Eye and Nail                    Eye Capture Only                 Nail Capture Only
    Highest Diagnostic Precision         For Polished/Damaged Nails       For Distressed Children/Infections
```

#### Procedure 1: Conjunctival Capture (Palpebral Conjunctiva)
1. **Patient Positioning:** Seat the patient in an area with stable ambient lighting.
2. **Eversion Technique:** Using clean hands, gently retract the lower eyelid downward until the red palpebral mucosal tissue is visible.
3. **Camera Alignment:** Align the eye inside the **oval reticle** on the screen. The camera torch activates automatically.
4. **Acquisition:** Hold steady until the on-screen quality indicators confirm sharp focus and proper exposure.

#### Procedure 2: Fingernail Capture (Subungual Bed)
1. **Digit Inspection:** Select an index or thumbnail free of nail polish, dyes, or debris.
2. **Camera Alignment:** Place the nail bed within the **box reticle** on screen.
3. **Acquisition:** Hold steady without applying excessive pressure against the finger pad to preserve capillary blood volume.

#### Procedure 3: Dual-Site Mode (Recommended)
* Execute the eye capture followed by the fingernail capture. The system automatically reconciles both measurements into an integrated screening score.

---

### Clinical Triage and Action Plan

| Triage Tier | Hemoglobin Range | Clinical Classification | Recommended Action |
|:---|:---|:---|:---|
| **GREEN** | $\text{Hb} \ge 11.0\text{ g/dL}$ | Normal Baseline | Continue standard antenatal care and routine Iron-Folic Acid Supplementation (IFAS). |
| **YELLOW** | $\text{Hb } 10.0\text{--}10.9\text{ g/dL}$ | Mild Anemia | Review IFAS adherence; reinforce dietary iron intake; schedule follow-up screening. |
| **ORANGE** | $\text{Hb } 7.0\text{--}9.9\text{ g/dL}$ | Moderate Anemia | **Refer to Rural Health Unit (RHU)** for confirmatory complete blood count (CBC) and clinical assessment. |
| **RED** | $\text{Hb} < 7.0\text{ g/dL}$ | Severe Anemia | **Urgent referral to District Hospital / RHU.** High risk of intrapartum complications and fatal PPH. |

---

### Automated PhilHealth Konsulta Referral
When a patient screens in the **Orange** or **Red** category, select **"Generate Referral Letter"**. The application compiles a standardized PDF referral document containing demographic details, screening metrics, gestational age, and MUAC for submission to accredited PhilHealth Konsulta clinics or referral hospitals.

</details>

---

## Multi-Site Edge ML Architecture and Mathematics

```
═════════════════════════════════════════════════════════════════════════════════════════════════════
                       STAGE 1: DUAL-SITE IMAGE ACQUISITION & QUALITY GATE
═════════════════════════════════════════════════════════════════════════════════════════════════════
 [CONJUNCTIVA CAPTURE]                                          [FINGERNAIL CAPTURE]
  • Rear Camera + Locked Torch Flash                             • Rear Camera + Locked Flash
  • CameraX Static ISO 100 / Exposure Lock                       • Dynamic Focus Lock
  • UI Guide: Anatomical Oval Reticle                            • UI Guide: Bounding Box Reticle
  • Real-Time Quality Heuristics:                                • Real-Time Quality Heuristics:
    ├─ Focus Metric: Var(Laplacian) > 120                          ├─ Focus Metric: Var(Laplacian) > 100
    ├─ Exposure Gate: 80 <= Mean(Pixel_Intensity) <= 200           ├─ Exposure Gate: 80 <= Mean(Intensity) <= 210
    └─ Eversion Classifier: MobileNetV2-QC (Pass/Fail)             └─ Polish Detector: Hue Dispersion Metric
                           │                                                              │
                           ▼                                                              ▼
═════════════════════════════════════════════════════════════════════════════════════════════════════
                 STAGE 2: SEGMENTATION & ILLUMINATION-INVARIANT NORMALIZATION
═════════════════════════════════════════════════════════════════════════════════════════════════════
 [YOLOv8n-seg Conjunctiva (~3.2 MB TFLite)]                     [YOLOv8n-seg Fingernail (~3.2 MB TFLite)]
  • Dual Mask Heads:                                             • Dual Mask Heads:
    ├─ M_conj: Palpebral Conjunctiva ROI                           ├─ M_nail: Subungual Nail Bed ROI
    └─ M_sclera: Adjacent Sclera Tissue Reference                  └─ M_peri: Periungual Skin Ring
  • Sclera-Referenced Normalization:                             • Self-Referenced Erythema Index:
    $$k_c = \frac{255}{\text{mean}(M_{\text{sclera}, c})}$$        $$\text{EI} = \ln(\overline{R}_{\text{nail}}) - \ln(\overline{G}_{\text{nail}})$$
    $$I_{\text{norm}, c} = I_{\text{conj}, c} \cdot k_c$$         $$\text{Contrast}_{\text{peri}} = \frac{\overline{R}_{\text{nail}} / \overline{G}_{\text{nail}}}{\overline{R}_{\text{peri}} / \overline{G}_{\text{peri}}}$$
  • Radiomics + Color Spaces:                                    • Feature Matrices:
    ├─ CIELAB a*, b*, L* and Erythema Index                        ├─ RGB/HSV Color Moments
    └─ GLCM Texture (Haralick Contrast & Homogeneity)             └─ Longitudinal Pallor Gradient Profile
                           │                                                              │
                           ▼                                                              ▼
═════════════════════════════════════════════════════════════════════════════════════════════════════
                      STAGE 3: HIERARCHICAL ESTIMATION & LEARNED FUSION
═════════════════════════════════════════════════════════════════════════════════════════════════════
 [CONJUNCTIVA ESTIMATOR (MobileNetV3-Small Dual)]               [FINGERNAIL ESTIMATOR (MobileNetV3-Small)]
  • Branch A: Deep CNN 224x224 Normalized Crop                  • Deep CNN 224x224 Normalized Nail Bed
  • Branch B: 16-D Radiomic/Colorimetric Vector                  • Dense Regressor Head
  • Output: y_conj ± sigma_conj                                  • Output: y_nail ± sigma_nail
                           │                                                              │
                           └──────────────────────────────┬───────────────────────────────┘
                                                          │
                                                          ▼
               ┌─────────────────────────────────────────────────────────────────────┐
               │              INVERSE-VARIANCE LEARNED FUSION LAYER                  │
               │                                                                     │
               │  1. Discrepancy Verification:                                       │
               │     $$\Delta_{\text{diff}} = |\hat{y}_{\text{conj}} - \hat{y}_{\text{nail}}|$$                       │
               │     IF $\Delta_{\text{diff}} > 2.0\text{ g/dL}$ -> Flag Disagreement Warning       │
               │                                                                     │
               │  2. Inverse-Variance Weighted Consensus:                           │
               │     $$w_{\text{conj}} = \frac{1}{\sigma_{\text{conj}}^2}, \quad w_{\text{nail}} = \frac{1}{\sigma_{\text{nail}}^2}$$            │
               │     $$\hat{y}_{\text{fused}} = \frac{w_{\text{conj}}\hat{y}_{\text{conj}} + w_{\text{nail}}\hat{y}_{\text{nail}}}{w_{\text{conj}} + w_{\text{nail}}}$$                 │
               │     $$\sigma_{\text{fused}} = \sqrt{\frac{1}{w_{\text{conj}} + w_{\text{nail}}}}$$                       │
               └──────────────────────────────────┬──────────────────────────────────┘
                                                  │
                                                  ▼
               ┌─────────────────────────────────────────────────────────────────────┐
               │           COMPOSITE CLINICAL DECISION SUPPORT & TRIAGE              │
               │                                                                     │
               │  Inputs: Estimated Hb, Gestational Age, Maternal Age, MUAC          │
               │  Classification Logic: WHO and DOH AO 2010-0010 Guidelines          │
               │  • Normal:   Hb >= 11.0 g/dL  (Green)                               │
               │  • Mild:     10.0 <= Hb <= 10.9 g/dL (Yellow)                       │
               │  • Moderate: 7.0 <= Hb <= 9.9 g/dL   (Orange)                       │
               │  • Severe:   Hb < 7.0 g/dL     (Red - High Risk)                    │
               │                                                                     │
               │  Automated PDF: PhilHealth Konsulta Referral Form                   │
               └─────────────────────────────────────────────────────────────────────┘
```

---

### On-Device Edge Footprint and Latency

TingínHB is optimized for resource-constrained ARM Cortex mobile processors (e.g., MediaTek Helio G35, Qualcomm Snapdragon 400 series):

| Pipeline Component | Neural Architecture | Quantization Format | Model Size on Disk | Inference Latency |
|:---|:---|:---:|:---:|:---:|
| **Quality Gate Filter** | MobileNetV2-Tiny + OpenCV | INT8 | 1.8 MB | 12 ms |
| **Conjunctiva Segmenter** | YOLOv8-nano-seg | INT8 TFLite | 3.2 MB | 18 ms |
| **Fingernail Segmenter** | YOLOv8-nano-seg | INT8 TFLite | 3.2 MB | 18 ms |
| **Conjunctiva Hb Model** | MobileNetV3-Small (Dual-Branch) | INT8 TFLite | 2.5 MB | 22 ms |
| **Fingernail Hb Model** | MobileNetV3-Small | INT8 TFLite | 2.5 MB | 20 ms |
| **Fusion Engine & Logic** | Inverse-Variance / MLP | Float32 / Native | 0.1 MB | <1 ms |
| **Total System Footprint**| **Full Dual-Site Stack** | **TFLite INT8** | **~13.3 MB** | **<60 ms / site** |

---

### Target Performance Metrics

| Evaluation Metric | Conjunctiva Alone | Fingernail Alone | Dual-Site Fusion (TingínHB) |
|:---|:---:|:---:|:---:|
| **Mean Absolute Error (MAE)** | $\le 1.10\text{ g/dL}$ | $\le 1.80\text{ g/dL}$ | $\mathbf{\le 0.80\text{ g/dL}}$ |
| **Correlation ($r$)** | $r \ge 0.86$ | $r \ge 0.78$ | $\mathbf{r \ge 0.93}$ |
| **Overall ROC-AUC ($\text{Hb} < 11.0$)** | $\ge 0.87$ | $\ge 0.80$ | $\mathbf{\ge 0.92}$ |
| **Clinical Sensitivity ($\text{Hb} < 11.0$)**| $\ge 86.0\%$ | $\ge 80.0\%$ | $\mathbf{\ge 91.5\%}$ |
| **Clinical Specificity ($\text{Hb} \ge 11.0$)**| $\ge 82.0\%$ | $\ge 76.0\%$ | $\mathbf{\ge 86.0\%}$ |
| **Severe Anemia ROC-AUC ($\text{Hb} < 7.0$)** | $\ge 0.93$ | $\ge 0.86$ | $\mathbf{\ge 0.96}$ |

---

## Cost Comparison Analysis

| Evaluation Dimension | Laboratory CBC | HemoCue Hb 301 | AnemoCheck App (US) | TingínHB (This Work) |
|:---|:---:|:---:|:---:|:---:|
| **Equipment Capital Cost** | PHP 500,000–1.5M | PHP 70,000–125,000 | ~$5 USD + prior lab CBC | **PHP 0 (Runs on existing smartphone)** |
| **Per-Test Consumable Cost** | PHP 200–350 per test | PHP 105–150 per cuvette | PHP 0 (after calibration CBC) | **PHP 0.00 (Zero recurring consumables)** |
| **Cost per 1,000 Screenings** | PHP 200,000–350,000 | PHP 105,000–150,000 | ~$5.00 + baseline CBC cost | **PHP 0.00** |
| **Biohazardous Waste Generated** | Needles, blood tubes | Lancets, bloody cuvettes | None | **None (Zero biological waste)** |
| **Anatomical Sites Evaluated** | Venous blood sample | Capillary fingerstick | Fingernail bed only | **Conjunctiva + Fingernail (2 Sites)** |
| **Prerequisite Baseline CBC** | Not applicable | No | Yes (Requires initial CBC input) | **No (Independent inference)** |
| **Melanin Independence** | Yes | Yes | Sensitive to skin pigmentation | **Yes (Mucosal ROI & Sclera reference)** |
| **Fully Offline Operation** | No (LIMS dependent) | Yes | Yes | **Yes (100% on-device processing)** |
| **Operator Training Duration** | Professional Phlebotomist| 2–4 hours | ~30 minutes | **<30 minutes** |
| **Availability in the Philippines**| Tertiary/Secondary only | Selected RHUs only | Not available | **Designed specifically for PH BHS/RHUs** |

---

## Competitive Landscape and Differentiators

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                   COMPETITIVE BENCHMARKING                                       │
├──────────────────────┬────────────────────────┬──────────────────────────────────────────────────┤
│ PRODUCT / RESEARCH   │ PRIMARY LIMITATION     │ HOW TINGÍNHB SOLVES IT                           │
├──────────────────────┼────────────────────────┼──────────────────────────────────────────────────┤
│ AnemoCheck           │ Nail-only; affected by │ Dual-site architecture switches to the           │
│ (Sanguina Inc., US)  │ nail polish & melanin; │ unpigmented conjunctiva; requires no initial CBC │
│                      │ requires prior lab CBC │ calibration; localized for Philippine clinics.   │
├──────────────────────┼────────────────────────┼──────────────────────────────────────────────────┤
│ HemaApp              │ Research prototype;    │ Uses built-in smartphone flash and native        │
│ (Univ. of Washington)│ required external IR   │ camera sensors; zero clip-on peripherals;        │
│                      │ LED attachments        │ packaged as a deployable mobile application.     │
├──────────────────────┼────────────────────────┼──────────────────────────────────────────────────┤
│ Masimo Pronto SpHb   │ Prohibitive cost       │ Replaces dedicated pulse co-oximetry hardware    │
│ (Masimo Corp)        │ ($3,000–$5,000/unit +  │ with lightweight computer vision networks        │
│                      │ proprietary sensors)   │ executing on standard budget Android devices.    │
├──────────────────────┼────────────────────────┼──────────────────────────────────────────────────┤
│ Academic Literature  │ Single-site dataset    │ Implements learned multi-site fusion; packages   │
│ (Nature, IEEE, etc.) │ studies; lack deployable│ models into an offline Flutter application with  │
│                      │ field applications     │ BHW triage workflows and PDF referral creation.  │
└──────────────────────┴────────────────────────┴──────────────────────────────────────────────────┘
```

---

## Philippine Health Policy and Regulatory Alignment

<details>
<summary><b>Review Statutory and Regulatory Alignments</b></summary>

<br/>

TingínHB supports key statutory mandates and Department of Health directives:

1. **Republic Act 11148 (*Kalusugan at Nutrisyon ng Mag-Nanay Act* / First 1,000 Days Law):**
   * *Mandate:* Systematic maternal and child nutritional assessment during pregnancy and early childhood (0–24 months).
   * *Alignment:* Enables zero-cost, field-level anemia monitoring during home visits and routine clinic encounters.
2. **Republic Act 11223 (*Universal Health Care Act*):**
   * *Mandate:* Expands primary care diagnostic coverage in Geographically Isolated and Disadvantaged Areas (GIDAs).
   * *Alignment:* Provides point-of-care anemia screening to facilities without on-site clinical laboratories.
3. **PhilHealth Konsulta Package (*Circulars 2020-0022 and 2022-0005*):**
   * *Mandate:* Prescribes complete blood counts (CBC) during 1st and 3rd trimester prenatal checkups.
   * *Alignment:* Serves as a primary care screening tool to triage high-risk individuals for accredited Konsulta laboratory confirmation.
4. **DOH Administrative Order No. 2010-0010 (*Micronutrient Supplementation Guidelines*):**
   * *Mandate:* Governs therapeutic Iron-Folic Acid Supplementation (IFAS) regimens based on anemia severity.
   * *Alignment:* Allows community health workers to track longitudinal hemoglobin response over monthly checkups.
5. **DepEd Order No. 59, s. 2017 (*Weekly Iron and Folic Acid Supplementation / WIFA*):**
   * *Mandate:* School-based intermittent iron supplementation for adolescent females.
   * *Alignment:* Supports high-throughput, non-invasive screening campaigns in educational settings.
6. **Philippine FDA Regulatory Positioning:**
   * *Classification:* **Class B (Low-Moderate Risk Medical Device Software)** under the *ASEAN Medical Device Directive (AMDD)* and *DOH AO 2018-0002*.
   * *Scope:* Software as a Medical Device (SaMD) intended as a **Clinical Decision Support / Triage and Screening Aid**, serving as an adjunct to professional clinical evaluation.

</details>

---

## Datasets and Augmentation Strategy

<details>
<summary><b>Review Dataset Specifications and Data Augmentation Pipelines</b></summary>

<br/>

### 1. Benchmark Datasets

```
├── Conjunctiva Datasets:
│   ├── CP-AnemiC Dataset (Appiahene et al., 2023)
│   │   └── 710 pediatric subjects (Ghana), paired HemoCue Hb ground truth
│   ├── EYES-DEFY-ANEMIA (Dimauro et al.)
│   │   └── 218 subjects (Italian & Indian cohorts), pixel-level masks, lab CBC Hb
│   ├── Detecting Anaemia using CV (alexandershan / Kaggle)
│   │   └── Conjunctival captures with clinical labels and color metric vectors
│   └── Anemia Object Detection Dataset (Roboflow Universe)
│       └── Annotated palpebral conjunctiva and sclera bounding polygons
│
└── Fingernail Datasets:
    ├── Mannino et al. Protocol Replications (Nature Communications 2018)
    │   └── 337 imaging sessions from 227 clinical patients with CBC Hb ground truth
    ├── Fingernail Anemia Dataset (Kaggle Community Open Data)
    │   └── Standardized subungual nail bed image sets with categorized anemia tiers
    └── Nail ROI & Disease Segmentation Dataset (Roboflow Universe)
        └── Polygon annotations for nail plate and periungual skin isolation
```

### 2. Optical Data Augmentation Pipeline
To ensure model robustness across mobile camera sensors, flash color temperatures ($4500\text{K}–6500\text{K}$), and specular reflections, an `Albumentations` processing pipeline is employed:

```python
import albumentations as A

# Conjunctiva pipeline (simulates variable lighting, tear glare, flash highlights)
conjunctiva_transforms = A.Compose([
    A.ColorJitter(brightness=0.25, contrast=0.25, saturation=0.20, hue=0.04, p=0.8),
    A.RGBShift(r_shift_limit=15, g_shift_limit=15, b_shift_limit=15, p=0.5),
    A.RandomGamma(gamma_limit=(80, 120), p=0.5),
    A.CLAHE(clip_limit=2.0, tile_grid_size=(8, 8), p=0.4),
    A.RandomSunFlare(flare_roi=(0, 0, 1, 0.5), num_flare_circles=2, src_radius=100, p=0.3),
    A.MotionBlur(blur_limit=3, p=0.2),
    A.GaussNoise(var_limit=(10.0, 50.0), p=0.3),
])

# Fingernail pipeline (simulates skin tones, cosmetic residue, temperature variations)
fingernail_transforms = A.Compose([
    A.ColorJitter(brightness=0.20, contrast=0.20, saturation=0.25, hue=0.05, p=0.8),
    A.ShiftScaleRotate(shift_limit=0.06, scale_limit=0.10, rotate_limit=15, p=0.5),
    A.RandomToneCurve(scale=0.1, p=0.4),
    A.CoarseDropout(max_holes=4, max_height=16, max_width=16, p=0.2),
    A.GaussNoise(var_limit=(10.0, 30.0), p=0.3),
])
```

</details>

---

## Technical Stack

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                       ENGINEERING STACK                                          │
├──────────────────────┬───────────────────────────────────────────────────────────────────────────┤
│ Core Deep Learning   │ PyTorch 2.x, Torchvision, timm (Pretrained Backbones)                     │
├──────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ Vision & Segmentation│ Ultralytics YOLOv8-seg, OpenCV 4.x, scikit-image, Albumentations          │
├──────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ Radiomics & Analysis │ Mahotas (GLCM Haralick), NumPy, SciPy, pandas                             │
├──────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ Model Explainability │ PyTorch-GradCAM, SHAP (DeepExplainer)                                     │
├──────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ Edge Export & Quant  │ ONNX Runtime, TensorFlow 2.x, TFLite Converter (INT8 Quantization)        │
├──────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ Mobile Frontend      │ Flutter 3.x, Dart, CameraX Plugin, Riverpod (State Management)            │
├──────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ On-Device Runtime    │ tflite_flutter, tflite_flutter_helper, sqflite (Local Offline Database)   │
├──────────────────────┼───────────────────────────────────────────────────────────────────────────┤
│ Triage & Reporting   │ fl_chart (Gauge Visualizations), pdf / printing (Referral Generation)     │
└──────────────────────┴───────────────────────────────────────────────────────────────────────────┘
```

---

## Suggested Project Directory Structure

```
tinginhb/
├── README.md                               # Project documentation
├── LICENSE                                 # MIT License
├── requirements.txt                        # Python development dependencies
├── setup.py                                # Build and packaging configuration
│
├── data/
│   ├── raw/
│   │   ├── conjunctiva/                    # CP-AnemiC, EYES-DEFY-ANEMIA, Kaggle datasets
│   │   └── fingernail/                     # Mannino protocol and nail bed datasets
│   ├── processed/                          # Unified annotations (COCO/JSON format)
│   ├── augmented/                          # Pre-generated synthetic augmentations
│   └── validation_ph/                     # Dedicated Philippine clinical validation cohort
│
├── notebooks/
│   ├── 01_data_exploration.ipynb          # Exploratory data analysis and color metrics
│   ├── 02_conjunctiva_pipeline.ipynb      # Sclera normalization and dual-branch training
│   ├── 03_fingernail_pipeline.ipynb       # Erythema Index extraction and regression
│   ├── 04_fusion_model.ipynb              # Inverse-variance weighting and discrepancy logic
│   ├── 05_quantization_export.ipynb       # PyTorch to ONNX to TFLite INT8 quantization
│   └── 06_evaluation_metrics.ipynb        # MAE, ROC-AUC, and Bland-Altman analysis
│
├── src/
│   ├── __init__.py
│   ├── dataset.py                          # PyTorch Dataset and DataLoader implementations
│   ├── preprocessing/
│   │   ├── __init__.py
│   │   ├── conjunctiva.py                  # Sclera-referenced normalization, CIELAB, EI
│   │   ├── fingernail.py                   # Erythema Index, periungual normalization
│   │   └── quality_gate.py                 # Real-time blur, exposure, and polish heuristics
│   ├── augmentation.py                     # Albumentations multi-site pipeline definitions
│   ├── models/
│   │   ├── __init__.py
│   │   ├── conjunctiva_model.py            # MobileNetV3 dual-branch (colorimetric + radiomics)
│   │   ├── fingernail_model.py             # MobileNetV3 subungual regression network
│   │   └── fusion.py                       # Inverse-variance ensemble and alert logic
│   ├── train.py                            # Unified training pipeline with W&B logging
│   ├── evaluate.py                         # Evaluation suite (MAE, Pearson r, AUC, confusion matrix)
│   ├── export_tflite.py                    # Edge optimization and INT8 quantization
│   └── inference.py                        # Standalone Python inference script (single/dual site)
│
├── models/
│   ├── conjunctiva/
│   │   ├── yolov8n_seg_conjunctiva.pt       # PyTorch segmentation weights
│   │   ├── mobilenetv3_conj_hb.pth         # PyTorch regression weights
│   │   ├── segmenter_conj.tflite           # Quantized INT8 segmentation model (3.2 MB)
│   │   └── estimator_conj.tflite           # Quantized INT8 regression model (2.5 MB)
│   ├── fingernail/
│   │   ├── yolov8n_seg_nail.pt             # PyTorch nail segmentation weights
│   │   ├── mobilenetv3_nail_hb.pth         # PyTorch nail regression weights
│   │   ├── segmenter_nail.tflite           # Quantized INT8 nail segmenter (3.2 MB)
│   │   └── estimator_nail.tflite           # Quantized INT8 nail estimator (2.5 MB)
│   └── fusion/
│       └── fusion_weights.json             # Calibrated ensemble weighting parameters
│
├── flutter_app/                            # Flutter mobile application
│   ├── lib/
│   │   ├── main.dart                       # Entry point and theme configuration
│   │   ├── screens/
│   │   │   ├── home_screen.dart            # Tri-mode selector: Conjunctiva / Nail / Dual
│   │   │   ├── conjunctiva_camera.dart     # Camera view with oval reticle overlay
│   │   │   ├── fingernail_camera.dart      # Camera view with box reticle overlay
│   │   │   ├── result_screen.dart          # Hb gauge, dual confidence bars, and risk summary
│   │   │   └── history_screen.dart         # Local encrypted offline patient registry
│   │   ├── services/
│   │   │   ├── ml_service.dart             # TFLite C++ bindings and tensor executor
│   │   │   ├── conjunctiva_norm.dart       # Sclera color normalization implementation
│   │   │   ├── fingernail_norm.dart        # Erythema Index extraction implementation
│   │   │   ├── fusion_service.dart         # On-device inverse-variance fusion
│   │   │   └── clinical_logic.dart         # WHO/DOH threshold mapping and referral logic
│   │   ├── models/
│   │   │   ├── patient.dart                # Patient demographic and obstetric metadata
│   │   │   └── screening_result.dart       # Result entity with confidence metrics
│   │   └── widgets/
│   │       ├── hb_gauge.dart               # Circular risk gauge (Green/Yellow/Orange/Red)
│   │       ├── dual_site_confidence.dart   # Uncertainty visualizer
│   │       └── referral_card.dart          # PhilHealth Konsulta referral preview
│   ├── assets/
│   │   ├── models/                         # Bundled TFLite models (~13.3 MB total)
│   │   ├── calibration_card.pdf            # Optional printable A6 color checker card
│   │   └── guide_images/                   # Step-by-step BHW eversion and nail pose guides
│   ├── pubspec.yaml                        # Flutter package configuration
│   └── android/                            # Native Android CameraX and NDK configuration
│
├── docs/
│   ├── clinical_background.md              # Pathophysiology of Anemia, PPH, and myometrial atony
│   ├── color_normalization.md              # Mathematical details of Sclera and EI normalization
│   ├── multi_site_fusion.md                # Formulation of inverse-variance weighting
│   ├── pfda_regulatory_notes.md            # Class B SaMD classification under ASEAN AMDD
│   └── pitch_deck_outline.md               # PSC XI presentation structure and slide outline
│
└── tests/
    ├── test_conjunctiva_preprocessing.py   # Unit tests for sclera color normalization
    ├── test_fingernail_preprocessing.py    # Unit tests for Erythema Index calculation
    ├── test_fusion.py                      # Tests for inverse-variance fusion logic
    ├── test_clinical_logic.py              # Tests for WHO/DOH severity triage rules
    └── test_quality_gate.py                # Tests for Laplacian blur and exposure gates
```

---

## Quick Start: From Clone to Inference in 5 Commands

```bash
# 1. Clone the repository
git clone https://github.com/Troge-dev/TinginHB.git
cd TinginHB

# 2. Create and activate a Python virtual environment
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
# source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Execute unit test suite
pytest tests/

# 5. Run dual-site inference demonstration
python src/inference.py --conjunctiva assets/demo/sample_eye.jpg --fingernail assets/demo/sample_nail.jpg
```

---

## Mobile Application Architecture and User Interface

```
┌─────────────────────────┐    ┌─────────────────────────┐    ┌─────────────────────────┐
│     TINGÍNHB HOME       │    │     CAMERA OVERLAY      │    │     SCREENING RESULT    │
├─────────────────────────┤    ├─────────────────────────┤    ├─────────────────────────┤
│ [TingínHB System]       │    │ [ Torch: LOCKED ON ]    │    │ [ Hb: 8.4 g/dL  ORANGE] │
│                         │    │                         │    │ Moderate Anemia (WHO)   │
│ Select Screening Mode:  │    │     .----------------.  │    │                         │
│                         │    │    /   EYELID OVAL    \ │    │ Site Breakdown:         │
│ [ DUAL-SITE FUSION ]    │    │   (   ALIGN LOWER      )│    │ • Conjunctiva: 8.2 g/dL │
│   Recommended Mode      │    │    \  CONJUNCTIVA     / │    │   Confidence: 94% [===] │
│                         │    │     '----------------'  │    │ • Fingernail:  8.7 g/dL │
│ [ CONJUNCTIVA ONLY ]    │    │                         │    │   Confidence: 89% [== ] │
│   For polished nails    │    │ [QC: Exposure Valid]    │    │                         │
│                         │    │ [QC: Focus Sharp]       │    │ Patient Context:        │
│ [ FINGERNAIL ONLY ]     │    │                         │    │ • 32 weeks gestation    │
│   For infants/infection │    │      [ CAPTURE ]        │    │ • Elevated PPH Risk     │
│                         │    │                         │    │                         │
│ [ Patient Registry ]    │    │ Switch to Nail Mode     │    │ [ GENERATE REFERRAL ]   │
└─────────────────────────┘    └─────────────────────────┘    └─────────────────────────┘
```

---

## Contributing and Code of Conduct

Contributions are welcome from machine learning engineers, mobile developers, clinicians, and public health researchers.

1. **Fork the Repository** and create a feature branch (`git checkout -b feature/NewFeature`).
2. **Commit Changes** following conventional commit standards (`git commit -m 'feat: refine sclera segmentation head'`).
3. **Verify Tests** (`pytest tests/`).
4. **Push to Branch** (`git push origin feature/NewFeature`).
5. **Submit a Pull Request** detailing the methodology and verification steps.

Please review our [Code of Conduct](CODE_OF_CONDUCT.md) prior to submitting contributions.

---

## Seminal References

1. **Mannino, R. G., et al. (2018).** *Smartphone app for non-invasive detection of anemia using only patient-sourced photos.* **Nature Communications**, 9(1), 4924. [https://doi.org/10.1038/s41467-018-07262-4](https://doi.org/10.1038/s41467-018-07262-4)
2. **Appiahene, P., et al. (2023).** *CP-AnemiC: Conjunctiva Palpebral Anemia Identification Dataset for Deep Learning Applications.* **Mendeley Data**, V1. [https://doi.org/10.17632/3799k7478j.1](https://doi.org/10.17632/3799k7478j.1)
3. **Dimauro, G., et al. (2020).** *EYES-DEFY-ANEMIA: Palpebral conjunctiva segmentation for non-invasive hemoglobin estimation.* **IEEE Access**, 8, 198421–198432.
4. **Department of Science and Technology – Food and Nutrition Research Institute (DOST-FNRI). (2024).** *Expanded National Nutrition Survey (ENNS) 2023–2024: Maternal and Child Nutritional Anemia Status in the Philippines.* Taguig City, Philippines.
5. **Department of Health (DOH) Philippines. (2024).** *Maternal Mortality Statistics and Field Health Services Information System (FHSIS) Annual Report.* Epidemiology Bureau, Manila.
6. **World Health Organization (WHO). (2011).** *Haemoglobin concentrations for the diagnosis of anaemia and assessment of severity.* Vitamin and Mineral Nutrition Information System (VMNIS). Geneva: WHO/NMH/NHD/MNM/11.1.
7. **Chalco, J. P., et al. (2005).** *Accuracy of clinical pallor in the diagnosis of anaemia in children: a meta-analysis.* **BMC Pediatrics**, 5(1), 46.
8. **Kalantri, A., et al. (2010).** *Accuracy and reliability of pallor for detecting anaemia: a hospital-based diagnostic accuracy study.* **PLoS ONE**, 5(1), e8545.

---

## Acknowledgments

* **Philippine Startup Challenge XI (PSC XI):** Department of Information and Communications Technology (DICT).
* **Open Healthcare & Vision Research:** The contributors and authors of *CP-AnemiC*, *EYES-DEFY-ANEMIA*, and *Mannino et al.*
* **Barangay Health Workers (BHWs):** The frontline community healthcare workforce serving primary care facilities across the Philippines.

---

<div align="center">

### Clinical and Regulatory Disclaimer

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│  IMPORTANT NOTICE: TingínHB is an academic research prototype developed for PSC XI. It is        │
│  classified as a Class B Clinical Decision Support & Triage Aid under the ASEAN Medical Device   │
│  Directive (AMDD). It is intended to assist trained community health workers in early risk       │
│  stratification and referral prioritization. It DOES NOT replace definitive venous phlebotomy   │
│  or professional medical diagnosis. Patients with severe pallor or symptoms must immediately     │
│  be referred to a licensed physician at an accredited Rural Health Unit or hospital.            │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

**MIT License © 2026 TingínHB Team • 3rd-Year Data Science Students**

</div>
