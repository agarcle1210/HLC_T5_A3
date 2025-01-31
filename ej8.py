def contar(texto):
    vocales="aeiouAEIOU"
    contador_vocales = 0
    contador_consonantes = 0
    for i in texto:
        if i in vocales:
            contador_vocales += 1
        else:
            contador_consonantes += 1
    return ("vocales:", contador_vocales, "consonantes:", contador_consonantes)
print(contar("viva el Betis"))
    
