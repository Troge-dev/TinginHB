<div align="center">

# TingínHB

### *Non-Invasive, Zero-Consumable Smartphone Hemoglobin Screening for Maternal Health*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Early%20Development-orange.svg)]()

<br/>

> **"Tingin"** *(Tagalog: Look / See)* + **"HB"** *(Hemoglobin)*
> **"See Anemia Before It Kills."**

</div>

---

## What is TingínHB?

TingínHB is a smartphone-based, non-invasive hemoglobin screening tool designed to turn every Barangay Health Worker's phone camera into a zero-consumable anemia detector — directly preventing maternal death from postpartum hemorrhage.

The tool photographs the patient's everted lower eyelid (palpebral conjunctiva), segments the tissue using edge ML, normalizes colors against the sclera as a built-in white reference, and estimates hemoglobin concentration in under one second — all fully offline on an entry-level Android phone.

**Developed for the Philippine Startup Challenge XI (PSC XI) — Prototype-Ready Solution Track**
*By 3rd-Year Data Science Students*

---

## The Problem

### The Crisis

- The Philippines has a Maternal Mortality Ratio (MMR) of **119–144 per 100,000 live births** (SDG target: <70 by 2030).
- **Postpartum Hemorrhage (PPH)** is the #1 direct killer of Filipino mothers, accounting for 25–30% of all maternal deaths.
- **21.8%** of pregnant Filipino women are anemic (DOST-FNRI 2023–2024 Expanded National Nutrition Survey).
- Anemic mothers (Hb < 9 g/dL) face a **2.5×–4× higher risk** of fatal PPH due to uterine atony, depleted physiological reserve, and impaired coagulation.
- Approximately **2,000+ maternal deaths** occur annually in the Philippines; a substantial fraction are preventable through earlier anemia detection.

### The Diagnostic Gap

- Rural Barangay Health Stations (BHS) and Rural Health Units (RHUs) lack hemoglobin analyzers.
- HemoCue 301 devices cost **₱70,000–₱125,000** per unit plus **₱105–₱150** per disposable microcuvette test.
- Barangay Health Workers (BHWs) rely on subjective visual conjunctival pallor assessment, which has:
  - Sensitivity of only **10%–60%** for mild-to-moderate anemia
  - Inter-observer agreement (κ) of only **0.20–0.45** (Poor)
  - Misses **>50%** of anemic individuals in the critical Hb 9–11 g/dL intervention range

### Why the Palpebral Conjunctiva?

- The palpebral conjunctiva is a mucosal membrane with **zero melanin pigmentation** and very high microvascular density.
- This makes it the ideal optical site for hemoglobin estimation because skin tone (Fitzpatrick III–VI) does not confound the measurement.
- The adjacent sclera (white of the eye) serves as a natural, built-in white reference in every captured image, enabling illumination-invariant color normalization.

---

## Our Approach

A three-stage edge ML pipeline that runs entirely on-device:

1. **Image Acquisition & Quality Gate** — Real-time blur detection, exposure validation, and eyelid eversion verification to ensure capture quality before processing.
2. **ROI Segmentation & Color Normalization** — A lightweight segmentation model identifies the conjunctiva and sclera regions, then uses the sclera as an in-frame white reference to normalize colors across lighting conditions.
3. **Hemoglobin Estimation & Clinical Classification** — A dual-branch model combines colorimetric features with vascular texture analysis to produce both a continuous Hb estimate (g/dL) and a WHO severity classification (Normal / Mild / Moderate / Severe).

The system outputs a composite clinical risk score integrating Hb estimate, patient age, gestational week, and MUAC, along with an auto-generated PhilHealth Konsulta-compliant referral letter.

**Target specs:** ~7.7 MB total model size, <60 ms inference, zero consumables, 100% offline.

---

## Project Status

This repository is in **early development**. Core research, dataset preparation, and model architecture design are underway.

---

## License

This project is licensed under the [MIT License](LICENSE).

<br/>

<div align="center">
  <sub>TingínHB is a student research prototype created for PSC XI. It is designed as a triage and screening aid and does not substitute for definitive venous blood laboratory diagnosis.</sub>
</div>
