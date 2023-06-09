#Desarrollar un algoritmo que permita convertir un número
#entero en sistema decimal a sistema binario.

x=int(input("ingrese un numero:"))

def binario(x):
    binario=""
    proceso=None
    while proceso==None or proceso > 0:
        proceso=x//2
        resto=x%2
        x=proceso
        binario=str(resto)+binario
    return binario
print(binario(x))