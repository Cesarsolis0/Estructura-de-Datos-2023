# Desarrollar un algoritmo que contenga seis productos de supermercado utilizando colas
# con Python, implementando las siguientes funciones:
# a) Hacer un metodo que agregue un producto a la cola. ´
# b) Crear otro metodo para eliminar el primer producto de la cola. ´
# c) Otra funcion que muestre los productos en la cola sin modificar la cola, utilizando ´
# ciclos.
# d) Un metodo que invierta el orden de productos de la cola. ´
# e) Una funcion que elimine todos los productos de la cola. 

class cola:

    def __init__(self):
        self.item=[]
    def encolar(self,producto):
        self.item.append(producto)
    def desencolar(self):
        if self.is_empty():
            raise ValueError("la cola esta vacia")
        return self.item.pop(0)
    def is_empty(self):
        return len(self.item)==0
    def imprimir(self):
        for i in self.item:
            print(i)
    def invertir(self):
        self.item=self.item[::-1]
    def limpiar(self):
        self.item.clear()
    
productos=cola()
print("Productos:")
productos.encolar("pan")
productos.encolar("mantequilla")
productos.encolar("leche")
productos.encolar("manzanas")
productos.encolar("cereal")
productos.imprimir()
print()
productos.desencolar()
print("productos actualizados:")
productos.imprimir()
print()
print("productos invertidso:")
productos.invertir()
productos.imprimir()
productos.limpiar()
print()
print("la cola esta vacias?")
print(productos.is_empty())

    
        
