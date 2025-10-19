'''Enunciado: Desarrolla una clase CuentaBancaria que modele una cuenta simple. 
Debe tener un atributo de saldo. Implementa un método depositar(cantidad) que incremente 
el saldo, y un método retirar(cantidad) que disminuya el saldo solo si hay suficiente 
dinero (si no hay suficiente, que imprima un mensaje de error indicando saldo insuficiente). 
Además, agrega un método consultar_saldo() que imprima el saldo actual. Demuestra su 
funcionamiento creando una cuenta, realizando depósitos y retiros válidos e inválidos'''

# Definimos la clase CuentaBancaria
class CuentaBancaria:
    # Método constructor para inicializar los atributos de la cuenta
    def __init__(self, saldo):
        # Inicializamos el saldo de la cuenta con el valor proporcionado
        self.saldo = saldo

    # Método para depositar dinero en la cuenta
    def depositar(self, cantidad):
        # Validamos que la cantidad a depositar sea positiva
        if cantidad <= 0:
            print("No puedes depositar una cantidad negativa o cero.")
            print("")  # Línea en blanco para separar mensajes
            return  # Salimos del método si la cantidad no es válida
        # Incrementamos el saldo con la cantidad depositada
        self.saldo += cantidad
        # Informamos al usuario que el depósito fue exitoso
        print(f"Has depositado {cantidad:.2f}€.")
        print("")  # Línea en blanco para separar mensajes

    # Método para retirar dinero de la cuenta
    def retirar(self, cantidad):
        # Validamos que la cantidad a retirar sea positiva
        if cantidad <= 0:
            print("No puedes retirar una cantidad negativa o cero.")
        # Verificamos si hay suficiente saldo para realizar el retiro
        elif self.saldo < cantidad:
            print(f"Estás intentando retirar {cantidad:.2f}€ pero el saldo es insuficiente."
                  f" Te quedan {self.saldo:.2f}€ en la cuenta.")
        else:
            # Reducimos el saldo si la operación es válida
            self.saldo -= cantidad
            print(f"Has retirado {cantidad:.2f}€ de tu cuenta, te quedan {self.saldo:.2f}€.")
        print("")  # Línea en blanco para separar mensajes

    # Método para consultar el saldo actual de la cuenta
    def consultar_saldo(self):
        # Mostramos el saldo actual al usuario
        print(f"Tu saldo actual es: {self.saldo:.2f}€")
        print("")  # Línea en blanco para separar mensajes

# Pruebas del funcionamiento de la clase CuentaBancaria
# Creamos una cuenta con un saldo inicial de 1000€
cuenta1 = CuentaBancaria(1000)

# Consultamos el saldo inicial
cuenta1.consultar_saldo()

# Realizamos un depósito de 100€
cuenta1.depositar(100)

# Consultamos el saldo después del depósito
cuenta1.consultar_saldo()

# Intentamos retirar 200€, lo cual es válido
cuenta1.retirar(200)

# Intentamos retirar 1000€, lo cual excede el saldo disponible
cuenta1.retirar(1000)

# Intentamos depositar una cantidad negativa (-50€), lo cual no es válido
cuenta1.depositar(-50)

# Intentamos retirar 0€, lo cual no es válido
cuenta1.retirar(0)

# Retiramos exactamente el saldo disponible (900€)
cuenta1.retirar(900)

# Consultamos el saldo final después de todas las operaciones
cuenta1.consultar_saldo()