def crear_diccionario_longitudes(lista_palabras):
    diccionario = {palabra: len(palabra) for palabra in lista_palabras}
    return diccionario

lista_palabras = ["saul", "gitano", "python", "javascript"]
diccionario = crear_diccionario_longitudes(lista_palabras)
print(diccionario)