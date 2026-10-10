# TingínHB — Competitive Landscape & Market Benchmark

> **Document Type:** Strategic Market & Technical Benchmarking Report  
> **Project:** TingínHB — Non-Invasive Multi-Site Mobile Anemia Screening  
> **Target Event:** Philippine Startup Challenge XI (PSC XI)  
> **Last Updated:** October 2026  

---

## Executive Summary

Anemia affects over **1.62 billion people globally**, with severe health and economic burdens concentrated in developing nations. In the Philippines, the Department of Science and Technology – Food and Nutrition Research Institute (DOST-FNRI) reports high anemia prevalence among pregnant women (24.6%), infants (39.4%), and elderly populations.

Current standard-of-care screening relies almost exclusively on **invasive capillary blood sampling (e.g., HemoCue)** or centralized laboratory Complete Blood Counts (CBC). In resource-constrained and Geographically Isolated and Disadvantaged Areas (GIDA), these invasive methods fail due to recurring consumable costs (₱75–₱150 per microcuvette), needle phobia, biohazard disposal risks, and a chronic lack of trained phlebotomists.

While numerous digital health startups and academic teams have attempted camera-based non-invasive hemoglobin estimation over the past decade, nearly all have stalled or remained restricted to "wellness" categorization. **TinginHB overcomes the core technical pitfalls of prior solutions through dual-site cross-referenced anatomical fusion (conjunctiva + nail bed), dynamic self-referencing (sclera and periungual skin), and zero-cost, offline edge inference tailored for Southeast Asian skin phototypes (Fitzpatrick III–V).**

---

## 1. Head-to-Head Comparison Matrix

| Solution / Product | Organization & Origin | Modality & Approach | Hardware Needed | Unit / Test Cost | Regulatory Classification | Primary Bottleneck |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **Ruby** *(formerly AnemoCheck Mobile)* | **Sanguina** (Emory / Georgia Tech spinoff, USA) | Fingernail bed pallor | Smartphone camera only | Free / $3–$5/mo subscription | Wellness Tracker *(Not cleared as diagnostic)* | Requires lab blood test to personalize; fails under variable lighting & high melanin |
| **HemaChrome** *(mHematology)* | **Purdue University** (Young Kim Lab, USA) | Palpebral conjunctiva via super-resolution spectroscopy & radiomics | Smartphone camera only | Pre-commercial (Research) | Clinical Trials *(Kenya & Rwanda)* | Eye-only vulnerability to allergies, jaundice, and pediatric resistance to eyelid eversion |
| **Eyenaemia** | Seah & Tang (Australia / MS Imagine Cup Winner) | Conjunctiva with physical color calibration card | Smartphone + plastic card | Concept / Discontinued | Prototype Only *(Never deployed)* | Cumbersome physical card required next to eye; lighting shadows and card wear |
| **AnaeCare** | Univ. Nacional de San Martín (Peru) | Multimodal (palm video, fingertip video, nail photos) | Smartphone camera only | Academic research | Research Only *(Peru cohort)* | Heavy video processing; categorical classification only *(no continuous Hb g/dL)* |
| **Masimo Rad-67 / Pronto** | **Masimo Corp.** (USA) | Multi-wavelength pulse co-oximetry (SpHb) | Handheld console + finger sensor | **$2,500 – $5,000+** per device | **FDA 510(k) Cleared** *(Spot-check monitor)* | Prohibitive hardware cost; **not cleared for pregnant women or children**; perfusion-sensitive |
| **OrSense NBM-200** | **OrSense** (Israel / USA) | Occlusion spectroscopy (finger pneumatic ring sensor) | Tabletop console + sensor cuff | **$3,000+** per device | **FDA 510(k) Cleared** *(Blood banks)* | Bulky, 60s pneumatic cuff occlusion; designed for fixed blood banks, not mobile rural screening |
| **EzeCheck** | **EzeRx Health Tech** (India) | Spectroscopic optical fingertip sensor | Handheld IoT device | Device purchase + software fee | CE Mark / CDSCO *(India)* | Requires purchasing and maintaining proprietary physical readers; peripheral cold sensitivity |
| **ToucHb** | **Biosense Technologies** (India) | LED-photodiode transillumination finger probe | Handheld probe | ~$300 – $500 per device | Approved in India *(Early pioneer, 2012)* | Wide error margins in field trials (Bland-Altman limits of agreement ±2.5 g/dL) |
| **HemoCue Hb 301** *(The Incumbent)* | **Radiometer / HemoCue** (Sweden) | Invasive capillary blood finger-prick onto microcuvette | Tabletop reader + disposable cuvettes | **$1,200** reader + **₱75–₱150/cuvette** | **FDA Cleared / WHO Gold Standard** | Painful, biohazardous waste; recurring microcuvette consumable costs paralyze rural clinics |
| **TinginHB** | **TinginHB Team** (Philippines) | **Dual-Site Fusion: Eye (Conjunctiva) + Nail Bed** | **Commodity Android smartphone only** | **₱0.00 / test** | **Software Pre-Screening & Triage Tool** | Evaluates multi-site consistency; zero hardware; 100% offline on ₱5k phones |

---

## 2. In-Depth Competitor Analysis

### Category A: Software-Only Smartphone Applications (Direct Competitors)

#### 1. Ruby / AnemoCheck Mobile (Sanguina, USA)
* **Technology:** Computer vision segmentation of the thumb fingernail bed. Measures erythema and pallor to compute an "Iron Score" and estimate hemoglobin concentration.
* **Funding & Validation:** Spinoff from Emory University / Children's Healthcare of Atlanta. Backed by NIH grants and published in *Nature Communications* (Mannino et al., 2018).
* **Critical Limitations:**
  * **The "Personalization" Crutch:** Sanguina's accuracy claims rely on user personalization—the user must input a recent laboratory CBC result to calibrate the camera's baseline. Without this anchor, camera-to-camera sensor differences and ambient lighting variations cause wide prediction errors.
  * **Melanin Distortion:** Direct fingernail color analysis without self-referenced dermal contrast struggles on Fitzpatrick skin types IV–VI, where melanin in surrounding tissue confounds camera auto-exposure and white balance.
  * **Regulatory Wall:** Sanguina obtained FDA clearance *only* for their chemical capillary blood test kit (**AnemoCheck Home**). Their smartphone app is legally marketed only as a "wellness and tracking tool."

#### 2. HemaChrome (Purdue University, USA)
* **Technology:** Developed by Dr. Young Kim's laboratory. Originally transformed smartphone images of the palpebral conjunctiva into virtual hyperspectral bands using super-resolution mobile spectroscopy. In 2024–2025, shifted toward **grayscale radiomics and microvascular textural patterns** to sidestep color shifts under varied ambient lighting.
* **Clinical Trials:** Validated in collaboration with Moi Teaching and Referral Hospital in Kenya and the Rwanda Biomedical Center.
* **Critical Limitations:**
  * **Single-Site Vulnerability:** Conjunctival microvasculature is highly sensitive to non-anemic confounders: allergic conjunctivitis, environmental smoke irritation, dry eye, and subclinical jaundice (scleral icterus).
  * **Patient Hesitancy:** Requires pulling down the lower eyelid, which triggers patient anxiety, pediatric non-compliance, and infection transmission concerns in field environments.

#### 3. Eyenaemia (Australia)
* **Technology:** Analyzed conjunctival pallor using a smartphone camera. Required holding a standardized physical color-calibration card adjacent to the patient's eye to adjust for ambient illumination.
* **Traction & Fate:** Won the Microsoft Imagine Cup World Championship in 2014.
* **Why it Stalled:** Field operations demonstrated that relying on an external physical card was impractical: cards get lost, soiled, bent, or held at improper angles relative to incident sunlight, introducing significant measurement artifacts.

#### 4. AnaeCare (Universidad Nacional de San Martín, Peru)
* **Technology:** Multimodal dataset and machine learning pipeline (Valles-Coral et al., 2025) analyzing fingertip videos, palm opening/closing videos, and nail photographs across 909 subjects.
* **Critical Limitations:** Relies on video recordings, resulting in massive computational overhead (tens of thousands of frames per cohort). The system only classifies into broad ordinal categories (*Normal*, *Mild*, *Moderate*) rather than providing a continuous, actionable hemoglobin reading in g/dL.

---

### Category B: Dedicated Non-Invasive Hardware Devices (Indirect Competitors)

#### 1. Masimo Rad-67 & Pronto / Pronto-7 (USA)
* **Technology:** Pulse CO-Oximetry measuring total hemoglobin (SpHb) via multi-wavelength optical sensors clipped onto the finger.
* **Regulatory Status:** FDA 510(k) cleared as an adjunct spot-check monitor for adult patients.
* **Why it Failed to Replace Blood Tests:**
  * **Severe Demographic Exclusions:** The FDA clearance explicitly **excludes pregnant women and pediatric patients**, precisely the two most vulnerable target populations for community anemia screening.
  * **Perfusion Dependency:** In hypothermic patients, dehydrated individuals, or those with peripheral vasoconstriction, the optical signal deteriorates, leading to measurement failure or wide error margins.
  * **Prohibitive Capital Cost:** Units cost $2,500 to $5,000+, with proprietary sensors requiring periodic replacement. Equipping hundreds of Barangay Health Stations across a Philippine province is fiscally impossible for Local Government Units (LGUs).

#### 2. OrSense NBM-200 (Israel / USA)
* **Technology:** Occlusion spectroscopy utilizing a ring-shaped pneumatic finger sensor. The cuff inflates above systolic pressure to temporarily arrest capillary blood flow, creating a blood pool that is interrogated with multi-wavelength light.
* **Regulatory Status:** FDA 510(k) cleared specifically for non-invasive pre-donation hemoglobin screening in blood donor centers.
* **Limitations:** Bulky tabletop hardware ($3,000+); the 60-second pneumatic squeeze causes donor discomfort; strictly built for stationary clinical stations rather than mobile community health workers.

#### 3. EzeCheck (EzeRx Health Tech, India)
* **Technology:** Handheld, battery-powered optical biosensor that measures spectroscopic reflection from the fingertip in 60 seconds and syncs via Bluetooth to an Android app.
* **Traction:** Widely deployed in rural Indian health outreach programs (National Health Mission).
* **Limitations:** While significantly more affordable than Masimo, EzeCheck still requires manufacturing, procuring, and physically distributing proprietary hardware devices to rural health staff.

---

### Category C: Invasive Point-of-Care Standard (The Incumbent Baseline)

#### HemoCue Hb 201+ / Hb 301 (Radiometer / Sweden)
* **The Global Standard:** The World Health Organization (WHO) and Philippine Department of Health (DOH) standard for field hemoglobin testing. Capillary blood from a finger prick is drawn into a reagent-coated microcuvette and read spectrophotometrically in 15–60 seconds.
* **The "Consumables Trap":**
  * Capital cost: **$1,000 to $1,800** per device.
  * Recurring consumable cost: **₱75 to ₱150 per microcuvette ($1.00–$2.50)**.
  * **The Rural Health Reality in the Philippines:** Donated or LGU-purchased HemoCue machines frequently sit unused in Barangay Health Stations because local government health budgets run out of consumable microcuvette allocations.
  * Generates biohazardous sharps waste requiring dedicated biohazard disposal protocols that many remote rural barangays lack.

---

## 3. The 4 Engineering Traps That Stalled Prior Art

```
┌────────────────────────────────────────────────────────────────────────┐
│               THE 4 TRAPS OF NON-INVASIVE ANEMIA TECH                  │
├────────────────────────────────────────────────────────────────────────┤
│ 1. The Melanin Bias Trap:                                              │
│    Relying on fingernails alone causes darker skin types (Fitzpatrick  │
│    IV–VI) to absorb higher blue/green light, falsely mimicking pallor  │
│    unless mathematically normalized against surrounding tissue.        │
├────────────────────────────────────────────────────────────────────────┤
│ 2. The Ambient Lighting Trap:                                          │
│    A photo taken under fluorescent clinic bulbs vs. outdoor sunlight   │
│    shifts RGB channels by 30–50%. Without an anatomical reference      │
│    (like the adjacent white sclera), raw pixel color is useless.       │
├────────────────────────────────────────────────────────────────────────┤
│ 3. The Single-Site Failure Mode:                                       │
│    Eye-only fails during conjunctivitis or jaundice; nail-only fails   │
│    during cold vasoconstriction or nail trauma. Neither is robust.     │
├────────────────────────────────────────────────────────────────────────┤
│ 4. The Consumables Trap (HemoCue):                                     │
│    Rural clinics get donated readers, but run out of disposable        │
│    microcuvettes ($1–$2 each), leaving the device sitting in a drawer. │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 4. TingínHB’s Strategic Moat (PSC XI Value Proposition)

### 1. Dual-Site Cross-Referenced Fusion (Eye + Nail)
* **The Problem:** Single-site screening cannot distinguish systemic anemia from localized tissue anomalies.
* **The TinginHB Innovation:** Integrates **melanin-free palpebral conjunctiva** with **self-referenced fingernail bed colorimetry**.
* **Automated Discrepancy Gatekeeper:** If a patient has allergic conjunctivitis or cold extremities, TinginHB evaluates:
  $$|\hat{y}_{\text{conj}} - \hat{y}_{\text{nail}}| > \delta$$
  Anomalous sites are mathematically down-weighted via Bayesian inverse-variance fusion, or the health worker is alerted to re-inspect, preventing erroneous clinical triage.

### 2. Anatomical Self-Referencing (No Physical Calibration Cards)
* **Sclera-Referenced Normalization:** TinginHB uses the patient's own white sclera tissue adjacent to the palpebral conjunctiva as an internal white-balance anchor:
  $$k_c = \frac{255}{\text{mean}(M_{\text{sclera}, c})}, \quad I_{\text{norm}, c} = I_{\text{conj}, c} \cdot k_c$$
* **Differential Periungual Contrast:** The fingernail bed erythema index (EI) is divided by the surrounding periungual skin ring, normalizing out baseline melanin without requiring user personalization:
  $$\text{Contrast}_{\text{peri}} = \frac{\overline{R}_{\text{nail}} / \overline{G}_{\text{nail}}}{\overline{R}_{\text{peri}} / \overline{G}_{\text{peri}}}$$

### 3. Native Optimization for Southeast Asian Skin (Fitzpatrick III–V)
* Prior models trained on Caucasian cohorts suffer high false-positive rates when deployed on Filipino populations. TinginHB benchmarks against diverse intermediate-melanin datasets (AnaeCare Peru, Ghana cohorts, and local Philippine clinical validation).

### 4. Zero Peripheral Hardware & Zero Consumable Cost
* **Marginal screening cost:** **₱0.00**.
* Eliminates microcuvette supply-chain dependency and biohazard sharps disposal logistics for remote island municipalities.

### 5. 100% Offline Edge AI for Philippine GIDA Barangays
* Designed specifically for Geographically Isolated and Disadvantaged Areas (GIDA) with zero cellular reception.
* Entire pipeline (YOLOv8n-seg ROI segmentation + MobileNetV3 dual-branch regression) runs on-device via quantized TFLite models in **< 400 ms on entry-level ₱5,000 Android phones**.

### 6. Realistic Regulatory Positioning: Community Triage Filter
* TinginHB is pitched **not as an illegal direct replacement for venous laboratory CBC**, but as an **objective community pre-screening filter**.
* Enables Barangay Health Workers (BHWs) during routine house-to-house monitoring to flag high-risk individuals and refer them to Rural Health Units for confirmatory testing, optimizing LGU healthcare resource allocation.
