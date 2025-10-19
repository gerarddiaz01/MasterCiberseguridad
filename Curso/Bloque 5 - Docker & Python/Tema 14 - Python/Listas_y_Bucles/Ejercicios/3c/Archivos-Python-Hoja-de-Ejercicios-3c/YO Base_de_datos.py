'''
Trabajas en colegio y estas encargado de mantener un seguimiento de las notas de los
estudiantes de un clase. En tu base de datos tienes una lista con los nombres de los estudiantes y
para cada estudiante debes guardar sus notas provenientes de deberes, exámenes y proyectos.
También necesitas calcular la nota media de cada estudiante y la nota media de la clase al
completo.
Pista: Para resolver este problema puedes usar una lista anidada donde guardes las notas para
cada estudiante. Entonces puedes usar un bucle para recorrer la lista de listas y calcular la nota
media de cada estudiante. También puedes usar otro bucle para calcular la nota media de toda la
clase. 
'''

#Hacemos la lista anidada con los datos de los estudiantes
datos_alumnos = [["Gerard", 7, 8, 6], ["Coline", 8, 9, 9], ["David", 5, 8, 5]]
notas_clase = []

#Con un bucle for recorremos la lista de listas y calculamos la nota media que hacemos print en cada iteración
#Añadimos la nota media de cada estudiante en la lista notas_clase para luego hacer la nota media de la clase omega easy
for alumno in datos_alumnos:
    nombre = alumno[0]
    notas = alumno[1:] #ponemos 1: porque decimos que a partir del indice 1 de la sublista todo lo demas sera notas (hay varias notas)
    nota_media = sum(notas) / len(notas)
    notas_clase.append(nota_media)
    print(f"La nota media de {alumno[0]} es {nota_media :.2f}") #:.2f es para redondear a dos decimales como mucho

#Sumamos las notas de la lista notas_clase para calcular la nota media de la clase
nota_media_clase = sum(notas_clase) / len(notas_clase)
print("La nota media de la clase es de {:.2f}".format(nota_media_clase)) #otra manera de redondear sin estar dentro del print(f"")