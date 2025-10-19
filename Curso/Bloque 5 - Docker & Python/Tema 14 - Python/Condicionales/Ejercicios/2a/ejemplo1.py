'''Crea un script que dado un usuario le dé una bienvenida 
personalizada si es el administrador y una bienvenida
genérica si es otra persona'''

#Pedir al usuario que introduzca su nombre
nombre = input("Introduce tu nombre de usuario: ")

#Nombre del administrador
administrador = "alejandro"

#Comprobar si ese nombre es el mismo que el del administrador
if nombre.lower() == administrador: #case insensitive
    print("¡Bienvenido, ", nombre.title(), "!")
else:
    print("¡Bienvenido, invitado!")