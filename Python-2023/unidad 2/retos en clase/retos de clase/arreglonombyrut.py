def arreglo():

    nombres=[]
    rut=[]

    for i in range(5):

        nombre=input("Ingrese el nombre de la persona: ")
        ci=input("ingrese el rut de la persona: ")

        nombres.append(nombre)
        rut.append(ci)

    print(f"los nombres son : {nombres}")
    print(f"los rut son : {rut}")


    nombres.sort()
    rut.sort()
    print(f"los nombres ordenados alfabeticamente son : {nombres}") 
    print(f"los rut ordenados ascendentemente son : {rut}")

print(arreglo())