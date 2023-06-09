# Crear una matriz la cual se debe solicitar por teclado la cantidad de filas y columnas que va a
# contener. También ingresar por consola un escalar. Los elementos de la matriz deben ser
# generados aleatoriamente (0 al 10). Por último, se debe multiplicar la matriz generada por el
# escalar ingresado.
import random
f1=int(input("ingrese el numero de filas de la matriz :"))
c1=int(input("ingrese el numero de columas de la matriz :"))
columnas=c1
filas=f1
def matriz(c1,f1):
    for i in range(filas):
        for j in range(columnas):
            print(random.randint(0,10),end=" ")
        print(" ")
        
matriz(f1,c1)

def multiplicar(matriz):
    n=input("ingrese un numero:")
    filas=len(filas)
    columnas=len(columnas)
    proceso=n*([filas],[columnas])#la idea era el numero n multiplique a todos los elementos que contienen las filas y columnas.
    print(proceso)

multiplicar(matriz)