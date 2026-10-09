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
*By **Team DataLunas** — Department of Data Science, College of Information Technology and Computing, University of Science and Technology of Southern Philippines (USTP)*

</div>

---

## Executive Summary

**TingínHB** is a non-invasive edge-AI anemia screening and triage application designed for frontline Philippine community health workers. Rather than attempting to replace hospital venous phlebotomy, TingínHB functions as a **first-line clinical filter and risk-stratification aid**. It digitizes and standardizes the subjective visual pallor examination of an experienced physician by evaluating two complementary microvascular sites: the **palpebral conjunctiva** (inner lower eyelid, primary site) and the **fingernail bed** (pediatric and clinical fallback).

Operating 100% on-device in under **2 seconds** on an entry-level **PHP 5,000 Android smartphone**, TingínHB requires **PHP 0 per test** (zero chemical reagents, zero disposable microcuvettes, zero biohazard sharps waste). It stratifies patients into actionable WHO risk tiers, flagging mothers and infants at high risk of fatal postpartum hemorrhage (PPH) or neurodevelopmental delay before clinical crises emerge.

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                   THE REPOSITIONED VALUE PILLARS                                 │
├───────────────────────┬────────────────────────┬────────────────────────┬────────────────────────┤
│   ZERO CONSUMABLES    │ OPERATIONAL HIERARCHY  │   100% OFFLINE EDGE    │ POLICY & GRANT ALIGNED │
│   PHP 0/test vs       │ Primary: Conjunctiva   │   13.5 MB total models │ RA 11148 First 1,000   │
│   PHP 150 for HemoCue │ Fallback: Fingernail   │   <60ms on low-end SoC │ Days, PhilHealth       │
│   Preserves RHU strips│ Multi-site consistency │   Zero cloud/data sync │ Konsulta, & NGO Grants │
└───────────────────────┴────────────────────────┴────────────────────────┴────────────────────────┘
```

---

## Competition Deliverables & Repository Map

| Deliverable | Format | File / Link | Description |
| :--- | :---: | :--- | :--- |
| **Official Concept Note** | DOCX | [`DataLunas_Concept Note_PSCXI.docx`](./DataLunas_Concept%20Note_PSCXI.docx) | Fully elaborated proposal strictly formatted to DICT PSC XI requirements (99 paragraphs, 4 tables, entrepreneurial tone). |
| **Pitch Deck (16:9 PDF)** | PDF | [`DataLunas_PitchDeck_PSCXI.pdf`](./DataLunas_PitchDeck_PSCXI.pdf) | Clean Light Mode 10-slide keynote export in 16:9 widescreen (`1152 x 648 pt`). Plain solid backgrounds, crisp vector typography. |
| **Interactive Keynote Deck** | HTML | [`DataLunas_PitchDeck_PSCXI.html`](./DataLunas_PitchDeck_PSCXI.html) | Standalone browser keynote with edge drawers, theme toggle (<kbd>T</kbd>), fullscreen presentation (<kbd>F</kbd>), and print support. |
| **Canva Pitch Deck (10 Slides)** | Cloud | [Open Full Deck in Canva](https://canva.link/8och5btu1zgpc6a) | Native Canva pitch deck in Light Mode with plain solid white backgrounds and high-contrast clinical styling. |
| **Canva Engineering Core Slide** | Cloud | [Open Slide 6 in Canva](https://canva.link/1ldt8owl4mddkdz) | Standalone modular slide for the Six Core Engineering Features & System Architecture. |
| **Canva Blueprint Outline** | TXT | [`docs/canva_pitch_deck_outline.txt`](./docs/canva_pitch_deck_outline.txt) | Complete text, sizing, and color token blueprint for Canva slide generation. |
| **Dataset Clinical Audit Report** | HTML | [`docs/dataset_descriptive_analysis_report.html`](./docs/dataset_descriptive_analysis_report.html) | Comprehensive statistical and forensic audit of Kaggle and Mendeley clinical datasets. |
| **Mentor Request Email Draft** | TXT | [`docs/mentor_request_email.txt`](./docs/mentor_request_email.txt) | Formal correspondence to USTP Department Head requesting a dedicated PSC XI faculty mentor. |

---

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

1. **Mode 1: Conjunctiva Primary (Standard Protocol)**  
   *Operational Trigger:* Patient everts lower eyelid; fingernails obstructed by cosmetics, artificial nails, dirt, or cold peripheral vasoconstriction.  
   *Methodology:* YOLOv8n-seg isolates conjunctival tissue and sclera; sclera normalization standardizes illumination channels; dual-branch MobileNetV3 extracts colorimetric and deep features.  
   *Target Clinical Benchmark:* $\text{Sensitivity} \ge 90\%$ for detecting Moderate/Severe Anemia ($\text{Hb} < 9.0\text{ g/dL}$), $\text{AUC} \ge 0.88$, $\text{MAE} \approx 1.0\text{--}1.2\text{ g/dL}$.

2. **Mode 2: Fingernail Fallback (Pediatric & Infection Protocol)**  
   *Operational Trigger:* Eyelid eversion impractical (uncooperative infants, active conjunctivitis, cataracts, or eye trauma).  
   *Methodology:* YOLOv8n-seg segments subungual nail bed; computes differential Erythema Index ($\Delta \text{EI} = \text{EI}_{\text{nail}} - \text{EI}_{\text{skin}}$) to suppress periungual skin melanin bias; MobileNetV3 performs risk grading.  
   *Target Clinical Benchmark:* Triage Screening Sensitivity $\ge 82\%$, $\text{AUC} \ge 0.80$.

3. **Mode 3: Dual-Site Verification (Consistency Check)**  
   *Operational Trigger:* Both conjunctiva and fingernail captures pass optical quality verification during standard prenatal visits.  
   *Methodology:* Acts as a mutual consistency check ($|\Delta_{\text{diff}}| > 2.0\text{ g/dL}$ flags anomaly/rescreening requirement); inverse-variance weighted risk tier consensus.  
   *Target Clinical Benchmark:* Clinical Rule-Out Sensitivity $\ge 92\%$, Specificity $\ge 85\%$.

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

## Repository Structure & Project Organization

### Current Active Repository Tree (PSC XI Deliverables Phase)

```
TinginHB/
├── DataLunas_Concept Note_PSCXI.docx      # Official DICT PSC XI Concept Note (Complete narrative, 4 tables)
├── DataLunas_PitchDeck_PSCXI.pdf          # 16:9 Keynote Pitch Deck (High-resolution print export, 10 slides)
├── DataLunas_PitchDeck_PSCXI.html         # Interactive 16:9 Pitch Deck (Web keynote with drawer & theme toggle)
├── README.md                              # Comprehensive clinical, technical, and commercial specification
├── LICENSE                                # MIT License (Team DataLunas, USTP 2026)
├── .gitignore                             # Git exclusion rules (raw image binaries, lockfiles)
│
├── .agents/                               # Antigravity developer & presentation agent configurations
│   └── skills/
│       └── presentation-deck-design/      # Specialized skill for 16:9 pitch decks & Canva design
│           ├── SKILL.md                   # Visual design rules, typography scale, color tokens
│           └── references/
│               └── design_tokens.md       # Dark & Light mode color definitions
│
├── data/                                  # Clinical datasets and imagery protocols
│   ├── DATASETS.md                        # Dataset provenance, download links, and ethical licensing
│   ├── raw/                               # Downloaded clinical imagery (CP-AnemiC, EYES-DEFY; gitignored)
│   ├── processed/                         # Standardized ROI masks and metadata
│   ├── augmented/                         # Synthetic multi-condition color-calibrated augmentations
│   └── validation_ph/                     # Philippine cohort clinical validation metadata
│
└── docs/                                  # Supporting blueprints, audits, and formal correspondence
    ├── canva_pitch_deck_outline.txt       # Light-mode Canva design blueprint and typography spec
    ├── dataset_descriptive_analysis_report.html # Statistical demographic & diagnostic audit report
    └── mentor_request_email.txt           # Formal faculty mentor endorsement request letter
```

### Planned Technical Architecture (Phases 2 & 3 Deployment)

For the subsequent edge-AI engineering, clinical model training, and Flutter cross-platform deployment, the codebase expands into the following modular packages:

```
tinginhb/
├── notebooks/                             # Research and exploratory analysis notebooks
│   ├── 01_data_exploration.ipynb          # Exploratory data analysis and color metrics
│   ├── 02_conjunctiva_pipeline.ipynb      # Sclera normalization and dual-branch training
│   ├── 03_fingernail_pipeline.ipynb       # Erythema Index extraction and regression
│   ├── 04_fusion_model.ipynb              # Inverse-variance weighting and discrepancy logic
│   ├── 05_quantization_export.ipynb       # PyTorch to ONNX to TFLite INT8 quantization
│   └── 06_evaluation_metrics.ipynb        # MAE, ROC-AUC, and Bland-Altman analysis
│
├── src/                                   # Core Python machine learning pipelines
│   ├── dataset.py                         # PyTorch Dataset and DataLoader implementations
│   ├── preprocessing/                     # Sclera-referenced normalization, CIELAB, EI, quality gates
│   ├── models/                            # MobileNetV3 dual-branch, fingernail regression, fusion
│   ├── train.py                           # Unified training pipeline with W&B logging
│   ├── evaluate.py                        # Evaluation suite (MAE, Pearson r, AUC, confusion matrix)
│   ├── export_tflite.py                   # Edge optimization and INT8 quantization
│   └── inference.py                       # Standalone Python inference script (single/dual site)
│
├── models/                                # Serialized PyTorch and quantized TFLite models
│   ├── conjunctiva/                       # YOLOv8n-seg and MobileNetV3 conjunctiva models
│   ├── fingernail/                        # YOLOv8n-seg and MobileNetV3 fingernail models
│   └── fusion/                            # Calibrated ensemble weighting parameters
│
├── flutter_app/                           # Flutter mobile application (100% offline edge)
│   ├── lib/                               # Screens, camera overlays, TFLite services, clinical logic
│   └── assets/                            # Bundled TFLite models (~13.3 MB total) & BHW guide assets
│
└── tests/                                 # Unit, integration, and clinical rule verification suites
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

## Contributing & Community Guidelines

Contributions are welcome from machine learning engineers, mobile developers, clinicians, and public health researchers passionate about maternal healthcare equity.

1. **Fork the Repository** and create a feature branch (`git checkout -b feature/NewFeature`).
2. **Commit Changes** following conventional commit standards (`git commit -m 'feat: refine sclera segmentation head'`).
3. **Verify Integrity** with appropriate test suites and documentation.
4. **Push to Branch** (`git push origin feature/NewFeature`).
5. **Submit a Pull Request** detailing clinical methodology and verification steps.

### Code of Conduct

As an initiative rooted in clinical AI, maternal health equity, and open scientific inquiry, all contributors, researchers, and community members are expected to:
* **Uphold Clinical & Ethical Integrity:** Ensure algorithms, datasets, and claims strictly adhere to patient privacy, fairness across diverse demographic cohorts, and responsible medical AI standards.
* **Practice Inclusive & Respectful Collaboration:** Maintain a welcoming, harassment-free environment for collaborators of all backgrounds and skill levels.
* **Transparency & Reproducibility:** Document all data transformations, hyperparameter choices, and statistical evaluations honestly and rigorously.

---

## Team DataLunas & Innovator Attribution

**TingínHB** is developed by **Team DataLunas**, an undergraduate data science research and startup initiative from the **University of Science and Technology of Southern Philippines (USTP)**, Cagayan de Oro City:

* **Rogelio Q. Mandamian III** — *Team Lead / Machine Learning & Systems Architecture*  
  Department of Data Science, College of Information Technology and Computing (CITC)  
  *Focus:* Multi-site computer vision pipelines, on-device edge quantization, and clinical decision support systems.
* **Kirsten Roise Moog** — *Co-Lead / Clinical Research & Healthcare Product Development*  
  Department of Data Science, College of Information Technology and Computing (CITC)  
  *Focus:* Epidemiological data auditing, maternal health workflow integration, and regulatory compliance.
* **Academic & Clinical Mentorship** — *Department of Data Science, CITC, USTP*  
  Faculty guidance, clinical validation network liaisons, and startup incubation support.

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

**MIT License © 2026 Team DataLunas • Department of Data Science, USTP**

</div>
