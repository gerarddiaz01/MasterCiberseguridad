'''En este script hay mucho acoplamiento, tenemos que limpiarlo y aplicar los principios Solid'''

class Engine:
    def __init__(self):
        pass

    def getRPM(self):
        return 3000


class Vehicle:
    def __init__(self, name, speed):
        self._name = name
        self._engine = Engine() # Usa composición pero no siguiendo SOLID porque Vehiculo crea su propio motor en lugar de pasarselo cómo atributo ya creado

    def getName(self):
        return self._name

    def getEngineRPM(self):
        return self._engine.getRPM()

    def getMaxSpeed(self):
        return self._speed

    def printInfo(self):
        print(
            "Vehicle: {}, Max Speed: {}, RMP: {}".format(
                self._name, self._speed, self._engine.getRPM()
            )
        )


if __name__ == "__main__":
    vehicle = Vehicle("Car", 200)
    vehicle.printInfo()
