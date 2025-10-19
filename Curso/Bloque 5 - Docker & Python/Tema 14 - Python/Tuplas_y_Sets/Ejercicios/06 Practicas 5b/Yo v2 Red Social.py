""" Una red social tiene una base de datos de usuarios y sus correspondientes amistades.
Crea un programa que tome una base de datos de una red social como una lista de
tuplas, donde cada tupla contiene el nombre del usuario y una lista de sus amigos. Los
nombres repetidos en la lista de amigos corresponden a usuarios con varias cuentas
diferentes. Deberas eliminar las cuentas duplicadas y después devolver una tupla de
tuplas que contiene el número real de amigos por usuario y el usuario con más amigos. """

red_social = [("Juan", ["Maria", "Pedro", "Luis"]), ("Maria", ["Juan", "Pedro", "Juan"]), 
              ("Pedro", ["Juan", "Maria"]), ("Luis", ["Juan"])]

# Eliminar cuentas duplicadas
""" red_social_sin_duplicados = []
for usuario, amigos in red_social:
    amigos_sin_duplicados = list(set(amigos))
    red_social_sin_duplicados.append((usuario, amigos_sin_duplicados)) """
red_social_sin_duplicados = [(usuario, list(set(amigos))) for usuario, amigos in red_social]

# Hacer tupla de tuplas con el numero real de amigos por usuario
""" amigos_por_usuario = []
for usuario, amigos in red_social_sin_duplicados:
    amigos_por_usuario.append((usuario, len(amigos))) """
amigos_por_usuario = [(usuario, len(amigos)) for usuario, amigos in red_social_sin_duplicados]

amigos_por_usuario = tuple(amigos_por_usuario)
print(f"Usuarios junto con el número de amistades: {amigos_por_usuario}")

# Calcular el usuario con más amigos
usuarios = [tupla[0] for tupla in amigos_por_usuario]
numero_amigos = [tupla[1] for tupla in amigos_por_usuario]
index_mas_amigos = numero_amigos.index(max(numero_amigos))
usuario_mas_amigos = usuarios[index_mas_amigos]
print(f"El usuario con más amistades es: {usuario_mas_amigos}")