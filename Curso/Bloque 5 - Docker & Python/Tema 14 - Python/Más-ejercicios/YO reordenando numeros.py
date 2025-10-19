# numero = int(input("Ingrese un número de mas de una cifra: "))
# numero_str = str(numero)
# if numero < 10:
#     print("El número tiene una cifra")
# else:
#     for digito in numero_str:
#         print(digito)

# numero_2 = int(input("Ingresa un numero entero de cuatro cifras: "))
# numero_str_2 =  str(numero_2)
# if numero_2 < 1000:
#     print("El número tiene menos de cuatro cifras")
# else:
#     for digito in numero_str_2[::-1]:
#         print(digito)

#Pedir al usuario que introduzca un numero
numero = input("Please introduce un numero entero de cuatro cifras: ")

#Mostrar el numero componente a componente por pantalla
print(numero[0] + "\n" + numero[1] + "\n" + numero[2] + "\n" + numero[3])

#Creamos el string inverso
# numero_inverso = numero[3] + numero[2] + numero[1] + numero[0]

# #Impresion del string inverso
# print(numero_inverso)
print(numero[::-1])