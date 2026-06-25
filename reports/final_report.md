# AlphaCare Insurance Solutions – Data‑Driven Risk & Pricing Optimization

**Author:** Hawi Mekonen  
**Date:** June 2026  
**Project:** KAIM 9 – Week 3  
**GitHub:** <https://github.com/makda81/insurance-risk-analytics>

---

## 1. Executive Summary

AlphaCare Insurance Solutions (ACIS) sought to transition from intuition‑based pricing to analytics‑driven decisions using 18 months of historical claim data (Feb 2014 – Aug 2015).

**Key Outcomes:**

- Overall Loss Ratio: `[0.5281836596904845]` – indicating profitability.
- No statistically significant risk differences were found across provinces, zip codes, or gender – supporting fair pricing.
- Best claim probability model (Logistic Regression) achieved an AUC of **0.8045** – useful for identifying high‑risk policies.
- A combined premium formula was demonstrated: a sample policy's suggested premium is **3231.60** vs actual **3145.00** – a small upward adjustment indicating potential underpricing.

**Recommendation:** Implement the combined premium model to adjust individual premiums based on `PastClaims` and `RiskScore`, the most influential features.

---

## 2. Business Understanding & Approach

ACIS is a South African auto‑insurer aiming to grow market share. The project analyzed policy, client, vehicle, and claim data to identify low‑risk segments and build a risk‑based pricing framework.

- **Data:** 18 months of historical policies and claims.
- **Tools:** Python (pandas, scikit‑learn, XGBoost, SHAP), DVC for data versioning, Git/GitHub for collaboration.
- **Methods:** EDA, hypothesis testing (chi‑squared, t‑tests, Mann‑Whitney), regression (claim severity), classification (claim probability), SHAP for interpretability.

---

## 3. Exploratory Data Analysis (EDA)

### 3.1 Loss Ratio (TotalClaims / TotalPremium)

- **Overall:** `[0.5281836596904845]`

**By Province:**

| Province | Loss Ratio |
|----------|------------|
| Addis Ababa | `0.5224` |
| Oromia | `0.5373` |
| Amhara | `0.4776` |
| Somali | `0.6119` |
| Tigray | `0.5260` |

**By VehicleType:**

| Vehicle Type | Loss Ratio |
|--------------|------------|
| Luxury | `0.8424` |
| SUV | `0.5637` |
| Sedan | `0.4040` |
| Hatchback | `0.4202` |

**By Gender:**

| Gender | Loss Ratio |
|--------|------------|
| Male | `0.5276` |
| Female | `0.5287` |

### 3.2 Outliers & Distributions

- `TotalClaims` and `CustomValueEstimate` are highly right‑skewed with extreme outliers. Boxplots confirmed values above the 99th percentile.
- **Handling:** Used log‑transformation and robust models (Mann‑Whitney, tree‑based) to mitigate impact.

### 3.3 Temporal Trends

- Monthly claims `-9.4%` over the 18‑month period, with peaks observed in `2024-05`.

### 3.4 Vehicle Make Analysis

- **Highest Claim Makes:**
`Mercedes-Benz    3787.012618
BMW              3362.890855
Toyota           1372.520878`
- **Lowest Claim Makes:**
`Suzuki     1122.025761
Hyundai    1042.739272
Lifan       918.103987`

---

## 4. Hypothesis Testing (Task 3)

All four null hypotheses failed to be rejected (p > 0.05), indicating no significant risk differences in the tested segments:

| Hypothesis | Test(s) Used | p‑value(s) | Decision |
|------------|--------------|------------|----------|
| Province (Addis Ababa vs Oromia) | Chi2 (freq) + MW (sev) | 0.9199 / 0.5939 | ❌ Fail to reject |
| Zip code (10004 vs 10002) | Chi2 (freq) + MW (sev) | 0.2226 / 0.8081 | ❌ Fail to reject |
| Zip code Margin | t‑test | 0.2642 | ❌ Fail to reject |
| Gender (Male vs Female) | Chi2 (freq) + MW (sev) | 0.9638 / 0.7118 | ❌ Fail to reject |

**Implication:** ACIS can maintain uniform pricing across these segments without adverse selection – but should continue monitoring as more data accumulates.

---

## 5. Predictive Modeling (Task 4)

### 5.1 Claim Severity (Regression)

- **Best Model:** Linear Regression
- **RMSE:** 5,317.07
- **R²:** 0.2007
- **Interpretation:** Low R² is typical for insurance data – the model is useful for **ranking** risk rather than absolute prediction.

### 5.2 Claim Probability (Classification)

- **Best Model:** Logistic Regression
- **Accuracy:** 86.05% (misleading due to class imbalance)
- **F1 Score:** 0.3341 (moderate)
- **AUC:** 0.8045 (good discrimination – 80% chance of ranking a claim higher than a non‑claim)

### 5.3 SHAP Interpretation

- `PastClaims` and `RiskScore` are the most influential features – both increase claim probability.
- `AnnualPremium` has a negative effect (higher premiums correlate with lower risk, possibly due to selection effects).

### 5.4 Premium Formula Demo

For a sample policy:

- P(Claim) = 0.2617
- Predicted Severity = 11,226.94
- Suggested Premium (incl. 10% margin) = **3,231.60**
- Actual Existing Premium = **3,145.00**
- **Difference = +86.60** (slightly underpriced)

---

## 6. Recommendations

- **Implement dynamic pricing:** Use the combined formula `Premium = P(claim) × Severity × 1.1` to adjust premiums at the individual policy level.
- **Focus on key risk factors:** Prioritize `PastClaims` and `RiskScore` in underwriting – they are the strongest predictors.
- **Keep pricing fair:** No significant gender/regional differences were found – avoid discriminatory pricing.
- **Collect more data:** Add telematics (driving behaviour, mileage) to improve model performance (increase R² and F1).

---

## 7. Limitations & Future Work

- **Data:** Only 18 months, limited features. More granular data (accident history, mileage) would improve predictions.
- **Model performance:** R² of 0.20 and F1 of 0.33 are moderate – but usable for ranking and segmentation.
- **Future:** Deploy the model as a scoring engine and continuously retrain with new claims data.

---

## 8. Appendix

- **GitHub Repository:** <https://github.com/makda81/insurance-risk-analytics>
- **Notebooks:** `01_eda.ipynb`, `02_hypothesis_testing.ipynb`, `03_modeling.ipynb`
- **DVC:** Data versioned and reproducible via `dvc-storage`.
