import streamlit as st
import joblib

model = joblib.load("mymarksmodel")

st.title("Welcome to LW App")
st.write("This is Vivek")

#hrs = st.text_input("Enter ur hrs: ")

#st.write("Your Study: ",hrs)

hrs = st.slider("Select your hrs: ",0,10,4)

if int(hrs) <= 10:
	finalmarks = model.predict([[ int(hrs) ]])
	st.write("your final marks: ",finalmarks)
else:
	st.write("not supported")
