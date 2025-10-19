'''En una obra es necesario construir para el tejado de una casa una estructura 
triangular con tres piezas. El ingeniero se pregunta si dadas la largura de las piezas 
que ha recibido podrá construir esta estructura. Crea un script que dados tres 
longitudes indique si podría construirse un triangulo con esas piezas.
(Pista: la suma de dos piezas tiene que ser mayor que el lado restante. 
Esto debe ser así para todas las posibles combinaciones)'''

# Pedimos las longitudes de las piezas al usuario
lado1 = int(input("Introduce la longitud de la primera pieza: "))
lado2 = int(input("Introduce la longitud de la segunda pieza: "))
lado3 = int(input("Introduce la longitud de la tercera pieza: "))

# Comprobamos si se puede construir un triángulo con las piezas dadas
if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado1 + lado2):
    print("Se puede construir un triángulo con las piezas dadas")
else:
    print("No se puede construir un triángulo con las piezas dadas")