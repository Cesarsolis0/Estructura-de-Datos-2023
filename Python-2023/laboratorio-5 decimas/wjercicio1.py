import numpy as np

filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

print("Ingrese los valores de la primera matriz:")
matriz1 = np.zeros((filas, columnas))
for i in range(filas):
    for j in range(columnas):
        matriz1[i][j] = int(input(f"valor [{i+1}][{j+1}]: "))

print("Ingrese los valores de la segunda matriz:")
matriz2 = np.zeros((filas, columnas))
for i in range(filas):
    for j in range(columnas):
        matriz2[i][j] = int(input(f"valor [{i+1}][{j+1}]: "))

suma = np.add(matriz1, matriz2)
print(f"la suma de las matrizes es:{suma}")

resta = np.subtract(matriz1, matriz2)
print(f"la resta de las matrizes es:{resta}")