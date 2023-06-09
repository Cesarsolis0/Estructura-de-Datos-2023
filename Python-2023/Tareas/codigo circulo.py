#Calcular la circunferencia y superficie de un círculo

x=float(input("ingrese el radio del circulo:"))

def superficie(x):
    pi=3.14
    return (pi*x**2)

def circunferencia(x):
    pi=3.14
    return (2*pi*x)

print(f"la superficie es: {superficie(x)}")
print(f"la circunferencia es: {circunferencia(x)}")
