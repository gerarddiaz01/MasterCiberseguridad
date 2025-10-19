import functools
import time

""" Ejercicio de Memoización en Costos de Envío

Imagina que estás trabajando en un sistema de gestión de costos de envío para una empresa de logística. 
El sistema debe calcular el costo de envío para diferentes destinos, distancias y pesos de paquetes. 
Implementa una función llamada calcular_costo_envio que tome como entrada un destino, una distancia en 
kilómetros y un peso en kilogramos, y devuelva el costo total del envío.
Requerimientos:
El costo base de envío es de 5.0.
El costo por kilómetro de distancia es de 0.1.
El costo por kilogramo de peso es de 0.2.
Implementa la función de manera eficiente utilizando memoización para evitar recalcular el costo para los mismos destinos, 
distancias y pesos """

# Función para calcular el costo de envío con memoización
@functools.lru_cache(maxsize=None)
def calcular_costo_envio(destino, distancia, peso):
    costo_base = 5
    costo_distancia = distancia * 0.1
    costo_peso = peso * 0.2
    # Calculamos el costo total
    costo_total = costo_base + costo_distancia + costo_peso
    return costo_total

# Función para medir el tiempo sin memoización
def calcular_sin_memoizacion(destinos, distancias, pesos):
    inicio = time.time()
    costos = []
    for destino, distancia, peso in zip(destinos, distancias, pesos):
        costos.append(calcular_costo_envio(destino, distancia, peso))
    final = time.time()
    tiempo = final - inicio
    return costos, tiempo

# Función para medir el tiempo con memoización
def calcular_con_memoizacion(destinos, distancias, pesos):
    inicio = time.time()
    costos = []
    for destino, distancia, peso in zip(destinos, distancias, pesos):
        costos.append(calcular_costo_envio(destino, distancia, peso))
    final = time.time()
    tiempo = final - inicio
    return costos, tiempo

# Función principal para ejecutar el flujo completo
def main():
    # Datos de prueba
    destinos = ["Ciudad A", "Ciudad B"]
    distancias = [150, 100]
    pesos = [2.5, 4.5]

    # Calcular sin memoización
    costos_sin_memo, tiempo_sin_memo = calcular_sin_memoizacion(destinos, distancias, pesos)

    # Calcular con memoización
    costos_con_memo, tiempo_con_memo = calcular_con_memoizacion(destinos, distancias, pesos)

    # Calcular el tiempo ganado
    tiempo_ganado = tiempo_sin_memo - tiempo_con_memo

    # Imprimir resultados
    print("\nResultados:")
    for i, destino in enumerate(destinos):
        print(f"Costo sin memo para {destino} es de: {costos_sin_memo[i]}")
        print(f"Costo con memo para {destino} es de: {costos_con_memo[i]}")

    print("\nTiempos:")
    print(f"Tiempo sin memoización es de: {tiempo_sin_memo:.6f} segundos")
    print(f"Tiempo con memoización es de: {tiempo_con_memo:.6f} segundos")
    print(f"Tiempo ganado con memoización es de: {tiempo_ganado:.6f} segundos")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()