import streamlit as st
import joblib

model = joblib.load("salarymodel")

st.write("Welcome to salary prediction Application")
st.write("Created by vivek")

exp_yrs = st.slider("Select the year of experience: ",0.5,10.5,2.5)

if int(exp_yrs)<11:
    total_salary = model.predict([[ int(exp_yrs) ]])
    st.write("your salary: ",total_salary)
else:
    st.write("Invalid year")