'''Pedir un número por consola (entero) y escribir todos los números impares, 
en orden decreciente, desde ese número hasta el 1'''

#pedir el numero al usuario
num = int(input("Ingrese un numero: "))

'''
#escribir los numeros impares en orden decreciente con un bucle for
for i in range(num, 0, -1):
    if i % 2 != 0:
        print(i)
'''

#escribir los numeros impares en orden decreciente con un bucle while
i = num
while i >= 1:
    if i % 2 != 0:
        print(i)
    i -= 1
