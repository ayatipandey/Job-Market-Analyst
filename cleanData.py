import pandas as pd

MIN_PLAUSIBLE_SALARY = 10000

def clean_data(df):

    df = df.copy()

    rows_before = len(df)
    df.drop_duplicates(inplace=True)
    duplicates_removed = rows_before - len(df)

    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].str.strip()
    
    if "title" in df.columns:
        df["title"] = df["title"].str.title()
    if "company_name" in df.columns:
        df["company_name"] = df["company_name"].str.title()

    cols_to_fill = ["formatted_work_type", "formatted_experience_level", "work_type", "company_name", "title"]
    for col in cols_to_fill:
        if col in df.columns:
            df[col] = df[col].fillna("Unknown")
    
    if "location" in df.columns:
        df = parse_location(df)

    if "description" in df.columns:
        df = df[df["description"].notna()]
        df = df[df["description"].str.strip() != ""]
    
    if "normalized_salary" in df.columns:
        df["normalized_salary"] = pd.to_numeric(df["normalized_salary"], errors="coerce")
        df.loc[df["normalized_salary"] < MIN_PLAUSIBLE_SALARY, "normalized_salary"] = None

    print("Duplicates removed:", duplicates_removed)
    print("Rows after cleaning:", len(df))
    print("Missing salaries:", df["normalized_salary"].isna().sum())
    
    return df

def parse_location(df):
    cities = []
    states = []

    for location in df["location"]:
        if pd.isna(location) or str(location).strip() == "":
            cities.append("unknown")
            states.append("unknown")
            continue
        parts = str(location).split(",")

        if len(parts) >=2:
            cities.append(parts[0].strip().title())
            states.append(parts[-1].strip().title())
        else:
            cities.append("Unknown")
            states.append(str(location).strip().title())

    df["city"] = cities
    df["state"] = states
    
    return df

def get_missing_report(df):
    missing_counts = df.isnull().sum()
    missing_percentage = (missing_counts/ len(df) * 100)

    report = pd.DataFrame({
        "Column": missing_counts.index,
        "Missing Count": missing_counts.values,
        "Missing Percentage (%)": missing_percentage.values,
    })


    report = report[report["Missing Count"] > 0]
    report = report.sort_values("Missing Count", ascending=False)
    return report

from loadData import load_csv

if __name__ == "__main__": 
    filepath = "postings.csv"
    raw = load_csv(filepath)
    clean = clean_data(raw)

    print("\nMissing value report:")
    print(get_missing_report(clean))