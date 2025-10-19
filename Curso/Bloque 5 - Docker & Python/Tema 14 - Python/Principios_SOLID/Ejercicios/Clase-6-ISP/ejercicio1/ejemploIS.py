'''Éste script cumple con ISP: se crean interfaces separadas y cada clase implementa solo lo que necesita'''

from abc import ABC, abstractmethod


class ISwitchable(ABC):
    @abstractmethod
    def turn_on(self) -> None:
        pass

    def turn_off(self) -> None:
        pass


class ITemperatureRegulable(ABC):
    @abstractmethod
    def set_temperature(self, temperature: int) -> None:
        pass


class SmartLight(ISwitchable): # hereda de la clase que gestiona el turn on / turn off
    def turn_off(self) -> None:
        print("Turning light OFF")

    def turn_on(self) -> None:
        print("Turning light ON")


class SmartTemperature(ISwitchable, ITemperatureRegulable): # hereda de ambas clases: turn on / turn off y set temperature
    def turn_off(self) -> None:
        print("Turning Temp. OFF")

    def turn_on(self) -> None:
        print("Turning Temp. ON")

    def set_temperature(self, temperature: int) -> None:
        print(f"Setting temperature {temperature}")


smartLight = SmartLight()
smartLight.turn_off()
smartLight.turn_on()


smartTherm = SmartTemperature()
smartTherm.turn_off()
smartTherm.turn_on()
smartTherm.set_temperature(10)

'''ISP nos ayuda a crear interfaces pequeñas y específicas, para que las clases solo implementen lo que realmente necesitan.
En éste script, cada clase implementa solo los métodos que le corresponden (cumple ISP).
Esto hace que el código sea más limpio, fácil de mantener y menos propenso a errores.'''