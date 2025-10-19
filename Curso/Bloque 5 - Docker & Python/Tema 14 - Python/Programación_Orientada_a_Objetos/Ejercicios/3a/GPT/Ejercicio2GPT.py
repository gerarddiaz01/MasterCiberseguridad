class Coche:
    def __init__(self, marca, combustible, consumo):
        self.marca = marca
        self.combustible = combustible  # en litros
        self.consumo = consumo          # litros por km

    def conducir(self, distancia):
        litros_necesarios = distancia * self.consumo
        if litros_necesarios <= self.combustible:
            self.combustible -= litros_necesarios
            print(f"{self.marca} ha conducido {distancia} km, consumiendo {litros_necesarios:.2f} L." 
                  f"Combustible restante: {self.combustible:.2f} L.")
        else:
            print(f"{self.marca} no tiene suficiente combustible para recorrer {distancia} km."
                  f"Combustible actual: {self.combustible:.2f} L, se necesitan {litros_necesarios:.2f} L.")

    def repostar(self, litros):
        self.combustible += litros
        print(f"{self.marca} ha repostado {litros:.2f} L. Combustible total ahora: {self.combustible:.2f} L.")

# Prueba de la clase Coche
mi_coche = Coche("Toyota", 5.0, 0.2)   # 5 litros, consume 0.2 L/km
mi_coche.conducir(10)   # debería consumir 2 L (0.2*10) -> quedan 3 L
mi_coche.conducir(20)   # necesitaría 4 L, pero solo tiene 3 L -> no debería poder
mi_coche.repostar(10)   # añadimos 10 L -> total 13 L
mi_coche.conducir(20)   # ahora sí puede, consumirá 4 L -> quedan 9 L
