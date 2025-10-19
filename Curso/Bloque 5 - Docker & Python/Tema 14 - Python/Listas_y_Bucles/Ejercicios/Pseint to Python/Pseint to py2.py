'''Pedir dos números por consola (enteros) y sumar (entero) todos los números que hay entre ellos'''

#pedir los numeros al usuario
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número, mayor que el numero anterior: "))

'''
#sumar los numeros entre los dos numeros introducidos utilizando un bucle while
num_inicial = num1 + 1
suma = 0

while num_inicial < num2:
    suma = suma + num_inicial
    num_inicial += 1

print(suma)
'''

#sumar los numeros entre los dos numeros introducidos utilizando un bucle for
suma = 0
for i in range(num1+1, num2, +1):
    suma = suma + i

print(suma)


