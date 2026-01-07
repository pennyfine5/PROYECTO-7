import pandas as pd
import streamlit as st
import plotly_express as px


df_cars = pd.read_csv('vehicles_us.csv')

# Título de la aplicación

st.header('Análisis de os de Vehículos')


st.write(df_cars.head())

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

st.header('Tipos de Vehículos por Fabricante')

df_cars["manufacturer"] = df_cars["model"].str.split().str[0]
df_count = (
    df_cars.groupby(["manufacturer", "type"])
    .size()
    .reset_index(name="count")
)

fig = px.bar(
    df_count,
    x="manufacturer",
    y="count",
    color="type",
    title="Vehicle types by manufacturer",
)

st.plotly_chart(fig, use_container_width=True)




st.header('Modelo y Precio')

df_year = df_cars[["model_year", "price"]].dropna()

fig = px.scatter(
    df_year,
    x="model_year",
    y="price",
    title="Precio vs Año del modelo",
    labels={
        "model_year": "Año del modelo",
        "price": "Precio"
    },
    opacity=0.5
)


st.plotly_chart(fig, use_container_width=True)

st.header('Precios por condicion del vehiculo')


fig = px.box(
    df_cars,
    x="condition",
    y="price",
    title="Distribución de precios por condición del vehículo"
)

st.plotly_chart(fig, use_container_width=True)



