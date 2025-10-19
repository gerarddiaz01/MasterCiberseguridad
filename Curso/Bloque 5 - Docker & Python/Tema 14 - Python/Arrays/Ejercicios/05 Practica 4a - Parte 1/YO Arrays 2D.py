#1. Crea un array lleno de 1s con una longitud dada por el usuario
import numpy as np
longitud = int(input("Ingrese la longitud del array: "))
array1 = np.ones(longitud)
print(array1)
print("----------")

#2.Cambia la forma del array para que tenga una estructura de tipo (filas, columnas)
filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

if filas * columnas == longitud:
    array2 = np.reshape(array1, (filas,columnas))
    print("Array con nueva forma : \n", array2)
else:
    print("La cantidad de filas y columnas no es compatible con la longitud del array")
print("----------")

#3.Crea una “matriz identidad” con la misma forma que el array anterior (filas, columnas)
matriz_identidad = np.eye(filas,columnas)
print(matriz_identidad)
print("----------")

#4.Concatena ambas estructuras horizontalmente y verticalmente. (Pista: Investiga el 
# funcionamiento de concatenate() y de vstack() y hstack() de numpy)
array_columnas = np.concatenate((array2, matriz_identidad), axis=1)
print(f"Concatenación de ambos arrays en el eje 1 (columnas)")
print(array_columnas)
print("----------")
array_filas = np.concatenate((array2, matriz_identidad), axis=0)
print(f"Concatenación de ambos arrays en el eje 0 (filas)")
print(array_filas)
print("----------")