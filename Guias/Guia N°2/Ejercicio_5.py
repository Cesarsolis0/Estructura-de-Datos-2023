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

class Empleado:

    def __init__(self, nombre, cargo):
        self.nombre = nombre
        self.cargo = cargo
        self.subordinados = []

    #se agrega un subordinado a la lista subordinados
    def agregar_subordinado(self, subordinado):
        self.subordinados.append(subordinado)

    #se elimina un determinado subordinado de la lista de subordinados
    def eliminar_subordinado(self, subordinado):
        self.subordinados.remove(subordinado)

    #se obtiene la lista subordinados
    def obtener_subordinados(self):
        return self.subordinados

    #en caso de haverse agregado un jefe directo al momento de agregar el empleado
    #se obtiene el jefe ditecto correspondiente
    def obtener_jefe_directo(self):
        return self.jefe_directo

class Empresa:
    def __init__(self):
        self.raiz = None

    #Se agrega un empleado con su respectivo nombre y cargo, en caso de no ser
    #jefe directo, el valor predeterminado es None

    def agregar_empleado(self, nombre, cargo, jefe_directo=None):
        empleado = Empleado(nombre, cargo)
        if jefe_directo:
            jefe_directo.agregar_subordinado(empleado)
            empleado.jefe_directo = jefe_directo
        else:
            self.raiz = empleado

    #se busca el empleado con el metodo buscar_empleado()
    #y se elimina como subordinado de su respectivo jefe directo encontrado con
    #el metodo obtener_jefe_directo()

    def eliminar_empleado(self, nombre):
        empleado = self.buscar_empleado(nombre)
        if empleado:
            jefe_directo = empleado.obtener_jefe_directo()
            if jefe_directo:
                jefe_directo.eliminar_subordinado(empleado)
            else:
                self.raiz = None
            self.actualizar_jefe_directo(empleado, jefe_directo)
        else:
            print("No se encontró el empleado.")

    def actualizar_jefe_directo(self, empleado, nuevo_jefe_directo):
        subordinados = empleado.obtener_subordinados()
        for subordinado in subordinados:
            subordinado.jefe_directo = nuevo_jefe_directo
            self.actualizar_jefe_directo(subordinado, nuevo_jefe_directo)

    #busca el empleado y retorna el correspondiente objeto cuyo nombre coincida
    #con el nombre pasado como parametro. Se usa recursion para recorrer el arbol
    #partiendo desde la raiz.

    def buscar_empleado(self, nombre, nodo=None):
        if not nodo:
            nodo = self.raiz

        if nodo.nombre == nombre:
            return nodo

        for subordinado in nodo.obtener_subordinados():
            resultado = self.buscar_empleado(nombre, subordinado)
            if resultado:
                return resultado

        return None
    
    #si la raiz es distinta de None, se llama al metodo mostrar_arbol 
    #que muestra todo el arbol construido

    def mostrar_jerarquia(self):
        if self.raiz:
            self.mostrar_arbol(self.raiz)

    #muestra todo el arbol, con su respectiva identacion para decir que elemento
    #es hijo de quien

    def mostrar_arbol(self, empleado, nivel=0):
        espacio = "  " * nivel
        print(espacio + empleado.nombre + " - " + empleado.cargo)

        subordinados = empleado.obtener_subordinados()
        for subordinado in subordinados:
            self.mostrar_arbol(subordinado, nivel + 1)

    #obtiene el jefe directo de un determinado empleado, si efectivamente lo 
    #tiene lo muestra, de lo contrario devuelve un mensaje que informa que el empleado
    #no tiene jefe directo. De igual forma, se informa que el empleado no se encontro.

    def obtener_jefe_directo(self, nombre):
        empleado = self.buscar_empleado(nombre)
        if empleado:
            jefe_directo = empleado.obtener_jefe_directo()
            if jefe_directo:
                return jefe_directo.nombre + " - " + jefe_directo.cargo
            else:
                return "No tiene jefe directo."
        else:
            return "No se encontró el empleado."



empresa = Empresa()
empresa.agregar_empleado("Juan", "Gerente")
empresa.agregar_empleado("María", "Supervisor", empresa.buscar_empleado("Juan"))
empresa.agregar_empleado("Pedro", "Analista", empresa.buscar_empleado("María"))
empresa.agregar_empleado("Pepe", "Analista", empresa.buscar_empleado("María"))
empresa.agregar_empleado("Andrés", "sub-Analista", empresa.buscar_empleado("Pepe"))

print("Jerarquía completa:")
empresa.mostrar_jerarquia()

print("Buscar empleado:")

empleado_buscado = "María"
resultado_busqueda = empresa.buscar_empleado(empleado_buscado)
if resultado_busqueda:
    print("Nombre: " + resultado_busqueda.nombre)
    print("Cargo: " + resultado_busqueda.cargo)
    subordinados = resultado_busqueda.obtener_subordinados()
    if subordinados:
        print("Subordinados:")
        for subordinado in subordinados:
            print("- " + subordinado.nombre)
else:
    print(f'El empleado buscado no existe.')

print()

print("Obtener jefe directo:")
empleado_jefe = "Pedro"
jefe_directo = empresa.obtener_jefe_directo(empleado_jefe)
print(f'Jefe directo de  {empleado_jefe} : {jefe_directo}')
