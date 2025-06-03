# 🧪 Cage Flag Optimization Experiment Report

## 1. Objective

The goal of this experiment was to determine whether flagging cages in a fulfillment center impacts their **dwell time**, defined as the time a cage waits before being stowed.

---

## 2. Methodology

- **Design**: A/B comparison between flagged and unflagged cages.
- **Data**: Synthetic data generated with 500 entries.
- **Primary Metric**: Dwell time in minutes.
- **Analysis**: Summary statistics, visualizations, and an independent two-sample t-test.

---

## 3. Summary Statistics

| Flag Status | Count | Mean Dwell Time (min) | Std Dev |
|-------------|-------|------------------------|---------|
| Flagged     | 259   | 12.17                  | 3.10    |
| Unflagged   | 241   | 14.86                  | 2.92    |

These results suggest that flagged cages had, on average, **2.69 fewer minutes** of dwell time compared to unflagged cages.


*(Replace with your actual values from the notebook)*

---

## 4. Visual Analysis

![Boxplot](figures/boxplot.png)  
*(Save your matplotlib figures using `plt.savefig('../reports/figures/boxplot.png')`)*

- Flagged cages show a consistently lower dwell time.
- Distribution appears tighter with fewer high outliers.

---

## 5. Statistical Test

- **T-statistic**: -10.23  
- **P-value**: 0.00001

**Interpretation**:  
Because the p-value < 0.05, we reject the null hypothesis. There is a **statistically significant difference** in dwell times. Flagged cages had **lower average dwell time**.

---

## 6. Conclusion

The results suggest that **flagging cages significantly reduces dwell time** in the fulfillment center. This insight may guide operational policy toward expanding the use of cage flagging.

---

## 7. Next Steps

- Validate results with real operational data.
- Measure downstream impacts (e.g., stowing speed, labor cost).
- Consider automated flagging systems or real-time dashboards.

