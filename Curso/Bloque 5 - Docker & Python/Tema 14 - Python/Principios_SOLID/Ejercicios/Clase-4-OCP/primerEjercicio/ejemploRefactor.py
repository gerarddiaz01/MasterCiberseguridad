'''El abstract method es una manera de definir un método en la clase base para que las subclases estén obligadas a implementar dicho método.
Es fundamental para el Open/Close Principle porque permite extender el comportamiento del sistema (añadiendo nuevas subclases) sin modificar 
el código existente.'''

from abc import ABC, abstractmethod


# clase maestra
class ManejadorPedidos(ABC): # Clase abstracta
    @abstractmethod # Obliga a las subclases a implementar éste método
    def procesar_pedido(self, detalles): # Método abstracto
        pass # Open/Closed Principle: podemos crear nuevas formas de pedido sin modificar la clase base ni el resto del sistema


class PedidoParaLlevar(ManejadorPedidos):
    def procesar_pedido(self, detalles):
        print(f"Procesando pedido para llevar: {detalles}")


class PedidoLocal(ManejadorPedidos):
    def procesar_pedido(self, detalles):
        print(f"Procesando pedido para comer en el local: {detalles}")


class PedidoEntregaADomicilio(ManejadorPedidos):
    def procesar_pedido(self, detalles):
        print(f"Procesando pedido para entrega a domicilio: { detalles}")


class PedidoEspecial(ManejadorPedidos):
    def procesar_pedido(self, detalles):
        print(f"Procesando pedido para evento especial: {detalles}")


class Restaurante:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.manejadores_pedido = []

    def registrar_pedidos(self, tipo_pedido):
        self.manejadores_pedido.append(tipo_pedido)

    def realizar_pedido(self, tipo_pedido, detalles):
        tipo_pedido.procesar_pedido(detalles) # Nos evitamos poner if/elif porque usamos "tipo_pedido" y se adapta según la instancia, es general para 
                                              # todas las subclases, perfecto para ampliar el código sin modificar la lógica, simplemente añadimos subclases


restaurante = Restaurante("Mi restaurante de pastas ") # Se crea un restaurante y se le da un nombre
# Se registran dos tipos de pedidos, para llevar y especial
restaurante.registrar_pedidos(PedidoParaLlevar()) # Se añade instancia de la clase PedidoParaLlevar() a la lista interna del restaurante
restaurante.registrar_pedidos(PedidoEspecial()) # Se añade instancia de la clase PedidoEspecial() a la lista interna del restaurante
# Se realizan los pedidos, y se llama a procesar_pedido(), lo que imprime el mensaje correspondiente según el tipo de pedido
restaurante.realizar_pedido(PedidoParaLlevar(), "Plato de pasta grande") # Se crea una instancia de la clase PedidoParaLlevar() y se pasan los detalles
restaurante.realizar_pedido(PedidoEspecial(), "Plato especial de mariscos") # Se crea una instancia de la clase PedidoEspecial() y se pasan los detalles
