import pandas as pd
import streamlit as st
import plotly_express as px

car_data = pd.read_csv('C:/Users/AMD/Desktop/ERIKA/DATA ANALYST/SPRINT 7/PROYECTO SPRINT 7/PROYECTO7/vehicles_us.csv') # leer los datos

st.header("Realice usted mismo su análisis de ventas de vehículos en US")

hist_button = st.checkbox('Construir histograma')

if hist_button: # al hacer clic en el botón
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches') # escribir un mensaje
    fig = px.histogram(car_data, x="odometer")  # crear un histograma
         
    st.plotly_chart(fig, use_container_width=True)   # mostrar un gráfico Plotly interactivo

disp_button = st.checkbox("construir gráfico de dispersión")

if disp_button: # al hacer clic en el botón
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches') # escribir un mensaje
    fig = px.scatter(car_data, x="odometer", y="price") # crear un grafico de dispersión
         
    st.plotly_chart(fig, use_container_width=True)   # mostrar un gráfico Plotly interactivo
         
     
         
         