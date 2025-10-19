'''La clase Pedido tiene dos responsabilidades claras: calcular el total del pedido y manejar el envío de un correo de confirmación. 
Esto infringe el SRP. Se te pide refactorizar el diseño de la siguiente manera:
Deja a Pedido solo la responsabilidad de manejar la lista de ítems y el cálculo del total. Crea una nueva clase, por ejemplo Notificador, 
con la responsabilidad de enviar mensajes de confirmación (podría ser correo electrónico u otro medio en un caso real, pero bastará 
con que simulemos un envío). Haz que Pedido use a Notificador en lugar de enviar correos directamente.'''


class Pedido:
    def __init__(self, items):
        self.items = items  # lista de (producto, precio)

    def calcular_total(self):
        total = sum(precio for _, precio in self.items)
        return total

class Notificador:
    def enviar_confirmacion(self, pedido,  email):
        # Creamos el mensaje usando los datos del pedido
        total = pedido.calcular_total()
        mensaje = f"Gracias por su compra. El total es {total}€."
        # (Simulación) Enviar correo - Aquí simplemente imprimimos:
        print(f"Enviando correo a {email}: '{mensaje}'")

items = [("Libro", 20), ("Cojín", 10)]
pedido = Pedido(items)
notificador = Notificador()
notificador.enviar_confirmacion(pedido, "gerarddiazgibert@gmail.com")