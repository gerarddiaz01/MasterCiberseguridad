'''Enunciado: Imagina que estás creando un sistema de registro de usuarios y necesitas 
verificar la fortaleza de una contraseña. Escribe una función verificar_contraseña(password) 
que verifique si la contraseña cumple ciertos criterios, por ejemplo uno básico: 
al menos 8 caracteres. Si la contraseña es muy corta, la función debería lanzar una 
excepción personalizada llamada ContraseñaCortaError. Si la contraseña cumple con el criterio, 
la función puede devolver True (o simplemente no lanzar nada). Luego, escribe código que use 
dicha función dentro de un bloque try/except para probarla: pide al usuario una contraseña, 
la validas con verificar_contraseña y capturas la excepción ContraseñaCortaError para notificar 
al usuario en caso de que falle la validación. Si no hay excepción, felicita al usuario por una 
contraseña válida'''

# Definimos una excepción personalizada para manejar contraseñas cortas
class ContraseñaCortaError(Exception):
    '''Excepción personalizada para nuestra aplicación que detecta la longitud corta del password'''
    pass  # No necesitamos agregar lógica adicional, solo usamos esta clase para identificar el error

# Función para verificar la fortaleza de la contraseña
def verificar_contraseña(password):
    '''
    Verifica si la contraseña cumple con los criterios de longitud mínima.
    - Si la contraseña tiene menos de 8 caracteres, lanza una excepción personalizada ContraseñaCortaError.
    - Si cumple con el criterio, devuelve True.
    '''
    if len(password) < 8:  # Verificamos si la longitud de la contraseña es menor a 8
        # Lanzamos la excepción personalizada con un mensaje explicativo
        raise ContraseñaCortaError("La contraseña tiene que tener al menos 8 caracteres.")
    else:
        # Si la contraseña cumple con el criterio, devolvemos True
        return True

# Bloque principal del programa
try:
    # Solicitamos al usuario que ingrese una contraseña
    password = input("Ingrese una contraseña: ")
    
    # Llamamos a la función para verificar la contraseña
    # Si la contraseña no cumple con los criterios, se lanzará una excepción
    verificar_contraseña(password)

except ContraseñaCortaError as e:
    # Capturamos la excepción personalizada y mostramos un mensaje al usuario
    print(f"Error inesperado: {e}. Por favor, intente de nuevo.")

else:
    # Si no se lanza ninguna excepción, felicitamos al usuario por una contraseña válida
    print("La contraseña es válida, ¡felicidades!")
