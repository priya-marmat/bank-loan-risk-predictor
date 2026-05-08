# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model, scaler and columns
with open('loan_risk_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('train_columns.pkl', 'rb') as f:
    train_columns = pickle.load(f)

# App title
st.title("🏦 Bank Loan Risk Predictor")
st.write("Fill in the details below to check loan risk instantly!")

# ================================
# SECTION 1 — Basic Information
# ================================
st.header("📋 Basic Information")

col1, col2 = st.columns(2)

with col1:
    age            = st.number_input("Age (years)", min_value=18, max_value=90, value=35)
    loan_amount    = st.number_input("Loan Amount (₹)", min_value=0, value=300000, step=10000)
    loan_install   = st.number_input("Monthly Installment (₹)", min_value=0, value=15000, step=1000)
    employment_yrs = st.number_input("Years Employed", min_value=0, max_value=50, value=3)

with col2:
    gender = st.selectbox("Gender", ["Male", "Female"])
    loan_type = st.selectbox("Loan Type", ["Cash loans", "Revolving loans"])
    education = st.selectbox("Education Level", [
        "Lower secondary",
        "Secondary / secondary special",
        "Incomplete higher",
        "Higher education",
        "Academic degree"])
    income_source = st.selectbox("Income Source", [
        "Working", "Pensioner",
        "Commercial associate",
        "State servant", "Unemployed",
        "Student", "Maternity leave"])
    
col3, col4 = st.columns(2)
with col3:
    occupation = st.selectbox("Occupation", [
        "Laborers", "Core staff",
        "Managers", "Drivers",
        "Sales staff", "Cleaning staff",
        "Cooking staff", "Private service staff",
        "Medicine staff", "Security staff",
        "High skill tech staff", "Waiters/barmen staff",
        "Low-skill Laborers", "Realty agents",
        "Secretaries", "IT staff", "HR staff"])
with col4:
    family_status = st.selectbox("Family Status", [
        "Single / not married", "Married",
        "Civil marriage", "Widow", "Separated"])

# ================================
# SECTION 2 — Advanced Information
# ================================
with st.expander("⚙️ Advanced Information (Optional — improves accuracy)"):
    st.write("These scores come from credit bureaus. Higher score = lower risk!")
    col5, col6 = st.columns(2)
    with col5:
        ext2 = st.slider("Credit Score", 
                         min_value=0.0, 
                         max_value=1.0, 
                         value=0.51,
                         help="Credit bureau score between 0 and 1")
    with col6:
        ext3 = st.slider("Bureau Score", 
                         min_value=0.0, 
                         max_value=1.0, 
                         value=0.51,
                         help="External bureau score between 0 and 1")

# ================================
# PREDICT BUTTON
# ================================
st.write("")
if st.button("🎯 Check Loan Risk", use_container_width=True):

    # Education mapping
    education_order = {
        "Lower secondary"              : 1,
        "Secondary / secondary special": 2,
        "Incomplete higher"            : 3,
        "Higher education"             : 4,
        "Academic degree"              : 5
    }

    # Convert years to days
    days_employed = -(employment_yrs * 365)

    # Create empty input
    input_data = {col: 0 for col in train_columns}

    # Fill numerical
    input_data['loan_amount']      = loan_amount
    input_data['loan_installment'] = loan_install
    input_data['education_level']  = education_order[education]
    input_data['days_employed']    = days_employed
    input_data['ext_source_2']     = ext2
    input_data['ext_source_3']     = ext3
    input_data['age_years']        = age
    input_data['applied_amount']   = 0

    # Fill categorical
    if loan_type == 'Revolving loans':
        input_data['loan_type_Revolving loans'] = 1

    if gender == 'Male':
        input_data['gender_M'] = 1

    if income_source == 'Commercial associate':
        input_data['income_source_Commercial associate'] = 1
    elif income_source == 'Maternity leave':
        input_data['income_source_Maternity leave'] = 1
    elif income_source == 'Pensioner':
        input_data['income_source_Pensioner'] = 1
    elif income_source == 'State servant':
        input_data['income_source_State servant'] = 1
    elif income_source == 'Student':
        input_data['income_source_Student'] = 1
    elif income_source == 'Unemployed':
        input_data['income_source_Unemployed'] = 1
    elif income_source == 'Working':
        input_data['income_source_Working'] = 1

    if family_status == 'Married':
        input_data['name_family_status_Married'] = 1
    elif family_status == 'Separated':
        input_data['name_family_status_Separated'] = 1
    elif family_status == 'Single / not married':
        input_data['name_family_status_Single / not married'] = 1
    elif family_status == 'Widow':
        input_data['name_family_status_Widow'] = 1

    occ_col = f'occupation_{occupation}'
    if occ_col in input_data:
        input_data[occ_col] = 1

    # Create dataframe
    input_df = pd.DataFrame([input_data])

    # Scale
    scale_cols = ['loan_amount', 'loan_installment',
                  'days_employed', 'ext_source_2',
                  'ext_source_3', 'age_years',
                  'applied_amount']
    input_df[scale_cols] = scaler.transform(input_df[scale_cols])

    # Predict
    risk_prob = model.predict_proba(input_df)[0][1] * 100

    # ================================
    # SHOW RESULT
    # ================================
    st.header("📊 Risk Assessment Result")

    # Progress bar
    st.progress(int(risk_prob))

    # Metric
    st.metric("Risk Score", f"{risk_prob:.2f}%")

    if risk_prob >= 70:
        st.error(f"🔴 HIGH RISK — {risk_prob:.2f}%")
        st.write("❌ We recommend REJECTING this loan application!")
    elif risk_prob >= 40:
        st.warning(f"🟡 MEDIUM RISK — {risk_prob:.2f}%")
        st.write("⚠️ This application requires MANUAL REVIEW!")
    else:
        st.success(f"🟢 LOW RISK — {risk_prob:.2f}%")
        st.write("✅ This loan application can be APPROVED!")