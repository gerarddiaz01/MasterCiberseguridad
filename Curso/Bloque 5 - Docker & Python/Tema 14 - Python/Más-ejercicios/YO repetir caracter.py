# string = input("Ingresa un string de 5 caracteres: ")

# if len(string) != 5:
#     print("El string debe tener exactamente 5 caracteres.")
# else:
#     resultado = ''.join([char * 2 for char in string])
#     print("El string con caracteres duplicados es:", resultado)

#Pedir un string de 5 caracteres
palabra = input("Ingresa una palabra de 5 caracteres: ")

print(palabra[0]*2 + palabra[1]*2 + palabra[2]*2 + palabra[3]*2 + palabra[4]*2)
#or
# print(palabra[0] + palabra[0] + palabra[1] + palabra[1] + palabra[2] + \
#       palabra[2] + palabra[3] + palabra[3] + palabra[4] + palabra[4])
