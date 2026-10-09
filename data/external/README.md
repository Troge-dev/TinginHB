# External & Supplementary Datasets (`data/external/`)

This directory houses third-party, publicly available benchmark datasets and reference code repositories collected to evaluate, cross-validate, and calibrate TinginHB's multi-site non-invasive anemia screening pipeline.

> **Git Tracking Policy:**  
> All binary assets, raw image files, `.rar`, and `.zip` archives inside `data/external/` are strictly ignored by `.gitignore` to prevent repository bloat. Only this documentation is tracked.

---

## Catalog & Directory Structure

```text
data/external/
├── cp-anemic/
│   ├── Anemic/                           # 355 Conjunctival pallor images (anemic class)
│   ├── Non-anemic/                       # 355 Conjunctival pallor images (non-anemic class)
│   ├── Anemia_Data_Collection_Sheet.xlsx # Complete clinical sheet: exact Hb levels (g/dL), age, gender, hospital
│   └── CP-AnemiC_dataset.rar            # Original raw archive (~8.28 MB)
│
├── ghana-fingernails/
│   ├── Fingernails/                      # 4,260 Fingernail photos categorized by patient ID and anemia status
│   └── Fingernails.rar                   # Original raw archive (~27.45 MB)
│
├── ghana-palms/
│   ├── Palm/                             # 4,260 Palmar pallor photos categorized by patient ID and anemia status
│   └── Palm.rar                          # Original raw archive (~252.57 MB)
│
├── unas-palmas-yemas/
│   └── palmas_frames/                    # 1,020 Palm video frame extractions (224x224) from Peru AnaeCare cohort
│       └── palmas_frames/
│           ├── Leve/                     # Mild anemia cohort (Hb 11.0–11.9 g/dL)
│           ├── Moderada/                 # Moderate anemia cohort (Hb 8.0–10.9 g/dL)
│           └── Normal/                   # Non-anemic reference cohort (Hb >= 12.0 g/dL)
│
└── hemolens/                             # Cloned reference repository (yelabb/hemolens)
    ├── model/                            # MobileNetV2 / ResNet fingernail feature extractor
    ├── segmentation/                     # Fingernail boundary & ROI detection masks
    └── README.md                         # Pipeline documentation
```

---

## Detailed Dataset Profiles

### 1. CP-AnemiC (Conjunctival Pallor Dataset)
- **Source:** Mendeley Data (DOI: [`10.17632/m53vz6b7fx.1`](https://doi.org/10.17632/m53vz6b7fx.1))
- **Cohort:** 710 pediatric subjects (6–59 months) presenting to healthcare facilities across Ghana.
- **Modality:** Smartphone/tablet (Samsung Galaxy Tab 7A) palpebral conjunctiva captures.
- **Labels:** Continuous blood laboratory hemoglobin measurements (`HB_LEVEL` in g/dL), WHO severity classes (Normal, Mild, Moderate, Severe), demographic metadata (Age in months, Gender, Hospital, Region).
- **Primary Value for TinginHB:** Enables direct training and quantitative regression validation against continuous ground-truth Hb levels on smartphone conjunctival imagery.

### 2. Ghana Fingernails Dataset
- **Source:** Mendeley Data (DOI: [`10.17632/2xx4j3kjg2.1`](https://doi.org/10.17632/2xx4j3kjg2.1))
- **Authors:** Appiahene et al. (*Detection of Anemia using Colour of the Fingernails*)
- **Cohort:** Multi-subject clinical fingernail captures across anemic and non-anemic patients.
- **Modality:** 4,260 high-resolution smartphone fingernail photographs with natural indoor lighting and varying skin melanin tones.
- **Primary Value for TinginHB:** Large-scale fingernail bed colorimetry benchmark; ideal for evaluating periungual erythema index (EI) and contrast normalization across Fitzpatrick skin types IV–VI.

### 3. Ghana Palm Dataset
- **Source:** Mendeley Data (DOI: [`10.17632/ccr8cm22vz.1`](https://doi.org/10.17632/ccr8cm22vz.1))
- **Authors:** Appiahene et al. (*Anemia Detection using Palpable Palm*)
- **Cohort:** Multi-subject palmar erythema and palmar pallor clinical cohort.
- **Modality:** 4,260 palmar crease and palm bed photographs.
- **Primary Value for TinginHB:** Provides secondary multi-site palmar tissue validation data for cross-verifying palmar pallor against fingernail and conjunctival indices.

### 4. AnaeCare Peru Multimodal Dataset (`unas-palmas-yemas`)
- **Source:** Kaggle (`shimu080/unas-palmas-yemas`), based on Valles-Coral et al., 2025 (DOI: [`10.51252/rcsi.v5i2.955`](https://doi.org/10.51252/rcsi.v5i2.955))
- **Cohort:** 909 young adult subjects (18–25 years) at Universidad Nacional de San Martín Medical Center, Peru (Fitzpatrick skin types III–IV).
- **Modality:** 1,020 uniformly sampled, normalized (224×224) frames categorized into Mild (`Leve`), Moderate (`Moderada`), and Normal (`Normal`).
- **Primary Value for TinginHB:** High relevance to Southeast Asian Fitzpatrick phototypes (III–IV intermediate melanin), providing cross-ethnicity generalization tests.

### 5. HemoLens Reference Repository
- **Source:** GitHub (`yelabb/hemolens`)
- **Pipeline:** Mobile-optimized fingernail bed detection, color space transformation (HSV / Lab), and pallor quantification.
- **Primary Value for TinginHB:** Baseline architecture comparison for mobile fingernail ROI localization and on-device latency benchmarking.
