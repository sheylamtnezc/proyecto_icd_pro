import json
import matplotlib.pyplot as plt

def grafico_precio_usd(archive):
    with open("precio_usd.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    #Extrae los valores de precio
    precios = data["precio"]
    #Separa los valores de fecha y de precio
    dates = [item["fecha"] for item in precios]
    values_usd = [item["usd"] for item in precios]

    # Confección de la gráfica
    plt.figure(figsize=(14, 5))
    plt.plot(dates, values_usd, marker="*", linestyle=":", color="#002d6a", label="USD en CUP")
    plt.title("Cambio del precio del USD")
    plt.xlabel("Fecha")
    plt.ylabel("Precio en CUP")
    plt.xticks(rotation=90, ha ='right')
    plt.grid(True)
    plt.tight_layout()
    plt.legend()
    plt.show()

def promedio_precios_cup(archive):
    with open("tiendas.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    #Diccionario que recopila los valores necesarios
    dictionary_cup = {} 
    #Extrae los valores necesarios para calcular el promedio
    if "stores" in data:
        for store in data["stores"]:
            if "products" in store:
                for product in store["products"]:
                    if "type" in product and "price" in product:
                        type = product["type"]
                        #Deja solo el valor numérico de price
                        price_str = product["price"].split()[0]  
                        # Convierte el precio en float
                        if price_str.isdigit():
                            price = float(price_str)
                            if type not in dictionary_cup:
                                dictionary_cup[type] = []
                            dictionary_cup[type].append(price)
    #Calcula los promedios y los guarda en un diccionario
    prom_cup = {}
    for type in dictionary_cup:
        precios = dictionary_cup[type]
        if len(precios) > 0:
            suma = 0
            for p in precios:
                suma += p
            prom_cup[type] = suma / len(precios)
    return prom_cup

def graficar_promedios(prom_cup):
    keys = list(prom_cup.keys())
    values = list(prom_cup.values())
    plt.figure(figsize=(10, 6))
    plt.bar(keys, values, color="#0661d7")
    plt.axhline(y=3056, color="#1b1833", ls="--", label="Pensión mínima")
    plt.title("Precio promedio por tipo de producto")
    plt.xlabel("Tipo de producto")
    plt.ylabel("Precio promedio (CUP)")
    plt.xticks(rotation=45, ha="right")
    plt.grid(axis='y')
    plt.legend()
    plt.tight_layout()
    plt.show()

def data_habana(archive):
    with open("porciento_mercados.json", "r", encoding="utf-8") as f:
        datos = json.load(f)
    # Busca los datos de las categorías para La Habana
    for j in datos["Por ciento de establecimientos por región"]:
        if j["region"].lower() == "la habana":
            values = [j["estatal"], j["particular"], j["agropecuario"]]  
            labels = ["Estatal", "Particular", "Agropecuario"]
            return labels, values

def grafico_pie_habana(labels, values):
    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, autopct="%1.2f%%", startangle=90, colors=["#ff811e", "#ff0f54", "#ffe546"])
    plt.title("Porcentaje de Establecimientos en La Habana")
    plt.axis("equal")
    plt.show()

def data_ch(archive):
    with open("porciento_mercados.json", "r", encoding="utf-8") as f:
        datos = json.load(f)
    # Busca los datos de las categorías para Centro Habana
    for j in datos["Por ciento de establecimientos por región"]:
        if j["region"].lower() == "centro habana":
            values = [j["estatal"], j["particular"], j["agropecuario"]]  
            labels = ["Estatal", "Particular", "Agropecuario"]
            return labels, values

def grafico_pie_ch(labels, values):
    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, autopct="%1.2f%%", startangle=90, colors=["#e69002", "#bc0800", "#fff78b"])
    plt.title("Porcentaje de Establecimientos en Centro Habana")
    plt.axis("equal")
    plt.show()

def leche_en_polvo(archive):
    with open("tiendas.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    #Extrae los precios de la leche en polvo en las tiendas
    store_prices = []
    for store in data["stores"]:
        store_name = store["names"]
        for product in store["products"]:
            if product["type"] == "Leche en polvo" and product["net weight"] == "1 kg":
                price_str = product["price"].replace(" cup", "").strip()
                if price_str.isdigit():
                    store_prices.append((store_name, int(price_str)))
    return store_prices

def grafica_comp_leche(i):
    #Separa los elementos de las tuplas en listas
    store_names = []
    for pair in leche_en_polvo("tiendas.json"):
        name = pair[0]
        store_names.append(name)
    prices = []
    for pair in leche_en_polvo("tiendas.json"):
        price = pair[1]
        prices.append(price)

    plt.bar(store_names, prices, color="#ff8175")
    plt.axhline(y=1675, color="#f77f00", ls="--", label="Precio topado")
    plt.legend()
    plt.title("Comparación del precio de la leche en polvo")
    plt.xticks(rotation=45, ha="right")
    plt.annotate("Precio topado: 1045 CUP", xy=(len(store_names)//2, 1045), xytext=(len(store_names)//2, 1045), ha="center",)
    plt.tight_layout()
    plt.show()

def spaghetti(archive):
    with open("tiendas.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    #Extrae los precios del spaghetti en las tiendas 
    store_prices = []
    for store in data["stores"]:
        store_name = store["names"]
        for product in store["products"]:
            if product["type"] == "Spaghetti":
                price_str = product["price"].replace(" cup", "").strip()
                if price_str.isdigit():
                    store_prices.append((store_name, int(price_str)))
    return store_prices

def grafica_comp_spaghetti(i):
    #Separa las tuplas en listas
    store_names = []
    for pair in spaghetti("tiendas.json"):
        name = pair[0]
        store_names.append(name)
    prices = []
    for pair in spaghetti("tiendas.json"):
        price = pair[1]
        prices.append(price)

    plt.bar(store_names,prices,color="#ffcd58")
    plt.axhline(y=417, color="#f77f00",ls="--",label="Precio topado")
    plt.legend()
    plt.annotate("Precio topado: 417 CUP", xy=(len(store_names)//2, 417), xytext=(len(store_names)//2, 417), ha="center",)
    plt.title("Comparación del precio de las pastas")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

def aceite(archive):
    with open("tiendas.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    #Extrae los precios del aceite en las tiendas
    store_prices = []
    for store in data["stores"]:
        store_name = store["names"]
        for product in store["products"]:
            if product["type"] == "Aceite vegetal":
                price_str = product["price"].replace(" cup", "").strip()
                if price_str.isdigit():
                    store_prices.append((store_name, int(price_str)))
    return store_prices

def grafica_comp_aceite(i):
    #Separa las tuplas en listas
    store_names = []
    for pair in aceite("tiendas.json"):
        name = pair[0]
        store_names.append(name)
    prices = []
    for pair in aceite("tiendas.json"):
        price = pair[1]
        prices.append(price)
    
    plt.bar(store_names,prices,color="#fcbf49")
    plt.axhline(y=990,color="#f77f00",ls="--",label="Precio topado")
    plt.legend()
    plt.title("Comparación del precio del aceite")
    plt.annotate("Precio topado: 810 CUP", xy=(len(store_names)//2, 810), xytext=(len(store_names)//2, 810), ha="center",)
    plt.xticks(rotation=70, ha="right")
    plt.tight_layout()
    plt.show()

def tasa_usd(archive):
    with open("precio_usd.json", 'r', encoding='utf-8') as f:
        data_precio = json.load(f)
    #Calcula el precio promedio del usd
    precios_usd = []
    for item in data_precio["precio"]:
        if "usd" in item and type(item["usd"]) in [int, float]:
            precios_usd.append(item["usd"])
    tasa_usd = sum(precios_usd) / len(precios_usd)
    return tasa_usd

def promedio_precios_usd(archive):
    with open("tiendas_usd.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    #Diccionario que recopila los valores necesarios
    dictionary_usd = {} 
    #Extrae los valores necesarios para calcular el promedio
    if "usd_stores" in data:
        for store in data["usd_stores"]:
            if "products" in store:
                for product in store["products"]:
                    if "type" in product and "price" in product:
                        type = product["type"]
                        #Deja solo el valor numérico de price
                        price = product["price"] * tasa_usd("precio_usd.json")
                        if type not in dictionary_usd:
                            dictionary_usd[type] = []
                        dictionary_usd[type].append(price)
    #Calcula los promedios y los guarda en un diccionario
    prom_usd = {}
    for type in dictionary_usd:
        precios = dictionary_usd[type]
        if len(precios) > 0:
            suma = 0
            for p in precios:
                suma += p
            prom_usd[type] = suma / len(precios)
    return prom_usd

def grafica_comparacion(prom_cup, prom_usd):
    # Encuentra los tipos de productos comunes en ambos diccionarios    
    tipos_comunes = sorted(prom_cup.keys() & prom_usd.keys())
    # Extrae los valores promedio para cada tipo en común
    valores_cup = [prom_cup[tipo] for tipo in tipos_comunes]
    valores_usd = [prom_usd[tipo] for tipo in tipos_comunes]
    #Declara la variable x y el ancho de las barras
    x = range(len(tipos_comunes))
    ancho = 0.40
    #Graficar
    plt.figure(figsize=(12, 6))
    plt.bar([i - ancho/2 for i in x], valores_cup, width=ancho, label="Tiendas CUP", color="#ffd95d")
    plt.bar([i + ancho/2 for i in x], valores_usd, width=ancho, label="Tiendas USD (convertido)", color="#533527")
    plt.xticks(x, tipos_comunes, rotation=45)
    plt.ylabel("Precio promedio (CUP)")
    plt.title("Comparación de precios promedio por tipo de producto")
    plt.legend()
    plt.tight_layout()
    plt.show()

def porcientos(prom_cup):
    total = 3056  # Pensión mínima en CUP
    data = {}
    for type, price in prom_cup.items():
        porciento = round((price / total) * 100)
        data[type] = porciento
    # Crea un nuevo diccionario ordenado alfabeticamente por tipo de producto
    porcientos = {j: data[j] for j in sorted(data.keys())}
    return porcientos

def grafica_porciento(porcientos):
    labels = list(porcientos.keys())
    values = list(porcientos.values())
    # Define la posición de las barras
    x = [i*1.2 for i in range(len(labels))]
    #Confección de la gráfica
    plt.figure(figsize=(10, 6))
    plt.bar(x, values, color="#fffb44", width=1.0)
    bars = plt.bar(x, values, color="#fffb44", width=1.0)
    # Añade etiquetas de valor encima de cada barra
    for bar, value in zip(bars, values):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f"{value}%", ha="center", va="bottom")
    plt.title("Porcentaje de productos por tipo")
    plt.axhline(y=50, color="#142406", ls="--", label="50% de la pensión mínima")   
    plt.legend()
    plt.ylabel("Porcentaje (%)")
    plt.ylim(0, 100)
    plt.xticks(x, labels, rotation=45, ha="right")
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()