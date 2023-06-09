# Crear un algoritmo donde se solicite dos matrices por consola. Tanto la cantidad de columnas
# como de filas, deben ser ingresadas por teclado. Los elementos de las matrices deben ser
# generados de forma aleatoria (0 al 5). Estas dos matrices se deben sumar. Luego se solicita
# una tercera matriz. Al igual que las dos anteriores, se ingresan columnas y filas por consola, y
# sus elementos son generados aleatoriamente (0 a 5). Esta última matriz se restará con la
# matriz resultante entre la operación de suma
import random
f1=int(input("ingrese el numero de filas de la matriz 1:"))
c1=int(input("ingrese el numero de columas de la matriz 1:"))
columnas=c1
filas=f1
def matriz(c1,f1):
    for i in range(filas):
        for j in range(columnas):
            print(random.randint(0,5),end=" ")
        print(" ")
matriz(f1,c1)

f2=int(input("ingrese el numero de filas de la matriz 2:"))
c2=int(input("ingrese el numero de columas de la matriz 2:"))
columnas=c2
filas=f2
def matriz(c2,f2):
    for i in range(filas):
        for j in range(columnas):
            print(random.randint(0,5),end=" ")
        print(" ")
matriz(f2,c2)


def suma(matriz1,matriz2):   #esta funcion deberia sumar las matrizes generadas anteriormente.
    matriz1=matriz(c1,f1)
    matriz2=matriz(c2,f2)
    proceso=matriz1 + matriz2
    print(proceso)

suma(matriz(c1,f1),matriz(c2,f2))

