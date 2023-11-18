import streamlit as st
import plotly.express as px
import pandas as pd


df = pd.read_csv('happy.csv')
columns = list(df.columns[1:])
options = [option.replace('_',' ').title() for option in columns]

st.title("In search for Happiness")
x_value = st.selectbox('Select the data for X-axis', options)
y_value = st.selectbox('Select the data for Y-axis', options)


st.subheader(f'{x_value} and {y_value }')

x = df[x_value.replace(' ','_').lower()]
y = df[y_value.replace(' ','_').lower()]

figure = px.scatter(x=x, y=y, labels={'x': x_value, 'y': y_value})
st.plotly_chart(figure)