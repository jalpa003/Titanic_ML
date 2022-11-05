# This app was adapted from this source: https://github.com/krishnaik06/Dockers/blob/master/app.py
# Streamlit documentation: https://docs.streamlit.io/

# Load Libraries----------------
import numpy as np
import sklearn
import pickle
import pandas as pd
import streamlit as st 

# Import the Model--------------
pickle_in = open("rf.pkl","rb")
rf = pickle.load(pickle_in)


# A function to predict price------------------------------------------
def predict_survival(Pclass,SibSp,Parch,Fare):
    prediction=rf.predict([[Pclass,SibSp,Parch,Fare]])
    print(prediction)
    return prediction


# User Interface--------------------------------------------------------
def main():
    st.title("Titanic Survival Prediction")
    Pclass = st.text_input("# of Ticket class","Type Here")
    SibSp = st.text_input("# of siblings / spouses aboard the Titanic","Type Here")
    Parch = st.text_input("# of parents / children aboard the Titanic","Type Here")
    Fare = st.text_input("Passenger fare:", "Type Here")
    result=""
    if st.button("Predict"):
        result=predict_survival(Pclass,SibSp,Parch,Fare)
        #st.success('The output is {}'.format(result))
        if result[0] == 1:
            st.write("May Survive")
        else:
            st.write("May Not Survive")

if __name__=='__main__':
    main()