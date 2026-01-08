import json
with open("precio_usd.json", "r", encoding="utf-8") as f:
    data = json.load(f)

lista_usd = [registro["usd"] for registro in data]
lista_fechas = [registro["fecha"] for registro in data]
print(lista_usd)
print(lista_fechas)
