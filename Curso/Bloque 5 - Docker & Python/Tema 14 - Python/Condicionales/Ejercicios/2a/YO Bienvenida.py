#Pedir al usuario que introduzca su nombre
nombre = input("Introduce tu nombre de usuario: ")

#determinar los variables de los usuarios existentes
usuario1 = "alejandro"
usuario2 = "naomi"
usuario3 = "sergio"

#reformatear los nombres de usuario por si se escriben con un . o una #
nombre = nombre.replace(".", "").replace("#", "")

#Comprobar si el usuario introducido es uno de los usuarios existentes
if nombre.lower() == usuario1:
    print("¡Bienvenido, ", nombre.title(), "!")
elif nombre.lower() == usuario2:
    print("¡Bienvenido, ", nombre.title(), "!")
elif nombre.lower() == usuario3:
    print("¡Bienvenido, ", nombre.title(), "!")
else:
    print("¡Bienvenido, invitado!")
