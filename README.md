# README

## Author
Aziz Baran Kurtulus

## Directory Structure
```
first_assignment/
├── problem1_zipf.py          # Problem 1: Zipf's Law analysis
├── problem2_generator.py     # Problem 2: N-gram text generation
├── problem3_pmi.py           # Problem 3: PMI analysis
├── utils.py                  # Shared utility functions
├── ngram_model.py           # BasicNgram class (from course materials)
├── report.md                # Report with discussions and findings
├── data/
│   ├── kjv.txt              # King James Bible corpus
│   └── junglebook.txt       # Jungle Book corpus
├── outputs/
│   ├── plots/               # Zipf's Law visualizations
│   │   ├── kjv_zipf.png
│   │   ├── junglebook_zipf.png
│   │   ├── setimes_bg_zipf.png
│   │   └── setimes_tr_zipf.png
│   ├── generated_text/      # Generated text samples from Problem 2
│   │   ├── n2_sample1.txt (and n2_sample2.txt, n2_sample3.txt)
│   │   ├── n3_sample1.txt (and n3_sample2.txt, n3_sample3.txt)
│   │   └── n4_sample1.txt (and n4_sample2.txt, n4_sample3.txt)
│   ├── kjv_frequencies.txt
│   ├── junglebook_frequencies.txt
│   ├── setimes_bg_frequencies.txt
│   └── setimes_tr_frequencies.txt
├── pyproject.toml           # Project dependencies
└── README.md                # This file
```

## Versions
- Python: 3.13
- nltk: 3.8+
- matplotlib: 3.8+
- numpy: 1.26+
- datasets: 2.14+ (HuggingFace datasets for SETIMES corpus)
- ruff: 0.14+ (code formatting)

## Setup

### Install Dependencies

**Option 1: Using pip (recommended)**
```bash
pip install nltk matplotlib numpy datasets
```

Or if you have the `pyproject.toml` file:
```bash
pip install -e .
```

**Option 2: Using uv (alternative)**
```bash
uv sync
```

### Download NLTK Data (Required for Problem 2)
```python
import nltk
nltk.download('punkt')
```

## Runtime
- **Problem 1** (problem1_zipf.py): ~2-3 minutes
  - Corpus loading and frequency counting: ~30 seconds
  - SETIMES download from HuggingFace (first time): ~1 minute
  - Plot generation: ~30 seconds

- **Problem 2** (problem2_generator.py): ~1-2 minutes
  - N-gram model training: ~30-60 seconds (varies by n)
  - Text generation: ~10 seconds

- **Problem 3** (problem3_pmi.py): ~30 seconds
  - PMI calculation for word pairs: ~30 seconds

## How to Run

### Problem 1: Zipf's Law
```bash
python problem1_zipf.py
```
This will analyze all four corpora and generate plots in `outputs/plots/`.

### Problem 2: N-gram Text Generation
```bash
python problem2_generator.py
```
This will train n-gram models (n=2,3,4) and generate text samples in `outputs/generated_text/`.

### Problem 3: PMI Analysis
```bash
python problem3_pmi.py
```
This will calculate PMI scores for word pairs and display the top 20 highest and lowest PMI pairs.