import pandas as pd
import streamlit as st
import plotly_express as px


df_cars = pd.read_csv('vehicles_us.csv')

# Título de la aplicación

st.header('Análisis de Datos de Vehículos')


print(df_cars.head())


fig = px.histogram(df_cars, x="odometer") # crear un histograma
fig.show() # crear gráfico de dispersión



fig = px.scatter(df_cars, x="odometer", y="price") # crear un gráfico de dispersión
fig.show() # crear gráfico de dispersión



# Mostrar información básica (opcional)
st.write('Datos de vehículos usados')

# Botón para histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histogragte ma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(df_cars, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón para gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión')
    fig = px.scatter(df_cars, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

