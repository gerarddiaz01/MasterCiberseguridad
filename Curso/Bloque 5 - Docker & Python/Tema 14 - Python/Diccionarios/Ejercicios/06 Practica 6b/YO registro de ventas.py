'''
Tienes una tienda y deseas realizar un seguimiento de las ventas diarias
de tus productos. Cada producto tiene un nombre y una cantidad
vendida. Implementa un programa en Python que utilice un diccionario
para almacenar la información de las ventas. El programa debe permitir
registrar las ventas de productos, actualizar la cantidad vendida de un
producto existente y calcular el total de ventas diarias.
'''

# diccionario de ventas diarias
ventas = {
    "Producto1": 0,
    "Producto2": 0,
    "Producto3": 0
}

# Actualizar cantidad vendida de un producto existente
new_sell1 = int(input("Cuántas nuevas ventas de Producto1 deseas añadir?: "))
new_sell2 = int(input("Cuántas nuevas ventas de Producto2 deseas añadir?: "))
new_sell3 = int(input("Cuántas nuevas ventas de Producto3 deseas añadir?: "))
ventas["Producto1"] += new_sell1
ventas["Producto2"] += new_sell2
ventas["Producto3"] += new_sell3
print("")
# Imprimir el registro de ventas y el total de ventas diarias
print("Registro de ventas:")
for clave, valor in ventas.items():
    print(f"Ventas diarias del {clave}: {valor}")

print("")

total_ventas = 0
for valor in ventas.values():
    total_ventas += valor
#total_ventas = sum(ventas.values())

print(f"Las ventas totales diarias equivalen a {total_ventas}")