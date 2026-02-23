import streamlit as st

st.set_page_config(
    page_title="Heart Attack Risk Classifier",
    page_icon="❤️"
)

pg = st.navigation({
    "Main": [
        st.Page("pages/index.py", title="Landing Page", icon=":material/home:"),
        st.Page("pages/predict.py", title="Predict Heart Attack", icon=":material/edit:")
    ],
    "About": [
        st.Page("pages/team_credits.py", title="Team", icon=":material/diversity_1:")
    ],
})

pg.run()