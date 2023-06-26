# Se requiere gestionar una jerarquía de empleados en una empresa. Cada empleado tiene un
# cargo específico y puede tener uno o varios subordinados. Utilizando un árbol, elaborar el
# programa con las siguientes funcionalidades:
# A. Agregar empleado: Permite ingresar un nuevo empleado a la jerarquía. El
# empleado se agrega como subordinado de un empleado existente, especificando su
# cargo.
# B. Eliminar empleado: Elimina un empleado de la jerarquía, junto con todos sus
# subordinados. Al eliminar un empleado, todos sus subordinados pasan a ser
# subordinados del empleado superior.
# C. Mostrar la jerarquía: Muestra en consola la estructura jerárquica completa de la
# empresa, mostrando los empleados y sus respectivos subordinados en forma de
# árbol.
# D. Buscar empleado: Permite buscar un empleado en la jerarquía por su nombre y
# muestra su cargo y subordinados directos, si los tiene.
# E. Obtener jefe directo: Dado un empleado, muestra en pantalla el nombre y cargo de
# su jefe directo.

class Nodo:
#se crea un nodo el cual representara a cada empleado
    def __init__(self , id , cargo ):
        self.id = id
        self.cargo = cargo
        self.subordinados = []

class Arbol:
#se crea la clase arbol la cual representara la jerarquia de empleados
    def __init__ (self,id,cargo):
    #se inicializa dando los parametros de la raiz(jefe)
        self.raiz = Nodo(id, cargo)

    def agregar_empleado(self,id,cargo,encargado):
    #se crea un empleado que recibe un identificador y cargo
        empleado= Nodo(id,cargo)
        if encargado:
        # si el encargado existe se agrega el empleado como su suvordinado
           encargado.subordinados.append(empleado)
        else:
        #si el encargado no existe el empleado se vuelve el encargado
            self.raiz = empleado

    def mostrar_jerarquia(self):
    #este metodo es el que mostrara la jerarquia.establecemos desde donde se empezara a ver la jerarqia
        self.mostrar_jerarquia_recursivamente(self.raiz, 0)

    def mostrar_jerarquia_recursivamente(self, nodo, rama):
    #esta funcion recorre un nodo e imprime su contenido,si el nodo tiene subordinados,recorre la lista e imprime 
    # su contenido
        print("   " * rama + f"|_ {nodo.id}: {nodo.cargo}")
        for subordinado in nodo.subordinados:
            self.mostrar_jerarquia_recursivamente(subordinado, rama + 1)


# Jerarquia empresa
# CEO o director ejecutivo.
# Presidente.
# Vicepresidente.
# Jefes de cada departamento.
# Gerentes.
# Supervisores.
# Empleados.


jerarquia = Arbol(1,"director ejecutivo")

jerarquia.agregar_empleado(2,"presidente",jerarquia.raiz)
jerarquia.agregar_empleado(5,"jefe de departamento",jerarquia.raiz.subordinados[0])
jerarquia.agregar_empleado(10,"empleado",jerarquia.raiz.subordinados[0].subordinados[0])
jerarquia.agregar_empleado(11,"empleado",jerarquia.raiz.subordinados[0].subordinados[0])
jerarquia.agregar_empleado(6,"jefe de departamanto",jerarquia.raiz.subordinados[0])
jerarquia.agregar_empleado(10,"empleado",jerarquia.raiz.subordinados[0].subordinados[1])
jerarquia.agregar_empleado(11,"empleado",jerarquia.raiz.subordinados[0].subordinados[1])
jerarquia.agregar_empleado(4,"jefe de departamento",jerarquia.raiz.subordinados[0])
jerarquia.agregar_empleado(10,"empleado",jerarquia.raiz.subordinados[0].subordinados[2])
jerarquia.agregar_empleado(11,"empleado",jerarquia.raiz.subordinados[0].subordinados[2])
jerarquia.agregar_empleado(3,"vicepresdente",jerarquia.raiz)
jerarquia.agregar_empleado(7,"empleado",jerarquia.raiz.subordinados[1])
jerarquia.agregar_empleado(8,"empleado",jerarquia.raiz.subordinados[1])
jerarquia.agregar_empleado(9,"empleado",jerarquia.raiz.subordinados[1])
print("Jerarquia de la empresa:")
print()
jerarquia.mostrar_jerarquia()
