''' Ejercicio 4: Funciones lambda
Problema de Organización de Datos Empresariales:
Imagina que trabajas en una empresa internacional con equipos distribuidos en diferentes países. Cada equipo 
tiene una lista de empleados, representados como diccionarios, con información sobre el nombre, la edad y el 
rendimiento en proyectos recientes. Tu tarea es organizar una lista consolidada de todos los empleados de la empresa. 
La organización debe seguir ciertas reglas:
Los empleados se deben ordenar por el rendimiento en proyectos recientes de forma descendente.
Para aquellos con el mismo rendimiento, se deben ordenar por edad de forma ascendente. Además, deseas agrupar a los 
empleados por país para un análisis más efectivo. Utiliza funciones lambda. '''

from itertools import groupby

# Ordenar por país, rendimiento (descendente) y edad (ascendente)
def ordenar_empleados(empleados):
    empleados_ordenados = sorted(empleados,key=lambda emp: (emp["pais"], -emp["rendimiento"], emp["edad"]))
    return empleados_ordenados

# Agrupar por país
def agrupar_por_pais(empleados_ordenados):
    empleados_agrupados = groupby(empleados_ordenados, key=lambda emp: emp["pais"])
    return empleados_agrupados

# Mostrar los empleados agrupados por país
def mostrar_empleados(empleados_agrupados):
    for pais, grupo in empleados_agrupados:
        print(f"\nPaís: {pais}")
        for empleado in grupo:
            print(f"  {empleado}")

empleados = [
    {"nombre": "Juan Pérez", "edad": 30, "pais": "España", "rendimiento": 90},
    {"nombre": "María García", "edad": 28, "pais": "España", "rendimiento": 85},
    {"nombre": "Pedro Rodríguez", "edad": 26, "pais": "Argentina", "rendimiento": 95},
    {"nombre": "Ana Rodríguez", "edad": 32, "pais": "Argentina", "rendimiento": 105},
    {"nombre": "Sofía Gómez", "edad": 29, "pais": "Argentina", "rendimiento": 95},
    {"nombre": "José López", "edad": 32, "pais": "Bolivia", "rendimiento": 80},
    {"nombre": "Ana Sánchez", "edad": 35, "pais": "Bolivia", "rendimiento": 85},
]

empleados_ordenados = ordenar_empleados(empleados)
empleados_agrupados = agrupar_por_pais(empleados_ordenados)
mostrar_empleados(empleados_agrupados)

'''
sorted() con lambda: Ordena la lista de empleados según el criterio definido en la lambda. Usamos una tupla
en la lambda para ordenar por múltiples criterios.
    x["pais"]: Ordena primero por país.
    -x["rendimiento"]: Ordena por rendimiento en orden descendente.
    x["edad"]: Ordena por edad en orden ascendente.

groupby(): Agrupa elementos consecutivos de una lista según un criterio, en éste caso los empleados 
por el campo pais. La lista debe estar previamente ordenada por el campo de agrupación (pais).

Iteración sobre los grupos: groupby devuelve pares (clave, grupo), donde:
    clave: es el valor del campo de agrupación (pais).
    grupo: es un iterador con los empleados de ese grupo.

'''