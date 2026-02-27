import streamlit as st
import pandas as pd
from components.input_form import input_form
from utils.encoders_loader import load_encoders
from utils.model_loader import load_model
from utils.input_preprocessor import preprocess_input

st.set_page_config(page_title="Input Data", layout="centered",page_icon="✏️")

data = input_form()

if data is not None:
    # Load artifacts (cached)
    label_encoders, onehot_encoder, risk_encoder = load_encoders()
    model = load_model()

    # Dict → DataFrame
    input_df = pd.DataFrame([data])
    # Preprocess
    X = preprocess_input(input_df, label_encoders, onehot_encoder, risk_encoder)
    # Predict
    prediction = model.predict(X)[0]
    proba = model.predict_proba(X)[0]

    # Output
    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ High Risk of Heart Attack")
    else:
        st.success("✅ Low Risk of Heart Attack")

    st.metric(
        label="Confidence",
        value=f"{max(proba)*100:.2f}%"
    )

    st.write({
        "Low Risk Probability": f"{proba[0]*100:.2f}%",
        "High Risk Probability": f"{proba[1]*100:.2f}%"
    })