def min_max(lista):
    if not lista:
        return None, None
    return min(lista), max(lista)   

print(min_max([10,20,30,40,50]))
print(min_max([]))
print(min_max([5]))