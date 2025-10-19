'''Problema de Optimización de Subarreglo:
Imagina que estás trabajando en un sistema de análisis de datos y te han proporcionado una lista de números enteros. 
Tu tarea es desarrollar una función llamada max_subarray_sum que encuentre y devuelva la suma máxima de un subarreglo 
contiguo en la lista.

Por ejemplo, considera la lista [1, -2, 3, 10, -4, 7, 2, -5].
El subarreglo contiguo con la suma máxima es [3, 10, -4, 7, 2], y la suma de esos elementos es 18.
Por lo tanto, la función debería devolver 18 para esta lista.

Implementa la función max_subarray_sum, además, aplica memoización para mejorar su eficiencia en el cálculo de 
subarreglos de suma máxima en listas previamente procesadas.'''

from functools import lru_cache

@lru_cache(maxsize=None)
def max_subarray_sum(nums):
    nums = tuple(nums)  # Convertimos la lista en tupla porque lru_cache requiere argumentos hashables

    max_actual = max_total = nums[0]
    start = end = temp_start = 0  # Variables para rastrear el subarreglo

    for i in range(1, len(nums)): # Empezamos en la posición 1 porque ya estabamos en la posición 0 antes
        if nums[i] > max_actual + nums[i]:
            max_actual = nums[i]
            temp_start = i
        else:
            max_actual += nums[i]

        if max_actual > max_total:
            max_total = max_actual
            start = temp_start
            end = i

    # Devuelve la suma máxima y el subarreglo
    return max_total, nums[start:end + 1]

arr = [1, -2, 3, 10, -4, 7, 2, -5]

# Primera vez: lo calcula
resultado, subarreglo = max_subarray_sum(tuple(arr))
print("Suma máxima del subarreglo contiguo:", resultado)
print("Subarreglo contiguo con la suma máxima:", subarreglo)

# Segunda vez: lo saca de caché
resultado, subarreglo = max_subarray_sum(tuple(arr))
print("Suma máxima del subarreglo contiguo (desde caché):", resultado)
print("Subarreglo contiguo con la suma máxima (desde caché):", subarreglo)


'''
Explicacion de las variables utilizadas:
    max_actual:
        Representa la suma máxima de un subarreglo que termina en el elemento actual.
    max_total:
        Representa la suma máxima global encontrada hasta ahora.
    start, end, temp_start:
        Estas variables rastrean los índices del subarreglo que produce la suma máxima:
            start: Índice inicial del subarreglo máximo.
            end: Índice final del subarreglo máximo.
            temp_start: Índice temporal para rastrear el inicio del subarreglo actual.

Propósito del bucle for:
    Este es el núcleo del algoritmo de Kadane.
    Para cada elemento nums[i]:
        Actualizar max_actual:
            Compara si es mejor iniciar un nuevo subarreglo con el elemento actual (nums[i]) o extender el subarreglo 
            actual (max_actual + nums[i]).
            Si nums[i] es mayor, actualiza temp_start al índice actual (i).
        Actualizar max_total:
            Si el subarreglo actual (max_actual) es mayor que el máximo global encontrado hasta ahora (max_total), 
            actualiza max_total, start y end.
'''