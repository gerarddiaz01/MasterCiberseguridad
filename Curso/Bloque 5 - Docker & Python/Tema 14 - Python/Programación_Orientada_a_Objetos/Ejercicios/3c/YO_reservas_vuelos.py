'''SISTEMA DE RESERVAS DE VUELOS
Imagina que estás desarrollando un sistema de reservas de vuelos para una
aerolínea. Crea un sistema de clases que permita a los usuarios realizar
reservas de vuelos. Aquí tienes una posible estructura:
- Clase base: `Vuelo`
- Atributos: número de vuelo, origen, destino, capacidad máxima, lista de
pasajeros
- Métodos: agregar pasajero, verificar disponibilidad de asientos
- Clase derivada: `VueloEspecial` (hereda de `Vuelo`)
- Atributos adicionales: motivo del vuelo especial (por ejemplo, vacaciones,
trabajo)
Resuelve el problema creando instancias de estas clases y realizando
reservas para diferentes vuelos y tipos de vuelos especiales'''

class Vuelo:
    def __init__(self, numero_vuelo, origen, destino, capacidad_max):
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.capacidad_max = capacidad_max
        self.pasajeros = []
    
    def agregar_pasajero(self, nuevo_pasajero):
        if self.asientos_disponibles() > 0:
            self.pasajeros.append(nuevo_pasajero)
            print(f"Pasajero {nuevo_pasajero.nombre} agregado al vuelo {self.numero_vuelo}")
        else:
            print(f"No hay asientos disponibles en este vuelo")

    def asientos_disponibles(self): # Hacemos la verificación dinámicamente combinando métodos
         # Calculamos los asientos disponibles restando los pasajeros actuales de la capacidad máxima
         return self.capacidad_max - len(self.pasajeros)
    
    def mostrar_pasajeros(self):
        for pasajero in self.pasajeros:
            print(pasajero.nombre)

class VueloEspecial(Vuelo): #logica especifica: descuento si es por trabajo
    def __init__(self, numero_vuelo, origen, destino, capacidad_max):
        super().__init__(numero_vuelo, origen, destino, capacidad_max)
    
    def agregar_pasajero(self, nuevo_pasajero, motivo):
        super().agregar_pasajero(nuevo_pasajero)
        if motivo.lower() == "trabajo":
            print(f"Pasajero {nuevo_pasajero.nombre} tiene un descuento para éste vuelo de un 20%, porque vuela por {motivo}")

class Pasajero:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
    
    def __str__(self):
        # Representación legible del pasajero
        return f"{self.nombre}, Nacionalidad: {self.nacionalidad}"


# Creamos una instancia de Vuelo
vuelo1 = Vuelo("AB123", "Madrid", "París", 150)

# Creamos una instancia de VueloEspecial
vuelo_especial1 = VueloEspecial("CD456", "Barcelona", "Roma", 100)

# Creamos una instancia de Pasajero
pasajero_gerard = Pasajero("Gerard", "Español")

# Agregamos el pasajero al vuelo
vuelo1.agregar_pasajero(pasajero_gerard)
vuelo_especial1.agregar_pasajero(pasajero_gerard, "trabajo")

# Mostramos los asientos disponibles
print(f"Asientos disponibles: {vuelo1.asientos_disponibles()}")
print(f"Asientos disponibles: {vuelo_especial1.asientos_disponibles()}")

# Mostramos la lista de pasajeros
vuelo1.mostrar_pasajeros()
vuelo_especial1.mostrar_pasajeros()