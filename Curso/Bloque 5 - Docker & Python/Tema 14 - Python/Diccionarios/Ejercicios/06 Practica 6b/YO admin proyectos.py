'''Eres un gerente de proyectos y necesitas un programa para administrar
las tareas y responsabilidades de tu equipo. Cada tarea tiene un nombre,
una descripción y un responsable asignado. Implementa un programa en
Python que utilice un diccionario para almacenar la información de las
tareas. El programa debe permitir agregar nuevas tareas, asignar
responsables a las tareas existentes, actualizar las descripciones de las
tareas y mostrar la lista completa de tareas y responsables. '''

# Diccionario base de datos
tareas = {
    "Tarea1": {"descripcion": "Realizar analisis de requisitos", "responsable": "Juan"},
    "Tarea2": {"descripcion": "Desarrollar funcionalidad principal", "responsable": "Marta"},
    "Tarea3": {"descripcion": "Realizar validacion de proceso", "responsable": "Jacobo"}
}

# Función para imprimir la lista de tareas
def imprimir_tareas(tareas):
    print("Lista de tareas junto con sus descripciones y sus responsables:")
    for clave, valor in tareas.items():
        print(f"{clave}:")
        print(f"  Descripción: {valor['descripcion']}")
        print(f"  Responsable: {valor['responsable']}")
        print("")

# Función para modificar una tarea
def modificar_tarea(tareas):
    tarea = input("¿Qué tarea deseas modificar? (Ejemplo: Tarea1): ")
    if tarea in tareas:
        campo = input("¿Qué deseas modificar? (descripcion/responsable): ").lower()
        if campo in tareas[tarea]:
            nuevo_valor = input(f"Escribe el nuevo valor para {campo}: ")
            tareas[tarea][campo] = nuevo_valor
            print(f"{campo.capitalize()} de {tarea} actualizado correctamente.\n")
        else:
            print("Campo no válido. Intenta de nuevo.\n")
    else:
        print("Tarea no encontrada. Intenta de nuevo.\n")

# Función para agregar una nueva tarea
def agregar_tarea(tareas):
    nombre_tarea = input("¿Cuál es el nombre de la nueva tarea?: ")
    descripcion_tarea = input("Añade una descripción: ")
    responsable_tarea = input("¿Quién es el responsable?: ")
    tareas[nombre_tarea] = {"descripcion": descripcion_tarea, "responsable": responsable_tarea}
    print(f"Tarea {nombre_tarea} añadida correctamente.\n")

# Programa principal
while True:
    imprimir_tareas(tareas)
    accion = input("¿Qué deseas hacer? (modificar/agregar/salir): ").lower()
    if accion == "modificar":
        modificar_tarea(tareas)
    elif accion == "agregar":
        agregar_tarea(tareas)
    elif accion == "salir":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Acción no válida. Intenta de nuevo.\n")