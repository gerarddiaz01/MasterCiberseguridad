'''Using PROTOCOL pero no cumple con ISP: definimos una sola interfaz grande que obliga a todas las clases a tener los tres métodos.
Todas las clases deben implementar todos los métodos, aunque no los necesiten, lo que no es modular. Si una clase no implementa un método, puede lanzar 
un error o dejar el método vacío, lo que es mala práctica.
'''

from typing import Protocol


class IOpoeracionFinanciera(Protocol):
    def depositar(self, monto: float) -> None: ...
    def retirar(self, monto: float) -> None: ...
    def transferir(self, monto: float, a_cuenta: str) -> None: ...


class CuentaAhorros: # No implementa transferir, pero el protocolo lo exige (esto puede causar errores)
    def depositar(self, monto: float) -> None:
        print(f"Depositando { monto} en cuenta de ahorros")

    def retirar(self, amount: float) -> None:
        print(f"Retirando {amount} de cuenta de ahorros")
    # Raise una excepcion rompe ISP


class CuentaCorriente:
    def depositar(self, monto: float) -> None:
        print(f"Depositando { monto} en cuenta corriente")

    def retirar(self, amount: float) -> None:
        print(f"Retirando {amount} de cuenta corriente")

    def transferir(self, amount: float, a_cuenta: str) -> None:
        print(f"Transfiriendo {amount} de cuenta corriente a { a_cuenta}")


cuentaAhorros = CuentaAhorros()
cuentaAhorros.depositar(100)
cuentaAhorros.retirar(50)

cuentaCorriente = CuentaCorriente()
cuentaCorriente.depositar(100)
cuentaCorriente.retirar(50)
cuentaCorriente.transferir(20, "ABCSK189148")
