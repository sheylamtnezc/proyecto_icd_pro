import json
import matplotlib.pyplot as plt
import os

# Load JSON data
def grafico_lecheenpolvo(archive):
    with open("tiendas.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    store_prices = []
    for store in data["stores"]:
        store_name = store["names"]
        for product in store["products"]:
            if product["type"] == "Leche en polvo" and product["net weight"] == "1 kg":
                price_str = product["price"].replace(" cup", "").strip()
                if price_str.isdigit():
                    store_prices.append((store_name, int(price_str)))

    store_names = [name for name, _ in store_prices]
    prices = [price for _, price in store_prices]

    plt.bar(store_names,prices,color="#7c5c4b")
    plt.axhline(y=1045,color="#d5ba9f",ls="--",label="Precio topado")
    plt.legend()
    plt.title("Comparación del precio de la leche en polvo")
    plt.annotate("Precio topado: 1045",(1,2000),(0,1000))
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

grafico_lecheenpolvo("tiendas.json")