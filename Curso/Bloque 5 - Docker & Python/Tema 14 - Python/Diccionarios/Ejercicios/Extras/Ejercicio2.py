'''Tienes dos listas:
alumnos = ["Ana", "Luis", "Pedro"]
notas = [9.5, 8.2, 6.7]
Crea un diccionario que relacione a cada alumno con su nota. Luego:
Imprime: Ana tiene una nota de 9.5, etc.
Crea una lista con los nombres de los aprobados (nota >= 7)'''

alumnos = ["Ana", "Luis", "Pedro"]
notas = [9.5, 8.2, 6.7]

'''
estudiantes = {
    'Ana': 9.5, 
    'Luis': 8.2, 
    'Pedro': 6.7,
    }
'''

estudiantes = dict(zip(alumnos, notas))

for alumno, nota in estudiantes.items():
    print(f"{alumno} tiene una nota de {nota}")

""" aprobados = []
for alumno, nota in estudiantes.items():
    if nota >= 7:
        aprobados.append((alumno, nota)) """

aprobados = [alumno for alumno, nota in estudiantes.items() if nota >= 7]
print(f"Los aprobados son {aprobados}")