class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def describir(self):
        return f"Este vehiculo es un {self.marca} {self.modelo}"


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def describir(self):
        return f"Este automovil es un {self.marca} {self.modelo} con { self.puertas} puertas"


class Camion(Automovil):
    def __init__(self, marca, modelo, puertas, carga):
        super().__init__(marca, modelo, puertas)
        self.carga = carga

    def describir(self):
        return f"Este camion es un {self.marca} {self.modelo} con { self.puertas} puertas y una capacidad de carga {self.carga} kg"


vehiculo1 = Automovil("Toyota", "Corolla", 4)
vehiculo2 = Camion("Toyota", "FSHD", 2, 1000)
print(vehiculo1.describir())
print(vehiculo2.describir())
