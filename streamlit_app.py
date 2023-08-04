import numpy as np
import pickle
import streamlit as st
import altair as alt
from altair.vegalite.v4.api import Chart

# Loading the saved model
diabetes_model = pickle.load(open("scaler.sav", 'rb'))

# Creating a function for Prediction
def diabetes_prediction(input_data):
    # Changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # Reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = diabetes_model.predict(input_data_reshaped)
    print(prediction)

    if prediction[0] == 0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'

def main():
    # Giving a title
    st.title('Diabetes Prediction Web App')
    
    # Getting the input data from the user
    Pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=20, step=1)
    Glucose = st.number_input('Glucose Level', min_value=0, max_value=500, step=1)
    BloodPressure = st.number_input('Blood Pressure value', min_value=0, max_value=200, step=1)
    SkinThickness = st.number_input('Skin Thickness value', min_value=0, max_value=100, step=1)
    Insulin = st.number_input('Insulin Level', min_value=0, max_value=1000, step=1)
    BMI = st.number_input('BMI value', min_value=0, max_value=100, step=0.1)
    DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', min_value=0, max_value=2, step=0.01)
    Age = st.number_input('Age of the Person', min_value=0, max_value=150, step=1)
    
    # Code for Prediction
    diagnosis = ''
    
    # Creating a button for Prediction
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
    st.success(diagnosis)

if __name__ == '__main__':
    main()


#to run this app in browser we want to type streamlit run c:/Users/subha/streamlit/streamlit_app.py in command prompt
