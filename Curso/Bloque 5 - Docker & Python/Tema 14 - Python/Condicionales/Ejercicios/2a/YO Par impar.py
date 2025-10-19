#Pedir al usuario que introduzca un número y una potencia
numero = int(input("Introduce un número: "))
potencia = int(input("Introduce la potencia: "))

#Comprobar si el número elevado a la potencia es par o impar
resultado = numero ** potencia
if resultado % 2 == 0:
    print("El resultado es par")
else:
    print("El resultado es impar")