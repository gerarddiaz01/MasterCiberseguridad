# Python - Clase 7: Diccionarios (Parte 1)

## ¿Qué es un DICCIONARIO?

Un **diccionario** es una colección **no ordenada** de **pares
clave-valor**.

-   Cada elemento tiene una **clave** que apunta a un **valor**.

-   No se accede con índices, sino con claves.

Ejemplo:
```python
alumno = {
    "nombre": "Ana",
    "edad": 22,
    "carrera": "Ingeniería"
}
```
## SINTAXIS BÁSICA

### Diccionario vacío
```python
dict = {}
```
### Diccionario con valores
```python
dict = {"clave1": "valor1", "clave2": "valor2"}
```
-   Las **claves** pueden ser strings, números o incluso tuplas.

-   Los **valores** pueden ser de cualquier tipo.

## TRABAJAR CON ELEMENTOS

### Ejemplo:
```python
alumno = {
    "nombre": "Ana",
    "edad": 22,
    "carrera": "Ingeniería"
}
```
### Acceder a valores
```python
mi_diccionario = {"manzana": 1, "platano": 2, "naranja": 3}

print(mi_diccionario["manzana"])

# salida: 1
```
o
```python
alumno["nombre"] # "Ana"
```
### Modificar valores
```python
alumno["edad"] = 23
```
Agregar nuevos pares
```python
alumno["promedio"] = 8.9
```
Eliminar pares clave-valor
```python
del alumno["carrera"]
```

Trabajar con diccionarios vacíos
```python
mi_diccionario = {}

mi_diccionario["manzana"] = 1
mi_diccionario["platano"] = 2

print(mi_diccionario)
print(type(mi_diccionario))

# salida: {"manzana": 1, "platano": 2}
# class "dict"
```
## CASOS DE USO COMUNES

1) Información diversa de un objeto
```python
docente = {
    "nombre": "Luis",
    "materia": "Matemáticas",
    "años_exp": 10
}
```
2) Varios objetos de un mismo tipo de información
```python
notas = {
    "Ana": 8.5,
    "Luis": 9.0,
    "Sara": 7.5
}
```
## Buenas prácticas:

-   Usar claves claras y legibles.

-   Consistencia en el tipo de datos.

## MÉTODOS DE LOS DICCIONARIOS

### keys()

Devuelve una lista con todas las claves:
```python
alumno.keys() # dict_keys(['nombre', 'edad', 'promedio'])
```
### values()

Devuelve una lista con todos los valores:
```python
alumno.values()
```
### items()

Devuelve una lista de tuplas clave-valor:
```python
alumno.items()
```
### get()

Devuelve el valor de una clave, y evita error si no existe:
```python
alumno.get("edad") # 23

alumno.get("carrera") # None

alumno.get("carrera", "No registrada")
```
### pop()

Elimina la clave y almacena el valor de dicha clave en otra variable:
```python
alumno = {"nota": 8, "promedio": 9.3}

valor_promedio = alumno.pop("promedio")

print(valor_promedio)

# salida: 9.3
```
### clear()

Elimina todos los pares del diccionario:
```python
alumno.clear()
```
## CONVERTIR OTRAS ESTRUCTURAS A DICCIONARIO

### De **tuplas** a diccionario
```python
eventos = [("2023-01-01", 120), ("2023-01-02", 80)]

registro = dict(eventos)
```
⚠ Si hay claves duplicadas, se conserva el valor de la última:
```python
[("A", 1), ("A", 2)] # → {"A": 2}
```
### De **listas** a diccionario (usando zip())
```python
materias = ["Matemáticas", "Historia", "Física"]

notas = [9, 8, 10]

calificaciones = dict(zip(materias, notas))
```
⚠ Ambas listas deben tener la misma longitud.

### De **sets** a diccionario
```python
datos = {("Ana", 8.5), ("Luis", 9.0)}

dict = dict(datos)
```
## RECORRER DICCIONARIOS

### Recorrer pares (clave y valor)
```python
dic = {"nombre": "Ana", "edad": 22}

for clave, valor in dic.items():
    print(clave, ":", valor)
```
### Recorrer solo claves

**Forma explícita:**
```python
for clave in dic.keys():
    print(clave)
```
**Forma implícita (equivalente):**
```python
for clave in dic:
    print(clave)
```
### Recorrer solo valores
```python
for valor in dic.values():
    print(valor)
```
### Obtener solo valores únicos:
```python
valores_unicos = set(dic.values())
```
## ANIDAMIENTO EN DICCIONARIOS

### Lista de diccionarios

Ideal para representar colecciones de objetos.
```python
usuarios = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30},
    {"nombre": "Sara", "edad": 22}
]

for usuario in usuarios:
    print(usuario["nombre"], usuario["edad"])
```
o
```python
usuario_1 = {
    "nombre": "Ana",
    "edad": 25,
}

usuario_2 = {
    "nombre": "Luis",
    "edad": 30,
}

usuario_3 = {
    "nombre": "Sara",
    "edad": 22,
}

usuarios = [usuario_1, usuario_2, usuario_3]

usuario3_edad = usuarios[2]["edad"]

print(usuario3_edad)

# salida: 22
```
-   Se accede por índice de la lista y luego por clave del diccionario.

-   usuarios[2] corresponde al tercer elemento dentro de la colección
    de diccionarios, empezamos por 0 al ser un índice, y luego
    especificamos la clave del diccionario que queremos.

### Ejemplo:
```python
# Datos de un pedido de pizza

pizza = {
    'masa': 'fina',
    'ingredientes': ["aceitunas", "champiñones"],
}

# Resumen del pedido

print("Has pedido una pizza de masa " + pizza['masa'] + " con los siguientes ingredientes:")

for ingrediente in pizza['ingredientes']:
    print(ingrediente)
```
### Ejemplo:
```python
# Datos de trabajadores

programadores = {
    'juan': ['python', 'c++'],
    'sara': ['c', 'rust'],
    'eduardo': ['solidity', 'fortran'],
    'felipe': ['python', 'fortran', 'R'],
}

for nombre, lenguajes in programadores.items():
    print("\n" + nombre.title() + " sabe usar los lenguajes:")
    for lenguaje in lenguajes:
        print(lenguaje.title())
```
### Diccionarios con listas como valores

**Ejemplo: pedidos en un restaurante**
```python
pedidos = {
    "mesa1": ["pasta", "agua"],
    "mesa2": ["pizza", "vino"]
}
```
**Ejemplo: empleados por departamento**
```python
empresa = {
    "IT": ["Ana", "Luis"],
    "HR": ["Pedro", "Sara"]
}
```
### Diccionarios dentro de diccionarios
```python
alumnos = {
    "ana": {"edad": 23, "nota": 9},
    "luis": {"edad": 25, "nota": 8}
}

print(alumnos["ana"]["nota"]) # 9
```

**Diccionario con usuarios de una página web**
```python
users = {
    'lvene': {
        'nombre': 'lucas',
        'apellido': 'vene',
        'ubicacion': 'paris',
    },
    'crodriguez': {
        'nombre': 'carlos',
        'apellido': 'rodriguez',
        'ubicacion': 'madrid',
    },
    'tbauer': {
        'nombre': 'thomas',
        'apellido': 'bauer',
        'ubicacion': 'berlin',
    }
}
```
o
```python
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['nombre'] + " " + user_info["apellido"]
    ubicacion = user_info["ubicacion"]
    print("\tNombre completo: " + full_name.title())
    print("\tUbicacion: " + ubicacion.title())
```
**Atención:** Este tipo de estructura puede volver el código complejo
si no se maneja con claridad.

**Consejo**: Mantén la misma estructura interna para facilitar el acceso
y manipulación.