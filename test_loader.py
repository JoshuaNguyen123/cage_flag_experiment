# test_loader.py (optional)

from src.data_loader import load_raw_data, clean_data, save_cleaned_data

df = load_raw_data("fake_cage_data.csv")
df_clean = clean_data(df)
save_cleaned_data(df_clean)
