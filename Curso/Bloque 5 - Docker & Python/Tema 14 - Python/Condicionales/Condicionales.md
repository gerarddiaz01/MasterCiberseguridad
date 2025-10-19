# Python - Condicionales

## Test Condicionales

Los **tests condicionales** permiten comprobar si una afirmación es
**cierta** o **falsa**.

Ejemplo:

```python
nombre_usuario = "Juan"
print(nombre_usuario == "Juan") # True
print(nombre_usuario == "Fede") # False
```

### Operadores de Comparación:

-   "==" → Igualdad.
-   "!=" → Diferente.
-   "in" → Está contenido dentro de.
-   ">" → Mayor que.
-   "<" → Menor que.
-   ">=" → Mayor o igual que.
-   "<=" → Menor o igual que.

### Condiciones en Strings

Las comparaciones en strings son sensibles a mayúsculas y minúsculas
(**case sensitive**):

```python
usuario = "Juan"
print(usuario == "juan") # False
print(usuario.lower() == "juan") # True
```

### Comparaciones Numéricas

Podemos comparar números de diferentes maneras:
```python
edad = 18
print(edad >= 18) # True
print(edad < 21) # True
print(edad != 30) # True
```

## Testear Condiciones Múltiples

Se pueden combinar condiciones usando **and** y **or**.

### Uso de and

Ambas condiciones deben cumplirse para que el resultado sea True.
```python
nombre = "Juan"
edad = 21
if nombre == "Juan" and edad >= 18:
    print("Puede acceder al sitio")
```

### Uso de or

Basta con que **una** de las condiciones se cumpla para que el resultado sea True.
```python
edad = 17
acompañado = True
if edad >= 18 or acompañado:
    print("Puede entrar al local")
```

## Expresiones Booleanas

Los valores booleanos pueden ser True o False. Son útiles para
representar estados y realizar validaciones.
```python
activo = True
if activo:
    print("El sistema está activo")
```

## If Statements

Los condicionales if permiten ejecutar código si se cumple una
condición.

Ejemplo:
```python
edad = 20
if edad >= 18:
    print("Eres mayor de edad")
```

### If-Else

Ejecuta una acción si la condición es True y otra si es False.
```python
edad = 16
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

### If-Elif-Else

Permite evaluar múltiples condiciones en cascada.
```python
edad = 15
if edad >= 18:
    print("Mayor de edad")
elif edad >= 13:
    print("Adolescente")
else:
    print("Niño")
```

## If Statements Anidados

Podemos anidar condicionales dentro de otros condicionales.
```python
edad = 20
ciudadano = True
if edad >= 18:
    if ciudadano:
        print("Puedes votar")
    else:
        print("No eres ciudadano")
else:
    print("Eres menor de edad")
```

## Switch-Case en Python

Python no tiene switch-case como otros lenguajes, pero podemos usar un if-elif-else o un diccionario.

Ejemplo con if-elif-else:
```python
opcion = 2
if opcion == 1:
    print("Seleccionaste 1")
elif opcion == 2:
    print("Seleccionaste 2")
elif opcion == 3:
    print("Seleccionaste 3")
else:
    print("Opción no válida")
```
Ejemplo con diccionario:
```python
def switch(opcion):
    opciones = {
        1: "Seleccionaste 1",
        2: "Seleccionaste 2",
        3: "Seleccionaste 3"
    }
    return opciones.get(opcion, "Opción no válida")

print(switch(2))
```