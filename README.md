# Diabetes Prediction Web Deployment

Welcome to the Diabetes Prediction Web Deployment GitHub repository! This project focuses on deploying a diabetes prediction model with a user-friendly interface using Streamlit. The repository contains everything you need to set up and run the web application for predicting diabetes.

## Contents

1. **Requirement.txt**: This file includes the required packages and dependencies to run the project successfully. Make sure to install these packages before running the application.

2. **Diabetes.csv**: This dataset serves as the foundation for predicting diabetes. It consists of 9 columns, all containing numerical values. The dataset comprises a total of 769 rows, providing sufficient data for training and testing the model.

3. **Project_3_Diabetes_Prediction.ipynb**: This Jupyter Notebook file contains the code for training the diabetes prediction model. The model is built using an SVM classifier, leveraging the features from the Diabetes.csv dataset.

4. **DiabetesPredictionWebApp.py**: This Python script contains the front-end implementation of the web application, embedded with the trained model from the `Project_3_Diabetes_Prediction.ipynb` notebook. Users can interact with the app by entering relevant diabetes parameters and receiving predictions on whether they are diabetic or not.

## How to Use

1. Install the required packages by running:

   ```
   pip install -r Requirement.txt
   ```

2. Run the web application using the following command:

   ```
   streamlit run DiabetesPredictionWebApp.py
   ```

3. Access the application in your web browser at the provided address (usually `http://localhost:8501`).

4. Enter the necessary diabetes parameters into the interface and receive predictions on the likelihood of being diabetic.

Feel free to explore the code, dataset, and web application to better understand the implementation and customize it according to your needs. If you have any questions or issues, please don't hesitate to reach out.

Happy predicting!
