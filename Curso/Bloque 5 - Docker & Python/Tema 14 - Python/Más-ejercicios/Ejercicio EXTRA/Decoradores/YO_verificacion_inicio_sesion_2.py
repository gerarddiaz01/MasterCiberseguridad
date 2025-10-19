# Registro de usuarios
usuarios_registrados = {
    "usuario1": {"password": "contrasena123", "nombre_completo": "Juan Pérez", "correo_electronico": "juan@example.com"},
    "usuario2": {"password": "password456", "nombre_completo": "María Gómez", "correo_electronico": "maria@example.com"},
    "usuario3": {"password": "qwerty789", "nombre_completo": "Carlos Rodríguez", "correo_electronico": "carlos@example.com"}
}

# Decorador de autenticación
def verificar_inicio_sesion(func):
    def wrapper(usuario, password):
        if usuario in usuarios_registrados and usuarios_registrados[usuario]["password"] == password:
            print("[ACCESO PERMITIDO] Usuario autenticado correctamente.")
            datos = usuarios_registrados[usuario]
            return func(datos)
        else:
            print("[ERROR] Credenciales inválidas. Acceso denegado.")
    return wrapper

# Función que accede a la información del usuario
@verificar_inicio_sesion
def informacion_usuario(info_usuario):
    print("Información del usuario:")
    print(f"Nombre completo: {info_usuario['nombre_completo']}")
    print(f"Correo electrónico: {info_usuario['correo_electronico']}")

# Decorador en tiempo de ejecución
informacion_usuario("usuario1", "contrasena123")
    # Flujo:
    # Cuando llamamos a ésta función, en realidad llamamos a wrapper ya que reemplaza la función al aplicarle el decorador
    # Y cuando lo llamamos le pasamos los argumentos que son el nombre de usuario y la contraseña
    # Se ejecuta la lógica del wrapper, y cómo en el wrapper se ha hecho el return llamando a la función con los datos del usuario
    # y luego se hace la llamada del wrapper con el otro return, se ejecuta la función informacion_usuario() con los datos pasados
    # en el wrapper (return func(...))
print("\n---\n")
informacion_usuario("usuario2", "clave_incorrecta")
