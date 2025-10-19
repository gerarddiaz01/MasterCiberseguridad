'''CUENTA BANCARIA
Crea una clase "CuentaBancaria" con atributos como número de cuenta y
saldo. Implementa métodos para depositar y retirar dinero, y muestra el
saldo actual'''

class CuentaBancaria:
    def __init__ (self, numero_cuenta, saldo):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
    
    def depositar_dinero(self, dinero_depositado):
        self.saldo += dinero_depositado
    
    def retirar_dinero(self, dinero_retirado):
        self.saldo -= dinero_retirado

    def mostrar_saldo(self):
        print(f"El saldo actual de la cuenta bancaria numero {self.numero_cuenta} es: {self.saldo} €")

mi_cuenta = CuentaBancaria("1234", 5000)
mi_cuenta.mostrar_saldo()
print("")
mi_cuenta.depositar_dinero(4000)
print("")
mi_cuenta.mostrar_saldo()
print("")
mi_cuenta.retirar_dinero(8000)
print("")
mi_cuenta.mostrar_saldo()
