# def ocultar_numero_tarjeta(numero_tarjeta):
#     # Reemplaza todos los caracteres excepto los últimos cuatro con asteriscos
#     return '*' * (len(numero_tarjeta) - 4) + numero_tarjeta[-4:]

# # Solicita al usuario que ingrese el número de tarjeta de crédito
# numero_tarjeta = input("Introduce el número de tarjeta de crédito: ")

# # Imprime el número de tarjeta con los caracteres ocultos
# print(ocultar_numero_tarjeta(numero_tarjeta))

#Pedir al usuario que ingrese su numero de tarjeta de credito
numero_tarjeta = input("Introduce el número de tarjeta de crédito: ")

#Determinar la longitud del numero de tarjeta de credito
longitud = len(numero_tarjeta)

#Imprimir los ultimos 4 digitos del numero de tarjeta de credito
print(numero_tarjeta[longitud-4:longitud])

#Imprimir los numeros de la targeta de crédito ocultando los primeros 12 digitos
print("*" * (longitud-4), numero_tarjeta[longitud-4:longitud])
#or
# print("****" * 3, numero_tarjeta[12:16])
#or
# print("**** **** **** ", numero_tarjeta[12:16])