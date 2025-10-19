'''
En un sistema de monitoreo, existe la siguiente clase:

class SensorManager:
    def __init__(self):
        self.logger = ConsoleLogger()
    def leer_sensores(self):
        # ... código para leer múltiples sensores ...
        datos = {"temp": 24, "humedad": 60}
        self.logger.log(f"Lectura de sensores: {datos}")
        return datos

class ConsoleLogger:
    def log(self, mensaje):
        print(f"[LOG] {mensaje}")

SensorManager (alto nivel) se encarga de interaccionar con varios sensores y obtener sus datos. Actualmente, dentro de su constructor, instancia un 
ConsoleLogger para registrar las lecturas. Esto viola DIP: estamos acoplando la gestión de sensores con un detalle de implementación de logging 
(específicamente, loguear a la consola).

Objetivo: Aplicar DIP para que SensorManager pueda funcionar con diferentes tipos de logger sin depender de uno específico.
Define una interfaz (abstracción) Logger con el método log(mensaje) y haz que ConsoleLogger la implemente.
Crea otra implementación de Logger, por ejemplo FileLogger que escriba el log en un archivo, o SilentLogger que no haga nada (podría servir para 
desactivar el log).
Modifica SensorManager para que no instancie el logger por dentro, sino que lo reciba de afuera (inyección de dependencias). Puede ser por 
constructor o por setter; elige la que creas más adecuada aquí.
Ajusta el código de lectura de sensores para usar el logger abstracto.
Muestra cómo usar SensorManager con un ConsoleLogger y con tu nuevo FileLogger/SilentLogger para ver la diferencia.
'''

from abc import ABC, abstractmethod

# Abstracción
class Logger(ABC):
    @abstractmethod
    def log(self, mensaje):
        pass

# Implementaciones
class ConsoleLogger(Logger):
    def log(self, mensaje):
        print(f"[LOG] {mensaje}")

class SilentLogger(Logger):
    def log(self, mensaje):
        pass

# Método de alto nivel
class SensorManager:
    def __init__(self, logger: Logger): # Inyección de dependencias por constructor
        self.logger = logger

    def leer_sensores(self):
        # ... código para leer múltiples sensores ...
        datos = {"temp": 24, "humedad": 60}
        self.logger.log(f"Lectura de sensores: {datos}")
        return datos
    
console_logger = ConsoleLogger()
sensormanager = SensorManager(console_logger)# Inyección de dependencias
sensormanager.leer_sensores()

'''
¿Por qué el script cumple con DIP?
SensorManager (el módulo de alto nivel) no depende de una implementación concreta de logger (como ConsoleLogger), sino de una abstracción (Logger).
Hemos definido una interfaz abstracta (Logger) usando una clase abstracta con el método log.
Las implementaciones concretas (ConsoleLogger, SilentLogger) heredan de la abstracción y pueden ser intercambiadas sin modificar el código de SensorManager.
SensorManager recibe la dependencia desde fuera (inyección de dependencias) usando el método set_logger, en vez de crear la instancia internamente.
Podemos cambiar el tipo de logger (por ejemplo, de consola a silencioso) sin modificar la lógica de SensorManager.
'''