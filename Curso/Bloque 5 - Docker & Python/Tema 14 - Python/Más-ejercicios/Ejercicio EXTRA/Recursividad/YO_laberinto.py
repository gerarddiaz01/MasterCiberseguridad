''' Problema de Resolución de Laberinto: Imagina que eres parte de un equipo de desarrollo de IA que se encarga de 
crear un sistema para que un robot resuelva laberintos. El laberinto está 
representado por una matriz, donde ciertos valores indican caminos permitidos 
(0), paredes (1), y la salida (9). Tu tarea es implementar una función 
recursiva que encuentre la ruta más corta para que el robot salga del laberinto.
Toma en cuenta los siguientes puntos:
La matriz representa el laberinto, donde los valores son:
0 Camino permitido.
1 Pared, no se puede atravesar.
9 Salida del laberinto.
Debes implementar la función resolver_laberinto que utiliza recursividad 
para encontrar la ruta más corta desde una posición inicial hasta la salida.
La función debe devolver una lista de coordenadas que representan la ruta 
desde la posición inicial hasta la salida.
Puedes usar una lista de movimientos posibles: 
arriba ((-1, 0)), abajo ((1, 0)), izquierda ((0, -1)), derecha ((0, 1))
A continuacion un ejemplo de una posible entrada y salida de la solucion:
Entrada
 Laberinto (matriz)
 Indice de nicio (fila)
 Indice de Inicio (columna)
Salida
 Camino para salir del laberinto: (1,1),(1,2),(),()…
 '''

def resolver_laberinto(laberinto, fila, columna, visitados=None):
    # Inicializar la lista de visitados si es la primera llamada
    if visitados is None:
        visitados = set()
    
    # Verificar si la posición actual está fuera de los límites del laberinto
    if fila < 0 or fila >= len(laberinto) or columna < 0 or columna >= len(laberinto[0]):
        return None
    
    # Verificar si la posición actual es una pared o ya fue visitada
    if laberinto[fila][columna] == 1 or (fila, columna) in visitados:
        return None
    
    # Verificar si hemos encontrado la salida
    if laberinto[fila][columna] == 9:
        return [(fila, columna)]
    
    # Marcar la posición actual como visitada
    visitados.add((fila, columna))
    
    # Lista de movimientos posibles: arriba, abajo, izquierda, derecha
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Intentar moverse en cada dirección
    for movimiento in movimientos:
        nueva_fila = fila + movimiento[0]
        nueva_columna = columna + movimiento[1]
        
        # Llamada recursiva para explorar la nueva posición
        ruta = resolver_laberinto(laberinto, nueva_fila, nueva_columna, visitados)
        if ruta:  # Si encontramos una ruta válida, la devolvemos
            return [(fila, columna)] + ruta
    
    # Si no encontramos una ruta, retrocedemos (backtracking)
    visitados.remove((fila, columna))
    return None

def imprimir_laberinto(laberinto,camino):
  for fila in range(len(laberinto)):
    for columna in range(len(laberinto[0])):
      if (fila,columna) in camino:
        print("*",end=" ") #Representa el camino

      else:
        print(laberinto[fila][columna],end=" ")
    print()

# Ejemplo de uso
laberinto = [
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 1, 1, 9, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
]

inicio_fila = 0
inicio_columna = 0

ruta = resolver_laberinto(laberinto, inicio_fila, inicio_columna)
if ruta:
    print("Camino para salir del laberinto:", ruta)
else:
    print("No hay camino para salir del laberinto.")
print("")
imprimir_laberinto(laberinto,ruta)