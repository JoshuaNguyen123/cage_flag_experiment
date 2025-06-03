# src/data_loader.py

import pandas as pd
import os

RAW_DATA_PATH = "data/raw/"
PROCESSED_DATA_PATH = "data/processed/"

def load_raw_data(filename):
    """Load raw CSV file from the raw data directory."""
    file_path = os.path.join(RAW_DATA_PATH, filename)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    print(f"🔄 Loading data from {file_path}")
    return pd.read_csv(file_path)


def clean_data(df):
    """Clean and prepare the dataframe."""
    df = df.copy()

    # Normalize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Drop rows missing dwell time
    if "dwell_time_minutes" not in df.columns:
        raise ValueError("Missing required column: dwell_time_minutes")

    df = df.dropna(subset=["dwell_time_minutes"])

    # Ensure correct dtypes
    df["is_flagged"] = df["is_flagged"].astype(int)
    df["dwell_time_minutes"] = df["dwell_time_minutes"].astype(float)

    return df


def save_cleaned_data(df, output_filename="cleaned_data.csv"):
    """Save the cleaned dataframe to the processed data folder."""
    os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)
    output_path = os.path.join(PROCESSED_DATA_PATH, output_filename)
    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned data saved to {output_path}")
