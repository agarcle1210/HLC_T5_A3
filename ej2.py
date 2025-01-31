def eliminar_duplicados(lista_palabras):
    return list(set(lista_palabras))


palabras = ["betis", "villarreal", "betis", "real sociedad", "villarreal"]
resultado = eliminar_duplicados(palabras)
print(resultado)  