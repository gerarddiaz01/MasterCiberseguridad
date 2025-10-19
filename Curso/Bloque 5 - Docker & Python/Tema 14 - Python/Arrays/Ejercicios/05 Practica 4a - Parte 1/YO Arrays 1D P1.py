
import numpy as np
# 1. Crea un array_1 lleno ceros con una longitud de 8 elementos.
array_1 = np.zeros(8)
# 2. Haz que todos los elementos de este array sean igual a 2
array_1[:] = 2
print(array_1)
# 3. Crea un array_2 que contenga todos los números pares del 1 al 10.
array_2 = np.arange(2,11,2)
print(array_2)
# 4. Suma todos los elementos del array_2 usando un bucle y luego usando numpy.
suma = 0
for i in range(1, len(array_2)):
    suma += array_2[i]
print("Suma usando bucle:", suma)
suma_array = np.sum(array_2)
print("Suma usando numpy:", suma_array)
#5. Revierte array_2 y guárdalo en una variable independiente.
array_2_revertido = array_2[::-1] #Para que sea una variable independiente y no modifique el original tenemos que poner [:]
print("Array revertido:", array_2_revertido)
#6. Encuentra los elementos comunes entre array_1 y array_2 y entre array_2 y array_2_revertido
# (Pista: Investiga el uso de intersect1d() de numpy)
comunes_1_2 = np.intersect1d(array_1, array_2)
comunes_2_revertido = np.intersect1d(array_2, array_2_revertido)
print("Elementos comunes entre array_1 y array_2:", comunes_1_2)
print("Elementos comunes entre array_2 y array_2_revertido:", comunes_2_revertido)
#7. Crea un arrays lleno de 1s con una longitud dada por el usuario
longitud = int(input("Introduce la longitud del array: "))
array_usuario = np.ones(longitud)
print("Array de 1s:", array_usuario)