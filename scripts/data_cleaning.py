import pandas as pd
from pathlib import Path

# Base project directory
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# Load raw data
df = pd.read_csv(DATA_DIR / "raw_data.csv")

print("Before Cleaning:")
print(df.info())

# Remove rows with missing sales_amount
df = df.dropna(subset=["sales_amount"])

# Convert sales_amount to numeric
df["sales_amount"] = pd.to_numeric(df["sales_amount"], errors="coerce")
df = df.dropna(subset=["sales_amount"])

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.dropna(subset=["date"])

print("\nAfter Cleaning:")
print(df.info())

# Save cleaned data
df.to_csv(DATA_DIR / "cleaned_data.csv", index=False)

print("\nCleaned data saved successfully.")
