# TingínHB — Dataset Inventory

> **Last updated:** 2026-08-29  
> **Downloaded via:** Kaggle MCP + `python -m kaggle` CLI  
> **Total datasets:** 7 downloaded (Kaggle) + 3 external (Mendeley / Roboflow)

---

## Directory Structure

```
data/
├── raw/
│   ├── conjunctiva/                    # Palpebral conjunctiva (eye) datasets
│   │   ├── eyes-defy-anemia/           # ★ PRIMARY — EYES-DEFY-ANEMIA (Dimauro et al.)
│   │   ├── eye-conjunctiva/            # Conjunctiva classification images
│   │   ├── anemia-eye-pixel-dataset/   # RGB pixel values + Hb from eye images
│   │   └── anemia-detection-dataset/   # Pixel values + hemoglobin CSV
│   └── fingernail/                     # Subungual nail bed datasets
│       ├── fingernail-anemia-classified/  # ★ PRIMARY — Classified anemia/non-anemic nail images
│       ├── fingernail-anemia-ghana/       # Ghana cohort fingernail images
│       └── anemia-fingernail-ayush/       # Anemic vs Non-Anemic nail classification
├── processed/                          # (empty — for unified COCO/JSON annotations after preprocessing)
├── augmented/                          # (empty — for Albumentations-generated synthetic augmentations)
└── validation_ph/                      # (empty — reserved for Philippine clinical validation cohort)
```

---

## Conjunctiva Datasets (Primary Site)

### 1. EYES-DEFY-ANEMIA ★ PRIMARY

| Field | Details |
|:---|:---|
| **Kaggle Ref** | `harshwardhanfartale/eyes-defy-anemia` |
| **URL** | https://www.kaggle.com/datasets/harshwardhanfartale/eyes-defy-anemia |
| **Local Path** | `data/raw/conjunctiva/eyes-defy-anemia/` |
| **Size on Disk** | ~652.55 MB |
| **Files** | 865 files (images + documentation) |
| **License** | CC BY-SA 4.0 |
| **Description** | Eye conjunctiva photos from **Indian and Italian** patient cohorts (218 subjects total). Contains raw eye images plus pixel-level segmentation masks for forniceal, palpebral, and forniceal+palpebral conjunctiva regions. Each patient folder includes the original image and pre-segmented PNG masks. Paired with lab CBC hemoglobin ground truth. |
| **Structure** | `dataset anemia/India/{patient_id}/` and `dataset anemia/Italy/{patient_id}/` — each contains raw `.jpg` + `_forniceal.png`, `_palpebral.png`, and `_forniceal_palpebral.png` segmentation masks |
| **Use Case** | **Core training data** for the conjunctiva segmentation (YOLOv8n-seg) and hemoglobin regression (MobileNetV3 dual-branch) models. Pixel-level masks enable direct supervised segmentation training. The multi-cohort origin (India + Italy) provides skin tone diversity. |
| **Maps to README** | *"EYES-DEFY-ANEMIA (Dimauro et al.) — 218 subjects (Italian & Indian cohorts), pixel-level masks, lab CBC Hb"* |

---

### 2. Eye-Conjunctiva Classification

| Field | Details |
|:---|:---|
| **Kaggle Ref** | `nadiwidi/eyeconjunctiva` |
| **URL** | https://www.kaggle.com/datasets/nadiwidi/eyeconjunctiva |
| **Local Path** | `data/raw/conjunctiva/eye-conjunctiva/` |
| **Size on Disk** | ~2.08 MB |
| **Files** | 218 images |
| **License** | Unknown |
| **Description** | Resized conjunctiva images classified into Anemia vs. Normal categories. Pre-cropped to the conjunctival region. Lightweight dataset ideal for quick prototyping and classification model sanity checks. |
| **Structure** | `Resized Anemia/anemia{NNNN}.jpg` and `Resized Normal/normal{NNNN}.jpg` |
| **Use Case** | Supplementary classification data for training the quality gate MobileNetV2-QC eversion classifier (Pass/Fail). Can also augment conjunctiva training by providing additional cropped conjunctiva samples. |

---

### 3. Anemia Eye Pixel Dataset (RGB + Hb CSV)

| Field | Details |
|:---|:---|
| **Kaggle Ref** | `nahiyan1402/anemiadataset` |
| **URL** | https://www.kaggle.com/datasets/nahiyan1402/anemiadataset |
| **Local Path** | `data/raw/conjunctiva/anemia-eye-pixel-dataset/` |
| **Size on Disk** | ~4.4 KB (CSV) |
| **Files** | 1 file (`Anemia_Dataset.csv`) |
| **License** | Unknown |
| **Description** | Tabular dataset containing **Red, Green, and Blue pixel percentage values** extracted from eye conjunctiva images, paired with anemia labels. This provides pre-extracted color features from 218+ eye images with clinical labels. |
| **Structure** | Single CSV with columns for R%, G%, B% pixel distributions and anemia class |
| **Use Case** | Useful for the **16-D radiomic/colorimetric feature vector** branch of the dual-branch MobileNetV3 conjunctiva estimator. Provides ground truth for training color-metric-based regression baselines (Erythema Index, CIELAB color features). |
| **Maps to README** | *"Detecting Anaemia using CV (alexandershan / Kaggle) — Conjunctival captures with clinical labels and color metric vectors"* — This is a matching/related dataset. |

---

### 4. Anemia Detection Dataset (Pixel Values + Hemoglobin)

| Field | Details |
|:---|:---|
| **Kaggle Ref** | `shahriar26s/anemia-detection-dataset` |
| **URL** | https://www.kaggle.com/datasets/shahriar26s/anemia-detection-dataset |
| **Local Path** | `data/raw/conjunctiva/anemia-detection-dataset/` |
| **Size on Disk** | ~5.3 KB (CSV) |
| **Files** | 1 file (`anemia_dataset.csv`) |
| **License** | Apache 2.0 |
| **Description** | Tabular dataset with image pixel values (R, G, B percentages) paired with **hemoglobin level measurements** (continuous g/dL values) and binary anemia labels. Higher usability rating (1.0) and 2,202 downloads indicate well-structured data. |
| **Structure** | Single CSV with pixel color features and Hb ground truth |
| **Use Case** | Ideal for **regression baseline training** — predicting continuous hemoglobin g/dL from color features. Directly supports the colorimetric feature vector input of the conjunctiva estimator pipeline. Can be used to validate the Erythema Index ($\text{EI} = \ln(R) - \ln(G)$) relationship with Hb. |

---

## Fingernail Datasets (Complementary Fallback Site)

### 5. Fingernail Anemia — Classified Images ★ PRIMARY

| Field | Details |
|:---|:---|
| **Kaggle Ref** | `abhinavgolla/fingernail-anemia-22ndmay` |
| **URL** | https://www.kaggle.com/datasets/abhinavgolla/fingernail-anemia-22ndmay |
| **Local Path** | `data/raw/fingernail/fingernail-anemia-classified/` |
| **Size on Disk** | ~25.68 MB |
| **Files** | 4,260 PNG images |
| **License** | Other (specified in description) |
| **Description** | Standardized fingernail bed images classified with anemia tiers. Contains labeled nail images (`Anemic-FN-{ID}` naming convention) for supervised classification. The large sample count (4,260) makes it the most comprehensive fingernail dataset in our collection. |
| **Structure** | `Fingernails/Anemic-FN-{ID} ({augmentation_idx}).png` |
| **Use Case** | **Core training data** for the fingernail segmentation (YOLOv8n-seg) and hemoglobin regression (MobileNetV3-Small) models. Can be used to train the Erythema Index and periungual contrast ratio extraction pipeline. |
| **Maps to README** | *"Fingernail Anemia Dataset (Kaggle Community Open Data) — Standardized subungual nail bed image sets with categorized anemia tiers"* |

---

### 6. Fingernail Anemia — Ghana Cohort

| Field | Details |
|:---|:---|
| **Kaggle Ref** | `kritagyadev/anemia-using-fingernails-image-datasets-from-ghana` |
| **URL** | https://www.kaggle.com/datasets/kritagyadev/anemia-using-fingernails-image-datasets-from-ghana |
| **Local Path** | `data/raw/fingernail/fingernail-anemia-ghana/` |
| **Size on Disk** | ~25.68 MB |
| **Files** | 4,260 PNG images |
| **License** | Unknown |
| **Description** | Fingernail images from a **Ghanaian clinical cohort** with anemia classification labels. Provides diversity in skin pigmentation (Fitzpatrick V–VI), which is critical for model robustness across melanin-rich populations relevant to the Philippine context (Fitzpatrick III–V). |
| **Structure** | `Fingernails/Anemic-FN-{ID} ({augmentation_idx}).png` |
| **Use Case** | Supplements the primary fingernail dataset with **darker skin tone representation**. Essential for validating that the Erythema Index extraction and periungual normalization remain robust across melanin-diverse nail beds. |

---

### 7. Anemia Fingernail (Ayush — Binary Classification)

| Field | Details |
|:---|:---|
| **Kaggle Ref** | `ayushcl/anemia-fingernail` |
| **URL** | https://www.kaggle.com/datasets/ayushcl/anemia-fingernail |
| **Local Path** | `data/raw/fingernail/anemia-fingernail-ayush/` |
| **Size on Disk** | ~10.42 MB |
| **Files** | 1,777 images (90 Anemic + 1,687 Non-Anemic) |
| **License** | Apache 2.0 |
| **Description** | Binary classification fingernail dataset with a clear Anemic vs. Non-Anemic split. The heavy class imbalance (90 anemic vs 1,687 non-anemic) mirrors real-world prevalence and is useful for testing model sensitivity at low positive rates. |
| **Structure** | `Finger_Nails/Anemic/` and `Finger_Nails/Non-Anemic/` |
| **Use Case** | Useful for **classification threshold calibration** and testing the clinical sensitivity/specificity trade-off. The class imbalance is representative of community screening settings where anemia prevalence is 15–25%. |

---

## External Datasets (Not on Kaggle — Requires Separate Download)

> [!IMPORTANT]
> The following datasets referenced in the README are hosted on **Mendeley Data** and **Roboflow Universe**, not Kaggle. They need to be downloaded manually and placed into the corresponding directories.

### 8. CP-AnemiC Dataset (Mendeley Data)

| Field | Details |
|:---|:---|
| **Source** | Mendeley Data (Appiahene et al., 2023) |
| **DOI** | https://doi.org/10.17632/3799k7478j.1 |
| **Target Path** | `data/raw/conjunctiva/cp-anemic/` |
| **Description** | 710 pediatric subjects from Ghana with paired HemoCue Hb ground truth measurements. Contains palpebral conjunctiva images from a controlled clinical protocol. **Most critical benchmark dataset** referenced in the README for conjunctiva model validation. |
| **Status** | ⬜ **NOT YET DOWNLOADED** — Requires manual download from Mendeley Data |

### 9. Anemia Object Detection Dataset (Roboflow Universe)

| Field | Details |
|:---|:---|
| **Source** | Roboflow Universe |
| **Target Path** | `data/raw/conjunctiva/roboflow-anemia-detection/` |
| **Description** | Annotated palpebral conjunctiva and sclera bounding polygons for object detection. Pre-labeled with segmentation masks for direct YOLOv8 training. |
| **Status** | ⬜ **NOT YET DOWNLOADED** — Requires Roboflow account and API key |

### 10. Nail ROI & Disease Segmentation Dataset (Roboflow Universe)

| Field | Details |
|:---|:---|
| **Source** | Roboflow Universe |
| **Target Path** | `data/raw/fingernail/roboflow-nail-segmentation/` |
| **Description** | Polygon annotations for nail plate and periungual skin isolation. Designed for training segmentation models to isolate the subungual nail bed ROI from surrounding skin. |
| **Status** | ⬜ **NOT YET DOWNLOADED** — Requires Roboflow account and API key |

---

## Dataset Summary Table

| # | Dataset | Site | Source | Files | Size | Hb Ground Truth | Status |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | EYES-DEFY-ANEMIA | Conjunctiva | Kaggle | 865 | 652 MB | ✅ Lab CBC | ✅ Downloaded |
| 2 | Eye-Conjunctiva | Conjunctiva | Kaggle | 218 | 2 MB | ❌ Labels only | ✅ Downloaded |
| 3 | Anemia Eye Pixel (CSV) | Conjunctiva | Kaggle | 1 | 4 KB | ❌ Derived features | ✅ Downloaded |
| 4 | Anemia Detection (CSV) | Conjunctiva | Kaggle | 1 | 5 KB | ✅ Hb g/dL | ✅ Downloaded |
| 5 | Fingernail Anemia Classified | Fingernail | Kaggle | 4,260 | 26 MB | ❌ Tier labels | ✅ Downloaded |
| 6 | Fingernail Ghana Cohort | Fingernail | Kaggle | 4,260 | 26 MB | ❌ Tier labels | ✅ Downloaded |
| 7 | Anemia Fingernail (Binary) | Fingernail | Kaggle | 1,777 | 10 MB | ❌ Binary label | ✅ Downloaded |
| 8 | CP-AnemiC | Conjunctiva | Mendeley | ~710 | ~TBD | ✅ HemoCue Hb | ⬜ Manual DL needed |
| 9 | Roboflow Anemia Detection | Conjunctiva | Roboflow | ~TBD | ~TBD | ❌ Polygon masks | ⬜ Manual DL needed |
| 10 | Roboflow Nail Segmentation | Fingernail | Roboflow | ~TBD | ~TBD | ❌ Polygon masks | ⬜ Manual DL needed |

---

## Pipeline Mapping

```
Dataset → Model Pipeline Mapping:
═══════════════════════════════════════════════════════════════════

CONJUNCTIVA PIPELINE:
  EYES-DEFY-ANEMIA (865 files) ─────────┐
  Eye-Conjunctiva (218 images) ──────────┤
  CP-AnemiC [PENDING] (710 subjects) ────┼──→ YOLOv8n-seg Conjunctiva Segmenter
  Roboflow Anemia [PENDING] ─────────────┘       │
                                                  ▼
  Anemia Eye Pixel CSV (RGB features) ───┐  MobileNetV3-Small Dual-Branch
  Anemia Detection CSV (Hb g/dL) ────────┤  (Branch A: CNN 224×224 + Branch B: 16-D Radiomics)
  EYES-DEFY-ANEMIA (segmented ROIs) ─────┘       │
                                                  ▼
                                            ŷ_conj ± σ_conj

FINGERNAIL PIPELINE:
  Fingernail Classified (4,260 imgs) ────┐
  Fingernail Ghana (4,260 imgs) ─────────┤
  Anemia Fingernail Ayush (1,777 imgs) ──┼──→ YOLOv8n-seg Fingernail Segmenter
  Roboflow Nail Seg [PENDING] ───────────┘       │
                                                  ▼
                                            MobileNetV3-Small Regression
                                                  │
                                                  ▼
                                            ŷ_nail ± σ_nail

FUSION:
  ŷ_conj ± σ_conj ──┐
                     ├──→ Inverse-Variance Weighted Fusion ──→ ŷ_fused
  ŷ_nail ± σ_nail ──┘
```

---

## Next Steps

1. **Download CP-AnemiC** from [Mendeley Data](https://doi.org/10.17632/3799k7478j.1) → place in `data/raw/conjunctiva/cp-anemic/`
2. **Download Roboflow datasets** (requires Roboflow API key) → place in respective directories
3. **Run EDA notebook** (`notebooks/01_data_exploration.ipynb`) to analyze color distributions, class balance, and image quality
4. **Unify annotations** into COCO/JSON format in `data/processed/`
5. **Generate augmented data** using the Albumentations pipelines defined in the README → output to `data/augmented/`
