# Teoría de Arrays y Módulos en Python

## **Módulos en Python**

Un módulo es un archivo con extensión `.py` que contiene código de Python reutilizable y que puede ser importado dentro de otro archivo de Python.

### ⚡ **Importación de módulos**

Para utilizar un módulo en Python, se usa la palabra clave `import`. Ejemplo:

```python
import math
print(math.sqrt(16)) # Salida: 4.0
```

## **Paquetes y Librerías**

### 🔍 **Paquete (Package)**

Un paquete es un directorio que contiene varios módulos relacionados. Puede incluir subpaquetes y módulos.

### 📚 **Librería (Library)**

Una librería es un conjunto de módulos y paquetes que proporcionan funcionalidades específicas.
Ejemplos:
`numpy` (para cálculos numéricos)
`matplotlib` (para visualización de datos)
`pandas` (para manipulación de datos)

## 📉 **Arrays en Python**

### **Definición**

Un array es una colección ordenada de elementos del mismo tipo.

### ⚖ **Diferencias entre Listas y Arrays**

| Característica              | Listas                          | Arrays                      |
| --------------------------- | ------------------------------- | --------------------------- |
| **Tipo de datos**           | Pueden ser de distintos tipos   | Deben ser del mismo tipo    |
| **Creación**                | Se usa `[ ]`                    | Se usa la función `array()` |
| **Operaciones matemáticas** | No se pueden hacer directamente | Se pueden hacer             |

### **Ejemplo de una lista:**

```python
mi_lista = [1, "hola", 3.5]
```

### **Ejemplo de un array con numpy:**

```python
import numpy as np
mi_array = np.array([1, 2, 3, 4])
print(mi_array * 2) # [2 4 6 8]
```

## 🔬 **Módulo array**

El módulo `array` viene incluido por defecto en Python.

### ⚙ **Uso del módulo array**

```python
import array as arr
# Crear un array de enteros
array_int = arr.array('i', [1, 2, 3, 4, 5])
print(array_int)  # Salida: array('i', [1, 2, 3, 4, 5])
```

Podemos acceder a los elementos del array de la misma forma que con las listas, utilizando índices (comenzando desde 0):

```python
print(array_int[2])  # Salida: 3
```

También podemos modificar los elementos mediante sus índices:

```python
array_int[2] = 10
print(array_int)  # Salida: array('i', [1, 2, 10, 4, 5])
```
# Array Tridimensional

## Ejemplo:

Para cambiar la forma de un array (redimensionar), usamos `reshape()`:

```python
array_3d = np.array([
[1, 2],
[3, 4],
[5, 6]
]).reshape(1, 6)
print(array_3d)
# Resultado:
# [[1 2 3 4 5 6]]
```

Podemos usar `shape` para saber el número de filas y columnas:

```python
array1 = np.array([[1, 2, 3], [4, 5, 6]])
print(array1.shape) # Resultado: (2, 3) -> 2 filas y 3 columnas
```

Podemos usar `ndim` para saber el número de dimensiones en el array:

```python
print(array1.ndim)
# Resultado: 2
```

## Array Tridimensional (continuación del ejemplo anterior):

Para convertir un array multidimensional a un array unidimensional, usamos `reshape()` con un único número:

### Ejemplo:

```python
array_1 = np.array([[1, 2, 3], [4, 5, 6]])
print("array_1 shape:", array_1.shape, "dim", array_1.ndim)
print(array_1)
array_2 = array_1.reshape(6)
print("array_2 shape:", array_2.shape, "dim", array_2.ndim)
print(array_2)
# Resultado:
# array_1 shape: (2, 3) dim 2
# [[1 2 3]
#  [4 5 6]]
# array_2 shape: (6,) dim 1
# [1 2 3 4 5 6]
```

## 🛠 Contar elementos distintos a cero en un array:

Usamos `np.count_nonzero()`.

La función `np.count_nonzero` de NumPy se utiliza para contar el número de elementos distintos de cero en un array. Es útil cuando necesitas saber cuántos elementos en un array cumplen con una condición específica.

### Sintaxis:

```
np.count_nonzero(a, axis=None, keepdims=False)
```

### Parámetros:

* **a**: Array cuya cantidad de elementos no cero queremos contar.
* **axis**: Eje a lo largo del cual se cuentan los valores no cero. Por defecto, se cuentan en toda la matriz.
* **keepdims**: Si es `True`, mantiene las dimensiones originales del array; si es `False` (por defecto), las reduce.

**Retorno**: Devuelve un entero con el número de elementos no cero en el array.

### Ejemplo:

```python
import numpy as np
# Array de ejemplo
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
# Obtener los índices que ordenarían el array
indices_ordenados = np.argsort(arr)
print(indices_ordenados) # Salida: [ 1  3  6  0  9  2  8 10  4  7  5]
```

### Explicación del Ejemplo:

El array `arr` es `[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]`.

`np.argsort(arr)` devuelve `[1, 3, 6, 0, 9, 2, 8, 10, 4, 7, 5]`, que son los índices que ordenarían el array.

Si aplicas estos índices al array original, obtienes el array ordenado:

```python
arr[indices_ordenados] # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
```

## 🛠 Contar elementos distintos a cero en un array (continuación):

```python
arr = np.array([1, 0, 2, 0, 3, 0])
contador_no_ceros = np.count_nonzero(arr)
print(contador_no_ceros) # Salida: 3
```

En este ejemplo, el array `arr` contiene tres elementos distintos de cero (`1`, `2` y `3`), por lo que `np.count_nonzero(arr)` devuelve `3`.

## Operaciones básicas con arrays:

### ⚙ Creación de arrays con numpy

No es necesario especificar el tipo de dato. NumPy permite realizar operaciones matemáticas de forma eficiente.

### 📅 Instalación

Para instalar NumPy, usa:

```
pip install numpy
```

### ⚙ Creación de un array con numpy

No es necesario especificar el tipo de dato. Permite realizar operaciones matemáticas de forma eficiente.

```python
import numpy as np
# Convertir una lista a un array
my_list = [1, 2, 3, 4]
lista_a_array = np.array(my_list)
print(lista_a_array) # Salida: [1 2 3 4]
```

## De Lista a Array

Aunque listas y arrays parecen similares, convertir listas en arrays mejora la eficiencia en memoria.

### Características de las Listas:

* Pueden almacenar distintos tipos de datos (enteros, strings, booleanos, etc.).
* Gran flexibilidad, pero mayor consumo de memoria.

### Características de los Arrays:

* Almacenan un único tipo de dato.
* Uso eficiente de memoria al especificar el número de bits.

Comparación en memoria: Un entero de 64 bits es innecesario si solo necesitamos almacenar números pequeños (Ej. 1, 2, 3). Podemos optimizar con arrays de 8 bits, lo que reduce significativamente el consumo de memoria.

### Convertir una lista a un array, ejemplo:

```python
import numpy as np
my_list = [1, 2, 3, 4]
lista_a_array = np.array(my_list)
print(lista_a_array) # Salida: [1 2 3 4]
```

## Arrays Multidimensionales

Hasta ahora, trabajamos con arrays unidimensionales. Pero también existen arrays de varias dimensiones:

```python
# Array bidimensional de ejemplo
matriz_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz_2d)
# Salida:
# [[1 2 3]
#  [4 5 6]]

# Array tridimensional de ejemplo (2 matrices 2x2)
matriz_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(matriz_3d)
# Salida:
# [[[1 2]
#   [3 4]]
#  [[5 6]
#   [7 8]]]
```

⚠ Cuidado con `np.empty()`, sus valores iniciales son aleatorios.

Para crear arrays de ceros o unos:

```python
np.zeros((3,3))  # Matriz de 3x3 con ceros
np.ones((2,4))   # Matriz de 2x4 con unos
```

También podemos crear matrices identidad (matrices unidad):

```python
eye_array = np.eye(4)             # Matriz identidad de 4x4
eye_array_despl = np.eye(3, k=-1) # Matriz identidad de 3x3 desplazada una posición hacia abajo
print(eye_array)
print(eye_array_despl)
```

**Salida `eye_array`:**

```
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
```

**Salida `eye_array_despl`:**

```
[[0. 0. 0.]
 [1. 0. 0.]
 [0. 1. 0.]]
```

## 🖜 Concatenación de arrays

La concatenación se refiere a unir dos o más arrays en uno solo. NumPy ofrece varias funciones para concatenar arrays:

* `np.concatenate((a1, a2, ...), axis=0)` : Concatenar secuencialmente a lo largo de un eje especificado.
* `np.vstack(tup)` : Apilar arrays verticalmente (eje 0, uno encima de otro).
* `np.hstack(tup)` : Apilar arrays horizontalmente (eje 1, uno al lado de otro).

### np.concatenate:

#### Sintaxis:

```
numpy.concatenate((a1, a2, ...), axis=0, out=None, dtype=None, casting="same_kind")
```

* **a1, a2, ...**: Arrays que se van a concatenar. Deben tener la misma forma, excepto en la dimensión especificada por `axis`.
* **axis**: El eje a lo largo del cual se concatenarán los arrays. El valor por defecto es 0 (filas).
* **out**: Si se proporciona, el resultado se almacenará en este array.
* **dtype**: Si se proporciona, el tipo de datos del array resultante.
* **casting**: Controla cómo se pueden realizar las conversiones de tipo de datos.

### Ejemplo: Concatenar a lo largo del eje 0 (filas)

```python
import numpy as np
# Crear dos arrays 2D
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])
# Concatenar a lo largo del eje 0 (filas)
resultado = np.concatenate((array1, array2), axis=0)
print("Concatenar a lo largo del eje 0 (filas):")
print(resultado)
```

### Salida:

```
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
```

### Ejemplo: Concatenar a lo largo del eje 1 (columnas)

```python
# Crear un array identidad 2x2 para concatenar con array2
eye_array = np.eye(2)
# Concatenar a lo largo del eje 1 (columnas) array2 y eye_array
array_columnas = np.concatenate((array2, eye_array), axis=1)
print("Concatenación de array2 y eye_array en el eje 1 (columnas):")
print(array_columnas)
```

### Salida:

```
[[5. 6. 1. 0.]
 [7. 8. 0. 1.]]
```

## np.vstack():

La función `vstack()` de NumPy se utiliza para apilar arrays verticalmente (a lo largo del eje 0). Es una forma conveniente de concatenar arrays uno encima del otro, creando un nuevo array con más filas.

### Sintaxis:

```
numpy.vstack(tup)
```

* **tup**: Secuencia de arrays que se apilarán verticalmente. Deben tener la misma forma en todas las dimensiones excepto en la primera (número de filas puede diferir).

```python
# Ejemplo de vstack
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
vertical_stack = np.vstack((a, b))
print(vertical_stack)
```

### Salida:

```
[[1 2 3]
 [4 5 6]]
```

## np.hstack():

La función `hstack()` de NumPy se utiliza para apilar arrays horizontalmente (a lo largo del eje 1). Es útil para concatenar arrays uno al lado del otro, creando un nuevo array con más columnas.

### Sintaxis:

```
numpy.hstack(tup)
```

* **tup**: Secuencia de arrays que se apilarán horizontalmente. Deben tener la misma forma en todas las dimensiones excepto en la segunda (número de columnas puede diferir).

```python
# Ejemplo de hstack
c = np.array([[1, 2], [3, 4]])
d = np.array([[5, 6], [7, 8]])
horizontal_stack = np.hstack((c, d))
print(horizontal_stack)
```

### Salida:

```
[[1 2 5 6]
 [3 4 7 8]]
```

## Conclusión:

La elección entre listas y arrays depende del caso de uso. Para cálculos numéricos y operaciones matemáticas intensivas, los arrays (especialmente con NumPy) ofrecen ventajas significativas en cuanto a rendimiento y funcionalidad adicional. Por otro lado, las listas proporcionan más flexibilidad para almacenar distintos tipos de datos a costa de eficiencia.



# Ordenación de Arrays

Usamos `numpy.sort()` para ordenar los elementos de un array.

## Ejemplo:

```python
eye_array = np.eye(3, k=-1)
eye_array[eye_array == 0] = 2
eye_array[eye_array < 2] = 9
eye_array[1:, :2] = 4
sorted_array = np.sort(eye_array)
print(sorted_array)
```

```
[[2. 2. 9.]
 [4. 4. 9.]
 [2. 4. 4.]]
```

Ha ordenado fila a fila los números de menor a mayor. No ha tocado las columnas, solo las filas.

Para ordenar las columnas tendría que especificar el axis (eje) en el cual quiero hacer el sort.

## Ejemplo:

```python
eye_array = np.eye(3, k=-1)
# Aplicar sort a lo largo de las columnas, axis=0
sorted_array = np.sort(eye_array, axis=0)
print(sorted_array)
```

Podemos especificar el algoritmo de ordenamiento a utilizar en `numpy.sort()` mediante el parámetro `kind`:

```python
np.sort(mi_array, kind='mergesort')
```

Los algoritmos disponibles incluyen:

* **quicksort** (por defecto, rápido en la mayoría de casos).
* **mergesort** (estable, mantiene el orden de elementos iguales).
* **heapsort** (ordenamiento por montículos).
* **stable** (estable, alias de mergesort).

## 🛠 `np.argsort()`: obtener índices para ordenar arrays

La función `np.argsort` de NumPy se utiliza para obtener los índices que ordenarían un array. En otras palabras, devuelve un array de índices que, si se aplican al array original, lo ordenarían en orden ascendente.

### Sintaxis:

```python
np.argsort(a, axis=-1, kind='quicksort', order=None)
```

### Parámetros:

* **a**: El array de entrada que se desea ordenar.
* **axis**: El eje a lo largo del cual se ordena el array. El valor predeterminado es -1 (el último eje).
* **kind**: El algoritmo de ordenación a utilizar. Puede ser `'quicksort'`, `'mergesort'`, `'heapsort'` o `'stable'`. El valor predeterminado es `'quicksort'`.
* **order**: Si el array es una estructura con campos, este parámetro especifica el campo a ordenar.

### Retorno:

Devuelve un array de índices que ordenarían el array de entrada.

### Ejemplo:

```python
import numpy as np
# Array de ejemplo
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
# Obtener los índices que ordenarían el array
indices_ordenados = np.argsort(arr)
print(indices_ordenados)
```

```
# Salida: [1 3 6 0 9 2 8 10 4 7 5]
```

### Explicación del Ejemplo:

El array `arr` es `[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]`.

`np.argsort(arr)` devuelve `[1, 3, 6, 0, 9, 2, 8, 10, 4, 7, 5]`, que son los índices que ordenarían el array.

Si aplicas estos índices al array original:

```python
arr[indices_ordenados]
```

Obtendrás:

```
[1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
```

## 🛠 Contar elementos distintos a cero en un array

Usamos `np.count_nonzero()`.

La función `np.count_nonzero` de NumPy se utiliza para contar el número de elementos distintos de cero en un array. Es útil cuando necesitas saber cuántos elementos en un array cumplen con una condición específica.

### Sintaxis:

```python
np.count_nonzero(a, axis=None, keepdims=False)
```

# Creación de un Array

Para crear un array con NumPy, se utiliza la función `np.array()`.

```python
import numpy as np
mi_array = np.array([1, 2, 3, 4])
print(mi_array)
```

Esto genera un array unidimensional con los valores `[1, 2, 3, 4]`.

Para crear un array de ceros de dimensiones específicas:

```python
import numpy as np
a = np.zeros((3, 3))
a[:] = 2 # cambia todos los ceros por doses
print(a)
```

El código anterior genera una matriz 3x3 llena de 2.

Podemos utilizar otras funciones como `np.arange` para crear arrays con secuencias de números, y luego `reshape` para darles nuevas dimensiones.

## Ejemplo: apilar arrays

```python
import numpy as np
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])
resultado = np.vstack((array1, array2))
print("Apilar verticalmente:")
print(resultado)
resultado = np.hstack((array1, array2))
print("Apilar horizontalmente:")
print(resultado)
```

## Transposición de un Array

Intercambiamos filas y columnas de una matriz utilizando `transpose()`.

```python
import numpy as np
a = np.array([[1, 2], [3, 4]])
array_transp = a.transpose()
print(array_transp)
```

```
[[1 3]
 [2 4]]
```

En este caso, `transpose()` intercambia las filas por las columnas de la matriz `a` .

También podemos especificar los ejes con `transpose(axis1, axis2)`:

```python
import numpy as np
b = np.arange(1, 10).reshape((3, 3))
array_transp = b.transpose(1, 0)
print(array_transp)
```

(Nota: El resultado mostrado corresponde a un caso ilustrativo de 2×2. En una matriz 3×3 real, `transpose(1,0)` produciría la matriz transpuesta completa.)

También podemos intercambiar ejes con `swapaxes()`, que permite especificar dos ejes a
intercambiar:

```python
import numpy as np
b = np.arange(1, 10).reshape((3, 3))
array_transp = np.swapaxes(b, 0, 1)
print(array_transp)
```
Cambia las posiciones de filas y columnas de la matriz.

## Llenar Arrays con Valores
Para llenar un array con un valor específico, utilizamos `fill()` :
```python
mi_array = np.zeros(5)
mi_array.fill(7)
print(mi_array)  # [7. 7. 7. 7. 7.]
```
También podemos asignar valores directamente usando la indexación completa:
```python
mi_array = np.array([0, 0, 0, 0])
mi_array[:] = 2
print(mi_array)  # [2 2 2 2]
```
También podemos usar operadores de asignación compuesta. Por ejemplo, dada un array inicial:
```python
mi_array = np.array([2, 2, 2, 2])
mi_array += 6
print(mi_array)  # [8 8 8 8]
```

Para realizar operaciones que puedan cambiar el tipo (por ejemplo, división), debemos asegurarnos de que el tipo lo permita. Si tenemos un array de enteros y dividimos, obtenemos error porque el resultado no es entero:

```python
mi_array = np.array([0, 0, 0, 0], dtype=np.int64)
mi_array[:] = 2
# mi_array = 6  -> Error
```
Nos sale error porque estamos trabajando con enteros y el resultado de la división no es entero. Para evitar el error tendríamos que quitar `dtype=np.int64` o convertir el array a coma flotante antes de dividir.


## Sumar Elementos de un Array
Podemos calcular la suma total de los elementos de un array con `sum()`.
```python
mi_array = np.array([1, 2, 3, 4, 5])
print(mi_array.sum())  # 15
```
Para sumar a lo largo de un eje específico (por filas o por columnas):
```python
matriz = np.array([[1, 2], [3, 4]])
print(matriz.sum(axis=0))  # [4 6]
print(matriz.sum(axis=1))  # [3 7]
```

## Operaciones con Matrices
Podemos sumar o restar matrices elemento a elemento utilizando los operadores aritméticos
habituales.
```python
import numpy as np
a = np.zeros((3, 3))
a[:] = 2
b = np.arange(1, 10).reshape((3, 3))
resultado = (a + b - 2 * a) / 4
print(resultado)
```
En el ejemplo anterior, sumamos las matrices a y b , luego restamos 2*a y finalmente dividimos
todo por 4.

## Multiplicación Matricial
La multiplicación de matrices es clave en IA y machine learning.
- Multiplicación elemento a elemento: se realiza con el operador * (multiplica cada elemento
de una matriz por el elemento correspondiente de la otra).
- Multiplicación matricial: se realiza con métodos especiales (por ejemplo, np.matmul o el
operador @ en Python).

```python
import numpy as np
a = np.zeros((3, 3), dtype=np.int64)
a[:] = 2
b = np.arange(1, 10).reshape((3, 3))
matrix_multi = np.matmul(a, b)
print(matrix_multi)
print(a * b)  # elemento a elemento
```

## Máscaras Booleanas
Imaginemos que tenemos este array para las siguientes explicaciones:

```python
otro_array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```
Si aplicamos una condición lógica sobre el array, NumPy nos devuelve un array de valores booleanos del mismo tamaño, indicando con True dónde se cumple la condición. Por ejemplo:

```python
print(otro_array > 5)  
```
Salida:
```python
array([False, False, False, False, False, False, True, True, True, True])
```
Podemos usar este array de booleans para filtrar los elementos del array original:
```python
print(otro_array[otro_array > 5])  # [6 7 8 9]
```

¿En qué casos podemos usar esto? Por ejemplo, supongamos que tenemos un inventario de productos
y sus precios en dos arrays paralelos:

```python
inventario = np.array(["lavadora", "freidora", "sarten", "batidora"])
precio = np.array([200, 120, 50, 75])
```
Si queremos obtener los productos con precio superior a 100:

```python
print(inventario[precio > 100])  # ['lavadora' 'freidora']
```

## Compresión de listas
La compresión de listas es una forma concisa y eficiente de crear listas en Python. Permite generar una
nueva lista aplicando una expresión a cada elemento de una secuencia (como una lista, un rango, etc.) y
opcionalmente filtrando elementos con una condición.

Sintaxis básica:
```python
[nueva_expresion for elemento in secuencia if condicion]
```
- nueva_expresion: La expresión que se evalúa y se añade a la nueva lista.
- elemento: El elemento actual de la secuencia que se está iterando.
- secuencia: La secuencia (como una lista, un rango, etc.) que se está iterando.
- condicion: (Opcional) Una condición que debe cumplir el elemento para que se incluya en la nueva lista.

Ejemplo equivalente al filtro anterior usando compresión de listas:

```python
mi_lista = [inventario[i] for i in range(len(precio)) if precio[i] > 100]
print(mi_lista)  # ['lavadora', 'freidora']
```
En este caso, mi_lista contendrá ['lavadora', 'freidora'] , que son los elementos del
inventario cuyos precios superan 100, logrando el mismo resultado que con las máscaras booleanas en
NumPy.
