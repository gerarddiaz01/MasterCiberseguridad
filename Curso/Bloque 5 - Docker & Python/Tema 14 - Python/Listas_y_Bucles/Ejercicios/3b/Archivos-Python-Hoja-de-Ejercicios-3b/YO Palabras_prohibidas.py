'''
Define una lista de 5 palabras aleatorias y una lista de letras 
prohibidas que contenga tres letras. Filtra las palabras en tu lista 
original, y crea una nueva lista de palabras filtradas que solo contenga
aquellas palabras que no tienen ninguna letra prohibida. 
'''

#Definir las listas de palabras y letras prohibidas
palabras = ["casa", "perro", "gato", "sol", "luna"]
letras_prohibidas = ["p", "l", "t"]

#Crear una lista vacía para almacenar las palabras filtradas
lista_filtrada = []

#Recorrer cada palabra y verificar si contiene alguna letra prohibida
#si las tiene, añadir palabra a la nueva lista
for palabra in palabras:
    incluir = True
    for letra in letras_prohibidas:
        if letra in palabra:
           incluir = False
    if incluir:
        lista_filtrada.append(palabra)


print(palabras)
print(letras_prohibidas)
print(lista_filtrada)