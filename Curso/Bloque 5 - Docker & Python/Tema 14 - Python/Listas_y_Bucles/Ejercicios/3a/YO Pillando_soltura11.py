'''
Crea un programa que dada una lista de strings, devuelva otra lista con los strings en
mayúscula
'''

#Crear listas
frutas = ["manzana", "banana", "cereza", "durazno", "kiwi", "mango", "pera"]
frutas_mayuscula = []

#Recorrer la lista y añadir los strings en la nueva lista convirtiéndolos en mayúsculas
for fruta in frutas:
    frutas_mayuscula.append(fruta.upper())

print(frutas)
print(frutas_mayuscula)