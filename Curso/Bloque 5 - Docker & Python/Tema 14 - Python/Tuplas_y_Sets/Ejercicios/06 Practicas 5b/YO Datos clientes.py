""" Una compañía tiene dos bases de datos de clientes. La primera base de datos contiene
el nombre del cliente, la dirección de correo electrónico y el número de teléfono. La
segunda base de datos contiene el nombre del cliente, la dirección y el historial de
pedidos. Escribe un programa que tome las dos bases de datos como listas de tuplas y
devuelva una nueva lista de tuplas que contenga solo los clientes que aparecen en
ambas bases de datos. Los clientes se consideran iguales si tienen el mismo nombre. """


base_datos1 = [("Juan", "juan@example.com", "555-1234"), ("Maria", "maria@example.com", "555-5678"), ("Pedro", "pedro@example.com", "555-9012")]
base_datos2 = [("Juan", "Calle 123", ["Libro1", "Libro2"]), ("Maria", "Calle 456", ["Libro3"]), ("Luis", "Calle 789", ["Libro4"])]


# Se crean dos conjuntos de nombres de clientes en ambas bases de datos, utilizando una comprensión de listas
nombres1 = {nombre[0] for nombre in base_datos1}
nombres2 = {nombre[0] for nombre in base_datos2}


# Se encuentra la intersección de ambos conjuntos, es decir, los clientes que aparecen en ambas bases de datos
nombres_comunes = nombres1.intersection(nombres2)

# Se imprime la lista de nombres de clientes comunes
print(f"Los nombres comunes entre ambas listas son :{nombres_comunes}")

# Se crea una lista de tuplas de clientes comunes, recorriendo las dos bases de datos mediante un bucle for anidado
# y comprobando si el nombre del cliente aparece en la lista de clientes comunes.
# Si el cliente coincide en ambas bases de datos, se agrega una nueva tupla a la lista clientes_comunes
# con la información del cliente de ambas bases de datos

""" clientes_comunes = []
for cliente1 in base_datos1:
    if cliente1[0] in nombres_comunes:
        for cliente2 in base_datos2:
            if cliente2[0] == cliente1[0]:
                clientes_comunes.append((cliente1[0], cliente1[1], cliente1[2], cliente2[1], cliente2[2])) """

clientes_comunes = [(cliente1[0], cliente1[1], cliente1[2], cliente2[1], cliente2[2])
                    for cliente1 in base_datos1
                    for cliente2 in base_datos2
                    if cliente1[0] in nombres_comunes and cliente2[0] == cliente1[0]
                    ]


# Se imprime la lista completa de clientes comunes
print(clientes_comunes)