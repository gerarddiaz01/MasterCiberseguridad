'''Recursividad: 
Tienes a tu disposición un conjunto de discos numerados del 1 al N y tres torres 
etiquetadas como A, B y C. La torre A contiene inicialmente todos los discos 
apilados en orden descendente, desde el disco N en la parte inferior hasta el 
disco 1 en la parte superior.
 Tu tarea es implementar una solución recursiva para mover todos los discos 
desde la torre A hasta la torre C, siguiendo las reglas clásicas de las Torres de 
Hanoi:
  Puedes mover un disco a una torre adyacente.
  Solo puedes mover un disco a la cima de otra pila si esa pila está vacía o si 
el disco superior es más grande que el disco que estás colocando.
 Debes definir una función llamada 
torres_de_hanoi(n, origen, destino, auxiliar) 
que, dado el número total de discos 
n y las torres de A, B y C, 
imprima los pasos necesarios para lograr el movimiento de todos los discos 
desde la torre A hasta la torre C.
 A continuacion un ejemplo de una posible entrada y salida de la solucion:
 Entrada
  N de discos
  N de torres
  Torres : origen, destino, auxiliar
 Salida
 Mover disco de la torre A a la torre C
 Mover disco de la torre A a la torre B
 …'''

def mover_disco(desde, hacia, disco):
    print(f"Mover disco {disco} de la torre {desde} hacia la torre {hacia}")

def torres_de_hanoi(n, origen, destino, auxiliar):
    # Caso base
    if n == 1:
        mover_disco(origen, destino, n)
        return

    # Paso 1: Mover n-1 discos de origen a auxiliar
    torres_de_hanoi(n - 1, origen, auxiliar, destino)

    # Paso 2: Mover el disco n de origen a destino
    mover_disco(origen, destino, n)

    # Paso 3: Mover n-1 discos de auxiliar a destino
    torres_de_hanoi(n - 1, auxiliar, destino, origen)

# Llamada inicial con 3 discos
torres_de_hanoi(3, 'Origen', 'Destino', 'Auxiliar')

'''
Pasos para resolver las torres de hanoi:
    Mover los n-1 discos superiores de A a B (usando C como auxiliar).

    Mover el disco más grande (el disco n) de A a C.

    Mover los n-1 discos de B a C (usando A como auxiliar)
    
Lo más importante es entender que le pasas las POSICIONES Origen Destino Auxiliar (o A C B)
y luego en la función lo que haces es cambiar cual de los pilares es el origen, cual el destino yh cual el auxiliar:
A - torres_de_hanoi(n - 1, origen, auxiliar, destino)
B - torres_de_hanoi(n - 1, auxiliar, destino, origen)
En estas dos lineas de codigo hay que entender que en A el origen es origen, el destino es auxiliar y el auxiliar es destino
y en B el origen es auxiliar, el destino es destino y el auxiliar es origen. Las posiciones no se mueven, pero si se
mueven los pilares de origen a destino y auxiliar (un puto lio)
'''

