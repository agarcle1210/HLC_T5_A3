def quitar_pares(lista):
    for i in lista:
        if i % 2 == 0:
            lista.remove(i)
    return lista
print(quitar_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))