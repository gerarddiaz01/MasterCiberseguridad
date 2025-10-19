'''
Crea un script que pida al usuario una palabra 
y luego muestre por pantalla una a una las letras 
de la palabra introducida empezando por la última.
'''
# --- pedir palabra al usuario
palabra = input("Ingrese una palabra: ")

for letra in palabra[::-1]: #:: indica que quiero todo el string porque no indico valor inicial o final
    print(letra)            #-1 indica que vaya al reves