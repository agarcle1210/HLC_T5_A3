def obtener_divisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores

numero = 28
print(obtener_divisores(numero)) 