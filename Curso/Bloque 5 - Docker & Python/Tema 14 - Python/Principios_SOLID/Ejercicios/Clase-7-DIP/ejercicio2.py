from abc import ABC, abstractmethod


# Definir la ABSTRACCION del servicio de almacenamiento de productos
class AlmacenamientoProductos(ABC):
    @abstractmethod
    def agregar_producto(self, nombre: str, cantidad: int):
        pass

    @abstractmethod
    def obtener_stock(self, nombre: str) -> int:
        pass


# Implentacion del almacenamiento de productos
# METODO DE BAJO NIVEL --> detallado
class MemoriaAlmacenamientoProductos(AlmacenamientoProductos):
    def __init__(self):
        self.inventario = {}

    def agregar_producto(self, nombre: str, cantidad: int):
        if nombre in self.inventario:
            self.inventario[nombre] += cantidad
        else:
            self.inventario[nombre] = cantidad

    def obtener_stock(self, nombre: str) -> int: # anotaciones de tipo para ayudar a entender mejor el script, mejor legibilidad y mantenimiento
        return self.inventario.get(nombre, 0)


# METODO DE ALTO NIVEL -- logica de negocios
class GestorProductos: # Podríamos inyectar las dependencias en el constructor pero lo hacemos en un setter para controlar cuando usarlas
    def set_almacenamiento(self, almacenamiento: AlmacenamientoProductos):
        self.almacenamiento = almacenamiento
    # El parámetro almacenamiento debe ser de tipo AlmacenamientoProductos o de cualquier clase que herede de AlmacenamientoProductos
    # La dependencia que inyectamos en GestorProductos es una instancia de MemoriaAlmacenamientoProductos, que implementa la abstracción AlmacenamientoProductos

    def agregar_producto(self, nombre: str, cantidad: int):
        self.almacenamiento.agregar_producto(nombre, cantidad) # llamamos a agregar_producto de la abstracción, no se preocupa de mirar los detalles
        print(f" Producto { nombre} agregado al inventario")

    def obtener_stock(self, nombre: str):
        stock = self.almacenamiento.obtener_stock(nombre) # llamamos a obtener.stock de la abstracción
        print(f"Stock de {nombre}:{stock}")
        return stock


almacenamiento_memoria = MemoriaAlmacenamientoProductos()

gestor_productos = GestorProductos()
gestor_productos.set_almacenamiento(almacenamiento_memoria)  # INYECCION DE DEPENDENCIAS
gestor_productos.agregar_producto("Camisa", 2)
gestor_productos.agregar_producto("Pantalon", 10)
gestor_productos.obtener_stock("Camisa")
gestor_productos.obtener_stock("Pantalon")

gestor_productos.agregar_producto("Camisa", 1)
gestor_productos.agregar_producto("Pantalon", 1)
gestor_productos.obtener_stock("Camisa")
gestor_productos.obtener_stock("Pantalon")

'''
-DIP dice: Los módulos de alto nivel (la lógica de negocio, como GestorProductos) no deben depender de implementaciones concretas, sino de abstracciones.
Así, GestorProductos no sabe ni le importa si el almacenamiento es en memoria, en base de datos, en la nube, etc.
Solo sabe que puede llamar a agregar_producto y obtener_stock porque la abstracción (AlmacenamientoProductos) lo garantiza.
-Inyección de dependencias:
En vez de crear el almacenamiento dentro de GestorProductos, se lo pasamos desde fuera (lo "inyectamos").
Esto hace que el código sea más flexible y fácil de cambiar:
Si mañana queremos usar otro tipo de almacenamiento, solo creamos otra clase que herede de AlmacenamientoProductos y la pasamos al gestor, sin cambiar el 
código del gestor.
¿Qué ganamos con esto?
    - Flexibilidad: Podemos cambiar la implementación del almacenamiento sin tocar la lógica de negocio.
    - Reutilización: Podemos usar GestorProductos con cualquier clase que implemente la abstracción.
    - Testabilidad: Podemos pasar un "almacenamiento de prueba" para hacer tests fácilmente.
    - Desacoplamiento: El gestor no depende de detalles concretos, solo de lo que la abstracción promete.
Inyectar dependencias en el constructor es lo más habitual (constructor injection), pero también podemos hacerlo con un setter (setter injection).
Usar un setter nos permite decidir en qué momento del ciclo de vida del objeto queremos establecer la dependencia, no necesariamente al crearlo.
Esto puede ser útil si, por ejemplo, necesitamos cambiar la dependencia durante la ejecución, o si la dependencia no está disponible al momento de 
crear el objeto.
'''