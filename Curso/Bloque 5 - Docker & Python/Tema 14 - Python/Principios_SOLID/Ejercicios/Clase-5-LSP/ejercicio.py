'''Principio de Sustitución de Liskov: Si tienes una clase base y una clase hija, deberías poder usar la clase hija en lugar 
de la clase base sin que el programa deje de funcionar correctamente.'''

class MetodoPagoBase: # Define la interfaz común para todos los métodos de pago
    def procesar_pago():
        pass


class MetodoPagoAutomatico(MetodoPagoBase):
    def procesar_pago(self, cantidad):
        pass


class MetodoPagoManual(MetodoPagoBase):
    def procesar_pago(self, cantidad):
        pass


# Metodos de pago automaticos, cada método de pago implementa su propia versión de procesar_pago()
class PagoTarjeta(MetodoPagoAutomatico):
    def __init__(self, numero_tarjeta):
        self.numero_tarjeta = numero_tarjeta

    def procesar_pago(self, cantidad):
        print(
            f"Procesando pago automatico de {cantidad} usando tarjeta { self.numero_tarjeta}"
        )


class PagoPayPal(MetodoPagoAutomatico):
    def __init__(self, cuenta_paypal):
        self.cuenta_paypal = cuenta_paypal

    def procesar_pago(self, cantidad):
        print(
            f"Procesando pago automatico de {cantidad} usando PayPal cuenta { self.cuenta_paypal}"
        )


class PagoBitcoin(MetodoPagoAutomatico):
    def __init__(self, direccion_bitcoin):
        self.direccion_bitcoin = direccion_bitcoin

    def procesar_pago(self, cantidad):
        print(
            f"Procesando pago automatico de {cantidad} usando Bitcoin { self.direccion_bitcoin}"
        )


# Metodos de pago manual
class PagoCheque(MetodoPagoManual):
    def __init__(self, numero_cheque):
        self.numero_cheque = numero_cheque

    def procesar_pago(self, cantidad):
        print(
            f"Procesando pago manual de {cantidad} usando cheque {self.numero_cheque}"
        )

# Funciones de alto nivel
def realizar_pago_automatico(metodo_pago: MetodoPagoAutomatico, cantidad): # se recibe un objeto de método de pago
    metodo_pago.procesar_pago(cantidad) # se llama al método procesar_pago() que cambiará según el método de pago que se le ha pasado


def realizar_pago_manual(metodo_pago: MetodoPagoManual, cantidad):
    metodo_pago.procesar_pago(cantidad)


# Instanciar las clases: se crean objetos concretos y se usan en las funciones de pago
pago_tarjeta = PagoTarjeta("123 456 789 123")
pago_paypal = PagoPayPal("mi_cuenta@pago.com")
pago_bitcoin = PagoBitcoin("892173912udfhie938")
pago_cheque = PagoCheque("123456768")

realizar_pago_automatico(pago_tarjeta, 1000)
realizar_pago_automatico(pago_paypal, 400)
realizar_pago_automatico(pago_bitcoin, 6000)

realizar_pago_manual(pago_cheque, 3000)

'''
Aplicación del LSP: Cuando se usa la función de realizar_pago_automatico(), Se le puede pasar cualquier objeto que sea una subclase de
MetodoPagoAutomatico (PagoTarjeta, PagoPaypal o PagoBitcoin) y el código funcionará igual. Se puede sustituir la clase base por cualquier subclase sin romper
el programa.
'''