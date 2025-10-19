'''Crea un script que pida al usuario 3 números diferentes y le indique si alguno de ellos 
es la suma de los otros dos'''

# Pedimos los números al usuario
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

# Comprobamos si alguno de los números es la suma de los otros dos
if num1 == num2 + num3:
    print(num1, "es la suma de", num2, "y", num3) 
elif num2 == num1 + num3:
    print(num2, "es la suma de", num1, "y", num3)
elif num3 == num1 + num2:
    print(num3, "es la suma de", num1, "y", num2)
else:
    print("Ningún número es la suma de los otros dos")
