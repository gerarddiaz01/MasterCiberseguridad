def mover_torres_visual(n, origen, destino, auxiliar, torres):
    if n == 1:
        # Mover el disco más pequeño (el primero en la lista de la torre origen)
        disco = torres[origen].pop()
        torres[destino].append(disco)
        print(f"Mover disco {disco} de {origen} a {destino}")
        imprimir_torres(torres)
    else:
        # Paso 1: Mover los n-1 discos de origen a auxiliar usando destino como auxiliar
        mover_torres_visual(n-1, origen, auxiliar, destino, torres)
        # Paso 2: Mover el disco n de origen a destino
        disco = torres[origen].pop()
        torres[destino].append(disco)
        print(f"Mover disco {disco} de {origen} a {destino}")
        imprimir_torres(torres)
        # Paso 3: Mover los n-1 discos de auxiliar a destino usando origen como auxiliar
        mover_torres_visual(n-1, auxiliar, destino, origen, torres)

def imprimir_torres(torres):
    # Mostrar el estado actual de las torres
    for torre, discos in torres.items():
        print(f"{torre}:")
        for disco in reversed(discos):  # Mostrar los discos desde la base hacia arriba
            print(" " * (20 - len(disco)) + disco)  # Centrar los discos
        print("-" * 30)  # Separador entre las torres
    print("\n")
    
# Ejemplo de uso
n = 3  # Número de discos
torres = {
    'A': ["-" * (5 * i) for i in range(n, 0, -1)],  # Torre A con los discos
    'B': [],  # Torre B vacía
    'C': []   # Torre C vacía
}

print("Estado inicial:")
imprimir_torres(torres)
mover_torres_visual(n, 'A', 'C', 'B', torres)