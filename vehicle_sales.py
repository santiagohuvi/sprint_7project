import pandas as pd
import plotly.express as px
import streamlit as st


data = pd.read_csv('/sprint_7project/vehicles_us.csv')

st.header('Análisis según año/modelo/precio/condición')


