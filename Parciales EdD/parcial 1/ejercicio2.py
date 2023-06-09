#  Crear tres matrices donde la cantidad de filas2 y columnas de todas las matrices serán 3 x 3.
# a. Las 3 matrices deben ser generadas de forma aleatoria.
# b. La primera matriz de números 1 al 10
# c. La segunda matriz de números del 11 al 30
# d. La tercera matriz de números del -1 al -10
# Se solicita demostrar la siguiente propiedad de producto de matrices:
# >>> (A+B)· C = A· C + B · C
# Se pueden utilizar librerías para resolver todo el ejercicio.
import random
import sys

filas1=3
columnas1=3

def matriz(filas1,columnas1):
    matriz=[]
    for i in range(filas1):
        fila=[]
        for j in range(columnas1):
            fila.append(random.randint(1,10))
        matriz.append(fila)
    return matriz

matriz1=matriz(filas1,columnas1)

filas2=3
columnas2=3

def matriz(filas2,columnas2):
    matriz=[]
    for i in range(filas2):
        fila=[]
        for j in range(columnas2):
            fila.append(random.randint(11,30))
        matriz.append(fila)
    return matriz

matriz2=matriz(filas2,columnas2)

filas3=3
columnas3=3

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

#esta funcion calcula la suma entre la matriz A Y B
def suma(matriz1,matriz2):
    if len(matriz1)==len(matriz2):
        suma=[]
        for i in range(len(matriz1)):
            suma.append([])
            for j in range(len(matriz1[i])):
                suma[i].append(matriz1[i][j]+matriz2[i][j])
        return suma
    else:
        print("las matrizes no se pueden sumar ya que no son de la misma longitud")
        sys.exit()
sumas=suma(matriz1,matriz2)

#esta funcion multiplica el resultado de (A+B) por la matriz C
def multiplicar(sumas,matriz2):
    if len(sumas[0]) != len(matriz2):
        print("No se pueden multiplicar las matrices. Las dimensiones no son válidas.")
        sys.exit()
        
    producto=[]
    for i in range(len(sumas)):
        fila=[]
        for j in range(len(matriz2[0])):
            proceso=0
            for k in range(len(matriz2)):
                proceso = proceso + sumas[i][k] * matriz2[k][j]
            fila.append(proceso)
        producto.append(fila)
    return producto

productos=multiplicar(sumas,matriz2)
print("el producto de la multiplicacion entre (A+B)*C es:")
imprimir_matriz(productos)

 #esta funcion multiplica la matriz A * C
def multiplicar(matriz1,matriz3):
    if len(matriz1[0]) != len(matriz3):
        print("No se pueden multiplicar las matrices. Las dimensiones no son válidas.")
        sys.exit()
        
    producto=[]
    for i in range(len(matriz1)):
        fila=[]
        for j in range(len(matriz3[0])):
            proceso=0
            for k in range(len(matriz3)):
                proceso = proceso + matriz1[i][k] * matriz3[k][j]
            fila.append(proceso)
        producto.append(fila)
    return producto
producto1=multiplicar(matriz1,matriz3)

#esta funcion calcula la multiplicacion entre la matriz B*C
def multiplicar(matriz2,matriz3):
    if len(matriz2[0]) != len(matriz3):
        print("No se pueden multiplicar las matrices. Las dimensiones no son válidas.")
        sys.exit()
        
    producto=[]
    for i in range(len(matriz2)):
        fila=[]
        for j in range(len(matriz3[0])):
            proceso=0
            for k in range(len(matriz3)):
                proceso = proceso + matriz2[i][k] * matriz3[k][j]
            fila.append(proceso)
        producto.append(fila)
    return producto
producto2=multiplicar(matriz2,matriz3)
#esta funcion calcula la suma entre la multiplicacion de las matrices A· C + B · C

def suma(producto1,producto2):
    if len(producto1)==len(producto2):
        suma=[]
        for i in range(len(producto1)):
            suma.append([])
            for j in range(len(producto1[i])):
                suma[i].append(producto1[i][j]+producto2[i][j])
        return suma
    else:
        print("las matrizes no se pueden sumar ya que no son de la misma longitud")
        sys.exit()
sumas2=suma(producto1,producto2)
print("la suma de A*C y B*C es:")
imprimir_matriz(sumas2)

if productos==sumas2:
    print("la propiedad se cumple")
else:
    print("la propiedad no se cumple")
    sys.exit()