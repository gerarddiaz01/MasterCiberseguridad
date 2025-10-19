'''
Analisis de precios de productos:
Escribir un programa en Python que analice una lista de precios de productos
y determine el precio mas alto, el precio mas bajo y el precio promedio de todos los productos.
Soluciona el ejercicio sin utilizar la función max() ni min()
'''

#inicializamos la lista de precios
precios = [10.99, 14.99, 13.76, 12.50, 11.98]
precio_total = 0
precio_max = 0.0
precio_min = float("inf") #cualquier precio sera menor que este y podemos empezar el bucle

#hacer el bucle para recorrer la lista de precios
for precio in precios:
#comprobar si el precio es el mas alto que el anterior
    if precio > precio_max:
        precio_max = precio
#comprobar si el precio es el mas bajo que el anterior
    if precio < precio_min:
        precio_min = precio
#sumar todos los precios para calcular el promedio
    precio_total += precio

#calcular el precio promedio
promedio = precio_total / len(precios)

#imprimir los resultados
print("El precio más alto es: ", precio_max)
print("El precio más bajo es: ", precio_min)
print("El precio promedio es: ", promedio)