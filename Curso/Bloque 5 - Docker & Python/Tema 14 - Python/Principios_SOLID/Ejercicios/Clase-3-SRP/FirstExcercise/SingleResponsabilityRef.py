'''Cojemos el script de SingleResponsabilityAco.py y lo ordenamos siguiendo los principios SOLID, composición y cohesión:
- Separa claramente las responsabilidades.
- Se usa bien la composición: El motor Engine() se pasa como dependencia a Vehicle(), permitiendo cambiar el motor fácilmente.
- Error: si vehículo crea su propio motor "self._engine = Engine()", es composición pero no siguiendo SOLID, es mejor crear el motor así "engine = Engine()"
y luego pasárselo a Vehicle() cómo atributo ya creado.
- El objetivo es que si queremos cambiar algo podamos hacerlo facilmente, que no se modifiquen otras partes de nuestro código y se vuelva loco.
'''


class Engine: # No hay __init__ porque no necesita inicializar atributos
    def getRPM(self): # Sólo tiene un método de valor fijo
        return 3000  # valor por defecto del motor


class Vehicle:
    def __init__(self, name, speed, engine): # Pasamos Engine cómo atributo: Composición
        self._name = name
        self._speed = speed
        self._engine = engine # Aquí se guarda una instancia de Engine: Composición

    def getName(self): # son getters porque permiten acceder a metodos privados
        return self._name

    def getEngineRPM(self): # dichos getters son la unica manera de acceder a éstes métodos privados
        return self._engine.getRPM()

    def getMaxSpeed(self):
        return self._speed


class VehiclePrinter: # Ésta clase se encarga solo de imprimir la información de un vehículo
    def __init__(self, vehicle): # Recibe un vehicle en su constructor y la guarda como atributo
        self._vehicle = vehicle

    def printInfo(self): # Imprime los datos del vehículo usando el método format de los strings, para insertar valores dentro de un texto
        print(
            "Vehicle: {}, Max Speed: {}, RPM: {}".format(
                self._vehicle.getName(),
                self._vehicle.getMaxSpeed(),
                self._vehicle.getEngineRPM(),
            )
        ) # reemplazamos las llaves {} por los valores de los métodos del vehículo


class VehiclePersistance: # Representa la responsabilidad de guardar (persistir) los datos de un vehículo en algún lugar, cómo una base de datos
    def __init__(self, vehicle, db): # Recibe un vehicle y el nombre de una base de datos en el constructor
        self._vehicle = vehicle
        self._persistance = db
        print("Hey, storing data! in", self._persistance)


if __name__ == "__main__":
    engine = Engine() # Creamos un motor
    vehicle = Vehicle(name="Car", engine=engine, speed=200) # Le pasamos el motor creado a la class Vehicle(): Composición
    persistance = VehiclePersistance(vehicle=vehicle, db="SQL") # Si queremos cambiar de base de datos, cambiamos implemente aquí y el resto se cambia solo
    printer = VehiclePrinter(vehicle=vehicle)
    printer.printInfo()
