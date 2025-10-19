'''Pide un numero por pantalla e indica si el numero es
divisible por 3 (en el sentido de que la division dé
cómo resultado un número entero)'''

#Pedir al usuario que introduzca un número
numero = int(input("Introduce un número: "))

#Comprobar si el número es divisible por 3
if numero % 3 == 0:
    print("El número", numero, "es divisible por 3")
else:
    print("El número", numero, "no es divisible por 3")