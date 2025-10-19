'''
CALCULO DE NOTAS FINALES
Supongamos que tienes un conjunto de calificaciones de un grupo de estudiantes en un
curso. Cada estudiante tiene cuatro calificaciones: dos exámenes, un trabajo final y una
participación en clase. Quieres calcular la nota final de cada estudiante, donde los
exámenes valen un 30% cada uno, el trabajo final vale un 30% y la participación en clase
vale un 10%. Para ello, puedes usar NumPy para crear un array de 4 columnas y n filas,
donde n es el número de estudiantes. Cada columna representa una de las calificaciones
y cada fila representa un estudiante. Luego, puedes usar operaciones de NumPy para
calcular la nota final de cada estudiante y almacenarla en un nuevo array de una sola
columna.
'''
'''
import numpy as np

#Definir el numero de estudiantes
n_estudiantes = 5

#Crear un array de calificaciones con valores aleatorios entre 0 y 100
#Columnas: [Examen 1, Examen 2, Trabajo Final, Participación en Clase]
calificaciones = np.random.randint(0, 101, size=(n_estudiantes, 4))
print("Array de calificaciones:")
print(calificaciones)

#Calcular la nota final de cada estudiante
notas_finales = np.zeros(n_estudiantes)
for i in range(n_estudiantes):
    nota_final = (calificaciones[i, 0] * 0.30 + calificaciones[i, 1] * 0.30 + calificaciones[i, 2] * 0.30 + calificaciones[i, 3] * 0.10)
    notas_finales[i] = nota_final

#Convertir el array a una columna
notas_finales_columna = notas_finales.reshape(n_estudiantes, 1)

print("Notas finales de cada estudiante")
print(notas_finales_columna)'
'''

# importar modulos
import numpy as np

# calificaciones de los estudiantes / input 
calificaciones = np.array([
    [8, 7, 9, 10],
    [6, 8, 7, 9],
    [9, 9, 8, 8],
    [7, 6, 6, 7],
    [10, 9, 10, 10]
])

# separar los datos en diferentes arrays
examen1 = calificaciones[:,0]
examen2 = calificaciones[:,1]
trabajo_final = calificaciones[:,2]
participacion = calificaciones[:,3]

# calcular las notas segun peso
nota_final = examen1 * 0.3 + examen2 * 0.3 + trabajo_final * 0.3 + participacion * 0.1

# mostrar los resultados
for i in range(len(nota_final)):
    print("La nota final del estudiante", i+1, "es:", nota_final[i])