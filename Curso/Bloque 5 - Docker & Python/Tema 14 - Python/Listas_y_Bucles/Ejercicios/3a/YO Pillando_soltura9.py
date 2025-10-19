'''
Escribe un programa que lea una lista de enteros y cree una nueva lista que contenga solo
números positivos de la lista original
'''

#Crear lista e inicializar lista de numeros positivos
lista_original = [12, -7, 5, -3, 9, -1, 0, 4, -6, 8, -2, 11, -4, 3, -5]
lista_positivos = []

#Recorrer lista original y si el numero es positivo añadirlo a la lista de positivos
for numero in lista_original:
    if numero > 0:
        lista_positivos.append(numero)

#Imprimir lista de positivos
print(f"La lista de numeros positivos es la siguiente: {lista_positivos}")