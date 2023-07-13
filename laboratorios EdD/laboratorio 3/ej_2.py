diccionario = {}
for i in range(3):
    carrera = input("Carrera:")
    departamento = input("DEpartamento:")
    asignaturas_set = set()

    for x in range(3):
        asignatura = input(f"asignatura{x+1}:")
        asignaturas_set.add(asignatura)

    docentes = []
    for x in range(3):
        docente = input(f"Docente {x+1}:")
        docentes.append(docente)

    diccionario[i]={
        "Carrera":carrera,
        "Departamento":departamento,
        "Asignaturas":asignaturas_set,
        "Docentes":docentes
    }
    print()

for i in diccionario.values():
    for clave,valor in i.items():
        print(f"{clave}:{valor}")
    print()