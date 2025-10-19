'''
Crea un programa en el que se pregunte al usuario por una frase y una letra, y muestre por
pantalla el número de veces que aparece la letra en la frase
'''

import time

#Pedir una frase al usuario
print("Vamos a contar cuantas veces aparece una letra en una frase...")
time.sleep(3)
print("... pero antes necesito que hagas algo por mi.")
time.sleep(2)
frase = input("Introduce una frase: ")
print("Vale, ahora un último favor...")
time.sleep(2)
#Pedir una letra al usuario
letra = input("Introduce una letra: ")

#Inicializar un contador
contador = 0

#Recorrer la frase y contar cuantas veces aparece la letra en la frase
for digito in frase:
    if digito.lower() == letra.lower():
        contador += 1
print("Calculando...")
time.sleep(2)
print("La letra introducida aparece", contador, "veces en la frase que has introducido")