# Un supermercado necesita un programa para el manejo de un almacén de productos en una
# de sus sucursales. Los productos se reciben en una pila y se despachan en una cola para su
# entrega a los clientes. Se solicita implementar un algoritmo que incluya tanto el uso de pila y
# cola. Debe realizarse las siguientes operaciones:
# A. Agregar producto: Permite ingresar un nuevo producto al almacén. El producto se
# agrega a la pila de productos recibidos.
# B. Despachar producto: Remueve el producto más antiguo de la cola y lo entrega al
# cliente. Si la cola está vacía, muestra un mensaje indicando que no hay productos
# disponibles para despachar.
# C. Verificar si la pila de productos recibidos está vacía: Devuelve un mensaje que
# indica si la pila de productos recibidos está vacía.
# D. Verificar si la cola de productos para despachar está vacía: Devuelve un mensaje
# que indica si la cola de productos para despachar está vacía.
# E. Imprimir lista de productos recibidos: Muestra en consola los productos
# almacenados en la pila de productos recibidos.
# F. Imprimir lista de productos para despachar: Muestra en consola los productos
# almacenados en la cola de productos para despachar.
# G. Mostrar cantidad total de productos en el almacén: Muestra en consola la
# cantidad total de productos que hay en el almacén, sumando la cantidad de
# productos recibidos en la pila y la cantidad de productos para despachar en la cola.

class Almacen:
    
    def __init__(self):
        self.productos_recibidos = []
        self.productos_despacho = []

    def agregar_producto(self,producto):
    #agrega un producto a self.productos_recibidos.
        self.productos_recibidos.append(producto)

    def despachar_producto(self):
    #si self.productos_recibidos tiene algun producto elimina el ultimo producto agregado y lo asigna a la variable
    #producto,luego esta se añade a self.productos_despacho y luegos se despacha(elimina de self.productos_despacho),
    # sino imprime un mensaje diciendo que no hay productos para despachar.
        if self.productos_recibidos:
            producto=self.productos_recibidos.pop()
            self.productos_despacho.append(producto)
            self.productos_despacho.pop(0)
        else:
            print("No hay productos disponibles para despachar")

    def productos_recibidos_is_empty(self):
    #si productos_Recibidos no tiene elementos devuelve un mensaje confirmandolo.
        if len(self.productos_recibidos)==0:
            print("La pila de productos recibidos está vacía")
 
    def productos_despacho_is_empty(self):
    #si productos_despacho no tiene elementos devuelve un mensaje confirmandolo.
        if len(self.productos_despacho)==0:
            print("La cola de productos para despachar está vacía")
    
    def imprimir_productos_recibidos(self):
    #imprime en un lista los elementos de productos_recibidos.
        print(self.productos_recibidos)

    def imprimir_productos_despacho(self):
    #imprime en un lista los elementos de productos_despacho.
        print(self.productos_despacho)

    def total_productos(self):
    #suma la cantidad de productos que se encuentran en la pila y cola,y devuelve el total de productos.
        recibidos=len(self.productos_recibidos)
        despacho=len(self.productos_despacho)
        total=recibidos+despacho
        print(f"Hay {total} productos.")
        
almacen = Almacen()
almacen.productos_recibidos_is_empty()
almacen.productos_despacho_is_empty()
almacen.agregar_producto("pan")
almacen.agregar_producto("gallatas")
almacen.agregar_producto("torta")
almacen.agregar_producto("carne")
almacen.agregar_producto("chocolate")
almacen.imprimir_productos_recibidos()
almacen.imprimir_productos_despacho()
almacen.despachar_producto()
almacen.despachar_producto()
almacen.despachar_producto()
almacen.despachar_producto()
almacen.despachar_producto()
# almacen.despachar_producto()
almacen.imprimir_productos_recibidos()
almacen.imprimir_productos_despacho()
almacen.total_productos()






    
    
