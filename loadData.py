import pandas as pd
import os

REQUIRED_COLUMNS = {"job_id","title","description","location","company_name","formatted_work_type","normalized_salary",}

COLUMN_LABELS = {
    "job_id": "Job ID",
    "title": "Job Title",
    "description": "Job Description",
    "location": "Location",
    "company_name": "Company Name",
    "formatted_work_type": "Work Type",
    "normalized_salary": "Normalized Salary",
}

def load_csv(filepath):

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    if not filepath.endswith(".csv"):
        raise ValueError("Only .csv files are supported.")

    df = pd.read_csv(filepath)

    if df.empty:
        raise ValueError("No data found.")
    
    missing_columns = []
    for column in REQUIRED_COLUMNS:
        if column not in df.columns:
            missing_columns.append(COLUMN_LABELS[column])

    if missing_columns:
        raise ValueError(f"The CSV is missing required columns: {', '.join(missing_columns)}.")
    
    return df