#Diseña un programa que solicite el valor de los tres lados de un triángulo y calcule el valor
#de su área y perímetro. 

print("ingrese el valor de los tres lados del triangulo")
lado1=int(input("ingrese el valor del lado 1:"))
lado2=int(input("ingrese el valor del lado 2:"))
lado3=int(input("ingrese el valor del lado 3:"))

def perimetro(lado1,lado2,lado3):
    resultado=(lado1+lado2+lado3)
    return resultado

def area(lado1,lado2,lado3):
    s=perimetro(lado1,lado2,lado3)/2
    proceso=s*(s-lado1)*(s-lado2)*(s-lado3)
    return proceso**0.5
    
print(f"el area del triangulo es: {area(lado1,lado2,lado3)}")
print(f"el perimetro del triangulo es: {perimetro(lado1,lado2,lado3)}")