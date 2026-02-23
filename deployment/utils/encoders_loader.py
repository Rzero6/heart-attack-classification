import streamlit as st
import pickle
from pathlib import Path

BASE_DIR = Path(__file__).parent
@st.cache_resource
def load_encoders():
    with open(BASE_DIR / "encoders" / "label_encoder.pkl", "rb") as f:
        label_encoder = pickle.load(f)
    with open(BASE_DIR / "encoders" / "onehot_encoder.pkl", "rb") as f:
        onehot_encoder = pickle.load(f)
    with open(BASE_DIR / "encoders" / "risk_encoder.pkl", "rb") as f:
        risk_encoder = pickle.load(f)
    
    return label_encoder, onehot_encoder, risk_encoder