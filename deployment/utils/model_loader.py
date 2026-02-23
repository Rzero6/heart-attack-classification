import streamlit as st
import pickle
from pathlib import Path

BASE_DIR = Path(__file__).parent

@st.cache_resource
def load_model():
    with open(BASE_DIR / "models" / "heart_attack_risk_classifier_xgb_model.pkl", "rb") as f:
        model = pickle.load(f)
    
    return model