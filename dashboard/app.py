import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from scipy.stats import ttest_ind

# Load and prep data
df = pd.read_csv("data/processed/cleaned_data.csv")
df["is_flagged"] = df["is_flagged"].map({0: "Unflagged", 1: "Flagged"})

# Page config
st.set_page_config(page_title="Cage Flag Optimization", layout="centered")
st.title("Cage Flag Optimization Dashboard")

# Section 1: Summary
st.header("Summary Statistics")
summary = df.groupby("is_flagged")["dwell_time_minutes"].agg(["count", "mean", "std"]).round(2).reset_index()
st.dataframe(summary)

# Section 2: Boxplot
st.header("Dwell Time Comparison")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(data=df, x="is_flagged", y="dwell_time_minutes", ax=ax)
ax.set_title("Dwell Time by Flag Status")
ax.set_xlabel("Flagged")
ax.set_ylabel("Dwell Time (minutes)")
st.pyplot(fig)

# Section 3: Statistical Test
st.header("Statistical Test (T-test)")
flagged = df[df["is_flagged"] == "Flagged"]["dwell_time_minutes"]
unflagged = df[df["is_flagged"] == "Unflagged"]["dwell_time_minutes"]
t_stat, p_val = ttest_ind(flagged, unflagged, equal_var=False)

st.write(f"**T-statistic:** {t_stat:.2f}")
st.write(f"**P-value:** {p_val:.4f}")
if p_val < 0.05:
    st.success("Statistically significant difference in dwell time.")
else:
    st.warning("No statistically significant difference found.")
