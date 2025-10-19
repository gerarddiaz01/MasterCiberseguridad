'''Una red social tiene una base de datos de usuarios y sus correspondientes amistades.
Crea un programa que tome una base de datos de una red social como una lista de
tuplas, donde cada tupla contiene el nombre del usuario y una lista de sus amigos. Los
nombres repetidos en la lista de amigos corresponden a usuarios con varias cuentas
diferentes. Deberas eliminar las cuentas duplicadas y después devolver una tupla de
tuplas que contiene el número real de amigos por usuario y el usuario con más amigos.

Pista 1: Tus datos de entrada podrían ser así —> red_social = [("Juan", ["Maria", "Pedro",
"Luis"]), ("Maria", ["Juan", “Pedro”,”Juan”]), ("Pedro", ["Juan", "Maria"]), ("Luis", [“Juan”])]

Pista 2: Para eliminar duplicidades puedes usar sets 
'''

#Establece la base de datos
red_social = [("Juan", ["Maria", "Pedro", "Luis"]), ("Maria", ["Juan", "Pedro", "Juan"]), 
              ("Pedro", ["Juan", "Maria"]), ("Luis", ["Juan"])]

# Eliminamos los duplicados en las listas de amigos pasándolo a set y lo volvemos a pasar a lista
""" red_social_sin_duplicados = []
for usuario, amigos in red_social:
    amigos_sin_duplicados = list(set(amigos))
    red_social_sin_duplicados.append((usuario, amigos_sin_duplicados)) """

red_social_sin_duplicados = [(usuario, list(set(amigos))) for usuario, amigos in red_social]

# Calculamos el numero de amigos por usuario, y convertirmos la lista de tuplas en tupla de tuplas
""" amigos_por_usuario = []
for usuario, amigos in red_social_sin_duplicados:
    amigos_por_usuario.append((usuario, len(amigos))) """

amigos_por_usuario = [(usuario, len(amigos)) for usuario, amigos in red_social_sin_duplicados]

amigos_por_usuario = tuple(amigos_por_usuario)
print("Usuarios junto con número de amistades", amigos_por_usuario)

# Encontrar el usuario con más amigos, separando los usuarios de los amigos y sacando 
# el indice del usuario con mas amigos
usuarios = [tupla[0] for tupla in amigos_por_usuario]
numero_amigos = [tupla[1] for tupla in amigos_por_usuario]

indice_mas_amigos = numero_amigos.index(max(numero_amigos))
usuario_con_mas_amigos = usuarios[indice_mas_amigos]

print("Usuario con mayor amistades:", usuario_con_mas_amigos)


