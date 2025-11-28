def moda(lista):
    if not lista:
        return None
    frecuencia = {}
    for numero in lista:
        if numero in frecuencia:
            frecuencia[numero] += 1
        else:
            frecuencia[numero] = 1
    max_frecuencia = max(frecuencia.values())
    modas = [num for num, freq in frecuencia.items() if freq == max_frecuencia]
    if len(modas) == len(frecuencia):
        return None  # No hay moda
    return modas

print(moda([10,20,20,30,30,30,40,50]))
print(moda([1,2,3,4,5]))
print(moda([]))