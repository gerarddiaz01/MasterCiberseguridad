'''Verificación de Inicio de Sesión con Decorador
Estás desarrollando un sistema de autenticación para una aplicación web y deseas implementar un sistema de inicio 
de sesión que verifique si las credenciales proporcionadas por el usuario son válidas antes de permitir el acceso 
a ciertas funciones. Además, deseas que una vez que el usuario haya iniciado sesión correctamente, 
se le proporcione información personal.
Implementa lo siguiente:
Un registro de usuarios que contenga información adicional, como el nombre completo y el correo electrónico.
Un decorador llamado verificar_inicio_sesion que acepte el nombre de usuario y la contraseña como argumentos.
Este decorador verificará si las credenciales proporcionadas son válidas comparándolas con el registro de usuarios.
Si las credenciales son válidas, la función decorada se ejecutará y se le pasará como argumento la información personal del usuario.
Una función llamada informacion_usuario que imprima la información personal del usuario después de que haya iniciado sesión 
correctamente.'''


usuarios_registrados = {
    "usuario1": {"password": "contrasena123", "nombre_completo": "Juan Pérez", "correo_electronico": "juan@example.com"},
    "usuario2": {"password": "password456", "nombre_completo": "María Gómez", "correo_electronico": "maria@example.com"},
    "usuario3": {"password": "qwerty789", "nombre_completo": "Carlos Rodríguez", "correo_electronico": "carlos@example.com"}
}
# Función externa que recibe los argumentos del decorador, su único propósito es devolver el decorador real
def verificar_inicio_sesion(nombre_usuario, password):
    # Decorador real, recibe cómo argumento la función que será decorada, devuelve el wrapper
    def decorador(func):
        # Contiene la la lógica adicional que se ejecutará antes y después de la función decorada
        # args y kwargs permiten que el decorador acepte cualquier numero de argumentos posicionales y palabras clave que se le pasen
        def wrapper(*args, **kwargs):
            # Verifica si el usuario existe en el registro
            if nombre_usuario in usuarios_registrados:
                # Si existe, verifica la contraseña, si es válida se imprime un mensaje de bienvenida
                if usuarios_registrados[nombre_usuario]["password"] == password:
                    print(f"[ACCESO PERMITIDO] Bienvenido, {usuarios_registrados[nombre_usuario]['nombre_completo']}!")
                    # Llama a la función decorada y le pasa la información del usuario como argumento
                    return func(usuarios_registrados[nombre_usuario], *args, **kwargs)
                else:
                    print("[ERROR] Contraseña incorrecta.")
            else:
                print("[ERROR] Usuario no encontrado.")
        return wrapper
    return decorador

@verificar_inicio_sesion("usuario1", "contrasena123") # Aplicamos el decorador y pasamos las credenciales del usuario como argumentos
def informacion_usuario(info_usuario): # Esta función imprime la información personal del usuario, recibe cómo argumento la
    print("Información del usuario:")  # información del usuario, que es proporcionada por el decorador en el return func(...)
    print(f"Nombre completo: {info_usuario['nombre_completo']}")
    print(f"Correo electrónico: {info_usuario['correo_electronico']}")

informacion_usuario()
    # Flujo:
    # El decorador verificar_inicio_sesion recibe los argumentos "usuario1" y "contrasena123"
    # La función decorador recibe la función informacion_usuario como argumento
    # La función wrapper verifica si "usuario1" está en el registro de usuarios y si su contraseña es válida
    # Como las credenciales son válidas, se imprime el mensaje de bienvenida,  se llama a informacion_usuario y le pasa la 
    # información del usuario (usuarios_registrados["usuario1"]) como argumento (info_usuario).

print("\n---\n")

@verificar_inicio_sesion("usuario2", "contraseña_incorrecta")
def informacion_usuario_incorrecta(info_usuario):
    print("Esto no debería imprimirse.")

informacion_usuario_incorrecta()