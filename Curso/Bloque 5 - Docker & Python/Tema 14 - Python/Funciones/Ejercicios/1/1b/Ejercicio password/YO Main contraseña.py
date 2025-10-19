'''Crea un script que solicite una contraseña, analice si es segura y si no lo es
sugiera una nueva contraseña. Para ello puedes crear un script validador.py
que contenga una funcion validar_contrasena que reciba una cadena y
verifique si cumple con los requisitos mínimos de una contraseña segura
(por ejemplo, longitud mínima, presencia de letras mayúsculas, letras
minúsculas, números y caracteres especiales). La función debe devolver un
valor booleano que indique si la contraseña es válida o no. Por otro lado
puedes crear otro script creador.py con una función llamada
generar_contrasena que genere contraseñas seguras de forma aleatoria. La
función debe permitir especificar la longitud de la contraseña y qué tipos de
caracteres deben incluirse (por ejemplo, letras mayúsculas, letras
minúsculas, números y caracteres especiales).
(Para el generador de contraseñas puedes probar a usar los modulos
random y string)'''

import yovalidador
import yogenerador

def solicitar_password():
    contraseña = input("Introduce una contraseña: ")

    valida = yovalidador.validar_contraseña(contraseña)

    if valida:
        print("Contraseña segura")
    else:
        print("Contraseña no segura, te sugerimos usar la siguiente contraseña...")
        sugerencia = yogenerador.generar_contrasena(longitud=10, incluir_mayusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_especiales=True)
        print(sugerencia)

solicitar_password()
