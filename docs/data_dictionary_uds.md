# NACC UDS Data Dictionary

- **Source File:** `data/raw/udslong_imputed.csv`
- **Total Rows:** 1,237
- **Total Columns:** 180

### Sentinel Codes Notice:
- `8`, `88`, `888`: Not Applicable
- `9`, `99`, `999`: Unknown / Missing

| # | Variable Name | Category | Data Type | Sample Value | Description |
|---|---|---|---|---|---|
| 001 | `NACCID` | Demographics | `str` | `NACC359836` | Subject Identification Number |
| 002 | `SEX` | Demographics | `float64` | `1.0` | Biological Sex (1=Male, 2=Female) |
| 003 | `HISPANIC` | Demographics | `float64` | `0.0` | Hispanic/Latino ethnicity (1=Yes, 0=No) |
| 004 | `HISPOR` | Demographics | `float64` | `88.0` | Hispanic origin detail (88=N/A) |
| 005 | `RACE` | Demographics | `float64` | `1.0` | Racial category |
| 006 | `PRIMLANG` | Demographics | `float64` | `1.0` | Primary language (1=English) |
| 007 | `EDUC` | Demographics | `float64` | `18.0` | Years of formal education |
| 008 | `MARISTAT` | Demographics | `float64` | `1.0` | Marital status (1=Married) |
| 009 | `NACCLIVS` | Demographics | `float64` | `2.0` | Living situation (1=Alone, 2=With partner) |
| 010 | `INDEPEND` | Demographics | `float64` | `1.0` | Independence level (1=Fully independent) |
| 011 | `RESIDENC` | Demographics | `float64` | `1.0` | Type of residence (1=Private home) |
| 012 | `NACCNIHR` | Demographics | `float64` | `1.0` | NIH defined race category |
| 013 | `NACCAGE` | Demographics | `float64` | `74.0` | Age of subject at visit (Years) |
| 014 | `NACCFAM` | Family History | `float64` | `0.0` | Family history of cognitive impairment (1=Yes, 0=No) |
| 015 | `NACCMOM` | Family History | `float64` | `0.0` | Cognitive impairment in mother |
| 016 | `NACCDAD` | Family History | `float64` | `0.0` | Cognitive impairment in father |
| 017 | `NACCAM` | Family History | `float64` | `0.0` | Maternal relatives affected |
| 018 | `NACCAMS` | Family History | `float64` | `9.0` | Maternal relatives severity/details |
| 019 | `NACCFM` | Family History | `float64` | `0.0` | Paternal relatives affected |
| 020 | `NACCFMS` | Family History | `float64` | `9.0` | Paternal relatives severity/details |
| 021 | `NACCOM` | Family History | `float64` | `0.0` | Other relatives affected |
| 022 | `NACCOMS` | Family History | `float64` | `9.0` | Other relatives severity/details |
| 023 | `NACCFADM` | Family History | `float64` | `0.0` | Family history of Alzheimer's Disease |
| 024 | `NACCFFTD` | Family History | `float64` | `0.0` | Family history of FTLD |
| 025 | `ANYMEDS` | Habits | `float64` | `0.8` | Reported any prescription medication use |
| 026 | `TOBAC30` | Habits | `float64` | `0.0` | Smoked tobacco in last 30 days |
| 027 | `TOBAC100` | Habits | `float64` | `1.0` | Smoked >= 100 cigarettes in lifetime |
| 028 | `SMOKYRS` | Habits | `float64` | `10.0` | Total years of smoking |
| 029 | `PACKSPER` | Habits | `float64` | `3.0` | Packs of cigarettes per day |
| 030 | `QUITSMOK` | Habits | `float64` | `30.0` | Age when quit smoking |
| 031 | `CVHATT` | Medical History | `float64` | `0.0` | Heart attack / Myocardial infarction |
| 032 | `CVAFIB` | Medical History | `float64` | `0.0` | Atrial fibrillation |
| 033 | `CVANGIO` | Medical History | `float64` | `0.0` | Coronary angioplasty |
| 034 | `CVBYPASS` | Medical History | `float64` | `0.0` | Coronary artery bypass graft |
| 035 | `CVPACDEF` | Medical History | `float64` | `0.0` | Pacemaker or defibrillator |
| 036 | `CVCHF` | Medical History | `float64` | `0.0` | Congestive heart failure |
| 037 | `CVOTHR` | Medical History | `float64` | `0.0` | Other cardiovascular condition |
| 038 | `CBSTROKE` | Medical History | `float64` | `0.0` | Stroke history |
| 039 | `CBTIA` | Medical History | `float64` | `0.0` | Transient Ischemic Attack (TIA) |
| 040 | `SEIZURES` | Medical History | `float64` | `0.0` | Seizures or epilepsy history |
| 041 | `NACCTBI` | Medical History | `float64` | `0.0` | History of Traumatic Brain Injury (TBI) |
| 042 | `TBI` | Medical History | `float64` | `0.0` | TBI reported |
| 043 | `TBIBRIEF` | Medical History | `float64` | `0.0` | TBI with brief loss of consciousness (<5 min) |
| 044 | `TBIEXTEN` | Medical History | `float64` | `0.0` | TBI with extended loss of consciousness (>=5 min) |
| 045 | `TBIWOLOS` | Medical History | `float64` | `0.0` | TBI without loss of consciousness |
| 046 | `DIABETES` | Medical History | `float64` | `0.0` | Diabetes diagnosed |
| 047 | `DIABTYPE` | Medical History | `float64` | `8.0` | Diabetes type (1=Type1, 2=Type2, 8=N/A) |
| 048 | `HYPERTEN` | Medical History | `float64` | `1.0` | Hypertension (High Blood Pressure) |
| 049 | `HYPERCHO` | Medical History | `float64` | `1.0` | Hypercholesterolemia (High Cholesterol) |
| 050 | `B12DEF` | Medical History | `float64` | `9.0` | Vitamin B12 deficiency |
| 051 | `THYROID` | Medical History | `float64` | `0.0` | Thyroid disease |
| 052 | `ARTHRIT` | Medical History | `float64` | `1.0` | Arthritis history |
| 053 | `ARTHTYPE` | Medical History | `float64` | `2.0` | Type of arthritis |
| 054 | `ARTHUPEX` | Medical History | `float64` | `0.0` | Upper extremity arthritis |
| 055 | `ARTHLOEX` | Medical History | `float64` | `1.0` | Lower extremity arthritis |
| 056 | `ARTHSPIN` | Medical History | `float64` | `0.0` | Spine arthritis |
| 057 | `ARTHUNK` | Medical History | `float64` | `0.0` | Arthritis location unknown |
| 058 | `INCONTU` | Medical History | `float64` | `0.0` | Urinary incontinence |
| 059 | `INCONTF` | Medical History | `float64` | `0.0` | Fecal incontinence |
| 060 | `APNEA` | Medical History | `float64` | `9.0` | Sleep apnea |
| 061 | `RBD` | Medical History | `float64` | `0.0` | REM sleep behavior disorder |
| 062 | `INSOMN` | Medical History | `float64` | `0.0` | Insomnia disorder |
| 063 | `OTHSLEEP` | Medical History | `float64` | `0.0` | Other sleep disorder |
| 064 | `ALCOHOL` | Medical History | `float64` | `0.0` | Alcohol abuse / dependence |
| 065 | `ABUSOTHR` | Medical History | `float64` | `0.0` | Other substance abuse |
| 066 | `PTSD` | Medical History | `float64` | `0.0` | Post-Traumatic Stress Disorder |
| 067 | `BIPOLAR` | Medical History | `float64` | `0.0` | Bipolar disorder |
| 068 | `SCHIZ` | Medical History | `float64` | `0.0` | Schizophrenia spectrum disorder |
| 069 | `DEP2YRS` | Medical History | `float64` | `0.0` | Depression episode in last 2 years |
| 070 | `DEPOTHR` | Medical History | `float64` | `1.0` | Other depression episodes |
| 071 | `ANXIETY` | Medical History | `float64` | `0.0` | Anxiety disorder |
| 072 | `OCD` | Medical History | `float64` | `0.0` | Obsessive-Compulsive Disorder |
| 073 | `NPSYDEV` | Medical History | `float64` | `0.0` | Developmental neuropsychiatric disorder |
| 074 | `PSYCDIS` | Medical History | `float64` | `0.0` | Other psychiatric condition |
| 075 | `NACCAAAS` | Medication Class | `float64` | `0.0` | Aspirin and anti-inflammatory use |
| 076 | `NACCAANX` | Medication Class | `float64` | `0.2` | Anxiolytics use |
| 077 | `NACCAC` | Medication Class | `float64` | `0.4` | Anticholinergic drugs use |
| 078 | `NACCACEI` | Medication Class | `float64` | `0.0` | ACE inhibitors use |
| 079 | `NACCADEP` | Medication Class | `float64` | `0.0` | Antidepressants use |
| 080 | `NACCAHTN` | Medication Class | `float64` | `0.6` | Antihypertensive agents use |
| 081 | `NACCAMD` | Medication Class | `float64` | `4.2` | Other medical drugs count/indicator |
| 082 | `NACCANGI` | Medication Class | `float64` | `0.2` | Antianginal medications |
| 083 | `NACCAPSY` | Medication Class | `float64` | `0.0` | Antipsychotics use |
| 084 | `NACCBETA` | Medication Class | `float64` | `0.0` | Beta-blockers use |
| 085 | `NACCCCBS` | Medication Class | `float64` | `0.4` | Calcium channel blockers use |
| 086 | `NACCDBMD` | Medication Class | `float64` | `0.0` | Diabetes medication use |
| 087 | `NACCDIUR` | Medication Class | `float64` | `0.2` | Diuretics use |
| 088 | `NACCEMD` | Medication Class | `float64` | `0.0` | Estrogen / Hormonal replacement |
| 089 | `NACCEPMD` | Medication Class | `float64` | `0.0` | Antiepileptic / Mood stabilizers |
| 090 | `NACCHTNC` | Medication Class | `float64` | `0.0` | Centrally acting antihypertensives |
| 091 | `NACCLIPL` | Medication Class | `float64` | `0.2` | Lipid lowering agents (Statins) |
| 092 | `NACCNSD` | Medication Class | `float64` | `0.4` | NSAIDs use |
| 093 | `NACCPDMD` | Medication Class | `float64` | `0.2` | Parkinson's disease medications |
| 094 | `NACCVASD` | Medication Class | `float64` | `0.0` | Vasodilators use |
| 095 | `HEIGHT` | Physical/Vitals | `float64` | `68.1` | Height (inches) |
| 096 | `WEIGHT` | Physical/Vitals | `float64` | `146.0` | Weight (pounds) |
| 097 | `BPSYS` | Physical/Vitals | `float64` | `145.0` | Systolic Blood Pressure (mmHg) |
| 098 | `BPDIAS` | Physical/Vitals | `float64` | `98.0` | Diastolic Blood Pressure (mmHg) |
| 099 | `HRATE` | Physical/Vitals | `float64` | `64.0` | Heart Rate (beats/min) |
| 100 | `VISION` | Physical/Vitals | `float64` | `1.0` | Vision status (1=Adequate) |
| 101 | `VISCORR` | Physical/Vitals | `float64` | `0.0` | Vision corrected (glasses/lenses) |
| 102 | `VISWCORR` | Physical/Vitals | `float64` | `8.0` | Vision without correction |
| 103 | `HEARING` | Physical/Vitals | `float64` | `1.0` | Hearing status (1=Adequate) |
| 104 | `HEARAID` | Physical/Vitals | `float64` | `0.0` | Hearing aid used |
| 105 | `HEARWAID` | Physical/Vitals | `float64` | `8.0` | Hearing without aid |
| 106 | `NACCBMI` | Physical/Vitals | `float64` | `22.1` | Body Mass Index (BMI) |
| 107 | `NACCNREX` | Physical/Vitals | `float64` | `1.0` | Neurological exam conducted |
| 108 | `NORMEXAM` | Physical/Vitals | `float64` | `0.0` | Neurological exam status (1=Normal) |
| 109 | `NPIQINF` | NPI-Q | `float64` | `1.0` | Informant for NPI-Q reliable |
| 110 | `DEL` | NPI-Q | `float64` | `0.0` | Delusions present (1=Yes, 0=No) |
| 111 | `DELSEV` | NPI-Q | `float64` | `8.0` | Delusions severity (1=Mild, 2=Mod, 3=Severe, 8=N/A) |
| 112 | `HALL` | NPI-Q | `float64` | `0.0` | Hallucinations present |
| 113 | `HALLSEV` | NPI-Q | `float64` | `8.0` | Hallucinations severity |
| 114 | `AGIT` | NPI-Q | `float64` | `0.0` | Agitation / Aggression present |
| 115 | `AGITSEV` | NPI-Q | `float64` | `8.0` | Agitation severity |
| 116 | `DEPD` | NPI-Q | `float64` | `0.0` | Depression / Dysphoria present |
| 117 | `DEPDSEV` | NPI-Q | `float64` | `8.0` | Depression severity |
| 118 | `ANX` | NPI-Q | `float64` | `0.0` | Anxiety present |
| 119 | `ANXSEV` | NPI-Q | `float64` | `8.0` | Anxiety severity |
| 120 | `ELAT` | NPI-Q | `float64` | `0.0` | Elation / Euphoria present |
| 121 | `ELATSEV` | NPI-Q | `float64` | `8.0` | Elation severity |
| 122 | `APA` | NPI-Q | `float64` | `0.0` | Apathy / Indifference present |
| 123 | `APASEV` | NPI-Q | `float64` | `8.0` | Apathy severity |
| 124 | `DISN` | NPI-Q | `float64` | `0.0` | Disinhibition present |
| 125 | `DISNSEV` | NPI-Q | `float64` | `8.0` | Disinhibition severity |
| 126 | `IRR` | NPI-Q | `float64` | `0.0` | Irritability / Lability present |
| 127 | `IRRSEV` | NPI-Q | `float64` | `8.0` | Irritability severity |
| 128 | `MOT` | NPI-Q | `float64` | `1.0` | Aberrant motor behavior present |
| 129 | `MOTSEV` | NPI-Q | `float64` | `1.0` | Aberrant motor behavior severity |
| 130 | `NITE` | NPI-Q | `float64` | `1.0` | Nighttime behavior disturbance present |
| 131 | `NITESEV` | NPI-Q | `float64` | `2.0` | Nighttime disturbance severity |
| 132 | `APP` | NPI-Q | `float64` | `1.0` | Appetite / Eating changes present |
| 133 | `APPSEV` | NPI-Q | `float64` | `1.0` | Appetite changes severity |
| 134 | `NOGDS` | GDS | `float64` | `0.0` | GDS was not administered |
| 135 | `SATIS` | GDS | `float64` | `0.0` | Satisfied with life |
| 136 | `DROPACT` | GDS | `float64` | `0.0` | Dropped activities and interests |
| 137 | `EMPTY` | GDS | `float64` | `0.0` | Feels life is empty |
| 138 | `BORED` | GDS | `float64` | `0.0` | Often gets bored |
| 139 | `SPIRITS` | GDS | `float64` | `0.0` | In good spirits most of the time |
| 140 | `AFRAID` | GDS | `float64` | `0.0` | Afraid bad things will happen |
| 141 | `HAPPY` | GDS | `float64` | `0.0` | Feels happy most of the time |
| 142 | `HELPLESS` | GDS | `float64` | `0.0` | Feels helpless |
| 143 | `STAYHOME` | GDS | `float64` | `0.0` | Prefers to stay at home |
| 144 | `MEMPROB` | GDS | `float64` | `0.0` | Feels has more memory problems |
| 145 | `WONDRFUL` | GDS | `float64` | `0.0` | Wonderful to be alive right now |
| 146 | `WRTHLESS` | GDS | `float64` | `0.0` | Feels worthless the way they are |
| 147 | `ENERGY` | GDS | `float64` | `0.0` | Feels full of energy |
| 148 | `HOPELESS` | GDS | `float64` | `0.0` | Feels situation is hopeless |
| 149 | `BETTER` | GDS | `float64` | `0.0` | Most people are better off than them |
| 150 | `NACCGDS` | GDS | `float64` | `0.0` | Total Geriatric Depression Score (0-15) |
| 151 | `BILLS` | Functional Activities | `float64` | `0.0` | Managing finances / Writing checks |
| 152 | `TAXES` | Functional Activities | `float64` | `0.0` | Assembling tax records |
| 153 | `SHOPPING` | Functional Activities | `float64` | `0.0` | Shopping alone for clothes/groceries |
| 154 | `GAMES` | Functional Activities | `float64` | `0.0` | Playing a game of skill or hobby |
| 155 | `STOVE` | Functional Activities | `float64` | `0.0` | Turning off stove after use |
| 156 | `MEALPREP` | Functional Activities | `float64` | `0.0` | Preparing a balanced meal |
| 157 | `EVENTS` | Functional Activities | `float64` | `0.0` | Keeping track of current events |
| 158 | `PAYATTN` | Functional Activities | `float64` | `0.0` | Paying attention to TV or book |
| 159 | `REMDATES` | Functional Activities | `float64` | `8.0` | Remembering appointments and family occasions |
| 160 | `TRAVEL` | Functional Activities | `float64` | `1.0` | Traveling out of neighborhood independently |
| 161 | `DECSUB` | Cognitive / Diagnostic | `float64` | `0.0` | Clinical decline noted by subject |
| 162 | `ANIMALS` | Cognitive / Diagnostic | `float64` | `26.0` | Category fluency: Number of animals in 1 min |
| 163 | `VEG` | Cognitive / Diagnostic | `float64` | `11.0` | Category fluency: Number of vegetables in 1 min |
| 164 | `TRAILA` | Cognitive / Diagnostic | `float64` | `25.0` | Trail Making Test Part A (Time in seconds) |
| 165 | `TRAILARR` | Cognitive / Diagnostic | `float64` | `0.0` | Trail Making Test Part A Commission errors |
| 166 | `TRAILALI` | Cognitive / Diagnostic | `float64` | `24.0` | Trail Making Test Part A Correct lines |
| 167 | `TRAILB` | Cognitive / Diagnostic | `float64` | `70.0` | Trail Making Test Part B (Time in seconds) |
| 168 | `TRAILBRR` | Cognitive / Diagnostic | `float64` | `0.0` | Trail Making Test Part B Commission errors |
| 169 | `TRAILBLI` | Cognitive / Diagnostic | `float64` | `24.0` | Trail Making Test Part B Correct lines |
| 170 | `MOCATOTS` | Cognitive / Diagnostic | `float64` | `25.0` | MoCA Total Cognitive Score (0-30) |
| 171 | `NACCAPOE` | Cognitive / Diagnostic | `float64` | `4.0` | APOE genotype (Genetic risk factor: allele e4) |
| 172 | `NACCUDSD` | Cognitive / Diagnostic | `float64` | `1.0` | Primary Clinical Diagnosis (1=Normal, 2=Impaired, 3=MCI, 4=Dementia) |
| 173 | `MEMORY` | Cognitive / Diagnostic | `float64` | `0.0` | CDR Memory domain score |
| 174 | `ORIENT` | Cognitive / Diagnostic | `float64` | `0.0` | CDR Orientation domain score |
| 175 | `JUDGMENT` | Cognitive / Diagnostic | `float64` | `0.0` | CDR Judgment & Problem Solving score |
| 176 | `COMMUN` | Cognitive / Diagnostic | `float64` | `0.0` | CDR Community Affairs score |
| 177 | `HOMEHOBB` | Cognitive / Diagnostic | `float64` | `0.0` | CDR Home & Hobbies score |
| 178 | `PERSCARE` | Cognitive / Diagnostic | `float64` | `0.0` | CDR Personal Care score |
| 179 | `CDRSUM` | Cognitive / Diagnostic | `float64` | `0.0` | Clinical Dementia Rating (CDR) Sum of Boxes |
| 180 | `CDRGLOB` | Cognitive / Diagnostic | `float64` | `0.0` | Clinical Dementia Rating (CDR) Global Score (0, 0.5, 1, 2, 3) |
