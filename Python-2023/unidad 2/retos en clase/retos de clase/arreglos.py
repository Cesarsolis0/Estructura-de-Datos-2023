arreglo=[5,8,6,4,3,9,10,1]
print(arreglo)
def decreciente(arreglo):
    arreglo.sort()
    print (arreglo)

decreciente(arreglo)

import random
# def aleatorio(arreglo):
#     longitud=len(arreglo)
#     for i in arreglo:
#         print(random.randint(0,longitud-1))

# aleatorio(arreglo)
random.shuffle(arreglo)
print(arreglo)