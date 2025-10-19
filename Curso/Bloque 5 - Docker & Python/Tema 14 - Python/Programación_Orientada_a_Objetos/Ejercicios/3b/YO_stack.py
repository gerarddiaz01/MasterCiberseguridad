'''PILA (STACK) BÁSICA
Crea una clase "Pila" que represente una pila (stack) básica. Implementa
métodos para agregar elementos a la pila, quitar elementos y mostrar el
contenido actual.'''

class Pila:
    def __init__(self):
        self.elementos = []
    
    def agregar_elemento(self, nuevo_elemento):
        self.elementos.append(nuevo_elemento)

    def quitar_elemento(self):
        self.elementos.pop()
        print("")
    
    def mostrar_elementos(self):
        for i, elemento in enumerate(self.elementos, 1):
            print(f"{i}. {elemento}")
    
stack = Pila()
stack.agregar_elemento("Libro")
stack.agregar_elemento("Mesa")
stack.agregar_elemento("PC")
stack.agregar_elemento("Estanteria")
stack.agregar_elemento("Cojin")
stack.mostrar_elementos()
stack.quitar_elemento()
stack.mostrar_elementos()
stack.quitar_elemento()
stack.mostrar_elementos()