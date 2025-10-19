'''
Eres un profesor y deseas realizar un seguimiento de la asistencia de tus
estudiantes a lo largo del semestre. Cada estudiante tiene un nombre y
una lista de fechas en las que asistió a clases. Implementa un programa
en Python que utilice un diccionario para almacenar la información de las
asistencias. El programa debe permitir registrar la asistencia de los
estudiantes, agregar nuevas fechas de asistencia y mostrar la lista de
estudiantes y las fechas en las que asistieron.
'''

# diccionario base de datos
asistencias = dict()

# Registrar asistencias de estudiantes
asistencias["Gerard"] = ["2022-01-01", "2022-01-03", "2022-01-05"]
asistencias["Marc"] = ["2022-01-02", "2022-01-05", "2022-01-07"]
asistencias["Lea"] = ["2022-01-01", "2022-01-07", "2022-01-09"]

# Poder agregar nuevas asistencias, al ser una lista usamos append
asistencias["Gerard"].append("2022-01-15")

# Imprimir la lista de asistencias
for clave, valor in asistencias.items():
    print(clave)
    for fecha in valor:
        print(fecha)
    print("")
    #print(f" {valor[0]}\n {valor[1]}\n {valor[2]}") pero si añadimos más fechas no salen aqui