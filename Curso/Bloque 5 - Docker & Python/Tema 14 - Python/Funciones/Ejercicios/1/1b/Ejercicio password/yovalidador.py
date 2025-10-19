'''Para ello puedes crear un script validador.py
que contenga una funcion validar_contrasena que reciba una cadena y
verifique si cumple con los requisitos mínimos de una contraseña segura
(por ejemplo, longitud mínima, presencia de letras mayúsculas, letras
minúsculas, números y caracteres especiales). La función debe devolver un
valor booleano que indique si la contraseña es válida o no'''

def validar_contraseña(password):
    if len(password) < 5:
        return False # Longitud mínima
    elif not any(char.isupper() for char in password):
        return False # Al menos una letra mayúscula
    elif not any(char.islower() for char in password):
        return False # Al menos una letra minúscula
    elif not any(char.isdigit() for char in password):
        return False # Al menos un número
    caracteres_especiales = "!@#$%^&*()-_=+[]|;:',.<>?/`~"
    if not any(char in caracteres_especiales for char in password):
        return False # Al menos un carácter especial

    return True # Cumple con todos los requisitos