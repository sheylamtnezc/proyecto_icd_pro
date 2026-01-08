def prom(numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

def mediana(numeros):
    if not numeros:
        return 0
    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)
    mitad = n // 2
    if n % 2 == 0:
        return (numeros_ordenados[mitad - 1] + numeros_ordenados[mitad]) / 2
    else:
        return numeros_ordenados[mitad]
    

def moda(numeros):
    if not numeros:
        return None
    frecuencia = {}
    for numero in numeros:
        frecuencia[numero] = frecuencia.get(numero, 0) + 1
    max_frecuencia = max(frecuencia.values())
    modas = [num for num, freq in frecuencia.items() if freq == max_frecuencia]
    if len(modas) == len(frecuencia):
        return None
    return modas

def minimo(numeros):
    if not numeros:
        return None
    return min(numeros)

def maximo(numeros):
    if not numeros:
        return None
    return max(numeros)

def rango(numeros):
    if not numeros:
        return 0
    return max(numeros) - min(numeros)

def varianza(numeros):
    if not numeros:
        return 0
    media = prom(numeros)
    return sum((x - media) ** 2 for x in numeros) / len(numeros)

def conteo_categorias(categorias):
    conteo = {}
    for categoria in categorias:
        conteo[categoria] = conteo.get(categoria, 0) + 1
    return conteo

def porcentaje_categorias(categorias):
    total = len(categorias)
    if total == 0:
        return {}
    conteo = conteo_categorias(categorias)
    porcentaje = {categoria: (count / total) * 100 for categoria, count in conteo.items()}
    return porcentaje

def frecuencia_acumulada(categorias):
    conteo = conteo_categorias(categorias)
    categorias_ordenadas = sorted(conteo.keys())
    frecuencia_acum = {}
    acum = 0
    for categoria in categorias_ordenadas:
        acum += conteo[categoria]
        frecuencia_acum[categoria] = acum
    return frecuencia_acum

def porcentaje_acumulado(categorias):
    total = len(categorias)
    if total == 0:
        return {}
    frecuencia_acum = frecuencia_acumulada(categorias)
    porcentaje_acum = {categoria: (count / total) * 100 for categoria, count in frecuencia_acum.items()}
    return porcentaje_acum