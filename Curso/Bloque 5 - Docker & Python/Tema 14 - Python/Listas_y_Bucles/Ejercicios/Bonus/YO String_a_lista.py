'''
Desarrolla un script en Python que dado una cadena de caracteres con la siguiente información:
nombre, apellido, DNI, código_asignatura, convocatoria, nota1, nota2, nota3 … Por ejemplo:
David Fernandez 12311267A 43527 2 2.1 4.6 3.4. El script debe crear una lista con esos datos,
introducirlo en una lista de listas donde se encuentra la información de todos los alumnos e
imprimir la nota media de los alumnos junto con el DNI.
Supón ahora que tu input es un string como este:
"David Fernandez 12311267A 43527 2 9.1 7.6 2.4\n
Maria Garcia 12316487A 43527 2 7.1 8.6 5.4\n
Juan Perez 647829236A 43527 2 8.1 8.5 8.4\n"
Reescribe el script para que procese ese input adecuadamente e imprima la nota media y el DNI
de todos los alumnos en ese string. 
'''

#tener el string a convertir en lista
entrada = "David Fernandez 12311267A 43527 2 2.1 4.6 3.4"

#hacer el split para crear una lista de sublistas
lista = entrada.split()
suma_notas = 0
for i in range(5, 7+1):
    suma_notas = suma_notas + float(lista[i])

nota_media = suma_notas/3

print(f"DNI: {lista[2]}, Nota Media: {nota_media:.2f}")

print("----------")

#Parte 2
#tener el string a convertir en lista
entrada2 = "David Fernandez 12311267A 43527 2 9.1 7.6 2.4\n" \
"Maria Garcia 12316487A 43527 2 7.1 8.6 5.4\n" \
"Juan Perez 647829236A 43527 2 8.1 8.5 8.4"

#usar el método split para convertir el string en una lista de lineas separadas por \n
lineas = entrada2.split('\n')

#almacenar dichas lineas a una nueva lista para que sean tres sublistas distintas
lista_de_listas = []
for linea in lineas:
    elementos = linea.split(' ')
    lista_de_listas.append(elementos)

#recorrer la lista de listas para calcular la nota media y obtener el dni de cada alumno
for alumno in lista_de_listas:
    media_alumno = 0
    notas_alumno = 0
    dni = alumno[2]
    for i in range(5, 7+1):
        notas_alumno = notas_alumno + float(alumno[i])
    media_alumno = notas_alumno/3
    print(f"DNI: {dni}, Nota Media: {media_alumno:.2f}")


