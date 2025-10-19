'''
Crea un script que cuente el número de elementos más grandes que un determinado número
dado por el usuario (supón una lista numérica)'
'''

# Crear lista
lista = [10, 20, 4, 45, 99, 23, 75, 26, 13, 86, 54, 45, 69, 35, 895, 75, 24, 61, 43]

#Pedir al usuario un numero
numero_delimitador= int(input("Introduce un numero: "))
      
# Inicializar el contador
contador = 0

# Contar cuantos numeros están por encima del numero delimitador
for numero in lista:
    if numero > numero_delimitador:
        contador += 1

print("Hay", contador, "numeros por encima de", numero_delimitador)

'''

'''