''' Ejercicio 2: Composición de clases
Enunciado: Vamos a modelar un sistema sencillo de dispositivos. Crea una clase Bateria con un atributo carga 
(porcentaje de 0 a 100) y métodos usar(energia) (que reduzca la carga en cierto porcentaje, sin bajar de 0) 
y recargar() (que la ponga al 100%). Luego crea una clase Telefono con atributos marca y modelo. El teléfono 
debe tener una Bateria (instancia de Bateria). Agrega un método usar_app(tiempo) en Telefono que simule el uso 
de una aplicación por X minutos, reduciendo la batería (por ejemplo, 1% por minuto de uso). Finalmente, crea un 
objeto Telefono con su batería, úsalo por algunos minutos y muestra la carga de la batería antes y después de usarlo.'''

class Bateria:
    def __init__(self, carga):
        # Aseguramos que la carga inicial esté entre 0 y 100
        self.carga = max(0, min(carga, 100))
    
    def usar(self, uso_bateria):
        # Reduce la carga de la batería, pero no permite que baje de 0
        self.carga -= uso_bateria
        if self.carga < 0:
            self.carga = 0
        print(f"Bateria usada: {uso_bateria}%")
        print(f"Bateria restante: {self.carga}%")
    
    def recargar(self):
        # Recarga la batería al 100%
        self.carga = 100
        print(f"Bateria recargada al 100%")

class Telefono:
    def __init__(self, marca, modelo):
        # Inicializamos los atributos del teléfono
        self.marca = marca
        self.modelo = modelo
        # Relación de composición: el teléfono tiene una batería
        self.bateria = Bateria(carga=100)  # La batería comienza con 100% de carga
    
    def usar_app(self, minutos):
        # Simula el uso de una app, reduciendo la batería en 1% por minuto
        consumo = minutos * 1  # 1% de batería por minuto
        print(f"Usando el teléfono {self.marca} {self.modelo} durante {minutos} minutos")
        self.bateria.usar(consumo)  # Llama al método usar de la batería

# Creamos un teléfono con una batería al 100%
telefono1 = Telefono("Iphone", "14")

# Mostramos la carga inicial de la batería
print(f"Carga inicial: {telefono1.bateria.carga}%")

# Usamos la app por 30 minutos
telefono1.usar_app(30)

# Usamos la app por 50 minutos
telefono1.usar_app(50)

# Mostramos la carga después de usar la app
print(f"Carga después de usar la app: {telefono1.bateria.carga}%")

# Recargamos la batería
telefono1.bateria.recargar()