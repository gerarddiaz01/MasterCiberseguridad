'''
Crea un script dado un número introducido por el usuario o determinado al inicio del
programa, realice la suma de aquellos números que sean divisibles por este. 
'''

# Pedir un numero al usuario
divisor = int(input("Introduce un numero: "))

# Inicializar la variable suma a 0
suma = 0

# Hacer bucle para calcular la suma de los numeros divisibles por el numero introducido
for num in divisor:
    if num % divisor == 0:
        suma += num

#Imprimir los resultados
print("La suma de los numeros divisibles por", divisor, "es:", suma)
