'''
Crea un diccionario llamado estudiante con las claves: nombre, edad, carrera y promedio. Luego:
Accede al nombre.
Modifica el promedio.
Agrega una nueva clave aprobado con valor True o False según si el promedio es mayor o igual a 6.
Elimina la clave edad.'''

estudiante = {
    "nombre": "Gerard",
    "edad": 30,
    "carrera": "Conquer",
    "promedio": 7.1,
}
estudiante["promedio"] = 8.2

estudiante["aprobado"] = float(estudiante["promedio"]) >= 6

del estudiante["edad"]

for caracteristicas, valor in estudiante.items():
    print(f"{caracteristicas.title()}: {valor} \n")
