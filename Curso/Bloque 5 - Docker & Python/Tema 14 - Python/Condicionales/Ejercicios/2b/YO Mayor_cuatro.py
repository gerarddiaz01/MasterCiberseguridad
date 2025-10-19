'''Crea un script que pida al usuario 4 números diferentes y imprima el mayor de los cuatro por
pantalla'''

# Pedimos los 4 números
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))
num4 = float(input("Introduce el cuarto número: "))

# Comprobamos cuál es el mayor
if num1 > num2 and num1 > num3 and num1 > num4:
    print("El mayor es el primer número: ", num1)
elif num2 > num1 and num2 > num3 and num2 > num4:
    print("El mayor es el segundo número: ", num2)
elif num3 > num1 and num3 > num2 and num3 > num4:
    print("El mayor es el tercer número: ", num3)
else:
    print("El mayor es el cuarto número: ", num4)
