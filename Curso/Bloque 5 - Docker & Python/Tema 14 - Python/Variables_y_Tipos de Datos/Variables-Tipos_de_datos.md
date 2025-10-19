# Introducción a Python

## 1. ¿Qué es Python?

-   **Creado por:** Guido van Rossum en los años 80 en el Centro para
    las Matemáticas y la Informática (CWI) de los Países Bajos.

-   **Multiplataforma:** Funciona en Unix, Linux, MacOS, Windows.

-   **Multiparadigma:** Soporta programación orientada a objetos,
    estructurada y funcional.

-   **Sintaxis:** Compacta, sencilla e intuitiva, con una curva de
    aprendizaje mínima.

-   **Interpretado:** No se compila, se ejecuta directamente usando un
    intérprete.

### Ejemplo de sintaxis básica:
```python
print("Hola, mundo!")
```
## 2. Línea de Comandos vs Scripts

-   **Línea de comandos:** Ejecución interactiva de código Python en la
    terminal.

-   **Scripts:** Archivos de texto con código Python que se ejecutan
    como programas.

### Ejemplo de línea de comandos:
```python
3 + 2
# Salida: 5
```
### Ejemplo de script:
```python
# script.py
print("Hola, mundo!")
```
## 3. Variables

-   **Definición:** Espacio reservado en memoria con un identificador.

-   **Declaración:** En Python, las variables se inicializan
    directamente.

### Ejemplo de declaración e inicialización:
```python
sumaTotal = 12
precio = 20.5
nota = "Hola"
terminado = False
```
### Modificación de variables:
```python
sumaTotal = sumaTotal + 4
precio = 3.4 + 4.6
nota = "Adiós"
terminado = True
```
## 4. Asignación Múltiple

-   **Asignación múltiple:** Permite asignar varios valores a varias
    variables en una sola línea.

### Ejemplo:
```python
x = y = z = 10
print(x, y, z) # Salida: 10 10 10

x, y, z = 10, 20, 30
print(x, y, z) # Salida: 10 20 30
```
## 5. Pedir Valores con input()

-   **Función input():** Permite obtener texto escrito por el
    usuario.

### Ejemplo:
```python
nombre = input("¿Cómo te llamas? ")
print("Me alegro de conocerte,", nombre)
```
### Ejemplo con conversión de tipo:
```python
edad = int(input("¿Cuántos años tienes? "))
print("Has vivido aproximadamente", 365 * edad, "días")
```
## 6. Tipos de Datos y Conversión

-   **Funciones de tipo:** int(), float(), str(), bool().

-   **Función type():** Devuelve el tipo de dato.

### Ejemplo:
```python
numero_entero = 42
numero_decimal = float(numero_entero)
print(type(numero_entero)) # Salida: <class 'int'>
print(type(numero_decimal)) # Salida: <class 'float'>
```
## 7. Strings (Cadenas de Caracteres)

-   **Definición:** Variables de tipo texto.

-   **Funciones útiles:** title(), upper(), lower(), strip(), replace(),
    find(), startswith(), endswith().

Puede hacerse con 'xxx', "xxx" y empezar el párrafo con ''' y terminar
con '''

### Ejemplo:
```python
nombre = "juan gomez"
print(nombre.title()) # Salida: Juan Gomez
print(nombre.upper()) # Salida: JUAN GOMEZ
```
-   title()
```python
nombre = 'juan gomez'
print(nombre.title())
# Salida: Juan Gomez
```
-   upper()
```python
nombre = 'juan gomez'
print(nombre.upper())
# Salida: JUAN GOMEZ
```
EJEMPLO: crear una lista de todo en mayúsculas teniendo algo en
minúsculas.
```python
alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alfabeto_mayusculas = []
for letra in alfabeto:
    alfabeto_mayusculas.append(letra.upper())
```
-   lower()
```python
nombre = 'juan gomez'
print(nombre.lower())
# Salida: juan gomez
```
-   rstrip()
Sirve para eliminar espacios en blanco de la derecha.
```python
nombre = "python "
print(nombre.rstrip())
# Salida: python
```
-   lstrip()
Sirve para eliminar espacios a la izquierda.
```python
nombre = " python"
print(nombre.lstrip())
# Salida: python
```
-   strip()
Elimina espacios de la derecha e izquierda.
```python
nombre = " python "
print(nombre.strip())
# Salida: python
```
-   replace
Sustituir partes del string.
```python
string = "Hola.Mundo"
print(string.replace(".", " "))
# Salida: Hola Mundo
```
find()
Encontrar un string dentro de otro string, te da la posición empezando
en 0, si te da -1 significa que no se ha encontrado.
```python
string = "Hola Mundo"
print(string.find("Hol")) # Salida: 0
print(string.find("do"))  # Salida: 8
print(string.find("hey")) # Salida: -1
```
-   startswith()
Comprueba si el string empieza de cierta forma.
```python
string = "Hola Mundo"
print(string.startswith("Hol")) # Salida: True
print(string.startswith("Mun")) # Salida: False
```
-   endswith()
```python
string = "Hola Mundo"
print(string.endswith("do")) # Salida: True
print(string.endswith("Ho")) # Salida: False
```
**Concatenación de strings:**
```python
nombre = "juan"
apellido = "gomez"
nombre_completo = nombre + " " + apellido # Salida: juan gomez
print("Hola, " + nombre_completo.title() + "!") # Salida: ¡Hola, Juan Gomez!
```
### Tabs \t:
```python
print("Python")
# Salida: Python

print("\tPython")
# Salida:     Python
```
### Salto de linea \n:
```python
print("Lenguajes:\nPython\nJavaScript\nSolidity")
# Salida:
# Lenguajes:
# Python
# JavaScript
# Solidity
```
### Acceso a índices:
```python
nombre = "Juan"
print(nombre[0]) # Salida: J
```
## 8. Números y Operaciones Aritméticas

-   **Integer o Enteros:** +, -, *, /, ** (potencia), % (módulo).

-   **Floats o Flotantes:** Números decimales.

### Ejemplo:
```python
print(2 + 3) # Salida: 5
print(3 ** 2) # Salida: 9
print(4 % 3) # Salida: 1
```
### Precisión en flotantes:
```python
print(0.2 + 0.1) # Salida: 0.30000000000000004
```
## 9. Combinar Números y Strings

-   **Conversión necesaria:** No se pueden concatenar números y strings
    directamente.

### Ejemplo:
```python
numero_dias = 365
mensaje = "El año tiene " + str(numero_dias) + " días"
print(mensaje) # Salida: El año tiene 365 días
```
## 10. Comentarios

-   **Sintaxis:** Usar # para comentarios de una línea.

-   **Objetivo:** Explicar el código y su funcionamiento.

### Ejemplo:
```python
# Esto es un comentario
print("Hola, mundo!") # Esto también es un comentario
```
