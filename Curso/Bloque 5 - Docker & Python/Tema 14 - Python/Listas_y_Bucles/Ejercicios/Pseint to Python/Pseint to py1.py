'''Pedir un número (entero) y escribir por consola todos los números hasta ese número, en orden creciente. 
Ejemplo: si el número es 12, habría que escribir por consola todos los números desde el 1 hasta el 12. '''

num = int(input("Ingrese un numero: "))
'''
for i in range(1, num+1):
    print(i)
'''
i = 1
while i <= num:
    print(i)
    i += 1


