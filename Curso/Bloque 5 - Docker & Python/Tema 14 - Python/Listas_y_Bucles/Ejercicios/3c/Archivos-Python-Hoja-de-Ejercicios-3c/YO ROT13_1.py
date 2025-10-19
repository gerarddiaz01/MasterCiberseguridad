'''
El abecedario latino es el sistema de escritura alfabético más usado del mundo hoy en día. Se
compone de 26 letras principales, más ciertas modificaciones y letras adicionales según el idioma
del que se trate (por ejemplo, en castellano y gallego se incluye la ”ñ”, en portugués, francés y
catalán la ”Ç”, en alemán la ”ß”, etc.).
Aplicar el cifrado ROT13 a un texto se reduce a examinar sus caracteres alfabéticos y sustituirlos
por la letra que está 13 posiciones por delante en el alfabeto, volviendo al principio si es necesario
y conservando las mayúsculas y minúsculas: a se convierte en n, B se convierte en O, y así hasta
la Z, que se convierte en M. Solo quedan afectadas las 26 letras principales que aparecen en el
alfabeto latino; los números, símbolos, espacios y otros caracteres se dejan igual.

1. Desarrolla un script que recibiendo de entrada una cadena de caracteres devuelva el texto
codificado según el cifrado ROT13
2. Desarrolla ahora un script que compare dos cadenas de caracteres y nos diga si una de ellas
es la codificación ROT13 de la otra.
'''

#hacemos dos listas, una del abecedario latino y otra de rot13 para hacer la conversión
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
rot13 = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]

#hacemos el input de entrada que hay que convertir a rot13
entrada = input("Ingrese un texto para convertir a ROT13: ").lower()
'''
salida = []

#recorremos cada letra del string entrada, verificamos si está en la lista abc, si es el caso la convertimos a ROT13
for caracter in entrada:
    if caracter in abc:
        indice = abc.index(caracter)
        salida.append(rot13[indice])
    else:
        salida.append(caracter)

print(f"Traducción a ROT13:")
for letra in salida:
    print(letra, end="")
print() #salto de linea
'''
#recorremos cada letra del string entrada, verificamos si está en la lista abc, si es el caso la convertimos a ROT13
for caracter in entrada:
    if caracter in abc:
        indice = abc.index(caracter)
        print(rot13[indice], end="")
    else:
        print(caracter, end="")
print()
