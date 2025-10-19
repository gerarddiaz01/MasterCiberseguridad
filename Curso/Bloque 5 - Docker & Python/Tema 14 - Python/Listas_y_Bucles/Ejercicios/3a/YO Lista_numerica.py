'''
1. Crea una lista llamada “numeros“ que contenga los siguientes numeros enteros:
[1,2,3,4,5,6,7,8,9,10].
2. Crea una nueva lista con los números pares de la lista anterior en orden inverso
3. Escribe un bucle que recorra la lista “numeros“ e imprima el cuadrado de cada numero por
consola.
4. Intenta rehacer los pasos 2 y 3 con el menor número de lineas posible (método de
compresión).
5. Usa un método que te devuelva el número más pequeño de la lista e imprímelo por pantalla
6. Haz lo mismo con el número más alto
7. Suma todos los elementos de la lista con y sin un bucle.
8. Encuentra el índice correspondiente al número 8 en la lista original y en la lista resultante tras
el punto 2. 
'''

#1
numeros = list(range(1, 11))
#2
numeros_pares = list(range(10, 1, -2))
print(numeros_pares)
#3
for numero in numeros:
    print(numero ** 2)
#4
numeros_pares = [num for num in numeros if num % 2 == 0][::-1]
cuadrados = [num ** 2 for num in numeros]
print(cuadrados)
#5
print("El numero más pequeño es", min(numeros))
#6
print("El numero mas alto es", max(numeros))
#7
suma = 0
for numero in numeros:
    suma += numero
print("La suma de todos los numeros es", suma)

print("La suma de todos los numeros es", sum(numeros))
#8
indice_original = -1
for i in range(len(numeros)):
    if numeros[i] == 8:
        indice_original = i
        break
print("El índice del número 8 en la lista original es:", indice_original)

indice_pares = -1
for i in range(len(numeros_pares)):
    if numeros_pares[i] == 8:
        indice_pares = i
        break
if indice_pares != -1:
    print("El índice del número 8 en la lista de números pares es:", indice_pares)
else:
    print("El número 8 no está en la lista de números pares.")

#8.1
indice_8_original = numeros.index(8)
indice_8_invertida = numeros_pares_invertidos.index(8)

print(indice_8_original)
print(indice_8_invertida)

