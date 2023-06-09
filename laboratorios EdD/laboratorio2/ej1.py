# Crear dos matrices donde la cantidad de filas y columnas deben ser generadas de
# forma aleatoria (de 2 a 5). Los elementos de estas matrices deben ingresarse por
# teclado. Luego se deben restar estas matrices, solamente utilizando elementos
# propios de Python (no se permite uso de librerías).

import random
import sys

filas1=int(input("Ingrese el numero de filas:"))
columnas1=int(input("ingrese el numero de columnas:"))

def matriz(filas1,columnas1):
    matriz1=[]
    for i in range(filas1):
        filas=[]
        for j in range(columnas1):
            filas.append(int(input("ingrese los valores que tendra la matriz"+str(i+1)+str(j+1)+":")))
        matriz1.append(filas)
    return matriz1

matriz1=matriz(filas1,columnas1)
print(f"la primera matriz es :\n{matriz1}")

filas2=int(input("Ingrese el numero de filas:"))
columnas2=int(input("ingrese el numero de columnas:"))

def matriz(filas2,columnas2):
    matriz2=[]
    for i in range(filas2):
        filas=[]
        for j in range(columnas2):
            filas.append(int(input("ingrese los valores que tendra la matriz"+str(i+1)+str(j+1)+":")))
        matriz2.append(filas)
    return matriz2

matriz2=matriz(filas2,columnas2)
print(f"la segunda matriz es :\n{matriz2}")


def resta(matriz1,matriz2):

    if filas1 == filas2 and columnas1 == columnas2:

        filas=len(matriz1)
        columnas=len(matriz1[0])
        resultado=[]
        for i in range(filas):
            fila=[]
            for j in range(columnas):
                fila.append(matriz1[i][j] - matriz2[i][j])
            resultado.append(fila)
        return resultado
    else:
        print("No se pueden restar las matrices debido a que no tienen la misma cantidad de filas y columnas.")
        sys.exit()
    
resultadoresta = resta(matriz1, matriz2)
print(f"la resta de las matrices es:\n{resultadoresta}")

# La matriz resultado de la resta anterior se debe multiplicar por una nueva matriz,
# la que debe tener las dimensiones acordes para realizar la multiplicación entre
# ambas matrices. Esta matriz se debe ingresar por teclado tanto la cantidad de
# filas y columnas como sus elementos. Se permite el uso de la librería numpy.

import numpy
filas1=int(input("ingrese la cantidad de filas que tendra la matriz:"))
columnas1=int(input("ingrese la cantidad de columnas que tendra la matriz"))
matriz1=numpy.zeros((filas1,columnas1))
matriz2=resultadoresta

for i in range(0,filas1):
    for j in range(0,columnas1):
        matriz1[i][j]=input("valor del elemto "+str(i+1)+str(j+1)+":")  #o para valores aletorios:random.randint(1,5)
print(matriz1)

def multiplicacion(matriz1,matriz2):
    if filas1 == filas2 and columnas1 == columnas2:
        filas=len(matriz1)
        columnas=len(matriz1[0])
        resultado=[]
        for i in range(filas):
            fila=[]
            for j in range(columnas):
                fila.append(matriz1[i][j] * matriz2[i][j])
            resultado.append(fila)
        return resultado
    else:
        print("No se pueden multiplicar las matrices debido a que no tienen la misma cantidad de filas y columnas.")
        sys.exit()
producto=multiplicacion(matriz1,matriz2)
print(f"el resultado de la multiplicaion es: \n{producto}")

# Por último se debe corroborar la siguiente propiedad de las matrices traspuestas (se puede
# utilizar matrices anteriores)
# (A*B)T = BT*AT

import numpy
filas1=int(input("ingrese la cantidad de filas que tendra la matriz1:"))
columnas1=int(input("ingrese la cantidad de columnas que tendra la matriz1:"))
filas2=int(input("ingrese la cantidad de filas que tendra la matriz2:"))
columnas2=int(input("ingrese la cantidad de columnas que tendra la matriz2:"))
filas3=int(input("ingrese la cantidad de filas que tendra la matriz3:"))
columnas3=int(input("ingrese la cantidad de columnas que tendra la matriz3:"))
matriz1=numpy.zeros((filas1,columnas1))
matriz2=numpy.zeros((filas2,columnas2))
matriz3=numpy.zeros((filas3,columnas3))

for i in range(0,filas1):
    for j in range(0,columnas2):
        matriz1[i][j]=input("valor del elemto "+str(i+1)+str(j+1)+":") 
print(f"la primera matriz es : {matriz1}")

for i in range(0,filas2):
    for j in range(0,columnas2):
        matriz2[i][j]=input("valor del elemento "+str(i+1)+str(j+1))
print(f"la segunda matriz es : {matriz2}")

if (columnas1!=filas2):
    print("no se puede realizar la multiplicacion")
    sys.exit()

for i in range(0,filas1):
    for j in range(0,columnas2):
        for k in range(filas2):
            matriz3[i][j]=matriz3[i][j]+matriz1[i][k]*matriz2[k][j]

print(f"el resultado de la multiplicaciones:\n{matriz3}")

def transpuesta(matriz3):
    resultado=[]
    for i in range(len(matriz3[0])):
        fila=[]
        for j in range(len(matriz3)):
            fila.append(matriz3[j][i])
        resultado.append(fila)
    return resultado

transpuestamultiplicacion=transpuesta(matriz3)
print(f"la transúesta de la matriz es:\n{transpuestamultiplicacion}")

def transpuesta(matriz1):
    resultado=[]
    for i in range(len(matriz1[0])):
        fila=[]
        for j in range(len(matriz1)):
            fila.append(matriz1[j][i])
        resultado.append(fila)
    return resultado
transpuestam1=transpuesta(matriz1)
print(f"la transpuesta de la matriz1 es :{transpuestam1}")

def transpuesta(matriz2):
    resultado=[]
    for i in range(len(matriz2[0])):
        fila=[]
        for j in range(len(matriz2)):
            fila.append(matriz2[j][i])
        resultado.append(fila)
    return resultado
transpuestam2=transpuesta(matriz2)
print(f"la transpuesta de la matriz2 es :{transpuestam2}")

for i in range(0,filas1):
    for j in range(0,columnas2):
        for k in range(filas2):                     #esta funcion deberia multiplicar las matrizes1 y 2 transpuestas
            matriz3[i][j]=matriz3[i][j]+transpuestam1[i][k]*transpuestam2[k][j]

print(f"el resultado de la multiplicacion de transpuestas:\n{matriz3}")

if transpuestamultiplicacion == matriz3:
    print("se cumple la propiedad")
else:
    print("no se cumple la propiedad")
