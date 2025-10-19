# Ejercicio1 :
# Tienes a tu disposición un conjunto de discos numerados del 1 al N y tres torres etiquetadas como A, B y C. La torre A contiene inicialmente todos los discos apilados en orden descendente, desde el disco N en la parte inferior hasta el disco 1 en la parte superior.

# Tu tarea es implementar una solución ***recursiva*** para mover todos los discos desde la torre A hasta la torre C, siguiendo las reglas clásicas de las Torres de Hanoi:

# 1. Puedes mover un disco a una torre adyacente.
# 2. Solo puedes mover un disco a la cima de otra pila si esa pila está vacía o si el disco superior es más grande que el disco que estás colocando.

# Debes definir una función llamada **`torres_de_hanoi(n, origen, destino, auxiliar)`** que, dado el número total de discos **`n`** y las torres de origen, destino y auxiliar, imprima los pasos necesarios para lograr el movimiento de todos los discos desde la torre A hasta la torre C.

def mover_disco(desde,hacia,disco):
  print(f'Mover disco {disco} de la torre {desde} hacia la torre {hacia}')

def torres_de_hanoi(n,origen,destino,auxiliar):
  #caso base /// recursividad
  if n == 1 :
    mover_disco(origen,destino,n)
    return
  #continuando con la recursividad
  torres_de_hanoi(n-1,origen,auxiliar,destino)
  mover_disco(origen,destino,n)
  torres_de_hanoi(n-1,auxiliar,destino,origen)


torres_de_hanoi(3,'Origen','Destino','Auxiliar')
