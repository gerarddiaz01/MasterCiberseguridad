'''Éste código está mal organizado, en otro script se ordena y se aplica alta cohesión y bajo acoplamiento'''

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def enviar_correo(self, asunto, mensaje):
        print(
            f"Enviando correo a {self.email} con asunto: {asunto} y mensaje: {mensaje}"
        )

    def guardar_registro(self, accion):
        print(f"Guardando registro de acción: {accion}")


class GestorUsuarios:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, nombre, email):
        usuario = Usuario(nombre, email)
        self.usuarios.append(usuario)
        usuario.enviar_correo("Bienvenido", "Gracias por registrarte")
        usuario.guardar_registro("Registro de usuario")


# Ejemplo de uso
gestor_usuarios = GestorUsuarios()
gestor_usuarios.agregar_usuario("Juan", "juan@example.com")
