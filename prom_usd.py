import json

def promedio_precio_dolar(ruta_archivo):
    with open("precio_usd.json", 'r', encoding='utf-8') as file:
        data = json.load(file)

    precios = [item["usd"] for item in data.get("precio", []) if isinstance(item["usd"], (int, float))]

    if precios:
        return sum(precios) / len(precios)
    else:
        return None
    
promedio = promedio_precio_dolar("precio_usd.json")
print(f"Promedio del precio del dólar: {promedio:.2f} CUP")