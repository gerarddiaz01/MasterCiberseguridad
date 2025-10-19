'''
Crea un programa que imprima todos los números primos entre el 2 y el 100. Un numero primo es
un numero positivo y entero mayor que uno que no tiene un divisor positivo y entero que no sea 1
o sí mismo
'''

#bucle que recorra los numeros del 2 al 100
for num in range(2, 101, +1):
    prime = True
	#comprobar que para dicho numero, hay alguno que pueda ser su divisor, si lo puede ser no es primo
    for i in range(2,num):
        if num % i == 0:
            prime = False
            break
    if prime: #es lo mismo poner if primo == True pero lo acortamos, es un valor booolean
        print(num)
