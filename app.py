import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

st.set_page_config(page_title="Diabetes Prediction App", page_icon=":guardsman:", layout="wide")
st.title("Diabetes Prediction App")
st.write("This app predicts whether a person has diabetes or not based on their health parameters.")
#load the saved model
diabetes_model = pickle.load(open('diabetes_model.pkl', 'rb'))
#getting data from user
st.sidebar.header("User Input Parameters")
col1, col2, col3 = st.columns(3)
with col1:
    pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, value=0)
    glucose = st.number_input("Glucose Level", min_value=0, max_value=200, value=0)
    blood_pressure = st.number_input("Blood Pressure Level", min_value=0, max_value=150, value=0)
with col2:
    skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=0)
    insulin = st.number_input("Insulin Level", min_value=0, max_value=900, value=0)
    bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=0.0)
with col3:
    diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.0)
    age = st.number_input("Age", min_value=0, max_value=120, value=0)


#save the user input in a dataframe
input_data = pd.DataFrame([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]])
#predict whether the person has diabetes or not
diabetes_prediction = diabetes_model.predict(input_data)
if st.button("Predict"):
    if diabetes_prediction[0] == 1:
        st.error("The person is likely to have diabetes.")
    else:
        st.success("The person does not have diabetes.")
