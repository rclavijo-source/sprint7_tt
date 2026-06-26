import pandas as pd
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import streamlit as st


# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# crear una casilla de verificación para construir un histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:  # si la casilla de verificación está seleccionada

    # Lógica a ejecutar cuando se hace clic en el botón
    # Mensaje para mostrar en la aplicación
    hist_button = st.button('Construir histograma')
    st.write('Construir un histograma para la columna odómetro')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)


# crear una casilla de verificación para construir un diagrama de dispersión
build_dispersion = st.checkbox('Construir un diagrama de dispersión')

if build_dispersion:  # si la casilla de verificación está seleccionada

    # Lógica a ejecutar cuando se hace clic en el botón
    # Mensaje para mostrar en la aplicación
    disp_button = st.button('Construir diagrama de dispersión')
    st.write(
        'Creación de un diagrama de dispersión para las columnas odómetro vs precio')
    fig_d = go.Figure(data=[go.Scatter(x=car_data['odometer'],
                                       y=car_data['price'], mode='markers')])
    fig_d.update_layout(
        title_text='Diagrama de Dispersión del Odómetro vs Precio')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig_d, use_container_width=True)
