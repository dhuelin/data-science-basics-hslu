import pandas as pd

# Define file path
file_path = "./Data/various_health_care_cost.xlsx"

# Load the file, skipping the first two rows
df = pd.read_excel(file_path, sheet_name=0, skiprows=2)
print(df.head())

# Inspect column names for debugging
print(f"Original column names: {df.columns}")

# Drop unnecessary "Unnamed" columns
df = df.loc[:, ~df.columns.str.contains("Unnamed")]

# Rename columns manually to ensure clarity
df.columns = [
    "Measure", "Absolute Value", "Service Total", "M", "Service Provider Total",
    "Unknown Col 1", "Gender Total", "Unknown Col 2", "Age Group"
] + [str(year) for year in range(2010, 2023)]

# Drop rows where "Age Group" is NaN
df = df[df["Age Group"].notna()]

# Convert year columns to numeric
for year in range(2010, 2023):
    if str(year) in df.columns:
        df[str(year)] = pd.to_numeric(df[str(year)], errors="coerce")

# Save the cleaned data to a CSV file
output_path = "./Data/cleaned_various_health_care_costs.csv"
df.to_csv(output_path, index=False)

print(f"Cleaned data saved to '{output_path}'.")
