import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from PIL import Image
import seaborn as sns 
import matplotlib.pyplot as plt



st.title("Stroke Prediction Dashboard")
image = Image.open("stroke.png")

st.image(image, caption="stroke prediction Image")
data = pd.read_csv("stroke data.csv")
st.header("Data Set")
st.dataframe(data)
st.subheader('Effect of smoking habit on stroke')
fig , ax = plt.subplots()
sns.heatmap(data.corr(),ax=ax)
st.write(fig)
st.header("Indias stroke prediction")
a=data.iloc[0,1:5]
st.write(a)
labels=["formly smoked","smoked","never smoked","healthy"]
fig2 , ax = plt.subplots()
ax.pie(a,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
st.write(fig2)
