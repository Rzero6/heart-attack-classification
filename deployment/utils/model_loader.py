import streamlit as st
import pickle
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

@st.cache_resource
def load_model():
    with open(BASE_DIR / "models" / "tuned_rocauc_model_Logistic Regression.pkl", "rb") as f:
        model = pickle.load(f)
    
    return model