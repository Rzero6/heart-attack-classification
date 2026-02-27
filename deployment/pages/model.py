import streamlit as st

st.set_page_config(page_title="Model Information", layout="centered",page_icon="🧠")

st.title("📊 Model & Dataset Information", anchor=False)

st.markdown(
    """
    This page provides transparency about the machine learning model,
    training data, and evaluation metrics used in this application.
    """
)

st.divider()

st.header("🧠 Model Overview")

st.markdown(
    """
    - **Model Type:** Logistic Regression  
    - **Purpose:** Binary classification (Heart Attack Risk: Yes / No)  
    - **Reason for Selection:**  
      - Interpretable results  
      - Suitable for medical risk prediction  
      - Performs well on structured clinical data
    """
)

st.header("📁 Dataset Information")

st.markdown(
    """
    - **Source:** https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset  
    - **Number of Samples:** ~8763 records  
    - **Target Variable:** Heart attack Risk  
    - **Features Include:**  
        - Age  
        - Sex
        - Cholesterol  
        - Heart Rate
        - Diabetes
        - Family History
        - Smoking
        - Obesity
        - Alcohol Consumption
        - Exercise Hours Per Week
        - Diet
        - Previouse Heart Problems
        - Medication Use
        - Stress Level
        - Sedentary Hours Per Day
        - BMI
        - Triglycerides
        - Physical Activity Days Per Week
        - Sleep Hours Per Day
        - Country
        - Blood pressure
    """
)

st.info(
    "All data used is anonymized and intended strictly for educational and research purposes."
)

st.header("⚙️ Data Preprocessing")

st.markdown(
    """
    - Missing values handled appropriately  
    - Categorical features encoded  
    - Numerical features scaled  
    - Handled imbalance data with SMOTE
    - Dataset split into training and testing sets
    """
)

st.header("📈 Model Performance")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("ROC-AUC", "~0.51")

with col2:
    st.metric("Recall", "~0.50")

with col3:
    st.metric("Accuracy", "~0.50")

st.markdown(
    """
    **Metric Interpretation:**
    - **ROC-AUC:** Indicates strong ability to distinguish between high-risk and low-risk cases  
    - **Recall:** High recall ensures most high-risk individuals are correctly identified  
    - **Accuracy:** Overall correctness of predictions
    """
)

st.header("⚠️ Limitations")

st.markdown(
    """
    - The model is trained on a limited public dataset  
    - Predictions may not generalize to all populations  
    - The output should **not** be used as a medical diagnosis
    """
)
st.divider()
st.warning(
    "This application is for educational purposes only and does not replace professional medical advice."
)