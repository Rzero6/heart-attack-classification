import streamlit as st
st.set_page_config(page_title="Team", layout="centered")

st.title(":rainbow[Contributors]", anchor=False, width="stretch", text_alignment="center")
c1,c2 = st.columns(2)
with c1:
    st.subheader("Dhimas Primajaya",text_alignment="center")
    st.subheader("Dimas Tubagus Berlian",text_alignment="center")
    st.subheader("Dr. Elsye Maria Rosa",text_alignment="center")
    st.subheader("Jackson",text_alignment="center")
with c2:
    st.subheader("Reynold Kunarto",text_alignment="center")
    st.subheader("Rijki Hardiyanti",text_alignment="center")
    st.subheader("Wadhifatur Rosyidah",text_alignment="center")
    st.subheader("Zufar Bagas P.",text_alignment="center")