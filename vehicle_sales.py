import pandas as pd
import plotly.express as px
import streamlit as st


data = pd.read_csv('https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/Data_sprint_4_Refactored/vehicles_us.csv')

st.header('Análisis según año/modelo/precio/condición')

hist_button = st.button('Construir un histograma')
scatter_button = st.button('Construir un grafico de dispersion') 

if hist_button:
    st.write('creacion de un histograma para el conjunto de datos')

    fig1 = px.histogram(data, x = 'odometer')

    st.plotly_chart(fig1, use_container_width=True)

if scatter_button:
    st.write('Grafico de dispersion para el conjunto de datos comparando el modelo del auto con su precio')

    fig2 = px.scatter(data, y = 'price', x = 'model_year', hover_data = 'model', color = 'condition')
    

    st.plotly_chart(fig2, use_container_width=True)

  


