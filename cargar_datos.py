import json

# Cargar el archivo JSON
with open('tiendas.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Tipo de producto a buscar
tipo_objetivo = "Arroz" 

# Lista para almacenar los precios
precios = []

# Recorrer todas las tiendas y sus productos
for tienda in data["stores"]:
    for producto in tienda.get("products", []):
        if producto.get("type") == tipo_objetivo:
            # Extraer el número del precio (eliminar " cup" y convertir a entero)
            precio_str = producto.get("price", "0 cup").split()[0]
            try:
                precios.append(int(precio_str))
            except ValueError:
                pass  # Ignorar si el precio no es un número válido

# Mostrar la lista de precios
print(precios)
