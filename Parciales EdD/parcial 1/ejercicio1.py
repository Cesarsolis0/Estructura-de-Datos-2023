# Obtener la matriz resultante de la siguiente operación:
# >>> (A3 · B-1 · C) + (A3)-1 , para A, B, C ∈ IR4×4
# Todas las matrices se pueden generar de forma aleatoria. Sus elementos se
# deben encontrar del 0 al 10. Se pueden utilizar bibliotecas.
import random
import numpy as np

filas1=4
columnas1=4

def matriz(filas1,columnas1):
    matriz=[]
    for i in range(filas1):
        fila=[]
        for j in range(columnas1):
            fila.append(random.randint(1,10))
        matriz.append(fila)
    return matriz

matriz1=matriz(filas1,columnas1)

filas2=4
columnas2=4

def matriz(filas2,columnas2):
    matriz=[]
    for i in range(filas2):
        fila=[]
        for j in range(columnas2):
            fila.append(random.randint(11,30))
        matriz.append(fila)
    return matriz

matriz2=matriz(filas2,columnas2)

filas3=4
columnas3=4

def matriz(filas3,columnas3):
    matriz=[]
    for i in range(filas3):
        fila=[]
        for j in range(columnas3):
            fila.append(random.randint(-10,-1))
        matriz.append(fila)
    return matriz

matriz3=matriz(filas3,columnas3)

def imprimir_matriz(matriz):
    for filas in matriz:
        print(filas)
    print()

print("la primera matriz es:")
imprimir_matriz(matriz1)
print("la segunda matriz es:")
imprimir_matriz(matriz2)
print("la tercera matriz es:")
imprimir_matriz(matriz3)

#matriz elevada a 3
def elevada(matriz1):

    for i in range(0,filas1):
        for j in range(0,columnas1):
            for k in range(filas1):
                matriz2[i][j]=matriz2[i][j]+matriz1[i][k]*matriz1[k][j]
    return matriz1
A3=elevada(matriz1)

print(elevada(matriz1))

def inversa(matriz):
    inv=np.linalg.inv(matriz)
    return inv

B1=inversa(matriz2)
print(B1)

A31=inversa(A3)
def multiplicar(A3,B1,matriz3):
    resultado=[]
    for i in range(filas3):
        fila=[]
        for j in range(columnas3):
            proceso=0
            for k in range(filas1):
                proceso=proceso+A3[i][k]*B1[k][j]*matriz3[i][j]
            fila.append(proceso)
        resultado.append(fila)
    return resultado

multiplicacion=multiplicar(A3,B1,matriz3)


def suma(multiplicacion,A31):
    if len(multiplicacion)==len(A31):
        suma=[]
        for i in range(len(multiplicacion)):
            suma.append([])
            for j in range(len(multiplicacion[i])):
                suma[i].append(multiplicacion[i][j]+A31[i][j])
        return suma
sumas2=suma(multiplicacion,A31)
print("el resultado de (A3 · B-1 · C) + (A3)-1  es:")
imprimir_matriz(sumas2)
