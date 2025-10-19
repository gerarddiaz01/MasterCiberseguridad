'''
Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta
'''

# Importar la librería time
import time

# Definimos la variable contraseña
contraseña = "password"
respuesta = False


# Hacer un bucle que pida la contraseña al usuario hasta que sea correcta
while respuesta == False:
    pregunta = (input("Ingrese la contraseña: "))
    if pregunta == contraseña:
        respuesta = True
    else:
        print("Contraseña incorrecta, pruebe de nuevo")
        time.sleep(1)

print("Contraseña correcta")
