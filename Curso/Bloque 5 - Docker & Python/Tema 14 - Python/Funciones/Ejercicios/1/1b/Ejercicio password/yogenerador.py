'''
Por otro lado
puedes crear otro script creador.py con una función llamada
generar_contrasena que genere contraseñas seguras de forma aleatoria. La
función debe permitir especificar la longitud de la contraseña y qué tipos de
caracteres deben incluirse (por ejemplo, letras mayúsculas, letras
minúsculas, números y caracteres especiales).
(Para el generador de contraseñas puedes probar a usar los modulos
random y string)'''
import string
import random

def generar_contrasena(longitud=12, incluir_mayusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_especiales=True):
    # Construimos el conjunto de caracteres según las opciones seleccionadas
    caracteres = ""
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_especiales:
        caracteres += string.punctuation

    # Verificamos que al menos un tipo de carácter esté seleccionado
    if not caracteres:
        raise ValueError("Debe incluir al menos un tipo de carácter para generar la contraseña.")

    # Generamos la contraseña aleatoria
    return ''.join(random.choices(caracteres, k=longitud))