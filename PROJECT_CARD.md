# PROJECT CARD

## 1. Data source and files

- **Source:** National Alzheimer's Coordinating Center (NACC), Uniform Data Set (UDS) linked with structural MRI measures.
- **Track:** Track J (UDS + MRI, multi-faceted).
- **Subset used:** the pre-assigned subset of 1,237 participants who have both a UDS record and an MRI record.

| File | Role |
|---|---|
| `data/raw/udslong_imputed.csv` | Raw clinical (UDS) file, 1,237 rows, 180 columns |
| `data/raw/mriscanclean.csv` | Raw MRI file, 1,237 rows, 126 columns |
| `data/processed/udslong_cleaned.csv` | UDS after error codes were set to missing |
| `data/processed/uds_final.csv` | UDS after range and integer rules |
| `data/processed/mri_final.csv` | MRI after cleaning (12 unreliable scans set to missing) |
| `data/processed/mri_cleaning_log.csv` | Every MRI value that was flagged, and what was done |
| `data/processed/analysis_dataset.csv` | Final merged file used for all analyses ((1,237 × 313)) |

**Link key:** `NACCID`. One row per participant in each file; one-to-one inner join (1,237 matched, 0 unmatched).

## 2. Title

Association between clinical dementia severity (CDR Sum of Boxes) and entorhinal cortical thickness in the NACC UDS–MRI cohort

## 3. Main statistical question
How are entorhinal thickness and CDRSUM distributed across CDR groups in the 1,237 participants?

Secondary (descriptive only): the same comparison for the parahippocampal and middle temporal cortex.

## 4. Unit of observation and population

- **One row = one participant** (one UDS record linked to one MRI record). No participant appears twice.
- **Which visit the record comes from is not stated in the files**; this was decided when the files were prepared.
- **Population the results can describe:** older adults (median age 68, range 41–91) who volunteered at NIA-funded Alzheimer's Disease Research Centers, were evaluated with the UDS protocol, and have a usable MRI. Mostly highly educated (median 16 years); 68.5% normal cognition, 20.4% MCI, 10.6% dementia. Not the general population.

## 5. Variables

| Variable | File | Meaning | Type | Role |
|---|---|---|---|---|
| `CDRSUM` | UDS | CDR Sum of Boxes, 0–18 in steps of 0.5 (higher = more impaired) | Quantitative, discrete (61% are 0) | Explanatory |
| Entorhinal thickness (`LH_ENTORHINAL_AVGTH`, `RH_ENTORHINAL_AVGTH`; mean = `TH_ENTORHINAL`) | MRI | Average cortical thickness, mm | Quantitative, continuous | Response |
| `NACCAGE` | UDS | Age at visit, years | Quantitative (whole years) | Control |
| `SEX` | UDS | 1 = male, 2 = female | Nominal, binary | Control |
| `EDUC` | UDS | Years of education | Quantitative, discrete | Control |
| `CDR_group` | derived | `CDRSUM` in four groups: 0, 0.5–1.5, 2–4.5, ≥ 5 | Ordinal | Grouping (for tables and plots) |
| `NACCID` | both | Participant identifier | Nominal | Link key |

Secondary responses: parahippocampal and middle temporal thickness (quantitative, continuous, mm).

## 6. Type of question and starting idea

- **Type:** relationship (association) question, supported by a group comparison.
- **Starting idea (plain words):** we expect people with a higher `CDRSUM` to have, on average, a thinner entorhinal cortex. The exact test is defined in Phase 3.

## 7. Foreseeable limitations

1. **Single snapshot (cross-sectional):** we can see that two things go together, not that one causes the other.
2. **Clinic-based volunteers:** not a random sample of the population; highly educated, and the diagnosis mix is set by recruitment.
3. **`CDRSUM` is mostly zeros** and the highest group is small (≥ 5: n = 48).
4. **Age is mixed up with severity:** more impaired participants are about 4 years older and thickness falls with age, so age must be accounted for.
5. **Missing and imputed data:** the UDS file was imputed upstream, and imputed whole numbers cannot be identified, so the true amount of missing data is not known. 15 participants (1.2%) are lost for Q2.
6. **Cleaning choices are judgement calls** (3 × IQR, a scan is dropped if ≥13 of its values are flagged, 50% of the median). A sensitivity check showed the main result changes very little.
7. **Visit not documented:** which visit each record comes from is unknown.

## 8. How to reproduce

```bash
pip install -r requirements.txt
bash run_all.sh
```

See `README.md` for the folder layout and the run order.
