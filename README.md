# MS-RGCN+

MS-RGCN+ is a streamlined reimplementation of **Multi-Scale Relational Graph Convolutional Networks** for prostate histopathology, extending the original MS-RGCN by enabling **embedding-based** and **hybrid (spatial + embedding)** intra-magnification graph construction.

Original project: [MS-RGCN (AIMLab-UBC)](https://github.com/AIMLab-UBC/MS-RGCN)

---

## 🔧 Environment Setup

Use the provided `environment.yml` file to set up the Conda environment:

```bash
conda env create -f environment.yml
conda activate msrgcn
```

---

## 🚀 How to Run

Run the following steps in order. Update the paths based on your dataset structure:

### 1. Patch Extraction (GPU)
- Notebook: `multiscale_patch_extractor/multi_scale_patch_extractor_gpu.ipynb`
- Folder: `multiscale_patch_extractor_gpu`
- Purpose: Extract multi-scale patches from WSIs using GPU.

### 2. Color Normalization
- Notebook: `color_normalizer/Color_Normalization.ipynb`
- Folder: `color_normalizer`
- Purpose: Normalize stain colors to enable augmentation (Bazargani et al., 2023).

### 3. Label Extraction
- Notebook: `data/VPC/labelMaker.ipynb`
- Purpose: Generate patch-level labels from expert annotations.

### 4. Feature Extraction (6-class ResNet)
- Train model: `feature_extractor_6class/ResNet.ipynb`
- Get embeddings: `feature_extractor_6class/get_embeddings.ipynb`
- Purpose: Train a 6-class ResNet and extract patch embeddings.

### 5. Graph Construction & Model Training
- Graph building: `GNN_multiscale_ResNet_PANDA/graph_multi_magnification_plusplus.ipynb`  
  This script constructs the multi-scale graph using coordinates and embeddings. You can select the graph construction method using flags (see below).

- Model training & evaluation:  
  `GNN_multiscale_ResNet_PANDA/main_advanced_plus.ipynb`

---

## ⚙️ Graph Construction Modes

To select the graph type, modify the following flags inside `graph_multi_magnification_plusplus.ipynb`:

```python
USE_SIMGRID    = True    # Enable hybrid mode (spatial + cosine similarity)
USE_SIMILARITY = False   # If True: only cosine-similarity edges; if False: use distance-based (paper default)
SIM_THRESHOLD  = 0.85    # Cosine similarity threshold (range: 0.70 to 0.95 typical)
```

- **Baseline (original MS-RGCN)**  
  `USE_SIMGRID = False`  
  `USE_SIMILARITY = False`

- **Embedding-only (cosine similarity)**  
  `USE_SIMGRID = False`  
  `USE_SIMILARITY = True`

- **Combined (recommended)**  
  `USE_SIMGRID = True`

If all flags are False, the original MS-RGCN spatial graph will be used.

---

## 📂 Repository Structure

```
├── environment.yml
├── multiscale_patch_extractor/
│   └── multi_scale_patch_extractor_gpu.ipynb
├── color_normalizer/
│   └── Color_Normalization.ipynb
├── data/
│   └── VPC/
│       └── labelMaker.ipynb
├── feature_extractor_6class/
│   ├── ResNet.ipynb
│   └── get_embeddings.ipynb
└── GNN_multiscale_ResNet_PANDA/
    ├── graph_multi_magnification_plusplus.ipynb
    └── main_advanced_plus.ipynb
```

---

## 📊 Dataset

- **Dataset**: [Gleason 2019 Challenge (VPC Dataset)](https://gleason2019.grand-challenge.org/Home/)  
- This dataset contains prostate cancer histopathology slides with Gleason grading.  
- Patch filenames must encode their coordinates (x, y) and magnification level for graph construction.  
  Example: `patient123_x2000_y3500_mag20.png`  
- Labels are generated using `data/VPC/labelMaker.ipynb` from expert annotations.  
- You can adapt the pipeline to other histopathology datasets by following the same preprocessing steps (patch extraction, normalization, embeddings, graph construction).

---

## 🙏 Acknowledgments

- MS-RGCN Original Codebase:  
  [AIMLab-UBC/MS-RGCN](https://github.com/AIMLab-UBC/MS-RGCN)

---

## 📖 Citation

If you use this repository, please cite both the original MS-RGCN paper and any derivative work from MS-RGCN+:

```
@article{bazargani2024multi,
  title={Multi-scale relational graph convolutional network for multiple instance learning in histopathology images},
  author={Bazargani, Roozbeh and Fazli, Ladan and Gleave, Martin and Goldenberg, Larry and Bashashati, Ali and Salcudean, Septimiu},
  journal={Medical Image Analysis},
  volume={96},
  pages={103197},
  year={2024},
  publisher={Elsevier}
}
```

```
@misc{your_msrgnc_plus_paper,
  title={MS-RGCN+: Embedding-Aware Graph Construction for Multi-Scale Histopathology Classification},
  author={Your Name and Collaborators},
  year={2025},
  note={Under review}
}
```
