def calcular_promedio(estudiantes):
    total_notas = sum(estudiantes.values())
    promedio= total_notas/len(estudiantes)
    
    mejor_estudiante = max(estudiantes, key=estudiantes.get)    
    
    return "El promedio es: " ,promedio, ". Mejor estudiante " , mejor_estudiante , "con nota: ", estudiantes[mejor_estudiante]

print (calcular_promedio({"Andres": 10, "Saúl": 3.5, "Risketo Morales": 6, "Apazram": 7}))