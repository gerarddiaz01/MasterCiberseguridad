from abc import ABC, abstractmethod


class Vehiculo(ABC):
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.encendido = False

    def encender(self):
        self.encendido = True
        print("El vehículo está encendido.")

    def apagar(self):
        self.encendido = False
        print("El vehículo está apagado.")

    @abstractmethod
    def conducir(self):
        pass


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, color, tipo_combustible):
        super().__init__(marca, modelo, color)
        self.tipo_combustible = tipo_combustible

    def conducir(self):
        if self.encendido:
            print(
                f"Conduciendo el {self.marca} {self.modelo} - {self.tipo_combustible}."
            )
        else:
            print("No se puede conducir, el vehículo está apagado.")


class Camion(Vehiculo):
    def __init__(self, marca, modelo, color, capacidad_carga):
        super().__init__(marca, modelo, color)
        self.capacidad_carga = capacidad_carga

    def conducir(self):
        if self.encendido:
            print(
                f"Conduciendo el {self.marca} {self.modelo} - Capacidad de carga: {self.capacidad_carga}."
            )
        else:
            print("No se puede conducir, el vehículo está apagado.")


# Crear objetos de las clases derivadas
automovil1 = Automovil("Toyota", "Corolla", "Rojo", "Gasolina")
camion1 = Camion("Ford", "F-150", "Azul", "2 toneladas")

# Encender y conducir un automóvil
automovil1.encender()
automovil1.conducir()

# Apagar el automóvil
automovil1.apagar()
