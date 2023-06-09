import array
import random

lista = list(range(1,26))
random.shuffle(lista)
array1 = array.array('I', lista)
print(array1)

n = int(input('¿Que elemento quieres buscar? '))
print(f'El elemento {n} esta en la posición {array1.index(n)+1}.')
