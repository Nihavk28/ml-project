import streamlit as st
import pickle
from PIL import Image

def main():
    st.title(":blue[BANK MARKETING SUCCESS PREDICTION]")
    image=Image.open("download.jpg")
    st.image(image,width=700)
    X1=st.text_input("Age"," ")
    X2=st.radio("Type Of Job",['Admin','Blue_collar','Entrepreneur','Housemaid','Management','Retired','Self_employed','Serives','Student','Technician','Unemployed','Unknown'])
    if X2=='Admin':
        X2=0
    elif X2=='Blue_collar':
        X2=1
    elif X2=='Entrepreneur':
        X2= 2
    elif X2=='Housemaid':
        X2=3
    elif X2=='Management':
        X2=4
    elif X2=='Retired':
        X2=5
    elif X2=='Self-employed':
        X2=6
    elif X2=='Serives':
        X2=7
    elif X2=='Student':
        X2=8
    elif X2=='Technician':
        X2=9
    elif X2=='Unemployed':
        X2=10
    elif X2=='Unknown':
        X2=11

    X3=st.radio("Marital Status",['Divorced','Married','Single'])
    if X3=='Married':
        X3=1
    elif X3=='Divorced':
        X3=0
    else:
        X3=2
    X4=st.radio("Education",['Primary','Secondary','Tertiary','Unknown'])
    if X4=='Primary':
        X4=0
    elif X4=='Secondary':
        X4=1
    elif X4=='Tertiary':
        X4=2
    else:
        X4=3
    X5=st.radio("Do You Have Credit In Default",['Yes','No'])
    if X5=='Yes':
        X5=1
    else:
        X5=0
    X6=st.text_input("Average Yearly Balance In Euros"," ")
    X7=st.radio("Do You Have Housing Loan",['Yes','No'])
    if X7=='Yes':
        X7=1
    else:
        X7=0
    X8=st.radio("Do You Have Peronal Loan",['Yes','No'])
    if X8=='Yes':
       X8=1
    else:
        X8=0
    X9=st.radio("Communication Type",['Cellular','Telephone','Unknown'])
    if X9=='Cellular':
        X9=0
    elif X9=='Telephone':
        X9=1
    else:
        X9=2
    X10=st.text_input("Last contact day of the month"," ")
    X11=st.radio("Last contact month of the year",['January','February','March','April','May','June','July','August','September','October','November','December'])
    if X11=='January':
       X11=4
    elif X11=='February':
        X11=3
    elif X11=='March':
        X11=7
    elif X11=='April':
        X11=0
    elif X11=='May':
        X11=8
    elif X11=='June':
        X11=6
    elif X11=='July':
        X11=5
    elif X11=='August':
        X11=1
    elif X11=='September':
        X11=11
    elif X11=='October':
        X11=10
    elif X11=='November':
        X11=9
    elif X11=='December':
        X11=2

    X12=st.text_input("Last contact duration"," ")
    X13=st.text_input("Number of contacts performed for the campaign"," ")
    X14=st.text_input("Number of days after last campaign"," ")
    X15=st.text_input("Number of contacts performed before the campaign"," ")
    X16=st.radio("Outcome Of The Previous Marketing Campaign",['Failure','Other','Success','Unknown'])
    if X16=='Failure':
      X16=0
    elif X16=='Other':
        X16=1
    elif X16=='Success':
        X16=2
    else:
        X16=3
    features=[X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12,X13,X14,X15,X16]
    model=pickle.load(open('model_d.sav','rb'))
    scaler=pickle.load(open('scaler_00 (3).sav','rb'))
    pred = st.button('PREDICT')

    if pred:
        prediction = model.predict(scaler.transform([features]))
        if prediction == 1:
            st.write("Client will subscribe to term deposit")
        else:
            st.write("Client will not subscribe to term deposit")


main()
