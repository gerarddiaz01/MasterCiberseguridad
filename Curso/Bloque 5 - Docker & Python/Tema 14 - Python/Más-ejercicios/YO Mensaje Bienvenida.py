#Pedir nombre de usuario
nombre = input("Cómo te llamas")

#Reformatear nombre
nombre = nombre.replace(".", "")

#Escribimos mensaje en una variable
lenguaje = "python"
mensaje = "¡Hola, " + nombre.title() + "estás usando " + lenguaje.title() + "!"

#Imprimimos mensaje por pantalla
print(mensaje)
# print(mensaje.upper())
# print(mensaje.lower())