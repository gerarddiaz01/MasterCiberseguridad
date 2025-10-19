'''
Crea un script que tome una lista de strings y cree una nueva lista que contenga el tamaño de
los strings de la lista original
'''

#Crear lista e inicializar lista de tamaño
frutas = ["manzana", "banana", "cereza", "durazno", "kiwi", "mango", "pera"]
length = []

#Recorrer la lista de frutas y añadir la fruta con su tamaño en la nueva lista
for fruta in frutas:
    length.append(len(fruta))

#Imprimir el resultado para verificar
print("Lista original:", frutas)
print("Lista de tamaños:", length)
