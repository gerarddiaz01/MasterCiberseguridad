'''
Crea un diccionario empresa donde cada clave sea el nombre de un empleado y el valor sea otro diccionario con:
edad
departamento
activo
Luego:
Accede a la edad de Luis.
Cambia activo a False para Sara.
Agrega un nuevo empleado Pedro.
Muestra todos los nombres y departamentos.'''

empresa = {
    "Ana": {"edad": 30, "departamento": "IT", "activo": True},
    "Luis": {"edad": 35, "departamento": "HR", "activo": True},
    "Sara": {"edad": 28, "departamento": "Ventas", "activo": True}
}

print(empresa["Luis"]["edad"], "\n")

empresa["Sara"]["activo"] = False

empresa["Pedro"] = {"edad": 34, "departamento": "HR", "activo": False}

for empleado, empleado_info in empresa.items():
    print(f"{empleado} trabaja en el departamento de {empleado_info["departamento"]}")