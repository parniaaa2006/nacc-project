import pandas as pd
from pathlib import Path

csv_path = Path("data/raw/udslong_imputed.csv")
df = pd.read_csv(csv_path)

descriptions = {
    # Demographics & Admin
    "NACCID": ("Subject Identification Number", "Demographics"),
    "SEX": ("Biological Sex (1=Male, 2=Female)", "Demographics"),
    "HISPANIC": ("Hispanic/Latino ethnicity (1=Yes, 0=No)", "Demographics"),
    "HISPOR": ("Hispanic origin detail (88=N/A)", "Demographics"),
    "RACE": ("Racial category", "Demographics"),
    "PRIMLANG": ("Primary language (1=English)", "Demographics"),
    "EDUC": ("Years of formal education", "Demographics"),
    "MARISTAT": ("Marital status (1=Married)", "Demographics"),
    "NACCLIVS": ("Living situation (1=Alone, 2=With partner)", "Demographics"),
    "INDEPEND": ("Independence level (1=Fully independent)", "Demographics"),
    "RESIDENC": ("Type of residence (1=Private home)", "Demographics"),
    "NACCNIHR": ("NIH defined race category", "Demographics"),
    "NACCAGE": ("Age of subject at visit (Years)", "Demographics"),
    
    # Family History
    "NACCFAM": ("Family history of cognitive impairment (1=Yes, 0=No)", "Family History"),
    "NACCMOM": ("Cognitive impairment in mother", "Family History"),
    "NACCDAD": ("Cognitive impairment in father", "Family History"),
    "NACCAM": ("Maternal relatives affected", "Family History"),
    "NACCAMS": ("Maternal relatives severity/details", "Family History"),
    "NACCFM": ("Paternal relatives affected", "Family History"),
    "NACCFMS": ("Paternal relatives severity/details", "Family History"),
    "NACCOM": ("Other relatives affected", "Family History"),
    "NACCOMS": ("Other relatives severity/details", "Family History"),
    "NACCFADM": ("Family history of Alzheimer's Disease", "Family History"),
    "NACCFFTD": ("Family history of FTLD", "Family History"),

    # Smoking & Habits
    "ANYMEDS": ("Reported any prescription medication use", "Habits"),
    "TOBAC30": ("Smoked tobacco in last 30 days", "Habits"),
    "TOBAC100": ("Smoked >= 100 cigarettes in lifetime", "Habits"),
    "SMOKYRS": ("Total years of smoking", "Habits"),
    "PACKSPER": ("Packs of cigarettes per day", "Habits"),
    "QUITSMOK": ("Age when quit smoking", "Habits"),

    # Medical History (Cardio, Neuro, General)
    "CVHATT": ("Heart attack / Myocardial infarction", "Medical History"),
    "CVAFIB": ("Atrial fibrillation", "Medical History"),
    "CVANGIO": ("Coronary angioplasty", "Medical History"),
    "CVBYPASS": ("Coronary artery bypass graft", "Medical History"),
    "CVPACDEF": ("Pacemaker or defibrillator", "Medical History"),
    "CVCHF": ("Congestive heart failure", "Medical History"),
    "CVOTHR": ("Other cardiovascular condition", "Medical History"),
    "CBSTROKE": ("Stroke history", "Medical History"),
    "CBTIA": ("Transient Ischemic Attack (TIA)", "Medical History"),
    "SEIZURES": ("Seizures or epilepsy history", "Medical History"),
    "NACCTBI": ("History of Traumatic Brain Injury (TBI)", "Medical History"),
    "TBI": ("TBI reported", "Medical History"),
    "TBIBRIEF": ("TBI with brief loss of consciousness (<5 min)", "Medical History"),
    "TBIEXTEN": ("TBI with extended loss of consciousness (>=5 min)", "Medical History"),
    "TBIWOLOS": ("TBI without loss of consciousness", "Medical History"),
    "DIABETES": ("Diabetes diagnosed", "Medical History"),
    "DIABTYPE": ("Diabetes type (1=Type1, 2=Type2, 8=N/A)", "Medical History"),
    "HYPERTEN": ("Hypertension (High Blood Pressure)", "Medical History"),
    "HYPERCHO": ("Hypercholesterolemia (High Cholesterol)", "Medical History"),
    "B12DEF": ("Vitamin B12 deficiency", "Medical History"),
    "THYROID": ("Thyroid disease", "Medical History"),
    "ARTHRIT": ("Arthritis history", "Medical History"),
    "ARTHTYPE": ("Type of arthritis", "Medical History"),
    "ARTHUPEX": ("Upper extremity arthritis", "Medical History"),
    "ARTHLOEX": ("Lower extremity arthritis", "Medical History"),
    "ARTHSPIN": ("Spine arthritis", "Medical History"),
    "ARTHUNK": ("Arthritis location unknown", "Medical History"),
    "INCONTU": ("Urinary incontinence", "Medical History"),
    "INCONTF": ("Fecal incontinence", "Medical History"),
    "APNEA": ("Sleep apnea", "Medical History"),
    "RBD": ("REM sleep behavior disorder", "Medical History"),
    "INSOMN": ("Insomnia disorder", "Medical History"),
    "OTHSLEEP": ("Other sleep disorder", "Medical History"),
    "ALCOHOL": ("Alcohol abuse / dependence", "Medical History"),
    "ABUSOTHR": ("Other substance abuse", "Medical History"),
    "PTSD": ("Post-Traumatic Stress Disorder", "Medical History"),
    "BIPOLAR": ("Bipolar disorder", "Medical History"),
    "SCHIZ": ("Schizophrenia spectrum disorder", "Medical History"),
    "DEP2YRS": ("Depression episode in last 2 years", "Medical History"),
    "DEPOTHR": ("Other depression episodes", "Medical History"),
    "ANXIETY": ("Anxiety disorder", "Medical History"),
    "OCD": ("Obsessive-Compulsive Disorder", "Medical History"),
    "NPSYDEV": ("Developmental neuropsychiatric disorder", "Medical History"),
    "PSYCDIS": ("Other psychiatric condition", "Medical History"),

    # Medication Classes
    "NACCAAAS": ("Aspirin and anti-inflammatory use", "Medication Class"),
    "NACCAANX": ("Anxiolytics use", "Medication Class"),
    "NACCAC": ("Anticholinergic drugs use", "Medication Class"),
    "NACCACEI": ("ACE inhibitors use", "Medication Class"),
    "NACCADEP": ("Antidepressants use", "Medication Class"),
    "NACCAHTN": ("Antihypertensive agents use", "Medication Class"),
    "NACCAMD": ("Other medical drugs count/indicator", "Medication Class"),
    "NACCANGI": ("Antianginal medications", "Medication Class"),
    "NACCAPSY": ("Antipsychotics use", "Medication Class"),
    "NACCBETA": ("Beta-blockers use", "Medication Class"),
    "NACCCCBS": ("Calcium channel blockers use", "Medication Class"),
    "NACCDBMD": ("Diabetes medication use", "Medication Class"),
    "NACCDIUR": ("Diuretics use", "Medication Class"),
    "NACCEMD": ("Estrogen / Hormonal replacement", "Medication Class"),
    "NACCEPMD": ("Antiepileptic / Mood stabilizers", "Medication Class"),
    "NACCHTNC": ("Centrally acting antihypertensives", "Medication Class"),
    "NACCLIPL": ("Lipid lowering agents (Statins)", "Medication Class"),
    "NACCNSD": ("NSAIDs use", "Medication Class"),
    "NACCPDMD": ("Parkinson's disease medications", "Medication Class"),
    "NACCVASD": ("Vasodilators use", "Medication Class"),

    # Vitals & Exam
    "HEIGHT": ("Height (inches)", "Physical/Vitals"),
    "WEIGHT": ("Weight (pounds)", "Physical/Vitals"),
    "BPSYS": ("Systolic Blood Pressure (mmHg)", "Physical/Vitals"),
    "BPDIAS": ("Diastolic Blood Pressure (mmHg)", "Physical/Vitals"),
    "HRATE": ("Heart Rate (beats/min)", "Physical/Vitals"),
    "VISION": ("Vision status (1=Adequate)", "Physical/Vitals"),
    "VISCORR": ("Vision corrected (glasses/lenses)", "Physical/Vitals"),
    "VISWCORR": ("Vision without correction", "Physical/Vitals"),
    "HEARING": ("Hearing status (1=Adequate)", "Physical/Vitals"),
    "HEARAID": ("Hearing aid used", "Physical/Vitals"),
    "HEARWAID": ("Hearing without aid", "Physical/Vitals"),
    "NACCBMI": ("Body Mass Index (BMI)", "Physical/Vitals"),
    "NACCNREX": ("Neurological exam conducted", "Physical/Vitals"),
    "NORMEXAM": ("Neurological exam status (1=Normal)", "Physical/Vitals"),

    # Neuropsychiatric Symptoms (NPI-Q)
    "NPIQINF": ("Informant for NPI-Q reliable", "NPI-Q"),
    "DEL": ("Delusions present (1=Yes, 0=No)", "NPI-Q"),
    "DELSEV": ("Delusions severity (1=Mild, 2=Mod, 3=Severe, 8=N/A)", "NPI-Q"),
    "HALL": ("Hallucinations present", "NPI-Q"),
    "HALLSEV": ("Hallucinations severity", "NPI-Q"),
    "AGIT": ("Agitation / Aggression present", "NPI-Q"),
    "AGITSEV": ("Agitation severity", "NPI-Q"),
    "DEPD": ("Depression / Dysphoria present", "NPI-Q"),
    "DEPDSEV": ("Depression severity", "NPI-Q"),
    "ANX": ("Anxiety present", "NPI-Q"),
    "ANXSEV": ("Anxiety severity", "NPI-Q"),
    "ELAT": ("Elation / Euphoria present", "NPI-Q"),
    "ELATSEV": ("Elation severity", "NPI-Q"),
    "APA": ("Apathy / Indifference present", "NPI-Q"),
    "APASEV": ("Apathy severity", "NPI-Q"),
    "DISN": ("Disinhibition present", "NPI-Q"),
    "DISNSEV": ("Disinhibition severity", "NPI-Q"),
    "IRR": ("Irritability / Lability present", "NPI-Q"),
    "IRRSEV": ("Irritability severity", "NPI-Q"),
    "MOT": ("Aberrant motor behavior present", "NPI-Q"),
    "MOTSEV": ("Aberrant motor behavior severity", "NPI-Q"),
    "NITE": ("Nighttime behavior disturbance present", "NPI-Q"),
    "NITESEV": ("Nighttime disturbance severity", "NPI-Q"),
    "APP": ("Appetite / Eating changes present", "NPI-Q"),
    "APPSEV": ("Appetite changes severity", "NPI-Q"),

    # Geriatric Depression Scale (GDS)
    "NOGDS": ("GDS was not administered", "GDS"),
    "SATIS": ("Satisfied with life", "GDS"),
    "DROPACT": ("Dropped activities and interests", "GDS"),
    "EMPTY": ("Feels life is empty", "GDS"),
    "BORED": ("Often gets bored", "GDS"),
    "SPIRITS": ("In good spirits most of the time", "GDS"),
    "AFRAID": ("Afraid bad things will happen", "GDS"),
    "HAPPY": ("Feels happy most of the time", "GDS"),
    "HELPLESS": ("Feels helpless", "GDS"),
    "STAYHOME": ("Prefers to stay at home", "GDS"),
    "MEMPROB": ("Feels has more memory problems", "GDS"),
    "WONDRFUL": ("Wonderful to be alive right now", "GDS"),
    "WRTHLESS": ("Feels worthless the way they are", "GDS"),
    "ENERGY": ("Feels full of energy", "GDS"),
    "HOPELESS": ("Feels situation is hopeless", "GDS"),
    "BETTER": ("Most people are better off than them", "GDS"),
    "NACCGDS": ("Total Geriatric Depression Score (0-15)", "GDS"),

    # Functional Activities (FAQ)
    "BILLS": ("Managing finances / Writing checks", "Functional Activities"),
    "TAXES": ("Assembling tax records", "Functional Activities"),
    "SHOPPING": ("Shopping alone for clothes/groceries", "Functional Activities"),
    "GAMES": ("Playing a game of skill or hobby", "Functional Activities"),
    "STOVE": ("Turning off stove after use", "Functional Activities"),
    "MEALPREP": ("Preparing a balanced meal", "Functional Activities"),
    "EVENTS": ("Keeping track of current events", "Functional Activities"),
    "PAYATTN": ("Paying attention to TV or book", "Functional Activities"),
    "REMDATES": ("Remembering appointments and family occasions", "Functional Activities"),
    "TRAVEL": ("Traveling out of neighborhood independently", "Functional Activities"),

    # Cognitive Tests, Genetics & Clinical Diagnosis
    "DECSUB": ("Clinical decline noted by subject", "Cognitive / Diagnostic"),
    "ANIMALS": ("Category fluency: Number of animals in 1 min", "Cognitive / Diagnostic"),
    "VEG": ("Category fluency: Number of vegetables in 1 min", "Cognitive / Diagnostic"),
    "TRAILA": ("Trail Making Test Part A (Time in seconds)", "Cognitive / Diagnostic"),
    "TRAILARR": ("Trail Making Test Part A Commission errors", "Cognitive / Diagnostic"),
    "TRAILALI": ("Trail Making Test Part A Correct lines", "Cognitive / Diagnostic"),
    "TRAILB": ("Trail Making Test Part B (Time in seconds)", "Cognitive / Diagnostic"),
    "TRAILBRR": ("Trail Making Test Part B Commission errors", "Cognitive / Diagnostic"),
    "TRAILBLI": ("Trail Making Test Part B Correct lines", "Cognitive / Diagnostic"),
    "MOCATOTS": ("MoCA Total Cognitive Score (0-30)", "Cognitive / Diagnostic"),
    "NACCAPOE": ("APOE genotype (Genetic risk factor: allele e4)", "Cognitive / Diagnostic"),
    "NACCUDSD": ("Primary Clinical Diagnosis (1=Normal, 2=Impaired, 3=MCI, 4=Dementia)", "Cognitive / Diagnostic"),
    "MEMORY": ("CDR Memory domain score", "Cognitive / Diagnostic"),
    "ORIENT": ("CDR Orientation domain score", "Cognitive / Diagnostic"),
    "JUDGMENT": ("CDR Judgment & Problem Solving score", "Cognitive / Diagnostic"),
    "COMMUN": ("CDR Community Affairs score", "Cognitive / Diagnostic"),
    "HOMEHOBB": ("CDR Home & Hobbies score", "Cognitive / Diagnostic"),
    "PERSCARE": ("CDR Personal Care score", "Cognitive / Diagnostic"),
    "CDRSUM": ("Clinical Dementia Rating (CDR) Sum of Boxes", "Cognitive / Diagnostic"),
    "CDRGLOB": ("Clinical Dementia Rating (CDR) Global Score (0, 0.5, 1, 2, 3)", "Cognitive / Diagnostic"),
}
out_dir = Path("docs")
out_dir.mkdir(exist_ok=True)
md_file = out_dir / "data_dictionary_uds.md"

with open(md_file, "w", encoding="utf-8") as f:
    f.write("# NACC UDS Data Dictionary\n\n")
    f.write(f"- **Source File:** `data/raw/udslong_imputed.csv`\n")
    f.write(f"- **Total Rows:** {df.shape[0]:,}\n")
    f.write(f"- **Total Columns:** {df.shape[1]}\n\n")
    f.write("### Sentinel Codes Notice:\n")
    f.write("- `8`, `88`, `888`: Not Applicable\n")
    f.write("- `9`, `99`, `999`: Unknown / Missing\n\n")
    f.write("| # | Variable Name | Category | Data Type | Sample Value | Description |\n")
    f.write("|---|---|---|---|---|---|\n")

    for idx, col in enumerate(df.columns, 1):
        dtype = str(df[col].dtype)
        sample = str(df[col].iloc[0])
        desc, category = descriptions.get(col, ("Custom / Imputed variable", "Other"))
        f.write(f"| {idx:03d} | `{col}` | {category} | `{dtype}` | `{sample}` | {desc} |\n")

print(f"Data dictionary successfully generated at: {md_file}")
