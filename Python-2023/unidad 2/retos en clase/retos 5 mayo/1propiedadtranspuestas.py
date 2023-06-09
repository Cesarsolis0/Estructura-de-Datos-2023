import random

filas1 = int(input("Ingrese la cantidad de filas para la primera matriz: "))
columnas1 = int(input("Ingrese la cantidad de columnas para la primera matriz: "))

def matriz(filas1,columnas1):
    matriz=[]
    for i in range(filas1):
        fila=[]
        for j in range(columnas1):
            fila.append(random.randint(1,5))
        matriz.append(fila)
    return matriz

matriz1=matriz(filas1,columnas1)
print("la primera matriz es:")
print(matriz1)

filas2 = int(input("Ingrese la cantidad de filas para la segunda matriz: "))
columnas2 = int(input("Ingrese la cantidad de columnas para la segunda matriz: "))

def matriz(filas2,columnas2):
    matriz=[]
    for i in range(filas2):
        fila=[]
        for j in range(columnas2):
            fila.append(random.randint(1,5))
        matriz.append(fila)
    return matriz

matriz2=matriz(filas2,columnas2)
print("la segunda matriz es:")
print(matriz2)

def suma(matriz1, matriz2):

    if filas1 == filas2 and columnas1 == columnas2:

        filas=len(matriz1)
        columnas=len(matriz1[0])
        resultado=[]
        for i in range(filas):
            fila=[]
            for j in range(columnas):
                fila.append(matriz1[i][j] + matriz2[i][j])
            resultado.append(fila)
        return resultado
    else:
        print("No se pueden sumar las matrices debido a que no tienen la misma cantidad de filas y columnas.")
    
resultadosuma = suma(matriz1, matriz2)
print(f"la suma de las matrices es:\n{resultadosuma}")

def transpuesta(resultadosuma):
    resultado=[]
    for i in range(len(resultadosuma[0])):  
        fila=[]
        for j in range(len(resultadosuma)):
            fila.append(resultadosuma[j][i])
        resultado.append(fila)
    return resultado

transpuestasuma=transpuesta(resultadosuma)
print(f"la transpuesta de la suma es:\n{transpuestasuma}")

def transpuesta(matriz1):
    resultado=[]
    for i in range(len(matriz1[0])):  
        fila=[]
        for j in range(len(matriz1)):
            fila.append(matriz1[j][i])
        resultado.append(fila)
    return resultado

transpuesta1=transpuesta(matriz1)
print(f"la transpuesta de la matriz 1 es:\n{transpuesta1}")

def transpuesta(matriz2):
    resultado=[]
    for i in range(len(matriz2[0])): 
        fila=[]
        for j in range(len(matriz2)):
            fila.append(matriz2[j][i])
        resultado.append(fila)
    return resultado

transpuesta2=transpuesta(matriz2)
print(f"la transpuesta de la matriz 2 es:\n{transpuesta2}")

def suma(transpuesta1, transpuesta2):

    if filas1 == filas2 and columnas1 == columnas2:

        filas=len(transpuesta1)
        columnas=len(transpuesta1[0])
        resultado=[]
        for i in range(filas):
            fila=[]
            for j in range(columnas):
                fila.append(transpuesta1[i][j] + transpuesta2[i][j])
            resultado.append(fila)
        return resultado
    else:
        print("No se pueden sumar las matrices debido a que no tienen la misma cantidad de filas y columnas.")
    
sumatranspuestas = suma(transpuesta1, transpuesta2)
print(f"la suma de las transpuestas de las matrices es:\n{sumatranspuestas}")

if transpuestasuma == sumatranspuestas:
    print("Las transpuestas y la suma son iguales por lo tanto se cumple la 1 propiedad")
else:
    print("no se cumple la 1 propiedad")