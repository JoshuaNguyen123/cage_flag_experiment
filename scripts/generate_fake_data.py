# scripts/generate_fake_data.py

import pandas as pd
import numpy as np
import os

# Set seed for reproducibility
np.random.seed(42)

# Configuration
NUM_CAGES = 500
RAW_DATA_PATH = "data/raw/"
os.makedirs(RAW_DATA_PATH, exist_ok=True)

# Flag assignment: 50/50 split
is_flagged = np.random.choice([0, 1], size=NUM_CAGES, p=[0.5, 0.5])

# Simulate dwell times (in minutes)
# Flagged cages have shorter dwell time on average
dwell_times = [
    np.random.normal(loc=12, scale=3) if flag == 1 else np.random.normal(loc=15, scale=3)
    for flag in is_flagged
]

# Build DataFrame
df = pd.DataFrame({
    "cage_id": [f"CAGE_{i+1:04d}" for i in range(NUM_CAGES)],
    "is_flagged": is_flagged,
    "dwell_time_minutes": np.round(dwell_times, 2)
})

# Clip any negative dwell times to zero
df["dwell_time_minutes"] = df["dwell_time_minutes"].clip(lower=0)

# Save to CSV
output_path = os.path.join(RAW_DATA_PATH, "fake_cage_data.csv")
df.to_csv(output_path, index=False)

print(f"Fake data generated and saved to: {output_path}")
