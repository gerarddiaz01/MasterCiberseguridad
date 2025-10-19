class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email


class GestorCorreo:
    def enviar_correo(self, destinatario, asunto, mensaje):
        print(
            f"Enviando correo a {destinatario} con asunto: {asunto} y mensaje: {mensaje}"
        )


class RegistroAcciones:
    def guardar_registro(self, accion):
        print(f"Guardando registro de acción: {accion}")


class GestorUsuarios:
    def __init__(self, gestor_correo, registro_accion):
        self.usuarios = []
        self.gestor_correo = gestor_correo
        self.registro_accion = registro_accion

    def agregar_usuario(self, nombre, email):
        usuario = Usuario(nombre, email)
        self.usuarios.append(usuario)
        self.gestor_correo.enviar_correo(
            usuario.email, "Asunto : registro # 34", "Gracias por registrarte"
        )
        self.registro_accion.guardar_registro(f"Registro de usuario: {usuario.nombre}")


gestor_correo = GestorCorreo()
registro_accion = RegistroAcciones()
gestor_usuarios = GestorUsuarios(gestor_correo, registro_accion)
gestor_usuarios.agregar_usuario("Juan", "juan@example.com")

'''
-Composición:
Aplicamos composición porque la clase GestorUsuarios no hereda de GestorCorreo ni de RegistroAcciones, 
sino que recibe instancias de estas clases como atributos (gestor_correo y registro_accion). 
Así, GestorUsuarios puede usar los métodos de las clases que hemos pasado cómo atributo (enviar_correo y guardar_registro) sin depender de su implementación interna.
GestorUsuarios compone su funcionalidad usando objetos de otras clases (GestorCorreo y RegistroAcciones).
Esto permite que cada clase tenga una responsabilidad clara y se puedan reutilizar o cambiar fácilmente.

-Alta cohesión:
Cada clase tiene una única responsabilidad:
    Usuario: almacena datos del usuario.
    GestorCorreo: gestiona el envío de correos.
    RegistroAcciones: guarda registros de acciones.
    GestorUsuarios: administra usuarios y coordina acciones usando las otras clases.
Esto significa que las clases son altamente cohesivas.

-Bajo acoplamiento:
GestorUsuarios no depende directamente de la implementación de GestorCorreo ni de RegistroAcciones, solo de sus interfaces (métodos públicos).
Puedes cambiar la implementación de GestorCorreo o RegistroAcciones sin modificar GestorUsuarios, logrando bajo acoplamiento.
'''