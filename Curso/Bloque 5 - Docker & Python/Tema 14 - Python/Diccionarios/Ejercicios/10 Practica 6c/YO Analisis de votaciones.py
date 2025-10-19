'''
Supongamos que tienes los resultados de una elección con los nombres
de los candidatos y la cantidad de votos obtenidos por cada uno.
Implementa un programa en Python que permita registrar los votos,
mostrar la lista completa de candidatos y sus votos, encontrar al
candidato ganador (con más votos) y calcular el porcentaje de votos que
obtuvo cada candidato'''

# crear diccionario vacio e inicializar bucle a True
elecciones = {}
condition = True

# empezar el bucle while
while condition == True:
    # hacer el menu
    print(f"MENU\n1. Registrar voto\n2. Mostrar la lista completa de candidatos y sus votos\n3. Mostrar el candidato con más votos\n4. Calcular el porcentaje de votos de cada candidato\n5. Salir del programa")
    opcion = input("Escoge una de éstas opciones para continuar: ")

    # hacer el registro de los votos
    if opcion == "1":
        input_nombre = input("Introduce el nombre del candidato: ").capitalize()
        if input_nombre in elecciones:
            elecciones[input_nombre] += 1
        else:
            elecciones[input_nombre] = 1
        print("Voto registrado")
        print("")

    # mostrar la lista completa de candidatos y sus votos
    elif opcion == "2":
        for candidato, votos in elecciones.items():
            print(f"Candidato: {candidato}, Votos: {votos}")
        print("")

    # encontrar al candidato con más votos
    elif opcion == "3":
        if len(elecciones) == 0:
            print("No hay ningun voto registrado")
        else:
            max_votos = max(elecciones, key=elecciones.get)
            print(f"Candidato con mas votos: {max_votos}")
        print("")

    # calcular el porcentaje de votos que ha obtenido cada candidato
    elif opcion == "4":
        total_votos = sum(elecciones.values())
        print("Porcentaje de votos por candidato")
        for candidato, votos in elecciones.items():
            porcentaje = (votos/total_votos) * 100
            print(f"Candidato: {candidato}, Porcentaje de votos {porcentaje:.2f}%")

    # crear la salida del bucle
    elif opcion == "5":
        condition = False
        print("Saliendo del programa...")

    # error de input la opción
    else:
        print("Ésa opción no está disponible, pruebe de nuevo")
        print("")



