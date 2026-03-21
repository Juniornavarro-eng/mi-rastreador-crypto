import requests

# 1. Preguntamos qué moneda quiere buscar
moneda = input("¿Qué criptomoneda quieres buscar? (ej. bitcoin, ethereum): ").lower()

# 2. EL RETO: Preguntamos la cantidad
cantidad_texto = input(f"¿Cuántas monedas de {moneda} tienes?: ")

# Usamos float() para convertir el texto que escribes en un número (incluso si tiene decimales)
cantidad = float(cantidad_texto)

# 3. Preparamos la URL y hacemos la llamada
url = f"https://api.coingecko.com/api/v3/simple/price?ids={moneda}&vs_currencies=eur"
respuesta = requests.get(url)
datos = respuesta.json()

# 4. Extraemos el precio
precio_limpio = datos[moneda]['eur']

# 5. EL RETO: Calculamos el valor total (Cantidad por Precio)
valor_total = cantidad * precio_limpio

# 6. Imprimimos el resultado con un formato más visual
print("\n--- TU PORTAFOLIO ---")
print(f"Precio actual de 1 {moneda}: {precio_limpio} €")
print(f"El valor total de tus {cantidad} monedas es: {valor_total} €")
print("---------------------\n")