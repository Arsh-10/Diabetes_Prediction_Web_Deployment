import numpy as np 
import pickle
import pandas as pd
import streamlit as st
import pipreqs

#loading save model
loaded_model = pickle.load(open('trained_model.pkl', 'rb'))

def diabetesPrediction(input):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'
    
    
def main():
    #title
    st.title('Diabetes Prediction Web App')
    
    #getting input from users
    #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
    Pregnancies = st.text_input('Number Of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI Value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of person')
    
    #code for prediction
    diagnosis = ''
    
    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        diagnosis = diabetesPrediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age ])
        
    st.success(diagnosis)
    
if __name__ == '__main__':
    main()
