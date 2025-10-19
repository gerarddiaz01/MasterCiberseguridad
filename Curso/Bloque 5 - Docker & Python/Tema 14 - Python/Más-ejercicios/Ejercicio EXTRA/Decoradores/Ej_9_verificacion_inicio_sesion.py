# Ejercicio 9: Verificación de Inicio de Sesión con Decorador

# Estás desarrollando un sistema de autenticación para una aplicación web y deseas implementar un sistema de inicio de sesión que verifique si las credenciales proporcionadas por el usuario son válidas antes de permitir el acceso a ciertas funciones. Además, deseas que una vez que el usuario haya iniciado sesión correctamente, se le proporcione información personal.

# Implementa lo siguiente:

# Un registro de usuarios que contenga información adicional, como el nombre completo y el correo electrónico.
# Un decorador llamado verificar_inicio_sesion que acepte el nombre de usuario y la contraseña como argumentos. Este decorador verificará si las credenciales proporcionadas son válidas comparándolas con el registro de usuarios. Si las credenciales son válidas, la función decorada se ejecutará y se le pasará como argumento la información personal del usuario.
# Una función llamada informacion_usuario que imprima la información personal del usuario después de que haya iniciado sesión correctamente.
# Implementa este sistema de inicio de sesión utilizando decoradores.

usuarios_registrados = {
    "usuario1": {"contrasena": "contrasena123", "nombre_completo": "Juan Pérez", "correo_electronico": "juan@example.com"},
    "usuario2": {"contrasena": "password456", "nombre_completo": "María Gómez", "correo_electronico": "maria@example.com"},
    "usuario3": {"contrasena": "qwerty789", "nombre_completo": "Carlos Rodríguez", "correo_electronico": "carlos@example.com"}
}


def verificar_inicio_sesion(funcion):
  def wrapper(nombre_usuario,contrasena):
    if nombre_usuario in usuarios_registrados and usuarios_registrados[nombre_usuario]['contrasena']==contrasena:
      print(f" Inicio de sesion exitoso para el usuario {nombre_usuario}")
      usuario_info=usuarios_registrados[nombre_usuario]
      return(funcion(usuario_info))
    else:
      print("Inicio de sesion fallido, Verifica tu nombre de usuario y contrasena")
  return wrapper


@verificar_inicio_sesion
def informacion_usuario(usuario_info):
  print("Informacion personal del usuario:")
  print("Nombre completo: ",usuario_info["nombre_completo"])
  print("Correo electronico: ",usuario_info["correo_electronico"])

informacion_usuario('usuario1','contrasena123')
informacion_usuario('usuario2','password456')
