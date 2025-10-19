'''Crea una función recursiva llamada suma_lista que calcule la suma de todos
los elementos de una lista de enteros. Puedes asumir que la lista no está
vacía'''

def suma_lista(lista_enteros):
    ''' sumar los elementos de una lista de enteros'''
    #input: lista (lista de numeros enteros)
    #output: resultado (int, suma de los elementos de la lista)

    # caso base
    if len(lista_enteros) == 1:  # Caso base: si la lista tiene un solo elemento, devuelve ése elemento y se detiene la recursión
        return lista_enteros[0]
    
    # sentencia recursiva
    else: # Si la lista tiene más de un elemento
        # Suma el primer elemento (lista[0]) con la suma del resto de la lista
        return lista_enteros[0] + suma_lista(lista_enteros[1:]) # Usamos slicing para excluir el primer elemento de la lista
        # 1: significa que vamos el indice 1 hasta el final

lista = [1, 2, 3, 4, 5]
print(suma_lista(lista))  # Salida esperada: 15

# vamos reduciendo la lista con cada recursión hasta que queda solo un numero

# Primera llamada:
# lista_enteros = [1, 2, 3, 4, 5]
# lista_enteros[0] = 1
# lista_enteros[1:] = [2, 3, 4, 5]
# Resultado parcial: 1 + suma_lista([2, 3, 4, 5])

# Segunda llamada:
# lista_enteros = [2, 3, 4, 5]
# lista_enteros[0] = 2
# lista_enteros[1:] = [3, 4, 5]
# Resultado parcial: 1 + 2 + suma_lista([3, 4, 5])

# Tercera llamada:
# lista_enteros = [3, 4, 5]
# lista_enteros[0] = 3
# lista_enteros[1:] = [4, 5]
# Resultado parcial: 1 + 2 + 3 + suma_lista([4, 5])

# Cuarta llamada:
# lista_enteros = [4, 5]
# lista_enteros[0] = 4
# lista_enteros[1:] = [5]
# Resultado parcial: 1 + 2 + 3 + 4 + suma_lista([5])

# Quinta llamada (caso base):
# lista_enteros = [5]
# len(lista_enteros) == 1 + 2 + 3 + 4 + 5 = 15 ( en este caso ya entra en el if y se termina la recursividad)