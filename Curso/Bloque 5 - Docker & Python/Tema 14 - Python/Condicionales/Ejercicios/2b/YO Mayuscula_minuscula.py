'''Permite que el usuario introduzca una letra (del alfabeto latino) como input. Comprueba si esta es
una mayúscula o una minúscula.'''

# Pedir al usuario que introduzca una letra
letra = input("Introduce una letra: ")

# Comprobar si la letra es mayúscula
if letra.isupper():
    print("La letra introducida es mayúscula.")

# Comprobar si la letra es minúscula
elif letra.islower():
    print("La letra introducida es minúscula.")

