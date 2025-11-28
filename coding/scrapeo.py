import requests
from bs4 import BeautifulSoup
import json

def scrapear_productos(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    categorias = {}
    
    # Suponiendo que cada categoría está en un div con clase 'categoria'
    for categoria_div in soup.select('alimentos'):
        nombre_categoria = categoria_div.find('h2').get_text(strip=True)
        productos = []

        # Suponiendo que cada producto está en un div con clase 'producto'
        for producto_div in categoria_div.select('producto'):
            nombre = producto_div.find('h3').get_text(strip=True)
            descripcion = producto_div.find('p', class_='descripcion').get_text(strip=True)
            precio = producto_div.find('span', class_='precio').get_text(strip=True)

            productos.append({
                'nombre': nombre,
                'descripcion': descripcion,
                'precio': precio
            })

        categorias[nombre_categoria] = productos

    return json.dumps(categorias, indent=2, ensure_ascii=False)

# Ejemplo de uso
url = 'https://mercadoeltencent.com'
resultado_json = scrapear_productos(url)
print(resultado_json)