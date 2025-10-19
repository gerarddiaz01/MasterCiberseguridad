# PYTHON: LISTAS Y ESTRUCTURAS ITERATIVAS

## LISTAS EN PYTHON

### ¿QUÉ ES UNA LISTA?

Una lista es una colección de objetos en un orden particular. Puede
contener diferentes tipos de datos, como cadenas, números, etc.

**Ejemplos:**
```python
Lista1 = ["a", "b", "c", "d", "e", "f"]
Lista2 = [1, 2, 3, 4, 5, 6]
Lista3 = [1, 3, 7, 2, 5, 1, 13]
Lista4 = [1, "a", "b", 3, 7, "e"]
```
### ACCEDER A LOS ELEMENTOS DE UNA LISTA

Las listas son colecciones ordenadas, por lo que podemos acceder a los
elementos indicando su índice.

**Ejemplo:**
```python
embarcaciones = ['bote', 'yate', 'velero', 'catamarán']

print(embarcaciones[0]) # Salida: 'bote'
print(embarcaciones[-1]) # Salida: 'catamarán'

# El índice `-1` se refiere al último elemento de la lista.
```
### MODIFICAR ELEMENTOS DE UNA LISTA

Podemos modificar elementos de una lista accediendo a su índice.

**Ejemplo:**
```python
coches = ['bmw', 'audi', 'seat']

coches[2] = 'mercedes'

print(coches) # Salida: ['bmw', 'audi', 'mercedes']
```
### AÑADIR ELEMENTOS A UNA LISTA

- append(): Añade un elemento al final de la lista.
- insert(): Añade un elemento en una posición específica.

**Ejemplos:**
```python
coches = ['bmw', 'audi', 'seat']

coches.append('mercedes') # Añade 'mercedes' al final
print(coches) # Salida: ['bmw', 'audi', 'seat', 'mercedes']

coches.insert(0, 'mercedes') # Añade 'mercedes' en la posición 0
print(coches) # Salida: ['mercedes', 'bmw', 'audi', 'seat']
```
### BORRAR ELEMENTOS DE UNA LISTA

- pop(): Elimina el último elemento o un elemento en una posición específica.
- remove(): Elimina la primera aparición de un elemento específico.
- del: Elimina un elemento o la lista completa.

**Ejemplos:**
```python
coches = ['bmw', 'audi', 'seat']

coches.pop() # Elimina 'seat'
print(coches) # Salida: ['bmw', 'audi']

coches.remove('audi') # Elimina 'audi'
print(coches) # Salida: ['bmw']

del coches[0] # Elimina 'bmw'
print(coches) # Salida: []
```
### ORDENAR ELEMENTOS DE UNA LISTA

- sort(): Ordena la lista de manera permanente.
- sorted(): Ordena la lista de manera temporal.
- reverse(): Invierte el orden de la lista.

**Ejemplos:**
```python
coches = ['bmw', 'audi', 'seat']

coches.sort() # Ordena alfabéticamente
print(coches) # Salida: ['audi', 'bmw', 'seat']

print(sorted(coches)) # Ordena temporalmente

coches.reverse() # Invierte el orden
print(coches) # Salida: ['seat', 'bmw', 'audi']
```
### LONGITUD DE UNA LISTA

- len(): Devuelve el número de elementos en una lista.

**Ejemplo:**
```python
coches = ["bmw", 'audi', 'seat']

print(len(coches)) # Salida: 3
```
### BUSCAR ELEMENTOS EN LISTAS

Podemos comprobar si un elemento está en una lista usando `in`.

**Ejemplo:**
```python
coches = ['bmw', 'audi', 'seat']

if 'audi' in coches:
    print("Has escogido un audi")
else:
    print("No tenemos esa marca de coche")
```
### BUSCAR INDICES EN LISTAS PARA USARLOS

MANERA 1: usando el metodo index(). Tenemos que encontrar el indice en
la lista abc que corresponde a caracter, y luego usar ese indice en la
lista rot13. Para hacerlo creamos una variable llamada indice que SI
podemos usar como [indice] porque no es un string.
```python
for caracter in entrada:
    if caracter in abc:
        indice = abc.index(caracter)
        print(rot13[indice], end = "")
    else:
        print(caracter, end = "")
print()
```
MANERA 2: Con bucles anidados. Tenemos un mensaje, y tenemos que coger
cada letra individualmente del mensaje, encontrarla en el alfabeto,
mirar en que indice del alfabeto está y pasarla usando ése indice en
otro alfabeto para convertirlo en un mensaje cifrado.
```python
mensaje = "ejemplo"
alfabeto = "abcdefghijklmnopqrstuvwxyz"
mensaje_cifrado = ""

for char in mensaje: 
    if char in alfabeto:  # compruebo si se encuentra en el alfabeto
        for i in range(len(alfabeto)):  # recorrer el alfabeto
            if char == alfabeto[i]:  # cuando encuentre la letra guardo el indice
                char_indice = i
                if char_indice + 13 >= 26:  # si la letra está en la segunda mitad del alfabeto
                    char_indice = char_indice - 26
                nuevo_indice = char_indice + 13  # el nuevo indice cifrado será el antiguo + 13
                letra_cifrada = alfabeto[nuevo_indice]  # accedemos a la letra cifrada
                mensaje_cifrado = mensaje_cifrado + letra_cifrada  # añadimos la letra cifrada al mensaje
```
## ESTRUCTURAS ITERATIVAS (BUCLES)

### BUCLE `WHILE`

El bucle `while` se ejecuta mientras se cumpla una condición.

**Ejemplo:**
```python
import time

temporizador = int(input("Introduce el número de segundos del temporizador: "))

print("Comienza el temporizador...")

while temporizador > 0:
    print(f"Quedan {temporizador} segundos")
    time.sleep(1)
    temporizador = temporizador -1

print("¡El temporizador ha finalizado!")
```

### BUCLE `FOR`

El bucle `for` se utiliza para iterar sobre una secuencia (como una
lista).

Se puede usar el 'in range' o directamente lo que quieres recorrer.
```python
for i in range(valor_inicial, valor_final, paso): # si tienes un valor inicial y final
```

**Ejemplo:**
```python
for i in range(5):
    print(i) # Salida: 0, 1, 2, 3, 4
```
**Ejemplo: Recorrer un string digito a digito sin slicing**
```python
frase = "Hola me llamo Gerard"
letra = "a"
contador = 0

for digito in frase:
    if digito.islower() == letra.islower():
        contador += 1
```
**Ejemplo: Recorrer un string con slicing (en este caso indicando que recorremos el string en orden inverso)**
```python
palabra = input("Introduce una palabra: ")

for letra in palabra[::-1]:
    print(letra)
```
### INTERRUMPIR UN BUCLE: `BREAK` Y `CONTINUE`

- break: Detiene la ejecución del bucle. Es un exit point.
- continue: Salta a la siguiente iteración del bucle.

**Ejemplos:**
```python
for i in range(5):
    if i == 3:
        break # Sale del bucle cuando i es 3
    print(i) # Salida: 0, 1, 2

for i in range(5):
    if i == 3:
        continue # Salta la iteración cuando i es 3
    print(i) # Salida: 0, 1, 2, 4
```
### DEBUGGING CON LISTAS

Es común encontrar errores al trabajar con listas, como acceder a
índices fuera de rango.

**Ejemplo de error:**
```python
coches = ['bmw', 'audi', 'seat']

print(coches[3]) # Error: IndexError (índice fuera de rango)
```
## Recorrer una Lista con un Bucle

Para recorrer una lista en Python, podemos usar el bucle `for`.

### Aquí tienes un ejemplo básico:
```python
coches = ['bmw', 'audi', 'seat']

for coche in coches:
    print(coche)

# Salida:
# bmw
# audi
# seat
```
También podemos usar `range` para recorrer la lista por índices:
```python
coches = ['bmw', 'audi', 'seat']

for i in range(0, len(coches)):
    print(coches[i])

# Salida:
# bmw
# audi
# seat
```
**Otro ejemplo:**
```python
jugadores = ['Alejandro', 'Felipe', 'Samuel', 'Juan Marcos', 'Lucas', 'David']

print('Estos son los jugadores del equipo A: ')

for jugador in jugadores[0:3]:
    print(jugador)

# Salida:
# Estos son los jugadores del equipo A:
# Alejandro
# Felipe
# Samuel
```
**Otro ejemplo:**
```python
jugadores = ['Alejandro', 'Felipe', 'Samuel', 'Juan Marcos', 'Lucas', 'David']

print('Estos son los jugadores del equipo A: ')

for i in range(len(jugadores[0:3])):
    print(jugadores[i])

# Salida:
# Estos son los jugadores del equipo A:
# Alejandro
# Felipe
# Samuel
```
### Ejemplo con Formato Adicional

Podemos añadir más detalles al recorrer la lista:
```python
coches = ['bmw', 'audi', 'seat']

for i in range(0, len(coches)):
    print('Este coche es un', coches[i].title())

print('Lista de coches terminada')

# Salida:
# Este coche es un Bmw
# Este coche es un Audi
# Este coche es un Seat
# Lista de coches terminada
```
## Debugging: Errores Comunes

### Falta de Sangría (Indentación)

- Error común: Olvidar la sangría después de declarar un bucle `for`.
```python
coches = ['bmw', 'audi', 'seat']

for i in range(0, len(coches)):
print('Este coche es un', coches[i].title()) # Error: Falta sangría

# Mensaje de error:
# IndentationError: expected an indented block
```
### Falta de Dos Puntos

- Error común: Olvidar los dos puntos `:` al final de la declaración del bucle `for`.
```python
coches = ['bmw', 'audi', 'seat']

for i in range(0, len(coches)) # Error: Faltan los dos puntos
    print('Este coche es un', coches[i].title())

# Mensaje de error:
# SyntaxError: invalid syntax
```
## Listas Numéricas

Podemos crear listas numéricas usando la función `range()`:
```python
numeros = list(range(1, 6))

print(numeros)

# Salida:
# [1, 2, 3, 4, 5]
```
También podemos generar listas de números pares:
```python
numeros_pares = list(range(2, 11, 2))

print(numeros_pares)

# Salida:
# [2, 4, 6, 8, 10]
```
## Compresión de Listas

La comprensión de listas nos permite crear listas de manera más concisa.
Aquí tienes un ejemplo:

### Declaración extendida:
```python
numeros_cuadrados = []

for valor in range(1, 11): # irá del 1 al 10
    cuadrado = valor**2
    numeros_cuadrados.append(cuadrado)

print(numeros_cuadrados)

# Salida:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
### Declaración comprimida (compresión de listas):
```python
numeros_cuadrados = [valor**2 for valor in range(1, 11)]

print(numeros_cuadrados)

# Salida:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
## Funciones Específicas para Listas Numéricas

Python ofrece funciones útiles para trabajar con listas numéricas:
```python
digitos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(min(digitos)) # Mínimo de la lista
print(max(digitos)) # Máximo de la lista
print(sum(digitos)) # Suma de la lista

# Salida:
# 0
# 9
# 45
```
## Partes de una Lista (Slicing)

Podemos acceder a partes de una lista usando slicing:
```python
for digito in frase[::+1]: # el slicing es [::+1]
    pass
```

```python
digitos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

algunos_digitos = digitos[2:5]

print(algunos_digitos)

# Salida:
# [3, 4, 5]
```
También podemos dividir una lista en equipos:
```python
jugadores = ['Alejandro', 'Felipe', 'Samuel', 'Juan Marcos', 'Lucas', 'David']

equipo_A = jugadores[0:3]
equipo_B = jugadores[3:6]

print(equipo_A)
print(equipo_B)

# Salida:
# ['Alejandro', 'Felipe', 'Samuel']
# ['Juan Marcos', 'Lucas', 'David']
```

### Invertir un string digito a digito usando [::-1]
```python
# Pedir una palabra al usuario

palabra = input("Introduce una palabra: ")

# Recorrer la palabra letra por letra empezando por la ultima
for letra in palabra[::-1]:
    print(letra)
```
## Copiar una Lista

Es importante entender cómo copiar listas correctamente para evitar
modificar la lista original:

### Copia incorrecta (ambas listas están vinculadas):
```python
mi_comida = ['pizza', 'carne', 'tarta de queso']

comida_invitado = mi_comida

comida_invitado.append('helado')

print(mi_comida)
print(comida_invitado)

# Salida:
# ['pizza', 'carne', 'tarta de queso', 'helado']
# ['pizza', 'carne', 'tarta de queso', 'helado']
```
### Copia correcta (usando slicing):
```python
mi_comida = ['pizza', 'carne', 'tarta de queso']

comida_invitado = mi_comida[:]

comida_invitado.append('helado')

print(mi_comida)
print(comida_invitado)

# Salida:
# ['pizza', 'carne', 'tarta de queso']
# ['pizza', 'carne', 'tarta de queso', 'helado']
```
## Listas Anidadas

Las listas pueden contener otras listas, lo que se conoce como listas
anidadas:
```python
datos_alumnos = [['David', 27], ['Jose', 22], ['Lucas', 23]]

print(type(datos_alumnos))
print(datos_alumnos[0])
print(type(datos_alumnos[0]))

# Salida:
# <class 'list'>
# ['David', 27]
# <class 'list'>
```

**EJEMPLO:**

En este ejemplo tenemos una lista de sublistas con 4 elementos en las
sublistas, y tenemos que seleccionar la parte de nombres y de notas.
Recorremos la lista de sublistas y cogiendo el primer elemento (alumno)
con indice [0] lo atribuimos a nombre, y decimos que en la misma
sublista alumno con indice [1:] lo atribuimos a notas, ponemos 1: para
decir que todo lo demas que hay a partir del 1 lo atribuimos a notas,
si solo hubiese una nota pondriamos notas = alumno[1].

Luego vemos dos maneras de formatear los decimales, segun si estamos en
un print ya formateado o no.

```python
datos_alumnos = [["Gerard", 7, 8, 6], ["Coline", 8, 9, 9], ["David", 5, 8, 5]]

notas_clase = []

for alumno in datos_alumnos:
    nombre = alumno[0]
    notas = alumno[1:] # ponemos 1: porque decimos que a partir del indice 1 de la sublista todo lo demas sera notas (hay varias notas)
    nota_media = sum(notas) / len(notas)
    notas_clase.append(nota_media)
    print(f"La nota media de {alumno[0]} es {nota_media :.2f}") # :.2f es para redondear a dos decimales como mucho

nota_media_clase = sum(notas_clase) / len(notas_clase) # Sumamos las notas de la lista notas_clase para calcular la nota media de la clase

print("La nota media de la clase es de {:.2f}".format(nota_media_clase)) # otra manera de redondear sin estar dentro del print(f"")
```

## Matrices

En programación, una matriz es una estructura de datos bidimensional que
se representa como una lista de listas en Python. Cada lista interna
representa una fila de la matriz, y todas las listas internas deben
tener la misma longitud para que sea considerada una matriz válida.

En el contexto del script que tienes, una matriz se define como una
lista de listas donde todas las listas internas tienen el mismo número
de elementos. Si alguna de las listas internas tiene una longitud
diferente, entonces no se considera una matriz.

Aquí tienes un ejemplo de cómo verificar si una lista de listas es una
matriz en Python:
```python
def es_matriz(M):
    if not M:
        return False
    longitud_fila = len(M[0])
    for fila in M:
        if len(fila) != longitud_fila:
            return False
    return True
```
**Ejemplo de uso**
```python
M1 = [[2, 5, 3], [6, 1, 8], [7, 5, 4]]
M2 = [[4, 2, 3], [4, 5], [6, 8, 2]]

print(es_matriz(M1)) # Debería imprimir: True
print(es_matriz(M2)) # Debería imprimir: False
```
En este ejemplo, es_matriz es una función que toma una lista de listas M
y verifica si todas las listas internas tienen la misma longitud. Si es
así, devuelve True, indicando que M es una matriz; de lo contrario,
devuelve False.

## Metodo Split: String a Lista anidada

El método split() se utiliza para dividir un string en una lista de
subcadenas basadas en un delimitador especificado. Si no se especifica
un delimitador, el método utiliza por defecto cualquier espacio en
blanco (espacio, tabulación, nueva línea, etc.) como delimitador.

### Sintaxis
```python
string.split(sep = None, maxsplit = -1)
```
- sep: Es el delimitador que se utiliza para dividir el string. Si se
omite o se establece en None, se utilizarán los espacios en blanco como
delimitador.

- maxsplit: Es el número máximo de divisiones que se realizarán. Si se
establece en -1 (valor por defecto), no hay límite en el número de
divisiones.

### Ejemplos

Dividir un string en palabras usando el espacio como delimitador:
```python
texto = "Hola, ¿cómo estás?"

palabras = texto.split()

# Resultado: ['Hola,', '¿cómo', 'estás?']
```
Dividir un string usando un delimitador específico:
```python
datos = "nombre,apellido,DNI"

elementos = datos.split(',')

# Resultado: ['nombre', 'apellido', 'DNI']
```
Dividir un string en líneas usando el carácter de nueva línea (\n) como
delimitador:
```python
texto = "Línea 1\nLínea 2\nLínea 3"

lineas = texto.split('\n')

# Resultado: ['Línea 1', 'Línea 2', 'Línea 3']
```
Limitar el número de divisiones:
```python
texto = "uno dos tres cuatro"

partes = texto.split(' ', 2)

# Resultado: ['uno', 'dos', 'tres cuatro']
``` 
## Map(): aplicar una función específica a una lista, tupla, etc

Aplica una función especificada a cada elemento de un iterable (como una lista) y devuelve un objeto map (que es un iterable) con los resultados.

Se puede usar para transformar por ejemplo una lista de strings a float o int.

### Sintaxis:
```python
map(function, iterable, ...)
```
- function: es la función que se aplicará a cada elemento del iterable.
- iterable: es el iterable (como una lista, tupla etc) cuyos elementos se
transformarán mediante la función especificada.

**Ejemplo: tenemos una lista de notas en string y las queremos en float**
```python
notas_str = ['9.1', '7.6', '2.4']

notas_float = list(map(float, notas_str))

print(notas_float)

# Resultado: [9.1, 7.6, 2.4] en floats
```
## Repaso Final

### Listas: 
Colecciones de objetos que permiten acceder, modificar, añadir, borrar y ordenar elementos.

### Listas numéricas: 
Funciones específicas como `min()`,`max()`, y `sum()`.

### Slicing: 
Acceder a partes de una lista.

### Copiar listas: 
Usar slicing para evitar modificar la lista original.

### Listas anidadas: 
Listas que contienen otras listas.

### Bucles `For` y `While`

**Funcionamiento general:**
Recorrer elementos de una lista o ejecutar código repetidamente.

Uso de `range`: Generar secuencias de números.

Uso de `break` y `continue`: Controlar el flujo de los bucles.