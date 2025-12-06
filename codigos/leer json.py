import json

# Abrir y cargar el archivo JSON
with open("datos.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

# Acceder a un campo específico
nombre_tienda = datos["nombre"]
productos = datos["productos_alimentos"]

# Usar los datos en otro código
print("Nombre de la tienda:", nombre_tienda)
print("Primer producto:", productos[0]["tipo"])
