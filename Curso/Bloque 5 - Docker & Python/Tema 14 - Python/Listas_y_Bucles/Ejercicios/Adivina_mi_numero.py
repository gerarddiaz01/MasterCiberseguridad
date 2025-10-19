'''Juego “Adivina mi número”. Pedir al jugador que piense un número (entero) del 1 al 10, y 
dejarle 5 segundos para pensar (“Esperar 5 Segundos”). A partir de ahí, el ordenador tratará 
de adivinar el número, preguntando al jugador si su número es “X”. 
En caso de que no lo sea, volverá a preguntar por otro número. Tiene 5 intentos para 
tratar de adivinarlo. 
Nota: Utilizar las función “azar” para que el ordenador pregunte de forma aleatoria. 
Recordatorio: el juego acaba cuando el “número es acertado" O “se han hecho 5 intentos”'''

# Importamos la librería random y time
import random
import time

# Definimos la función azar
def azar():
    return random.randint(1, 10)

# Definimos la función adivina_mi_numero
def adivina_mi_numero():
    print("Piensa un número del 1 al 10")
    time.sleep(5)
    print("Voy a adivinar el número que has pensado, tengo 5 intentos")
    numero_acertado = False
    intentos = 0
    time.sleep(3)
    while numero_acertado == False and intentos < 5:
        print("Intento número " + str(intentos + 1))
        time.sleep(1)
        respuesta = input("¿Es tu número el " + str(azar()) + "? (s/n): ")
        while respuesta not in ["s", "n"]:
            respuesta = input("Por favor, responde con 's' o 'n': ")
        if respuesta == "s":
            numero_acertado = True
            print("¡He acertado!")
        else:
            print("No he acertado")
            intentos += 1
            time.sleep(1)
    if intentos == 5:
        print("Se han hecho 5 intentos, no he acertado el número")

# Llamamos a la función adivina_mi_numero
adivina_mi_numero()
