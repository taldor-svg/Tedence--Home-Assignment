# Tedence Data Scientist Technical Assignment

**Candidate:** Tal Dor \
**Position:** Data Scientist \
**Interviewer:** Matan Orr \
**Date:** November 21, 2026 \
**Time Estimate:** 3-4 hours \
**Deadline:** December 1, 2026

---

## Context

Tedence is developing non-invasive glucose monitoring using EMF (electromagnetic field) sensors. We collect two types of data:

1. **EMF signals** — High-frequency sensor readings from multiple body locations
2. **CGM (Continuous Glucose Monitor)** — Reference glucose measurements

Your task is to explore and characterize these datasets, then containerize your analysis for reproducibility.

---

## Contents

```
├── README.md                 # This file
├── data/
│   ├── emf_readings.parquet  # EMF sensor data (downsampled)
│   └── cgm_reference.xlsx    # Glucose reference measurements
├── notebooks/
│   └── template.ipynb        # Template notebook (start here)
├── Dockerfile                # Template (to be completed)
└── requirements.txt          # Python dependencies
```

---

## Deliverables

### 1. Data Exploration Notebook
Complete the template notebook with:
- [ ] Dataset structure summary (shape, columns, types, time ranges)
- [ ] Data quality assessment (missing values, anomalies, outliers)
- [ ] Key variable distributions (visualizations)
- [ ] Preprocessing recommendations (what would you do before analysis?)

### 2. Containerization
- [ ] Complete the Dockerfile
- [ ] Verify the container runs with: `docker build -t tedence-exploration . && docker run tedence-exploration`
- [ ] Document any setup notes in this README below

### 3. Optional Bonus
Pick one EMF sensor and the CGM glucose column. Plot them over time for a single patient/session. What do you notice? (No right answer—we're curious how you look at unfamiliar data.)

---

## What We're Looking For

- **Clarity of thought** — Can you make sense of unfamiliar data?
- **Communication** — Can you explain what you see?
- **Engineering hygiene** — Clean code, reproducible environment
- **Pragmatism** — Good judgment about what matters vs. what doesn't

We are *not* asking you to find correlations between EMF and glucose. That's a research question our team has been working on for months. Focus on understanding and characterizing the data.

---

## Setup Notes

### Running with Docker 🐳

```bash
# Build the container
docker build -t tedence-exploration .

# Run the analysis (outputs the HTML report and PNG figures to ./output/)
docker run -v $(pwd)/output:/app/output tedence-exploration
```

The notebook will execute and generate `output/template.html` plus PNG files for its visualizations. The figures are also embedded in the HTML report.

### Running Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook notebooks/template.ipynb
```

### Environment
- Python 3.10+
- See `requirements.txt` for full dependency list

---

## Submission

Push your completed work to a **public GitHub repository** and email the link to Matan by the deadline (December 1, 2026).

---

## Questions?

Email Matan at matan@tedence.com — happy to clarify anything.
# Tedence--Home-Assignment
# Tedence--Home-Assignment
# Tedence--Home-Assignment
# Tedence--Home-Assignment
# Tedence--Home-Assignment
# Tedence--Home-Assignment
# Tedence--Home-Assignment
# Tedence--Home-Assignment
# Tedence--Home-Assignment
# Tedence--Home-Assignment
# Tedence--Home-Assignment
