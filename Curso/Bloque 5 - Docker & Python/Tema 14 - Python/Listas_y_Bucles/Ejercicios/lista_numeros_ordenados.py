'''
Pide al usuario 4 numeros enteros y devuelve los numeros introducidos
en orden ascendente, junto con el numero mayor usando listas y el bucle for
'''

#Inicializamos la lista
lista_numeros = []

#Crear un bucle for para ir pidiendo los numerosy añadiendolos a la lista
for i in range(0,4):
    numero = int(input("Introduce un número entero: "))
    lista_numeros.append(numero)

#imprimir el mayor numero y la lista ordenada
print("El mayor número es: ", max(lista_numeros))
print("La lista ordenada es: ", sorted(lista_numeros))