import streamlit as st
import pickle

@st.cache_resource
def load_encoders():
    with open("encoders/label_encoder.pkl", "rb") as f:
        label_encoder = pickle.load(f)
    with open("encoders/onehot_encoder.pkl", "rb") as f:
        onehot_encoder = pickle.load(f)
    with open("encoders/risk_encoder.pkl", "rb") as f:
        risk_encoder = pickle.load(f)
    
    return label_encoder, onehot_encoder, risk_encoder