import json

# Función que carga el JSON y devuelve los productos con gramaje conocido
def obtener_productos_con_gramaje(ruta_archivo):
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
    
    productos = datos.get("productos_alimentos", [])
    
    # Filtrar productos que sí tienen gramaje especificado
    filtrados = [p for p in productos if p["gramaje_o_volumen"].lower() != "no especificado"]
    
    return filtrados

# Usar la función
productos_filtrados = obtener_productos_con_gramaje("datos.json")

# Mostrar resultados
for producto in productos_filtrados:
    print(f"{producto['marca']} - {producto['tipo']} - {producto['gramaje_o_volumen']}")