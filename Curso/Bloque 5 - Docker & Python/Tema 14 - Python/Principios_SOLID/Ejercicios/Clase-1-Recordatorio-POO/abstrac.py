class vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
        self.velocidad = 0

    def mostrar_vehiculo(self):
        print(f"Este es un {self.marca}  {self.modelo}")

    def encender(self):
        self.encendido = True
        print("El vehiculo esta encendido")

    def apagar(self):
        self.encendido = False
        print("El vehiculo esta apagado")

    def acelerar(self, incremento):
        if self.encendido:
            self.velocidad += incremento
            print(f"Vehiculo acelerado: {self.velocidad} km/h")
        else:
            print(f"No se puede acelerar, encienda el vehiculo")

    def frenar(self, decremento):
        if self.encendido:
            if self.velocidad - decremento >= 0:
                self.velocidad -= decremento
                print(f"El vehiculo desacelero a: {self.velocidad} km/h")
            else:
                self.velocidad = 0
                print(f"El vehiculo se detuvo")
        else:
            print(f"No se puede frenar, encienda el vehiculo")


vehiculo1 = vehiculo("Toyota", "Corolla")
vehiculo1.mostrar_vehiculo()
vehiculo1.encender()
vehiculo1.acelerar(10)
vehiculo1.frenar(10)
vehiculo1.apagar()
