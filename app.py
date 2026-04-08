

import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("loan_model_small.pkl")

# Page config
st.set_page_config(page_title="Loan Predictor", layout="wide")

# Title
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>💰 Loan Approval Predictor</h1>",
    unsafe_allow_html=True
)

st.markdown("---")

# Layout: 2 columns
col1, col2 = st.columns(2)

# ---------------- LEFT COLUMN ----------------
with col1:
    st.subheader(" Applicant Details")

    term = st.selectbox("Term", ["Short Term", "Long Term"])
    home = st.selectbox("Home Ownership", ["Rent", "Home Mortgage", "Own"])
    purpose = st.selectbox("Purpose", [
        "Debt Consolidation", "Home Renovation / Improvement",
        "Business / Startup Capital", "Car / Vehicle Purchase",
        "Vacation / Travel", "Medical Expenses",
        "Education / Tuition Fees", "Other / Miscellaneous"
    ])

    years_job = st.selectbox("Years in Current Job", ["0-2", "2-5", "5-10", "10+"])

    loan_amt = st.slider("Current Loan Amount", 0, 1000000, 10000)
    credit_score = st.slider("Credit Score", 300, 850, 650)
    income = st.slider("Annual Income", 0, 10000000, 500000)

# ---------------- RIGHT COLUMN ----------------
with col2:
    st.subheader(" Financial Details")

    monthly_debt = st.slider("Monthly Debt", 0, 50000, 5000)
    credit_history = st.slider("Years of Credit History", 0, 40, 10)
    delinq = st.slider("Months since last delinquent", 0, 120, 12)

    open_acc = st.slider("Open Accounts", 0, 20, 5)
    credit_prob = st.slider("Credit Problems", 0, 10, 0)

    credit_balance = st.slider("Current Credit Balance", 0, 1000000, 20000)
    max_credit = st.slider("Maximum Open Credit", 0, 2000000, 50000)

    bankruptcies = st.slider("Bankruptcies", 0, 5, 0)
    tax_liens = st.slider("Tax Liens", 0, 5, 0)

st.markdown("---")

# Prediction button
if st.button(" Predict Loan Status"):

    input_df = pd.DataFrame([{
        'Current Loan Amount': loan_amt,
        'Term': term,
        'Credit Score': credit_score,
        'Annual Income': income,
        'Years in current job': years_job,
        'Home Ownership': home,
        'Purpose': purpose,
        'Monthly Debt': monthly_debt,
        'Years of Credit History': credit_history,
        'Months since last delinquent': delinq,
        'Number of Open Accounts': open_acc,
        'Number of Credit Problems': credit_prob,
        'Current Credit Balance': credit_balance,
        'Maximum Open Credit': max_credit,
        'Bankruptcies': bankruptcies,
        'Tax Liens': tax_liens
    }])

    prediction = model.predict(input_df)[0]

    # Probability
    prob = model.predict_proba(input_df)[0]

    st.markdown("## 🔍 Prediction Result")

    colA, colB = st.columns(2)

    with colA:
        if prediction == 1:
            st.success("✅ Fully Paid (Low Risk)")
        else:
            st.error("❌ Charged Off (High Risk)")

    with colB:
        st.metric("📊 Confidence (Fully Paid)", f"{prob[1]*100:.2f}%")

    # Progress bar
    st.progress(float(prob[1]))

    # Extra insight
    st.markdown("### 📈 Risk Interpretation")

    if prob[1] > 0.8:
        st.success("Very safe applicant 🟢")
    elif prob[1] > 0.6:
        st.info("Moderate risk 🟡")
    else:
        st.error("High risk 🔴")