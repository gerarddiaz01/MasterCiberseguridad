'''Juego “Piedra, Papel, Tijera”. Vamos a enfrentarnos contra el ordenador en el juego de piedra, 
papel o tijera. 
Reglas: 
- Piedra gana a Tijera y pierde con Papel 
- Papel gana a Piedra y pierde con Tijera 
- Tijera gana a Papel y pierde con Piedra 
Pedir al jugador que escoja entre “Piedra | Papel | Tijera” (texto); el ordenador hará su 
elección al azar. Y se comparan las dos elecciones para ver quién gana. Al terminar una partida, 
se pedirá si se quiere jugar de nuevo (texto) y, en caso afirmativo, se reinicia el juego (sin que acabe el programa). 
Recordatorio: hay que controlar que el jugador introduzca una de las 3 opciones   
(Piedra | Papel | Tijera), y no otra. 
Pista: la función “azar(3)” devuelve un número al azar entre 0, 1 y 2. Cada una de estas  
opciones podríamos asociarla a “piedra”, “papel” o “ tijera”: “Si numAzar = 0 Entonces   
ordenador = “Piedra” SiNo …” '''

# importar la librería random
import random

# definir la función azar
def azar(num):
    return random.randint(0,num-1)

# definir las opciones del juego
opciones = ["Piedra","Papel","Tijera"]

# definir la variable para jugar de nuevo
jugar = "s"

# mientras el jugador quiera jugar
while jugar == "s":
    # pedir al jugador que escoja entre “Piedra | Papel | Tijera”
    jugador = input("Introduce Piedra, Papel o Tijera: ").title()
    # si el jugador no introduce una de las 3 opciones, pedir que lo haga
    while jugador not in opciones:
        jugador = input("Introduce Piedra, Papel o Tijera: ").title()
    # el ordenador hará su elección al azar
    numAzar = azar(3)
    ordenador = opciones[numAzar]
    # comparar las dos elecciones para ver quién gana
    if jugador == ordenador:
        print("Empate")
    elif (jugador == "Piedra" and ordenador == "Tijera") or (jugador == "Papel" and ordenador == "Piedra") or (jugador == "Tijera" and ordenador == "Papel"):
        print("Gana el jugador")
    else:
        print("Gana el ordenador")
    # pedir si se quiere jugar de nuevo
    jugar = input("¿Quieres jugar de nuevo? (s/n): ").lower()
    # si se quiere jugar de nuevo, reiniciar el juego
    if jugar == "s":
        print("Vamos a jugar de nuevo")
    else:
        print("Fin del juego")


