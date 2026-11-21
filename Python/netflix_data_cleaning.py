"""
Netflix Data Cleaning Script
"""

import pandas as pd
import numpy as np

# -----------------------------
# Step 1: Load Dataset
# -----------------------------
df = pd.read_csv("netflix_titles.csv")

# -----------------------------
# Step 2: Dataset Overview
# -----------------------------
print("Shape:", df.shape)
print(df.info())
print(df.isnull().sum())

# -----------------------------
# Step 3: Check Duplicate Rows
# -----------------------------
print("Duplicate Rows:", df.duplicated().sum())

# -----------------------------
# Step 4: Remove Unnecessary Columns
# -----------------------------
df.drop(columns=["show_id", "description"], inplace=True)

# -----------------------------
# Step 5: Rename Columns
# -----------------------------
df.rename(columns={
    "type": "content_type",
    "cast": "cast_members",
    "listed_in": "genres",
    "date_added": "date_added_to_netflix"
}, inplace=True)

# -----------------------------
# Step 6: Remove Duplicate Records
# -----------------------------
df.drop_duplicates(inplace=True)

# -----------------------------
# Step 7: Handle Missing Values
# -----------------------------
fill_cols = ["director", "cast_members", "country", "rating", "duration"]
for col in fill_cols:
    df[col] = df[col].fillna("Unknown")

# -----------------------------
# Step 8: Convert Data Types
# -----------------------------
df["date_added_to_netflix"] = pd.to_datetime(
    df["date_added_to_netflix"],
    errors="coerce"
)

df["release_year"] = df["release_year"].astype("Int64")

# -----------------------------
# Step 9: Remove Extra Spaces
# -----------------------------
text_cols = df.select_dtypes(include="object").columns

for col in text_cols:
    df[col] = df[col].str.strip()

# -----------------------------
# Step 10: Verify Cleaned Data
# -----------------------------
print(df.info())
print(df.head())
print(df.isnull().sum())

# -----------------------------
# Step 11: Export Clean Dataset
# -----------------------------
df.to_csv("netflix_cleaned.csv", index=False)

print("\nCleaning completed successfully!")
print("Cleaned dataset exported as netflix_cleaned.csv")
