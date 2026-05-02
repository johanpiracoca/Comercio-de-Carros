# Cargar liberias
import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px

# Cargar datos
car_data = pd.read_csv("C:/Users/jhoan/Escritorio/ACADEMICO/TRIPLE_TEN/CIENCIA_DE_DATOS/SPRINT_7/Proyecto/Comercio_de_autos/vehicles_us.csv")

# Poner título
st.header('¡Lo mejor en el mundo de los automoviles!', divider = "gray")

st.divider()

# Descargar dataset
st.subheader("Oprime y Descarga")
st.download_button(
    label = "Descargar dataset", 
    data = car_data.to_csv(index=False), 
    file_name = "car_data.csv"
)

st.divider()

# Muestra de la organizacion del data frame y sus datos
st.subheader("Aca tienes una muestra de los datos utilizados")
muestra = car_data.sample(100)
st.write(muestra)

st.divider()

# Grafico de barras de la clasificacion de autos segun su color y tipo
st.subheader("Color preferido de los clientes")

total_color = car_data.groupby('paint_color')['type'].value_counts()
df_total_color = total_color.reset_index(name='car_count')

bar_plot = px.bar(
    df_total_color,
    x = 'type',
    y = 'car_count',
    labels = {
        'type': 'Tipo de automóvil',
        'car_count': 'Cantidad',
        'paint_color': 'Colores'
        },
    title = "Clasificacion de autos segun su tipo y color",
    color = 'paint_color',
    color_discrete_map={
        'black': 'black',
        'blue': 'blue', 
        'brown': 'brown',
        'custom': 'gray',  
        'green': 'green',
        'grey': 'gray',
        'orange': 'orange',
        'purple': 'purple',
        'red': 'red',
        'silver': 'silver',
        'white': 'lightgray', 
        'yellow': 'yellow'
    },
    width = 700,
    height = 400
)
st.plotly_chart(bar_plot, use_container_width=True)

st.divider()

# Histograma de la variable Odometer
df_odometer = car_data.dropna(subset=['odometer'])

hist_plot = px.histogram(
    df_odometer, 
    x = 'odometer', 
    labels = {'fuel': 'Tipo de Combustible'},
    title = f"Distribución de Kilometraje clasificado Tipo de Combustible", 
    color = 'fuel',
    color_discrete_map={
        'diesel': 'black',
        'hybrid': 'blue', 
        'electric': 'green',
        'gas': 'red',
        'other': 'lightgray'
    }, 
    marginal = "box", 
    width = 700, 
    height = 400
)

# Grafico de dispersion Año de Modelo vs Precio
disp_plot = px.scatter(
    car_data, 
    x = 'model_year', 
    y = 'price', 
    labels = {'model_year': 'Año de Modelo',
              'price': 'Precio',
              'transmission': 'Transmision'},
    color = 'transmission', 
    title = f"Dispersión Año de Modelo vs. Precio", 
    color_discrete_map={  
        'automatic': 'green',
        'manual': 'orange',
        'other': 'lightgray'},
    width = 700, 
    height = 400
)

# Histograma y Dispersion interactivos
st.subheader("Algunos Estadisticos...")
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un diagrama de dispersión')

if build_histogram:

    st.plotly_chart(hist_plot, use_container_width=True)

    c1, c2, c3 = st.columns(3)

    with c1: 
        prom_odo = np.mean(df_odometer['odometer'])
        st.metric(
            label = "Media",
            value = "{:.1f}".format(prom_odo)
            )
    with c2:
        med_odo = np.median(df_odometer['odometer'])
        st.metric(
            label = "Mediana",
            value = "{:.1f}".format(med_odo)
            )
    with c3:
        desv_odo = np.std(df_odometer['odometer'])
        st.metric(
            label = "Desviación",
            value = "{:.1f}".format(desv_odo)
            )

st.divider()

if build_scatter:

    st.plotly_chart(disp_plot, use_container_width=True)

    correlacion = car_data['model_year'].corr(car_data['price'])
    st.metric(
        label = "Correlación de Pearson",
        value = "{:.1%}".format(correlacion)
    )

st.divider()
