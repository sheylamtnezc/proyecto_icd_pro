import json
import matplotlib.pyplot as plt

def grafico_precio_usd(archivo_json):
# Cargar los datos del archivo JSON
    with open('precio_usd.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Acceder a la lista de precios dentro de la clave "precio"
    precios = data["precio"]

    # Extraer fechas y valores de USD (sin convertir fechas a datetime)
    fechas = [item['fecha'] for item in precios]
    valores_usd = [item['usd'] for item in precios]

    # Crear la gráfica
    plt.figure(figsize=(14, 6))
    plt.plot(fechas, valores_usd, marker='o', linestyle='-', color='#9b7e59', label='USD en CUP')
    plt.title('Evolución del precio del USD')
    plt.xlabel('Fecha')
    plt.ylabel('Precio en CUP')
    plt.xticks(rotation=90, fontsize=8)
    plt.grid(True)
    plt.tight_layout()
    plt.legend()
    plt.show()

grafico_precio_usd("precio_usd.json")