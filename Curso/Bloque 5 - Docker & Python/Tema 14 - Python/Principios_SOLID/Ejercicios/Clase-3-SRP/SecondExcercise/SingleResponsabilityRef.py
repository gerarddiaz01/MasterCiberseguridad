'''Éste código está estructurado para que cada clase haga solo una cosa, facilitando el mantenimiento, la extensión y el testeo, que es la base de los principios 
SOLID. Así, si necesitamos cambiar la forma de pago, el cálculo del total, o la estructura del pedido, podemos hacerlo sin afectar el resto del sistema. '''

class Order:
    def __init__(self): # Construimos listas vacías y el estado inicial del pedido (cómo string)
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name: str, quantity: int, price: float) -> None: # Los tipos de datos son solo informativos, se llaman type hints
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

# El objetivo ahora es lograr un bajo acoplamiento con el pedido, es decir que el pedido se haga a parte de la siguientes funciones y que si
# es necesario modificarlo se pueda hacer facilmente sin tener que modificar las funciones en las que el pedido está involcurado, para lograrlo
# creamos una instancia de pedido, le añadimos productos y luego pasamos el pedido a las siguientes funciones como atributo

class PaymentProcesor: # Definimos la clase encargada de procesar pagos
    def pay(self, order: Order, security_code: str, payment_type: str): # "order" es el pedido que pasamos como atributo
        if payment_type == "debit":
            print("Processing debit payment type")
            print(f"Verifying security code: {security_code}")
            order.status = "paid"
        elif payment_type == "credit":
            print("Processing credit payment type")
            print(f"Verifying security code: {security_code}")
            order.status = "paid"
        else: # Si el tipo de pago no es reconocido, lanza una excepción
            raise Exception(f"Unknown payment type: {payment_type}")


class CalculateProcesor: # Definimos la clase encargada de calcular el total del pedido
    def total_price(self, order): # "order" es el pedido que pasamos como atributo
        total = 0
        # Recorremos las listas de cantidades y precios al mismo tiempo, multiplicando cada cantidad por su precio y sumando al total
        for quantity, price in zip(order.quantities, order.prices): # zip empareja elementos de order.quantities y order.prices
            total += quantity * price
        return total


order = Order() # Creamos un pedido primero, para cambiarlo facilmente si necesario
print(order.status)
order.add_item("Laptop", 3, 150) # Añadimos un producto al pedido, con la cantidad y el precio
# order.add_item("SSD", 2, 20)
# order.add_item("USB cable", 1, 5)

processor = PaymentProcesor() # Creamos a parte también el proceso de pago, para fácil modificación
processor.pay(order, "12345", "debit") # Composición: le añadimos el pedido con los productos, con el PIN y el tipo de pago
print(order.status)

total = CalculateProcesor() # Separamos la lógica de calcular el precio total del pedido para una facil extensión o modificación si necesario
print(total.total_price(order)) # Composición: le pasamos el pedido con sus productos para que lo calcule todo

'''Relación con SOLID:
-SRP (Single Responsibility Principle):
Cada clase tiene una única responsabilidad:
    Order gestiona los datos del pedido.
    PaymentProcesor gestiona el pago.
    CalculateProcesor calcula el total.
-Open/Closed Principle:
Podemos agregar nuevos métodos de pago o nuevas formas de calcular el total creando nuevas clases, sin modificar las existentes.
-Liskov Substitution, Interface Segregation, Dependency Inversion:
No se aplican directamente aquí, pero la estructura permite que podamos extender el sistema fácilmente para cumplirlos si fuera necesario.'''