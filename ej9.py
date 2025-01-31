lista = {"Jose": 9, "Saúl": 7, "Adri": 5}
def notas():
    promedio = 0
    maximo_estudiante  = ""
    mejor_nota = 0
    for name, nota in lista.items():
        if nota > mejor_nota:
            mejor_nota = nota
            maximo_estudiante = name
        promedio += nota/len(lista)
        
    return "Promedio: ",promedio," Nota máxima: ",mejor_nota,"Mejor estudiante: ",maximo_estudiante
print (notas())