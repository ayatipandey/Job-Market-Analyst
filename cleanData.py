import pandas as pd

# Filter out unrealistic salaries
MIN_PLAUSIBLE_SALARY = 10000

def clean_data(df):

    # Create a copy to avoid changining the original DataFrame
    df = df.copy()

    # Identify and remove duplicates 
    rows_before = len(df)
    df.drop_duplicates(inplace=True)
    duplicates_removed = rows_before - len(df)

    # Strip white spaces 
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].str.strip()
    
    #Captalise the first letter of each word
    if "title" in df.columns:
        df["title"] = df["title"].str.title()
    if "company_name" in df.columns:
        df["company_name"] = df["company_name"].str.title()

    # Fill missing values 
    cols_to_fill = ["formatted_work_type", "formatted_experience_level", "work_type", "company_name", "title"]
    for col in cols_to_fill:
        if col in df.columns:
            df[col] = df[col].fillna("Unknown")
    
    # Seperate cities and states
    if "location" in df.columns:
        df = parse_location(df)

    # Remove rows where job description is misisng 
    if "description" in df.columns:
        df = df[df["description"].notna()]
        df = df[df["description"].str.strip() != ""]
    
    # Convert salary to numeric 
    if "normalized_salary" in df.columns:
        df["normalized_salary"] = pd.to_numeric(df["normalized_salary"], errors="coerce")
        df.loc[df["normalized_salary"] < MIN_PLAUSIBLE_SALARY, "normalized_salary"] = None

    # Terminal Debugging 
    print("Duplicates removed:", duplicates_removed)
    print("Rows after cleaning:", len(df))
    print("Missing salaries:", df["normalized_salary"].isna().sum())
    
    return df

def parse_location(df):
    # Splits the location string
    cities = []
    states = []

    for location in df["location"]:
        if pd.isna(location) or str(location).strip() == "":
            cities.append("Unknown")
            states.append("Unknown")
            continue
        parts = str(location).split(",")

        if len(parts) >=2:
            cities.append(parts[0].strip().title())
            states.append(parts[-1].strip().title())
        else:
            cities.append("Unknown")
            states.append(str(location).strip().title())

    # Add lists as columns to the dataframe
    df["city"] = cities
    df["state"] = states
    
    return df