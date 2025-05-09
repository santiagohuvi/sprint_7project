import pandas as pd
import plotly.express as px
import streamlit as st
#import nbformat as nbf

data = pd.read_csv('https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/Data_sprint_4_Refactored/vehicles_us.csv')

st.header('Análisis según año/modelo/precio/condición')


