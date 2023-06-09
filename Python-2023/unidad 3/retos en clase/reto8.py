# Realizar un algoritmo que permita insertar elementos en un diccionario (Información de 3
# estudiantes). El docente debe ser capaz de ingresar la siguiente información por teclado:
# ● Nombres de los estudiantes
# ● Nombre de la asignatura
# ● Nota del Laboratorio N°1
# ● Nota del Laboratorio N°2
# La ponderación del Laboratorio N°1 es de un 30% del promedio final y el Laboratorio N°2
# pondera 70% de la nota final.
# El algoritmo debe arrojar toda la información ingresada más el promedio final ponderado.
# Este promedio debe estar en un formato de punto flotante de máximo 1 decimal. Guardar

numestudiantes = 3            #cantidad de estudiantes
curso = []                    #lista que contendra la cantidad de estudiantes

for i in range(numestudiantes):
    estudiantes={}
    estudiantes["nombre"]=input("Ingrese el nombre del estudiante: ")
    estudiantes["asignatura"]=input("ingrese el nombre de la asignatura: ")
    estudiantes["nota laboratorio1"]=float(input("ingrese la nota obtenida en el laboratorio 1 :"))
    estudiantes["nota laboratorio2"]=float(input("ingrese la nota obtenida en el laboratorio 2: "))
    estudiantes["nota final"]=round(float(0.3*estudiantes["nota laboratorio1"]+0.7*estudiantes["nota laboratorio2"]),1)
    curso.append(estudiantes)

# print(curso)

for estudiantes in curso:
    print("Estudiante:",estudiantes["nombre"])
    print("asignatura:",estudiantes["asignatura"])
    print("nota lab1:",estudiantes["nota laboratorio1"])
    print("nota lab2:",estudiantes["nota laboratorio2"])
    print("nota ponderada:",estudiantes["nota final"])
    print()



