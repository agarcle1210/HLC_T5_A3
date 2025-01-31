def frecuencia_palabras():
    frase="viva el Betis"
    palabras=frase.split()
    frecuencia={}

    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra]+=1
        else:
            frecuencia[palabra]=1

    return frecuencia

frecuencia_palabras()
print(frecuencia_palabras())