'''
Crea un script que extraiga los elementos comunes entre dos listas. 
'''

#Crear listas
lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [4, 5, 6, 7, 8, 9]
lista_comun = []

#Recorrer lista 1 y 2, si un elemento se repite lo añadimos a lista_comun
for elemento in lista1:
    if elemento in lista2:
         lista_comun.append(elemento)

print(f"Los elementos comunes entra las dos listas son: {lista_comun}")
