# NACC Exploratory Data Analysis & Clinical Modeling

This repository contains the complete analytical pipeline, statistical exploration, and reporting for Phase 1 of the NACC (National Alzheimer's Coordinating Center) dataset project, focusing on Longitudinal UDS (Uniform Data Set) clinical evaluations and MRI neuroimaging metrics.

---

## Project Structure
```text
├── PROJECT_CARD.md         # Detailed project metadata, scope, and objectives
├── README.md               # Main project setup and reproduction guide
├── requirements.txt        # Pinned Python package dependencies
├── .gitignore              # Ignores large raw datasets, caches, and venv
├── data/
│   ├── README.md           # Dataset sourcing, provenance, and reconstruction guide
│   └── processed/          # Intermediate cleaned data tables (excluded from git)
├── notebooks/
│   └── uds_exploration.ipynb # End-to-end data cleaning, EDA, and statistical tests
├── figures/                # Output figures and distribution plots for the report
└── reports/
└── phase1/
└── Phase1_Report.pdf # Final Phase 1 submission report

