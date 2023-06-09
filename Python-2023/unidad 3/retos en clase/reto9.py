# EJERCICIO DE PILA
# Realizar un algoritmo que permita simular el proceso de apilar libros en una biblioteca, y
# luego ir sacándolos utilizando el principio de pilas. Utilizar clases y funciones.

class pila:
    def __init__(self):
        self.top=None
        self.pila=[1]+"libro"
    def agregar(self,item):
        self.top=item
        self.pila.append(item)
        return self.top
    def quitar(self):
        if not self.is_empty():
            self.pila.pop()
            self.top = self.pila[-1]
            return self.top
        else:
            raise IndexError("la pila de libros esta vacia")
        
    def __str__(self):
        return str(self.pila)
    def is_empty(self):
        return len(self.pila)==0
    def size(self):
        return len(self.pila)

libros=pila()
pila.agregar(1,"libro")
pila.agregar(1,"libro")
pila.__str__(libros)