import numpy
import sys
fila1=int(input("ingrese la cantidad de filas de la primera matriz: "))
columna1=int(input("ingrese la cantidad de columnas de la primera matriz: "))

fila2=int(input("ingrese la cantidad de filas de la segunfa matriz: "))
columna2=int(input("ingrese la cantidad de columnas de la segunda matriz: "))

matriz1=numpy.zeros((fila1,columna1))
matriz2=numpy.zeros((fila2,columna2))
matriz3=numpy.zeros((fila1,columna2))   

for i in range(0,fila1):
    for j in range(0,columna1):
        matriz1[i][j]=input("valor del elemto "+str(i+1)+str(j+1)+":")  

print(f"la primera matriz es:\n{matriz1}")

for i in range(0,fila2):
    for j in range(0,columna2):
        matriz2[i][j]=input("valor del elemento "+str(i+1)+str(j+1))
print(f"la segunda matriz es:\n{matriz2}")

if (columna1!=fila2):
    print("no se puede realizar la multiplicacion")
    sys.exit()

for i in range(0,fila1):
    for j in range(0,columna2):
        for k in range(fila2):
            matriz3[i][j]=matriz3[i][j]+matriz1[i][k]*matriz2[k][j]

print(f"el resulatdo de la multiplicacion es:\n{matriz3}")