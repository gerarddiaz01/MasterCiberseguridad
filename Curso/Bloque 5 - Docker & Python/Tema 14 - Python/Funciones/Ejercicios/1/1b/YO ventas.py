'''Crea un programa que permita gestionar las ventas de una tienda. Utiliza una
estructura de datos adecuada para almacenar la información de las ventas
(por ejemplo, una lista de diccionarios). Implementa dos funciones, una para
agregar el producto vendido con su precio y otro para mostrar las ventas de
productos con sus respectivos precios.
(La base de datos puede tener la forma [{“Producto”: producto1, “Precio”:
precio1}, {“Producto”: producto2, “Precio”: precio2}…]) '''

def agregar_producto(lista):
    producto = input("Añadir producto: ")
    precio = int(input("Añadir el precio del producto: "))
    lista.append({"Producto": producto, "precio": precio})
    return lista

def mostrar_ventas(lista):
    for venta in lista:
        print("Producto:", venta["Producto"], "Precio:", venta["precio"])

lista_productos = []
continuar = True

while continuar:
    eleccion = input("Desea... 1. Añadir un producto a la lista, 2. Mostrar lista de ventas, 3. Salir del programa: ")
    if eleccion == "1":
        agregar_producto(lista_productos)
        print("")
    
    elif eleccion == "2":
        mostrar_ventas(lista_productos)
        print("")

    elif eleccion == "3":
        continuar = False
        print("Saliendo del programa...")

