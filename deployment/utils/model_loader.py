import streamlit as st
import pickle

@st.cache_resource
def load_model():
    with open("models/heart_attack_risk_classifier_xgb_model.pkl", "rb") as f:
        model = pickle.load(f)
    
    return model