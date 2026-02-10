import pandas as pd
import streamlit as st
import plotly_express as px


df = pd.read_csv('vehicles_us.csv')

# Limpieza de datos (precios válidos)
df_cars = df[df['price'] > 500].copy()

# Crear fabricante a partir del modelo
df_cars['manufacturer'] = df_cars['model'].str.split().str[0]

# Título de la aplicación

st.header('Análisis de os de Vehículos')

st.caption(
    f"Registros originales: {len(df)} | "
    f"Registros analizados: {len(df_cars)} (precio > $500)"
)



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







st.sidebar.title("🔧 Filtros")

year_range = st.sidebar.slider(
    "Rango de año del vehículo",
    int(df_cars["model_year"].min()),
    int(df_cars["model_year"].max()),
    (
        int(df_cars["model_year"].min()),
        int(df_cars["model_year"].max())
    )
)

selected_makes = st.sidebar.multiselect(
    "Fabricantes",
    options=sorted(df_cars["manufacturer"].unique()),
    default=["toyota", "ford", "chevrolet"]
)

# Aplicar filtros
filtered_df = df_cars[
    (df_cars["model_year"].between(*year_range)) &
    (df_cars["manufacturer"].isin(selected_makes))
]

# -----------------------------
# Main - Contenido
# -----------------------------
st.title("🚘 Análisis de Vehículos Usados en EE.UU.")
st.caption(
    f"Dataset original: {len(df)} registros | "
    f"Datos analizados: {len(filtered_df)} "
    f"(precios > $500)"
)

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Precio promedio", f"${filtered_df['price'].mean():,.0f}")
col2.metric("Precio mediano", f"${filtered_df['price'].median():,.0f}")
col3.metric("Vehículos analizados", len(filtered_df))

st.divider()

# -----------------------------
# Gráficos
# -----------------------------
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Distribución de precios")
    fig_price = px.histogram(
        filtered_df,
        x="price",
        nbins=50
    )
    st.plotly_chart(fig_price, use_container_width=True)

with col_right:
    st.subheader("Precio vs Kilometraje")
    fig_scatter = px.scatter(
        filtered_df,
        x="odometer",
        y="price",
        opacity=0.5
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

st.divider()

# -----------------------------
# Tabla exploratoria
# -----------------------------
st.subheader("Vista de datos")
st.dataframe(
    filtered_df[[
        "model_year", "manufacturer", "model",
        "price", "odometer"
    ]].sort_values("price", ascending=False),
    height=350
)