# Se tiene una tupla con las siguientes frutas:
# frutas = (“manzana”, “platano”, “pera”, “naranja”, “frutilla”, “manzana”) ´
# Realizar las siguientes operaciones:
# a) Eliminar los elementos repetidos de la tupla.
# b) Agregar la fruta “mango” por teclado.
# c) Eliminar la fruta platano. ´
# d) Calcular la cantidad de frutas que existen.

#se crea la tupla
frutas = ("manzana","platano","pera","naranja","frutilla","manzana")
print(frutas)
#se crea un conjunto sin elementos repetidos con set y lo convertimos a tupla nuevamente
nueva_lista=tuple(set(frutas))
print(nueva_lista)
#luego la tupla sin repetidos la convertimos a lista y la asignamos a una variable
lista=list(nueva_lista)
#como es una lista podemos usar el metodo append para agregar elemetos
lista.append(input("ingrese el nombre de la fruta :"))
print(lista)
#como queremos eliminar un elemenyo conociso usamos el emtodo remove
lista.remove("platano")
print(lista)
#luego la lista final(con las operaciones listas) la convertimos a tupla
nuevas_frutas = tuple(lista)
#obtenemos la cantidad de elementos con el metodo len
print("la cantidad de frutas es:")
print(len(nuevas_frutas))



