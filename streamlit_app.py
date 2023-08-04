import numpy as np
import pickle
import streamlit as st
import altair as alt
from altair.vegalite.v4.api import Chart




#loading the saved model
diabetes_model = pickle.load(open("diabetes_model.sav", 'rb'))



# creating a function for Prediction

def diabetes_prediction(input_data):
    # Changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = diabetes_model.predict(input_data_reshaped)
    print(prediction)

    if prediction[0] == 0:
        return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
    
def main():
    # Giving a title
    st.title('Diabetes Prediction Web App')
    
    
    # Code for Prediction
    diagnosis = ''
    
    # Creating a button for Prediction
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
    st.success(diagnosis)
    
    
    
if __name__ == '__main__':
    main()


#to run this app in browser we want to type streamlit run c:/Users/subha/streamlit/streamlit_app.py in command prompt
