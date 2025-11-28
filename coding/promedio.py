def promedio(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)

print(promedio([10,20,30,40,50]))
print(promedio([]))