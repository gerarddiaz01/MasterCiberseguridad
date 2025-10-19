'''Enunciado: Implementa una clase Coche con los siguientes atributos: marca, 
combustible (en litros, por ejemplo) y consumo (litros por kilómetro, que indica 
cuánto combustible gasta por km). Incluye un método conducir que reciba una distancia 
en kilómetros y reduzca el combustible según el consumo, imprimiendo cuántos litros 
consumió y cuántos le quedan. Si no hay suficiente combustible para la distancia 
indicada, debe indicar que el coche no puede conducir tanto. Añade también un método 
repostar que reciba una cantidad de litros y aumente el combustible en esa cantidad, 
imprimiendo el nuevo nivel de combustible. Prueba creando un objeto Coche y utilizando 
sus métodos en distintos escenarios (suficiente combustible, combustible insuficiente, 
repostaje, etc.)'''

# Definimos la clase Coche
class Coche:
    # Método constructor para inicializar los atributos del coche
    def __init__ (self, marca, combustibleLitros, consumoLitrosPorKm):
        # Atributo que almacena la marca del coche
        self.marca = marca
        # Atributo que almacena la cantidad de combustible disponible en litros
        self.combustible = combustibleLitros
        # Atributo que almacena el consumo del coche en litros por kilómetro
        self.consumo = consumoLitrosPorKm
    
    # Método para conducir el coche una cierta distancia
    def conducir(self, distanciaKm):
        # Calculamos el combustible necesario para recorrer la distancia solicitada
        combustible_necesario = self.consumo * distanciaKm
        
        # Verificamos si hay suficiente combustible para recorrer la distancia
        if combustible_necesario > self.combustible:
            # Si no hay suficiente combustible, mostramos un mensaje al usuario
            print(f"No hay suficiente combustible para hacer {distanciaKm} km.")
            print(f"Te quedan {self.combustible} litros de combustible. "
                  f"Puedes hacer {self.combustible / self.consumo:.2f} km.")
            print("")
            # Usamos return para detener la ejecución del método, para que no ejecute el resto
            # de la función
            return
        
        # Si hay suficiente combustible, lo reducimos según la distancia recorrida
        self.combustible -= combustible_necesario
        # Mostramos al usuario cuántos litros consumió y cuántos le quedan
        print(f"Después de conducir {distanciaKm} km...\n"
              f"Litros de combustible consumidos: {combustible_necesario}\n"
              f"Litros de combustible disponibles: {self.combustible}")
        print("")
    
    # Método para repostar combustible
    def repostar(self, LitrosRepostados):
        # Aumentamos el combustible disponible con la cantidad repostada
        self.combustible += LitrosRepostados
        # Mostramos al usuario el nuevo nivel de combustible y la distancia que puede recorrer
        print(f"Después de repostar quedan {self.combustible} litros de combustible."
              f" Puedes hacer {self.combustible / self.consumo} km.")
        print("")

# Creamos un objeto de la clase Coche con los valores iniciales
# Marca: Toyota, Combustible inicial: 80 litros, Consumo: 0.08 litros por kilómetro
coche1 = Coche("Toyota", 80, 0.08)

# Probamos el método conducir con una distancia de 300 km
# Esto debería consumir 24 litros de combustible (300 * 0.08)
coche1.conducir(300)

# Probamos el método conducir con una distancia de 400 km
# Esto debería mostrar un mensaje de combustible insuficiente
coche1.conducir(400)

# Probamos el método conducir con una distancia de 500 km
# Esto también debería mostrar un mensaje de combustible insuficiente
coche1.conducir(500)

# Probamos el método repostar con 20 litros
# Esto debería aumentar el combustible disponible a 76 litros
coche1.repostar(20)