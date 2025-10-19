'''Éste script cumple con ISP:
    - Cada clase implementa solo los métodos que necesita.
    - No se obliga a ninguna clase a tener métodos innecesarios.
    - Las funciones de alto nivel (como realizar_pago) trabajan con protocolos específicos.'''

from typing import Protocol


# Contratos de deposito, retiro y transferencia: tres protocolos (o interfaces pequeñas)
class IDepositar(Protocol):
    def depositar(self, monto: float) -> None: ... # Cualquier clase que tenga éste método es "compatible" con el protocolo
class IRetirar(Protocol):
    def retirar(self, monto: float) -> None: ...
class ITransferir(Protocol):
    def transferir(self, monto: float) -> None: ...

# Éstas clases pueden implementar sólo les métodos que necesitan si tener que heredar de una o varias clases (es más fácil y natural, más informal)
class CuentaAhorros: # No tiene método transferir() porqué no lo necesita
    def depositar(self, monto: float) -> None:
        print(f"Depositando { monto} en cuenta de ahorros ")

    def retirar(self, amount: float) -> None:
        print(f"Retirando {amount} de cuenta de ahorros")


class CuentaCorriente: # Tiene los tres métodos porque si los necesita, sin tener que heredar de cada una de las big clases
    def depositar(self, monto: float) -> None:
        print(f"Depositando { monto} en cuenta corriente")

    def retirar(self, amount: float) -> None:
        print(f"Retirando {amount} de cuenta corriente")

    def transferir(self, amount: float, a_cuenta: str) -> None:
        print(f"Transfiriendo {amount} de cuenta corriente a {a_cuenta}")

# Ésta función acepta cualquier objeto que implemente el método transferir (es decir, que cumpla el protocolo ITransferir).
def realizar_pago(cuenta: ITransferir, monto: float, a_cuenta) -> None:
    cuenta.transferir(monto, a_cuenta)


cuentaCorriente = CuentaCorriente()

realizar_pago(cuentaCorriente, 20, "Cuenta de X")

# cuentaAhorros.depositar(100, 20)
# cuentaAhorros.retirar(50)

# cuentaCorriente = CuentaCorriente()
# cuentaCorriente.depositar(100)
# cuentaCorriente.retirar(50)
# cuentaCorriente.transferir(20, "ABCSK189148")

'''
¿Qué es un Protocol en Python?
Un Protocol (del módulo typing) es una forma de definir una interfaz en Python:

Especifica qué métodos debe tener una clase para ser considerada "compatible" con ese protocolo.
No obliga a heredar explícitamente del protocolo; basta con que la clase tenga los métodos requeridos (esto se llama duck typing).

¿Para qué sirve?
Permite escribir código más flexible y seguro.
Facilita la comprobación estática de tipos (por ejemplo, con herramientas como mypy).
Ayuda a cumplir el ISP: podemos definir interfaces pequeñas y específicas, y las clases solo implementan lo que necesitan.
'''