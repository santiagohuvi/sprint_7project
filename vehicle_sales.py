import pandas as pd
import plotly.express as px
import streamlit as st
#import nbformat as nbf

data = pd.read_csv('/Users/hurvi/101010_git/sprint_7/sprint_7_project/vehicles_us.csv')

st.header('Análisis según año/modelo/precio/condición')


