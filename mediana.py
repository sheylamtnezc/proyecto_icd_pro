def mediana(lista):
    if not lista:
        return 0
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    mitad = n // 2
    if n % 2 == 0:
        return (lista_ordenada[mitad - 1] + lista_ordenada[mitad]) / 2
    else:
        return lista_ordenada[mitad]
    
print(mediana([10,20,30,40,50]))
print(mediana([]))
print(mediana([10,20,30,40]))