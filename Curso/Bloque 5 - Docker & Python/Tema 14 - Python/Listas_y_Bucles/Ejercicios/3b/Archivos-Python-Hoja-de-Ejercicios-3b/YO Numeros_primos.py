'''
Dado una lista de números enteros, escribe un script en Python que devuelva una nueva lista con
los números primos de la lista original. Además, el script debe devolver el número total de
números primos encontrados y la suma de los números primos encontrados.
Un numero primo es un numero positivo y entero mayor que uno que no tiene un divisor positivo y entero que no 
sea 1 o sí mismo.  
'''
#Hacer la lista de numeros enteros y la lista vacía para añadir luego los numeros primos
numeros_aleatorios = [12, 45, 67, 23, 89, 34, 56, 78, 90, 11, 22, 33, 44, 55, 66]
numeros_primos = []

#Hacer bucle para recorrer la lista de numeros y verificar si son primos, si lo son incluir en la otra lista
#las unicas condiciones que tiene un numero primo para serlo son: ser divisible únicamente por 1 y si mismo
for num in numeros_aleatorios:
    prime = True
    i = 2
    while prime == True and i < num: #si un numero del 2 a num -1 puede ser su divisor then no es primo
        if num % i == 0:
            prime = False
        i += 1
    if prime:
        numeros_primos.append(num)


print(numeros_aleatorios)
print(numeros_primos)
print ("Hemos encontrado", len(numeros_primos), "numeros primos")
print("La suma de los numeros primos es", sum(numeros_primos))