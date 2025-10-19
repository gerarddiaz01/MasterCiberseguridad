class Vehiculo:
    def __init__(self, marca):
        self.marca = marca
    
    def describir(self):
        print(f"Éste vehículo es un {self.marca}")

class Coche(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo
    
    def describir(self):
        print(f"Éste vehículo es un {self.marca} {self.modelo}")

vehiculo1 = Vehiculo("Toyota")
coche1 = Coche("Subaru", "Impreza")

vehiculo1.describir()
coche1.describir()