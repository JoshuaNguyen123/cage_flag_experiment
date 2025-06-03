# Cage Flag Optimization Experiment

## 📖 Project Description

This project evaluates whether flagging cages in a fulfillment center improves operational efficiency. Specifically, it compares **mean stowing times** between two groups:

- **Flagged Cages**
- **Unflagged Cages**

We use experimental design principles to determine if flagging provides a statistically significant impact.

---

## 🧪 Methodology

- **Design**: A/B testing setup
- **Metric**: Mean Processing time
- **Statistical Test**: Two-sample t-test
- **Goal**: Identify if flagging leads to faster processing

---

## 📁 Project Structure

cage_flag_experiment/
├── data/ # Raw and processed data
├── notebooks/ # Exploratory notebooks
├── src/ # Source code
├── reports/ # Reports and figures
├── dashboard/ # Optional Streamlit dashboard
├── tests/ # Unit tests
├── README.md # Project overview
└── requirements.txt # Dependencies


---

## ✅ Getting Started

```bash
# Set up environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
