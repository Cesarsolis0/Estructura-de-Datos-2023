#Determine la distancia entre dos puntos en el espacio (x1,y1, z1) y (x2, y2, z2).
print("ingrese el valor de las siguientes coordenadas")

print("primer punto:")
x1=int(input("coordenada x1:"))
y1=int(input("coordenada y1:"))
z1=int(input("coordenada z1:"))

print("segundo punto:")
x2=int(input("coordenada x2:"))
y2=int(input("coordenada y2:"))
z2=int(input("coordenada z2:"))

resultado=""
def distancia(x1,y1,z1,x2,y2,z2):
    resultado=(x1-x2)**2+(y1-y2)**2+(z1-z2)**2
    return resultado**0.5

print(f"la distancia entre el punto 1 y 2 es: {distancia(x1,y1,z1,x2,y2,z2)}")