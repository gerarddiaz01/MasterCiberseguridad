'''
Crea un script que cuente el número de apariciones de un elemento de una lista en dicha lista
(P.e. en la lista lista=[23, 65, 23] el número de apariciones de 23 es 2)
'''

#Cear lista
lista = [1, 2, 3, 4, 5, 3, 2, 1, 4, 4]

#Inicializar contador y pedir al usuario que numero verificar
numero = int(input("Qué numero deseas verificar: "))
contador = 0

#Recorrer la lista, si el numero ya está en la lista subir el contador
for elemento in lista:
    if numero == elemento:
        contador += 1

#Imprimir el resultado
print(f"El numero {numero} está {contador} veces presente en la lista")

'''
print(lista.count(numero))

or

for elemento in lista:
    print(f"El elemento {elemento}, aparece {lista.count(elemento)} en la lista")
'''

