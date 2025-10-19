'''
2. Desarrolla ahora un script que compare dos cadenas de caracteres y nos diga si una de ellas
es la codificación ROT13 de la otra.
'''
#hacemos dos listas, una del abecedario latino y otra de rot13 para hacer la conversión
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
rot13 = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]

#input de ambos strings
entrada1 = input("Introduce el primer string a convertir: ")
entrada2 = input("Introduce el segundo string a convertir: ")

print(f"String 1: {entrada1}")
print(f"String 2: {entrada2}")

comparacion = []

for caracter in entrada1:
    if caracter in abc:
        indice = abc.index(caracter)
        comparacion.append(rot13[indice])

join_comparacion = ''.join(comparacion)
print(join_comparacion)
if join_comparacion == entrada2:
    print("El segundo string es la traducción en ROT13")
else:
    print("No es la traducción")

