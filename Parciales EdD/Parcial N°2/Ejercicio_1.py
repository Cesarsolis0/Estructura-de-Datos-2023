# Desarrollar una solución para una aplicación de reproducción de videos utilizando una lista
# circular simple para administrar la lista de videos de cada usuario en específico. Cada nodo de la
# lista representa un video, cada video tiene un título, un autor y una duración. Se solicita
# implementar una lista enlazada para una lista de reproducción de videos. Debe contener las
# siguientes funciones:
# A. Clases respectivas del problema
# B. Método para agregar videos
# C. Método para mostrar la lista de videos
# D. Método para buscar videos
# E. Método eliminar un video
# F. Método para verificar si la lista de videos está vacía
# Nota: Se solicita no solo implementar las funciones requeridas, sino también probarlas y mostrar los
# resultados obtenidos anteriormente. Esto implica que se deben ej

class Nodo_video:

    def __init__(self,titulo,autor,duracion):
        self.titulo=titulo
        self.autor=autor
        self.duracion = duracion
        self.siguiente = None

class Lista_videos:

    def __init__(self):
        self.primero=None
        self.ultimo=None

    def is_empty(self):
        return self.primero == None

    def agregar_videos(self,titulo,autor,duracion):
        nuevo_video=Nodo_video(titulo,autor,duracion)
        if self.is_empty():
            self.primero = nuevo_video
            self.ultimo = nuevo_video
            self.ultimo.siguiente = self.primero
        else:
            temp = self.ultimo
            self.ultimo= temp.siguiente
            temp.ultimo = nuevo_video
            self.ultimo.siguiente = temp
            self.ultimo.siguiente = self.primero

    def mostrar_videos(self):
        temp = self.primero
        lista =[]
        while temp:
            lista.append(temp.titulo)
            lista.append(temp.autor)
            lista.append(temp.duracion)
            if temp == self.primero:
                break
        print(lista)
    
    def buscar_video(self,titulo):
        pass
    
    def eliminar_video(self):
        if self.is_empty():
            print("No hay videos para eliminar")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            temp = self.primero
            while temp.siguiente != self.ultimo:
                temp = temp.siguiente
            temp.siguiente = self.primero
            self.ultimo = temp

videos = Lista_videos()

print(videos.is_empty())
videos.agregar_videos("video 1","Cesar","3:15 s")
videos.agregar_videos("video 2","Juan","4:15 s")
videos.agregar_videos("video 3","Pedro","2:15 s")
videos.mostrar_videos()
videos.mostrar_videos()
print(videos.is_empty())
videos.eliminar_video()
videos.mostrar_videos()

            
