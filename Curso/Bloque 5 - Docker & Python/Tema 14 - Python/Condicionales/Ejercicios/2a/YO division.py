#pedir numeros al usuario para la división
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

#mostrar por pantalla el resultado de la división, indicar "error" si el divisor es 0
if numero2 == 0:
    print("Error")
else:
    print(numero1 / numero2)
