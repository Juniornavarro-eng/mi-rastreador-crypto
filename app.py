import streamlit as st
import requests

st.title("📈 Mi Rastreador Crypto")

moneda = st.text_input("¿Qué criptomoneda quieres buscar? (ej. bitcoin, ethereum):", "bitcoin").lower()
cantidad = st.number_input(f"¿Cuántas monedas de {moneda} tienes?:", min_value=0.0, value=1.0)

if st.button("Calcular Valor"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={moneda}&vs_currencies=eur"
    respuesta = requests.get(url)
    datos = respuesta.json()
    
    # Esta línea nueva te mostrará en pantalla qué dice la API de verdad
    st.write("Datos brutos de la API:", datos)
    
    if moneda in datos:
        precio_limpio = datos[moneda]['eur']
        valor_total = cantidad * precio_limpio
        
        st.metric(label=f"Precio actual de 1 {moneda.capitalize()}", value=f"{precio_limpio} €")
        st.success(f"El valor total de tus {cantidad} monedas es: {valor_total:.2f} €")
    else:
        st.error("Moneda no encontrada. Comprueba que el nombre esté bien escrito.")