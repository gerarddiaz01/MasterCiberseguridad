'''
1. Escribe un programa que pida al usuario un número entero y muestre por pantalla una
estructura como la de más abajo, donde el valor de entrada es el número de estrellas en el
centro de la estructura. 

*
**
***
****
*****
****
***
**
*
'''

# Pedimos al usuario un número entero
num = int(input("Introduce un número entero: "))

# Creamos un bucle que vaya desde 1 hasta n+1
for i in range (1, num, +1):
    print("*" * i)

# Creamos un bucle que vaya desde n+1 hasta 1
for i in range (num, 1, -1):
    print("*" * i)
