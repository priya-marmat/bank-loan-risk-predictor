# 🏦 Bank Loan Risk Predictor

A complete end-to-end machine learning project that predicts the risk percentage of a loan application using real-world bank data.

---

## 🎯 Project Goal

To analyze loan applicants and predict **how risky** a particular loan application is — helping banks make smarter, data-driven decisions on loan approvals.

---

## 📊 Dataset

- **Main Dataset** → 3,00,000+ loan applications
- **Previous Loans Dataset** → 1,00,000+ previous loan records
- **Source** → Home Credit Default Risk (Kaggle)

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core programming |
| Pandas & NumPy | Data cleaning & processing |
| Seaborn & Matplotlib | Data visualization |
| Scikit-learn | ML models & preprocessing |
| XGBoost | Final prediction model |
| SMOTE | Handling imbalanced data |
| Streamlit | Web application |
| Power BI | Interactive dashboard |

---

## 🔄 Project Workflow

```
Raw Data
   ↓
Data Cleaning & Merging
   ↓
Exploratory Data Analysis
   ↓
Feature Selection & Engineering
   ↓
Encoding & Scaling
   ↓
Handle Imbalanced Data (SMOTE)
   ↓
Model Training & Comparison
   ↓
Risk % Prediction
   ↓
Streamlit Web App + Power BI Dashboard
```

---

## 🤖 Models Compared

| Model | Accuracy |
|---|---|
| Logistic Regression | 67.51% |
| Random Forest | 71.25% |
| **XGBoost** ✅ | **74.46%** |

> XGBoost was selected as the final model for best accuracy!

---

## 🎯 Key Features

- ✅ Predicts **risk percentage** for each loan application
- ✅ Categorizes risk as **High / Medium / Low**
- ✅ **Live web app** — enter details and get instant prediction
- ✅ **Power BI dashboard** for visual risk analysis
- ✅ Handles **imbalanced data** using SMOTE
- ✅ **Feature selection** based on visual analysis

---

## 🚀 Run Locally

```bash
# Clone the repository
git clone https://github.com/priya-marmat/bank-loan-risk-predictor.git

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 📦 Requirements

```
streamlit
pandas
numpy
scikit-learn
xgboost
imbalanced-learn
pickle5
```

---

## 📈 Risk Categories

| Risk Score | Category | Decision |
|---|---|---|
| 70% and above | 🔴 High Risk | Reject |
| 40% to 70% | 🟡 Medium Risk | Manual Review |
| Below 40% | 🟢 Low Risk | Approve |

---

## 👤 Author

**Priya Marmat**
- LinkedIn → https://www.linkedin.com/in/priyamarmat/

---
