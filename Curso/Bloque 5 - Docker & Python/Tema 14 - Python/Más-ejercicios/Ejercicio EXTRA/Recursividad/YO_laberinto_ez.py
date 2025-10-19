def resolver_laberinto_simple(laberinto, fila, columna):
    # Verificar si hemos encontrado la salida
    if laberinto[fila][columna] == 9:
        return [(fila, columna)]
    
    # Marcar la posición actual como visitada
    laberinto[fila][columna] = 1  # Cambiar a 1 para indicar que está visitada
    
    # Lista de movimientos posibles: arriba, abajo, izquierda, derecha
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for movimiento in movimientos:
        nueva_fila = fila + movimiento[0]
        nueva_columna = columna + movimiento[1]
        
        # Verificar si la nueva posición es válida
        if 0 <= nueva_fila < len(laberinto) and 0 <= nueva_columna < len(laberinto[0]) and laberinto[nueva_fila][nueva_columna] in (0, 9):
            ruta = resolver_laberinto_simple(laberinto, nueva_fila, nueva_columna)
            if ruta:
                return [(fila, columna)] + ruta
    
    # Desmarcar la posición actual al retroceder
    laberinto[fila][columna] = 0
    return None

# Laberinto pequeño para principiantes
laberinto = [
    [0, 1, 9],
    [0, 1, 0],
    [0, 0, 0]
]

inicio_fila = 0
inicio_columna = 0

ruta = resolver_laberinto_simple(laberinto, inicio_fila, inicio_columna)
if ruta:
    print("Camino para salir del laberinto:", ruta)
else:
    print("No hay camino para salir del laberinto.")