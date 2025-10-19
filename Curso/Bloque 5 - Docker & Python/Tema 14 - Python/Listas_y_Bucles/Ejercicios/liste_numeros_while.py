'''
Pide al usuario 4 numeros enteros y devuelve los numeros introducidos
en orden ascendente, junto con el numero mayor usando listas y el bucle while
'''

#Inicializamos la lista
lista_numeros = []

#Crear un bucle while para ir pidiendo los numeros y añadirlos a la lista
while len(lista_numeros) < 4:
    numero = int(input("Introduce un número entero: "))
    if numero.isnumeric() == False: # Comprueba si el valor introducido es numérico, sin comas
        print("Por favor, introduce un número entero")
        continue   # Salta a la siguiente iteración si se introduce un valor no numérico
    lista_numeros.append(numero)

#Imprimir el mayor número y la lista ordenada
lista_numeros.sort()    # Ordena la lista de menor a mayor de manera definitiva
print("El numero mayor es ", lista_numeros[-1]) # Imprime el último elemento de la lista ya ordenada
print("La lista ordenada es: ", lista_numeros)
