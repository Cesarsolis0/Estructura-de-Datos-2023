# Crear una lista de diccionarios llamada pacientes donde cada diccionario representa a
# un paciente con su informacion personal. Se solicita crear una lista de 4 diccionarios. ´
# Agregar la informacion mediante teclado. La informaci ´ on personal de cada paciente es: ´
# a) Nombre (tipo String)
# b) Edad (tipo Int)
# c) Peso (tipo Float)
# d) Sintomas (Lista de String)
# Ademas realizar una b ´ usqueda en la lista de pacientes para encontrar un paciente en ´
# espec´ıfico por nombre y mostrar su ficha personal correspondiente.

pacientes = []

for i in range(4): 
    paciente = {}
    paciente["Nombre"] = input("ingrese el nombre del paciente:")
    paciente["Edad"] = int(input("ingrese la edad del paciente:"))
    paciente["Peso"] = float(input("ingrese el peso del paciente:"))
    pacientes.append(paciente)

nombre=input("ingrese el nombre del paciente que desea buscar:")

for paciente in pacientes:

    if nombre == paciente["Nombre"]:

        print("nombre:",paciente["Nombre"])
        print("edad:",paciente["Edad"])
        print("peso:",paciente["Peso"])
    else:
        print("no se encontro al paciente.")

### EN PROCESO ###



