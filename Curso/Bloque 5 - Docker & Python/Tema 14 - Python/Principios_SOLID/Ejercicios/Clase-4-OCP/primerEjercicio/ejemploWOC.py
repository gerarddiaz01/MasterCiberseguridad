'''Éste código está sucio, hay que limpiarlo e ordenarlo'''

class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre

    def realizar_pedido(self, tipo_pedido, detalles):
        if tipo_pedido == "para_llevar":
            # Lógica para manejar pedidos para llevar
            print(f"Procesando pedido para llevar: {detalles}")
        elif tipo_pedido == "comer_en_local":
            # Lógica para manejar pedidos para comer en el local
            print(f"Procesando pedido para comer en el local: {detalles}")
        elif tipo_pedido == "entrega_a_domicilio":
            # Lógica para manejar pedidos de entrega a domicilio
            print(f"Procesando pedido de entrega a domicilio: {detalles}")
        else:
            print("Tipo de pedido no válido")
