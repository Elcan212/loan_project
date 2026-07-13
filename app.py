import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model

# Modeli yüklə
model = load_model("loan_model.keras")

st.set_page_config(page_title="Loan Prediction", page_icon="🏦")

st.title("🏦 Loan Approval Prediction")
st.write("Müştərinin məlumatlarını daxil edin.")

# Inputlar
gender = st.selectbox("Gender", ["Female", "Male"])
married = st.selectbox("Married", ["No", "Yes"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["No", "Yes"])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_term = st.number_input("Loan Amount Term", min_value=0)
credit_history = st.selectbox("Credit History", ["No", "Yes"])
property_area = st.selectbox("Property Area", ["Rural", "Semiurban", "Urban"])

# Label Encoding (Notebookdakı LabelEncoder-ə uyğun)
gender = 1 if gender == "Male" else 0
married = 1 if married == "Yes" else 0

dep_map = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3+": 3
}
dependents = dep_map[dependents]

education = 0 if education == "Graduate" else 1
self_employed = 1 if self_employed == "Yes" else 0
credit_history = 1 if credit_history == "Yes" else 0

property_map = {
    "Rural": 0,
    "Semiurban": 1,
    "Urban": 2
}
property_area = property_map[property_area]

if st.button("Predict"):

    features = np.array([[
        gender,
        married,
        dependents,
        education,
        self_employed,
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_term,
        credit_history,
        property_area
    ]])

    prediction = model.predict(features)[0][0]

    st.subheader("Result")

    if prediction >= 0.5:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")

    st.write(f"Prediction Score: **{prediction:.4f}**")