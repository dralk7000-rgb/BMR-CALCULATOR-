import streamlit as st
from datetime import date

st.title("BMR Calculator")

name = str(st.text_input("Enter the username:"))

dob = st.date_input("Enter your date of birth", min_value=date(1920, 1, 1), max_value=date.today())
today = date.today()
age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

gender = st.radio("Select your gender", ["male", "female"])
height = int(st.number_input("enter your height: "))
weight = float(st.number_input("enter your body weight: "))

if st.button("GET RESULT"):
    mbmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    fbmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

    st.write("Your age is:", age, "years")

    if gender == "male":
        st.write("HI", name, "YOUR BMR=", mbmr)
        if mbmr > 1800:
            st.write("High BMR needs fitness advice")
        if mbmr < 1400:
            st.warning("Low BMR — please consult a doctor.")
        st.audio("result_note.mp3")

    elif gender == "female":
        st.write("HI", name, "YOUR BMR=", fbmr)
        if fbmr > 1400:
            st.write("High BMR needs fitness advice")
        if fbmr < 1400:
            st.warning("Low BMR — please consult a doctor.")
        st.audio("result_note.mp3")


#credit
st.divider()
st.markdown(
    """
    <div style='text-align: center;'>
        <p style='font-weight: bold; font-size: 16px;'>CREDIT</p>
        <p>This BMR Calculator is created by</p>
        <p style='font-weight: bold;'>ALAKH SHUKLA</p>
        <p>Contact: <b>9453536874</b></p>
    </div>
    """,
    unsafe_allow_html=True,
)
