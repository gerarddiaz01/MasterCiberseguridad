#1. Crea un array con 15 números enteros aleatorios entre 1 y 100
import numpy as np
array_random = np.random.randint(1, 101, size=15)
print("Array de randoms", array_random)

#2. Multiplica todos los elementos del array usando un bucle y luego usando una función de numpy
prod_bucle = 1 #no ponemos 0 porque sino la multiplicación será siempre 0
for numero in array_random:
    prod_bucle = prod_bucle * numero
print(prod_bucle)
prod_numpy = np.prod(array_random)
print(prod_numpy)
#3. Crea otro array con 15 números decimales aleatorios entre 0 y 1
array_decimales = np.random.uniform(0, 1, size=15) #o np.random.random(15)
print("Array de decimales random:", array_decimales)

#4. Suma los elementos de ambos arrays elementos por elemento. Resuélvelo usando un operador y después con una función de numpy
suma_operador = array_random + array_decimales
print("Suma de los arrays usando un operador:", suma_operador)
suma_numpy = np.add(array_random, array_decimales)
print("Suma de los arrays usando la función add() de numpy:", suma_numpy)

#5. Ahora réstalos. Resuélvelo usando un operador y después con una función de numpy
resta_operador = array_random - array_decimales
print("Resta de los arrays usando un operador:", resta_operador)
resta_numpy = np.subtract(array_random, array_decimales)
print("Resta de los arrays usando la función subtract() de numpy:", resta_numpy)

#6. Haz lo mismo con la multiplicación elemento por elemento. Usa un operador y después con una función de numpy
prod_operador = array_random * array_decimales
print("Producto de los arrays usando un operador:", prod_operador)
prod_numpy = np.multiply(array_random, array_decimales)
print("Producto de los arrays usando la función multiply() de numpy:", prod_numpy)

#7. Encuentra el valor más alto del primer array que has creado. 
max_array = np.max(array_random)
print("El numero máximo del primer array es", max_array)

#8. Calcula la media (mean), la mediana (median) y la deviación estandar (standard deviation) de los arrays (Nota: 
# No nos importa el significado matemático de estos valores, lo importante es que encuentres que función de numpy necesitas. 
# Puedes hacer la búsqueda en castellano o en inglés, aunque en inglés muchas veces suele haber más resultados).
media_random = np.mean(array_random)
mediana_random = np.median(array_random)
std_random = np.std(array_random)
media_decimales = np.mean(array_decimales)
mediana_decimales = np.median(array_decimales)
std_decimales = np.std(array_decimales)
print(f"La media del array_random es {media_random}")
print(f"La media del array_decimales es {media_decimales :.2f}")
print(f"La mediana del array_random es {mediana_random}")
print(f"La mediana del array_decimales es {mediana_decimales :.2f}")
print(f"La deviación estándar del array_random es {std_random}")
print(f"La deviación estándar del array_decimales es {std_decimales :.2f}")