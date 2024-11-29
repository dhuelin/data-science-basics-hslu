import pandas as pd

# Define file path
file_path = "./Data/various_health_care_cost.xlsx"

# Load the raw data
raw_df = pd.read_excel(file_path, sheet_name=0, header=None)

# Extract headers from rows 3 and 4
header_years = raw_df.iloc[2].fillna("")  # Replace NaN with empty strings
header_totals = raw_df.iloc[3].fillna("")  # Replace NaN with empty strings

# Combine headers into meaningful names, ensuring all are strings
headers = []
for year, total in zip(header_years, header_totals):
    year = str(year).strip()  # Ensure year is a string
    total = str(total).strip()  # Ensure total is a string
    if year:
        headers.append(f"{year}_{total}" if total else year)
    else:
        headers.append(total if total else "Unknown")

# Assign headers to the data
data = pd.read_excel(file_path, sheet_name=0, skiprows=4, header=None)
data.columns = headers[:len(data.columns)]

# Filter rows based on column G (gender grouping)
combined_data = data[data["Geschlecht - Total"] == -9].copy()
male_data = data[data["Geschlecht - Total"] == 1].copy()
female_data = data[data["Geschlecht - Total"] == 2].copy()

# Drop unnecessary columns
columns_to_drop = ["M", "Art der Leistungserbringung - Total", "Geschlecht - Total"]
for df in [combined_data, male_data, female_data]:
    df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True, errors="ignore")

# Identify and process year columns
year_columns = [col for col in data.columns if isinstance(col, str) and col.startswith("201")]
for df in [combined_data, male_data, female_data]:
    for col in year_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

# Save cleaned datasets
combined_data.to_csv("./Data/cleaned_combined_data.csv", index=False)
male_data.to_csv("./Data/cleaned_male_data.csv", index=False)
female_data.to_csv("./Data/cleaned_female_data.csv", index=False)

print("Cleaned datasets saved:")
print("- Combined: cleaned_combined_data.csv")
print("- Male: cleaned_male_data.csv")
print("- Female: cleaned_female_data.csv")
