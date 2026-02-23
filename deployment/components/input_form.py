import streamlit as st
import re

def is_valid_bp_format(bp: str) -> bool:
    bp = bp.strip()
    pattern = r"^\d{2,3}/\d{2,3}$"
    return bool(re.match(pattern, bp))
def extract_bp(bp: str):
    if not is_valid_bp_format(bp):
        return None, None

    systolic, diastolic = bp.split("/")
    return int(systolic), int(diastolic)

countries = [
    "South Korea",
    "Nigeria",
    "United States",
    "Colombia",
    "Thailand",
    "Australia",
    "Argentina",
    "Germany",
    "Canada",
    "China",
    "Brazil",
    "France",
    "United Kingdom",
    "Spain",
    "Vietnam",
    "New Zealand",
    "South Africa",
    "Japan",
    "Italy",
    "India",
    "Other",
]
obesity_bmi_threshold = 30.0
countries.sort()

def is_form_valid(
  age, height, weight, country, blood_pressure, triglycerides, heart_rate, cholesterol, diet
):
    return (
        age > 0
        and height > 0
        and weight > 0
        and triglycerides > 0
        and heart_rate > 0
        and cholesterol > 0
        and country is not None
        and diet is not None
        and is_valid_bp_format(blood_pressure)
    )

def input_form():
    with st.form("input_form"):
        st.subheader("General Info", divider=("gray"), anchor=False)
        a1, a2 = st.columns(2)
        with a1:
            age = st.number_input("Age", min_value=1, value=20)
            height = st.number_input(
                "Height (CM)",
                min_value=1.0,
                value=170.0,
                placeholder="Please input your height in centimeter"
            )
        with a2:
            sex = st.radio("Gender", ["Male", "Female"], horizontal=True)
            weight = st.number_input(
                "Weight (KG)",
                min_value=1.0,
                value=55.0,
                placeholder="Please input your weight in kilogram"
            )
        country = st.selectbox(
            "Country",
            countries,
            index=None,
            placeholder="Select where you live if not listed select 'Others'"
        )
        if country is None:
            st.warning("Select a country, if not listed pick **Other**.")
        
        st.subheader("Medical Info", divider=("gray"), anchor=False)
        
        b1, b2 = st.columns(2)
        with b1:
            blood_pressure = st.text_input(
                "Blood Pressure (Systolic/Diastolic)",
                placeholder="example: 140/80"
            )
            if blood_pressure and not is_valid_bp_format(blood_pressure):
                st.warning("Format must be like 120/80")
            triglycerides = st.number_input(
                "Triglycerides (mg/dL)",
                min_value=0,
                value=150
            )
            diabetes = st.checkbox("Diabetes")
            family_history = st.checkbox("Family History of Heart Disease")
            smoking = st.checkbox("Smoker")
        with b2:
            heart_rate = st.number_input("Heart Rate (bpm)", min_value=1, value=75)
            cholesterol = st.number_input("Cholesterol (mg/dL)", min_value=1, value=200)
            alcohol_consumption = st.checkbox("Alcohol Consumer")
            previous_heart_problems = st.checkbox("Previous Heart Problems")
            medication_use = st.checkbox("Medication Use")

        st.subheader("Lifestyle Info", divider=("gray"), anchor=False)
        diet = st.selectbox(
            "Diet Type",
            ["Average", "Healthy", "Unhealthy"],
            index=None,
            placeholder="Select your diet type"
        )
        stress_level = st.slider(
            "Stress Level (1 = Low, 10 = High)",
            min_value=1,
            max_value=10,
            value=5
        )
        physical_activity_days_per_week = st.slider(
            "Physical Activity Per Week (Days)",
            min_value=0,
            max_value=7,
            value=3
        )
        sleep_hours_per_day = st.slider(
            "Sleep Duration Per Day (Hours)",
            min_value=0.0,
            max_value=24.0,
            value=7.0,
            step=0.5
        )
        exercise_hours_per_week = st.slider(
            "Exercise Per Week (Hours)",
            min_value=0.0,
            value=4.0,
            max_value=24.0*7.0,
            step=.25
        )
        sedentary_hours_per_day = st.slider(
            "Sedentary Per Day (Hours)",
            min_value=0.0,
            max_value=24.0,
            value=6.0,
            step=0.5
        )
        
        
        
        submitted = st.form_submit_button(
            "Submit",
            icon=":material/send:",
            icon_position="right",
            width="stretch",
        )
    if submitted:
        #Validation
        valid = is_form_valid(
            age=age, 
            height=height, 
            weight=weight,
            country=country,
            blood_pressure=blood_pressure,
            triglycerides=triglycerides,
            heart_rate=heart_rate,
            cholesterol=cholesterol,
            diet=diet
            )
        if valid:
            st.success("Submitted")
            bmi = weight/(height*height/10000.0)
            obesity = bmi > obesity_bmi_threshold
            sys, dia = extract_bp(blood_pressure)
            
            data = {
                "Age": age,
                "Sex": sex,
                "Cholesterol": cholesterol,
                "Heart Rate": heart_rate,
                "Diabetes": diabetes,
                "Family History": family_history,
                "Smoking": smoking,
                "Blood Pressure": blood_pressure,
                "Obesity": obesity,
                "Alcohol Consumption": alcohol_consumption,
                "Exercise Hours Per Week": exercise_hours_per_week,
                "Diet": diet,
                "Previous Heart Problems": previous_heart_problems,
                "Medication Use": medication_use,
                "Stress Level": stress_level,
                "Sedentary Hours Per Day": sedentary_hours_per_day,
                "BMI": bmi,
                "Triglycerides": triglycerides,
                "Physical Activity Days Per Week": physical_activity_days_per_week,
                "Sleep Hours Per Day": sleep_hours_per_day,
                "Country": country,
                "Systolic BP": sys,
                "Diastolic BP": dia,
            }
            return data
        else:
            st.error("Data is not valid/empty, check form again.")