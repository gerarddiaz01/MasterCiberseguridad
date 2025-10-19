'''
Crea un script que pida al usuario una palabra y luego muestre por 
pantalla una a una las letras de la palabra introducida empezando 
por la última
'''

# Pedir una palabra al usuario
palabra = input("Introduce una palabra: ")

# Recorrer la palabra letra por letra empezando por la ultima
for letra in palabra[::-1]:
    print(letra)
#:: indica que quiero todo el string porque no indico valor inicial o final
#-1 indica que vaya al reves