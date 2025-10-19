'''
Implementa un programa en Python que permita registrar y mantener un
seguimiento de los puntajes de un juego. El programa debe permitir a los
jugadores ingresar sus nombres y puntajes, almacenarlos en un
diccionario y proporcionar funcionalidades para mostrar el puntaje más
alto, el promedio de puntajes y la cantidad total de jugadores.'''
 
registro = {}
continuacion = True

while continuacion:
    jugador = input("Introduce tu nombre (o 'salir' para gtfo): ")
    if jugador == "salir".lower():
        continuacion = False
        print("Gracias por participar!")
    else:
        puntos = int(input("Introduce los puntos de tu partida: "))
        registro[jugador] = puntos
    
        mejor_jugador = max(registro, key=registro.get)
        mejor_pts = registro[mejor_jugador]
        promedio = sum(registro.values()) / len(registro)
        print(f"Mejor jugador: {mejor_jugador}, con {mejor_pts} puntos")
        print("Promedio: ", promedio)
        print("Total de jugadores actuales: ", len(registro))
        print("")