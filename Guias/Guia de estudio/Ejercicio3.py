# Realizar un algoritmo utilizando la estructura de Pila en Python. Se desea almacenar el
# siguiente conjunto de documentos:
# documentos = [“Informe Final”, “Guia de Estudio”, “Tesis 4”, “Seminario Osorno”]
# a) Crear una funcion e imprimir el listado de documentos actual de la pila. ´
# b) Agregar el documento “Avance Tesis” y “Proyecto Integrador”.
# c) Obtener el ultimo elemento superior de la pila. ´
# d) Eliminar el documento de la parte superior.
# e) Imprimir la pila de documentos actualizadas.
# f) Verificar si esta vac´ıa la pila de documentos.

class pila:

    def __init__(self):
        self.item = []

    def agregar(self,item):
        self.item.append(item)

    def quitar(self):
        if not self.is_empty():
            self.item.pop()
        else:
            raise IndexError("la pila de documentos esta vacia")
        
    def is_empty(self):
        return len(self.item)==0
    
    def imprimir(self):
        for i in self.item:
            print(i)

    def ultimo_elemento(self):
        if not self.is_empty():
            self.top =self.item[-1]
            return self.top
        else:
            IndexError("la pila de documentos esta vacia")
    
documentos = pila()
documentos.agregar("Informe Final")
documentos.agregar("Guia de Estudios")
documentos.agregar("Tesis 4")
documentos.agregar("Seminario Osorno")
print("la pila esta vacia?")
print()
print(documentos.is_empty())
print()
print("los documentos en la pila son:")
print()
documentos.imprimir()
print()
documentos.agregar("Avance Tesis")
documentos.agregar("Proyecto Integrador")
print("la pila actualizada es:")
print()
documentos.imprimir()
print()
print(f"el ultimo eleemnto es:\n{documentos.ultimo_elemento()}")
print()
documentos.quitar()
print("los elementos de la pila son:")
print()
documentos.imprimir()

