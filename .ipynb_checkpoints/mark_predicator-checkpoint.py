import streamlit as st
import joblib

model = joblib.load("marks.model")

st.title("Welcome to LW App")
st.write("This is Vivek")

hrs = st.text_input("Enter ur hrs: ")

st.write("Your Study: ",hrs)

if int(hrs) <= 10:
	finalmarks = model.predict([[int(hrs)]])
	st.write("your final marks: ",finalmarks)
else:
	st.write("not supported")
