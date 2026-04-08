# 💳 CreditLens — Loan Approval Prediction System

## 🚀 Overview

**CreditLens** is an end-to-end machine learning project designed to predict loan approval status based on an applicant’s financial and credit profile.

The system analyzes key features such as credit score, income, debt, and credit history to classify whether a loan is likely to be **Fully Paid** or **Charged Off**.

project link -> [streamlit link](https://loaniq.streamlit.app/)
---

## 🎯 Problem Statement

Financial institutions face significant risk when approving loans.
Incorrect approvals can lead to defaults, while overly strict decisions may reject reliable customers.

**Goal:**
Build a robust ML model that:

* Predicts loan repayment behavior
* Minimizes financial risk
* Provides real-time predictions via a web interface

---

## 🧠 Model & Approach

### 📌 Data Processing

* Handled missing values (median, mode, defaults)
* Feature engineering:

  * Extracted and binned *Years in current job*
* Standardized categorical values (Purpose mapping)

### ⚙️ Pipeline

* Preprocessing:

  * Imputation
  * Encoding (Ordinal + OneHot)
* Model:

  * Random Forest Classifier

### 📊 Evaluation

* Validation Accuracy: **~82%**
* Observations:

  * High performance on majority class (*Fully Paid*)
  * Lower recall for minority class (*Charged Off*)
  * Indicates class imbalance challenge

---

## ⚠️ Key Insight

> Accuracy alone is misleading in financial systems.

The model prioritizes overall accuracy but requires improvement in detecting **risky loans**, which are more critical in real-world applications.

---

## 🌐 Deployment

The model is deployed using **Streamlit**, allowing users to:

* Input financial details
* Get instant loan predictions
* View confidence scores

---

## 🖥️ Demo Features

* Clean UI with structured input fields
* Real-time prediction
* Probability-based confidence score
* Risk interpretation (Low / Medium / High)

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit
* Joblib

---

## 📂 Project Structure

```id="v9d12x"
CreditLens/
│── app.py
│── loan_model_small.pkl
│── requirements.txt
│── README.md
│── notebook.ipynb
```

---

## ⚙️ Installation

```id="b3k9jd"
git clone https://github.com/Asadullah2412/CreditLens.git
cd CreditLens
pip install -r requirements.txt
streamlit run app.py
```

---

## 📈 Future Improvements

* Improve recall for default prediction using:

  * Class weighting / SMOTE
* Add explainability (SHAP values)
* Enhance UI with analytics dashboard
* Deploy on cloud platforms for scalability

---

## 💡 Conclusion

CreditLens demonstrates a complete ML lifecycle:

* Data preprocessing
* Feature engineering
* Model training & validation
* Deployment

It highlights the importance of handling class imbalance and evaluating models beyond accuracy in financial risk prediction systems.

---

## 👤 Author

**Asadullah**
Machine Learning Enthusiast 🚀

---
