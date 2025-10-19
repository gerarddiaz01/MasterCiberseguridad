'''Pedir un número por consola (entero) y decir si es menor, igual o mayor a 10. 
Hacer que el programa continúe pidiendo un número hasta que 
introduzcamos el 0, y entonces, terminará'''

#pedir un número por consola
num = int(input("Introduce un número: "))


#mientras el número sea distinto de 0 decir si es menor, igual o mayor a 10
while num!= 0:
    if num < 10:
        print("El número es menor a 10")
    elif num == 10:
        print("El número es igual a 10")
    else:
        print("El número es mayor a 10")
    num = int(input("Introduce un número: "))

print("Fin del programa")
