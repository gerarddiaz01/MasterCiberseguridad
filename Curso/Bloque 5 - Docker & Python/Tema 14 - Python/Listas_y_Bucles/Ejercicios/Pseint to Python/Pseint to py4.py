'''Pedir un número (entero) y calcular su factorial (entero) 
Recordatorio: el factorial de un número se calcula multiplicando los números 
desde el 1 hasta el propio número, incluidos los números intermedios'''

#pedir el numero al usuario
num = int(input("Ingrese un numero: "))

'''
#calcular el factorial del numero introducido
factorial = 1
for i in range(1, num+1, +1):
    factorial = factorial * i

print(factorial)
'''

#calcular el factorial del numero introducido con un bucle while
factorial = 1
numero_inicial = 1
while numero_inicial <= num:
    factorial = factorial * numero_inicial
    numero_inicial += 1

print(factorial)