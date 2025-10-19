'''
Escribe un script que pida un número al usuario y dada una lista encuentre el número 
más alto que es inferior al número introducido o determinado al inicio del programa. 
'''

#Pedir numero al usuario
numero = int(input("Introduce un numero: "))

#Crear lista
lista = [35, 74, 18, 95, 46, 62, 21, 10, 58, 89]

#Ordenar lista
lista.sort()

#Inicializamos la variable indice
indice = 0

#Encontrar el indice de la lista el cual empiezan los numeros superiores al numero
for i in range(len(lista)):
    if lista[i] >= numero:
        indice = i
        break
    else:
        indice = len(lista)

#Hacer la sublista de los numeros de la lista inferiores usando el indice
sublista = lista[:indice]

#Determinar el numero mas alto inferior al numero introducido e imprimirlo
if sublista:
    max_inferior = sublista[-1]
    print("El numero más grande inferior al numero introducido es", max_inferior)
else:
    print("No hay números en la lista que sean inferiores al número introducido")

'''
lista.sort()
for num in lista:
    if num < numero:
        resultado = num
print(resultado)
'''