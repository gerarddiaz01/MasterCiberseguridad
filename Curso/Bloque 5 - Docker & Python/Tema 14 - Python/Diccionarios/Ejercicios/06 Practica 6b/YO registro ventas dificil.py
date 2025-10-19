'''
Tienes una tienda y deseas realizar un seguimiento de las ventas diarias
de tus productos. Cada producto tiene un nombre y una cantidad
vendida. Implementa un programa en Python que utilice un diccionario
para almacenar la información de las ventas. El programa debe permitir
registrar las ventas de productos, actualizar la cantidad vendida de un
producto existente y calcular el total de ventas diarias.
'''

ventas = {}
control = True

while control:
    print("")
    opciones = input("1. Registrar venta\n2. Actualizar cantidad ya existente\n3. Calcular el total de ventas\n4. Salir del programa\nElige una opción: ")

    if opciones == "1":
        producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad vendida: "))
        if producto in ventas:
            ventas[producto] += cantidad
        else:
            ventas[producto] = cantidad
    elif opciones == "2":
        producto = input("Qué producto deseas actualizar? ")
        if producto in ventas:
            nueva_cantidad = int(input("Cuál es la nueva cantidad? "))
            ventas[producto] = nueva_cantidad
        else:
            print("Éste producto no está registrado.")
    elif opciones == "3":
        total_ventas = sum(ventas.values())
        print("")
        print("El total de ventas actual es:", total_ventas)
    elif opciones == "4":
        print("Saliendo del programa...")
        control = False
    else:
        ("Error: la opción ingresada no es válida")