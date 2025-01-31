def suma_promedio():
    numeros=[1,2,3,4,5]
    suma=0

    for i in numeros:
        suma+=i
    print("La suma de los numeros es", suma)
    print("El promedio de los numeros es", suma/len(numeros))

suma_promedio()