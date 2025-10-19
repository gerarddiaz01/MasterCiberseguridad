'''
Escribe un programa en Python para encontrar los elementos duplicados de una lista,
añadirlos a una nueva lista y borrarlos de la lista. Después imprime una lista con tan solo los
elementos únicos.
'''

# Hacer lista
lista = [1, 2, 3, 4, 5, 1, 2, 6, 7, 8, 9, 3, 10]

# Crear dos listas para ir añadiendo cada numero y verificar si está duplicado o no
vistos = []
duplicados = []

# Hacer bucle para verificar cada elemento de la lista
for numero in lista[:]:  # Usar una copia de la lista para evitar modificarla mientras se recorre
    if numero in vistos and numero not in duplicados:
        duplicados.append(numero)
    else:
        vistos.append(numero)

# Eliminar duplicados de la lista original
for numero in duplicados:
    while numero in lista:
        lista.remove(numero)

# Imprimir por pantalla
print("Lista sin numeros duplicados:", lista)
print("Elementos duplicados:", duplicados)

'''
elementos_duplicados = []
elementos_unicos = []
for elementos in lista:
    if lista.count(elemento) > 1: #si el elemento está más de una vez en la lista lo añade a la lista de duplicados
        if elementos not in elementos_duplicados: #para evitar añadir los elementos duplicados más de una vez
            elementos_duplicados.append(elementos)
    else:
        elementos_unicos.append(elemento)
for elemento in elementos_duplicados:
    lista.remove(elemento)
print("Elementos_unicos:", elementos_unicos)
print("Elementos_duplicados:", elementos_duplicados)
print("Lista nueva:", lista)
'''