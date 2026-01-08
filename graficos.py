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
    plt.plot(fechas, valores_usd, marker='o', linestyle='-', color='green', label='USD en CUP')
    plt.title('Evolución del precio del USD')
    plt.xlabel('Fecha')
    plt.ylabel('Precio en CUP')
    plt.xticks(rotation=90, fontsize=8)
    plt.grid(True)
    plt.tight_layout()
    plt.legend()
    plt.show()

def calcular_promedio_precios(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as file:
        data = json.load(file)

    acumulador = {}  # {tipo: [lista de precios]}

    for tienda in data.get("stores", []):
        for producto in tienda.get("products", []):
            tipo = producto["type"]
            precio_str = producto["price"].split()[0]  # "750 cup" → "750"

            # Validar que el precio es numérico antes de convertir
            if precio_str.replace('.', '', 1).isdigit():
                precio = float(precio_str)
                if tipo not in acumulador:
                    acumulador[tipo] = []
                acumulador[tipo].append(precio)

    promedios = {}
    for tipo in acumulador:
        precios = acumulador[tipo]
        if precios:
            promedios[tipo] = sum(precios) / len(precios)

    return promedios

import matplotlib.pyplot as plt

def graficar_promedio_precios(promedios):
    """
    Genera una gráfica de barras con los precios promedio por tipo de producto.

    Parámetros:
        promedios (dict): Diccionario {tipo_producto: promedio_precio}
    """
    tipos = list(promedios.keys())
    valores = list(promedios.values())

    plt.figure(figsize=(10, 6))
    plt.bar(tipos, valores, color='orange')
    plt.title("Precio promedio por tipo de producto")
    plt.xlabel("Tipo de producto")
    plt.ylabel("Precio promedio (CUP)")
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

ruta = "tiendas.json"
promedios = calcular_promedio_precios(ruta)
graficar_promedio_precios(promedios)

