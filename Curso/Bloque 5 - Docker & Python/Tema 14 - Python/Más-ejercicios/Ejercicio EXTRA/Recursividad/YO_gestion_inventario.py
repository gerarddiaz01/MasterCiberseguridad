'''
Problema de Gestión de Inventario: Imagina que trabajas en una empresa de logística y tu tarea es desarrollar un 
sistema de gestión de inventario. El inventario está representado como una lista 
de productos ordenados por sus códigos. Cada producto se describe como un diccionario con las claves 
'codigo' y 'cantidad'. Tu objetivo es implementar una función recursiva que realice una búsqueda binaria en 
este inventario y devuelva la cantidad disponible para un producto específico, dado su código.
A continuacion un ejemplo de una posible entrada y salida de la solucion:
Entrada
Inventario de productos (json,dic,etc)
Codigo de producto buscado
Salida
Cantidad disponible para el producto 307
80'''

def buscar_producto(inventario, codigo_buscado, inicio, fin):
    # Caso base: el rango de búsqueda es inválido
    if inicio > fin:
        return f"El producto con código {codigo_buscado} no se encuentra en el inventario."
    
    # Calcular el índice medio
    medio = (inicio + fin) // 2
    producto = inventario[medio]
    
    # Comparar el código del producto en la posición media con el código buscado
    if producto['codigo'] == codigo_buscado:
        return f"Cantidad disponible para el producto {codigo_buscado}: {producto['cantidad']}"
    elif producto['codigo'] < codigo_buscado:
        # Buscar en la mitad derecha
        return buscar_producto(inventario, codigo_buscado, medio + 1, fin)
    else:
        # Buscar en la mitad izquierda
        return buscar_producto(inventario, codigo_buscado, inicio, medio - 1)

# Ejemplo de uso
inventario = [
    {'codigo': 101, 'cantidad': 50},
    {'codigo': 203, 'cantidad': 30},
    {'codigo': 307, 'cantidad': 80},
    {'codigo': 412, 'cantidad': 20},
    {'codigo': 523, 'cantidad': 15}
]

codigo_buscado = 307
resultado = buscar_producto(inventario, codigo_buscado, 0, len(inventario) - 1)
print(resultado)