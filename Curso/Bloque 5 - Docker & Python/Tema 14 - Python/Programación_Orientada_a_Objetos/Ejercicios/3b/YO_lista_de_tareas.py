'''LISTA DE TAREAS
Crea una clase "ListaTareas" que contenga una lista de tareas pendientes.
Implementa métodos para agregar una tarea, marcar una tarea como
completada y mostrar todas las tareas'''

# Definimos la clase ListaTareas
class ListaTareas:
    def __init__ (self):
        # Inicializamos una lista vacía para almacenar las tareas pendientes
        self.tareas = []
    
    def agregar_tarea(self, nueva_tarea):
        # Agregamos una nueva tarea a la lista de tareas
        # Cada tarea se almacena como un diccionario con dos claves:
        # "tarea" para el texto de la tarea y "completada" para el estado (False por defecto)
        self.tareas.append({"tarea": nueva_tarea, "completada": False})
        # Mostramos un mensaje indicando que la tarea fue agregada
        print(f"Tarea '{nueva_tarea}' agregada a la lista.")

    def marcar_completada(self, indice):
        # Verificamos que el índice esté dentro del rango válido de la lista
        # Esto asegura que no intentemos acceder a un índice inexistente
        if 0 <= indice < len(self.tareas):  # Si el índice es válido...
            # Cambiamos el estado de la tarea a "completada"
            self.tareas[indice]["completada"] = True
            # Mostramos un mensaje indicando que la tarea fue marcada como completada
            print(f"Tarea '{self.tareas[indice]['tarea']}' marcada como completada.")
        else:
            # Si el índice no es válido, mostramos un mensaje de error
            print("Índice fuera de rango. No se puede marcar la tarea como completada.")
    
    def mostrar_tareas(self):
        # Mostramos todas las tareas pendientes en la lista
        print("Lista de tareas:")
        # Usamos enumerate para obtener tanto el índice como la tarea
        for indice, tarea in enumerate(self.tareas):
            # Determinamos el estado de la tarea (Pendiente o Completada)
            estado = "Completada" if tarea["completada"] else "Pendiente"
            # Mostramos el índice (comenzando en 1), el texto de la tarea y su estado
            print(f"{indice + 1}. {tarea['tarea']} - {estado}")

# Creamos una instancia de la clase ListaTareas
lista = ListaTareas()

# Agregamos la tarea "Comprar leche" a la lista
lista.agregar_tarea("Comprar leche")

# Agregamos la tarea "Hacer ejercicio" a la lista
lista.agregar_tarea("Hacer ejercicio")

# Agregamos la tarea "Leer un libro" a la lista
lista.agregar_tarea("Leer un libro")

# Marcamos la tarea "Comprar leche" como Completada
lista.marcar_completada(0)

# Mostramos todas las tareas actuales en la lista
lista.mostrar_tareas()