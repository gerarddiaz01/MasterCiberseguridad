'''Pedir un número (entero) y calcular qué números desde el 1 hasta el propio 
número son múltiplos de 2 y 3. 
Recordatorio: un número es múltiplo de 2 si al dividir por 2, el resto es 0; 
y es múltiplo de 3 si al dividir por 3, el resto es 0 
Ejemplo: dado el número 15, los números múltiplos de 2 y 3 hasta 15 son 6 y 12 (resto  
0 en ambas divisiones)'''

#pedir un número por consola
num = int(input("Introduce un número: "))

'''
#calcular los múltiplos de 2 y 3 desde 1 hasta el número introducido
for i in range(1,num+1, +1): #para i desde 1 hasta el número introducido incluido (num+1)
    if i%2 == 0 and i%3 == 0:
        print(i)
'''

#calcular los múltiplos de 2 y 3 desde 1 hasta el número introducido
i = 1
while i <= num:
    if i%2 == 0 and i%3 == 0:
        print(i)
    i = i + 1
print