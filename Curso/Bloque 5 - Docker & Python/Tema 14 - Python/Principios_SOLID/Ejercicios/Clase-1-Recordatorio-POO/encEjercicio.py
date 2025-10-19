class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo):
        self._numero_cuenta = numero_cuenta  # atributo protegido
        self.__saldo = saldo  # atributo privado

    def get_saldo(self):
        return self.__saldo

    def depositar(self, monto):
        self.__saldo += monto

    def retirar(self, monto):
        if self.__saldo >= monto:
            self.__saldo -= monto
        else:
            print("Saldo insuficiente")


# Modo de uso
cuenta = CuentaBancaria("12345", 1000)
print(cuenta._numero_cuenta)

# No es recomedable
# print(cuenta._CuentaBancaria__saldo)

# Correcto -> getter
valor = cuenta.get_saldo()

# utilizar metodos publicos
cuenta.depositar(500)
cuenta.retirar(200)
# print(cuenta.get_saldo())
