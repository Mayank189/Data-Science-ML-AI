import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly import graph_objs as go
from sklearn linear_model import LinearRegression
import numpy as np

data=pd.read_csv("data//Salary_Data.csv")

x=np.array(data['YearsofExperience']).reshape(-1,1)
lr=LinearRegression()
lr.fit(x,np.array(data['Salary']))

st.title("Salary Predictor)

nav=st.slidebar.radio("Navigation",["Home","Prediction","Contibute to Dataset"])

if nav== "Home":
    st.image("data//sal.jpg",width=800)
    if st.checkbox("Show Tables"):
        st.table(data)
    
    
    graph=st.selectbox("What kind of Graph ? ",["Non-Interactive","Interactive"])
    
    val=st.slider("Filter data using years",0,20)
    data=data.loc[data["YearsofExperience>=val]]
    if graph=="Non-Interactive":
        plt.figure(figsize=(10,5))
        plt.scatter(data["Years"],data["Salary"])
        plt.ylim(0)
        plt.xlabel("Years of Experience")
        plt.ylabel("Salary")
        plt.tight_layout()
        st.pyplot()
    if graph=="Interactive":
        layout=go.Layout(
            xaxis=dict(range=[0,16]),
            yaxis=dict(range=[0,2100000]))
        fig=go.Figure(data=go.scatter(x=data["YearsofExperience"],y=data["Salary"],mode="marker"),layout==layout)
        st.plotly_chart(fig)
    
    
if nav== "Prediction":
    st.header("Know your Salary")
    val=st.number_input("Enter you exp",0.00,20.00,step=0.25)
    val=np.array(val).reshape(1,-1)
    pred=lr.predict(val)[0]
    
    if st.button("Predit"):
        st.success(f "Your predicted salary is {round(pred)}")
    
if nav=="Contibute":
    st.header("Contribute to the dataset")
    ex=st.number_input("Enter your Experience",0.00,20.00)
    sal=st.number_input("Enter your Experience",0.00,100000.00,step=1000.00)
    if st.button("Submit"):
        to_add={"YearsofExperience":ex,"Salary":sal}
        to_add=pd.DataFrame(to_add)
        to_add.csv("data//Salary_Data.csv",mode=a,header=False,index=False)
        st.success("Submitted Successfully")
    