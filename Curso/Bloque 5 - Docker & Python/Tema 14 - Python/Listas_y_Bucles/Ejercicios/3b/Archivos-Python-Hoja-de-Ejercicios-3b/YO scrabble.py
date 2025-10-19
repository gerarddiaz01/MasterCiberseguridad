'''
Supongamos una lista de de caracteres llamada “palabras“ que representa una mano de
Scrabble. Cada string contiene dos caracteres: el primer carácter es la letra de una ficha y el
segundo el numero que representa los puntos de la ficha. Por ejemplo, el string "A5" representa la
ficha con la letra A y un valor de 5 puntos. Crea un script que calcule el valor total de los puntos
en una mano de scrabble. El valor total será la suma de los puntos de todas las fichas de la mano.
'''

#crear lista de strings
palabras = ["A5", "B3", "C2", "D4", "E1", "F6", "G2"]

#inicializar variable del total de puntos
suma_pts = 0

#recorrer la lista de strings para extraer el segundo caracter, convertirlo en numero y hacer la suma de los pts
for palabra in palabras:
    valor = int(palabra[1])
    suma_pts += valor

print(f"El numero total de puntos es {suma_pts}")