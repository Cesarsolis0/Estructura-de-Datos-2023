# Se necesita crear un sistema de gestión de tareas utilizando listas bidireccionales. Cada tarea
# tiene un identificador único, un título, una descripción y un estado (pendiente, en progreso, o
# completada). El sistema debe realizar las siguientes tareas:
# A) Permitir agregar tareas
# B) Eliminar tareas
# C) Buscar una tarea en específico
# D) Cambiar el estado de las tareas
# E) Mostrar las tareas en orden ascendente según su identificador
# Nota: Se solicita no solo implementar las funciones requeridas, sino también probarlas y mostrar los
# resultados obtenidos anteriormente. Esto implica que se deben ejecutar las funciones con datos de
# prueba o ejemplos específicos para demostrar su funcionamiento

class Nodo_tareas:
    def __init__(self,titulo,descripcion,estado):

        self.titulo=titulo
        self.descripcion = descripcion
        self.estado = estado
        self.siguiente=None
        self.anterior=None

class Lista_tareas:

    def __init__(self):

        self.primero=None
        self.ultimo=None
        self.size = 0

    def is_empty(self):
        return self.primero == None

    def agregar_tarea(self,titulo,descripcion,estado):
        nuevo_nodo = Nodo_tareas(titulo,descripcion,estado)
        if self.is_empty():
            self.primero = nuevo_nodo
            self.ultimo = self.primero
        else:
            temp = self.ultimo
            self.ultimo = nuevo_nodo
            temp.siguiente = self.ultimo
            self.ultimo.anterior = temp
        self.size +=1

    def buscar_tareas(self,titulo):
        pass

    def imprimir_tareas(self):
        temp = self.primero
        lista=[]
        while temp != None:
            lista.append(temp.titulo)
            lista.append(temp.descripcion)
            lista.append(temp.estado)
            temp = temp.siguiente
        print(lista)

    def cambiar_estado(self,estado):
        pass

    def eliminar_tarea(self):

        if self.is_empty():
            print("la lista esta vacia")
        elif self.ultimo.anterior==None:
            self.ultimo=self.primero==None
            self.size=0
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
            self.size -=1

tareas=Lista_tareas()
print(tareas.is_empty())
tareas.agregar_tarea("cocinar","hacer almuerzo","pendiente")
tareas.agregar_tarea("estudiar","prepararse para parcial","en progreso")
tareas.agregar_tarea("comprar","comprar pan","completado")
tareas.imprimir_tareas()
print(tareas.is_empty())
tareas.eliminar_tarea()
tareas.eliminar_tarea()
tareas.imprimir_tareas()
