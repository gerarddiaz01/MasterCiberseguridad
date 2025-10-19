''' Ejercicio 1: Herencia y sobrescritura de métodos
Enunciado: Crea una clase Persona con atributos nombre y edad, y un método saludar() que imprima un 
saludo genérico incluyendo esos datos. Luego crea una clase Estudiante que herede de Persona. Estudiante 
debe tener además un atributo universidad (por ejemplo, "UNAM", "MIT", etc.), y su método saludar() debe
sobreescribir al de Persona para incluir la información de la universidad. Finalmente, crea una instancia
de Estudiante y verifica que puede usar tanto el saludo personalizado como los atributos heredados de Persona'''

# Definimos la clase base Persona 
class Persona:
    def __init__ (self, nombre, edad):
        # Inicializamos los atributos nombre y edad
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        # Método que imprime un saludo genérico con el nombre y la edad
        print(f"Hola me llamo {self.nombre} y tengo {self.edad} años, encantado.")

# Definimos la clase Estudiante que hereda de Persona
class Estudiante(Persona):
    def __init__ (self, nombre, edad, universidad):
        # Llamamos al constructor de la clase base (Persona) para inicializar nombre y edad
        super().__init__ (nombre, edad)
        # Inicializamos el nuevo atributo universidad, específico de Estudiante
        self.universidad = universidad
    
    def saludar(self):
        # Sobrescribimos el método saludar para incluir información sobre la universidad
        print(f"Hola me llamo {self.nombre} y tengo {self.edad} años, encantado."
              f" También, voy a la universidad {self.universidad}.")

# Creamos una instancia de la clase Persona
persona1 = Persona("Coline", 25)
# Creamos una instancia de la clase Estudiante
estudiante1 = Estudiante("Gerard", 30, "ConquerBlocks")

# Llamamos al método saludar de Persona
persona1.saludar()  # Salida: Hola me llamo Coline y tengo 25 años, encantado.

# Llamamos al método saludar de Estudiante (sobrescrito)
estudiante1.saludar()  # Salida: Hola me llamo Gerard y tengo 30 años, encantado. También, voy a la universidad ConquerBlocks.

# Accedemos al atributo nombre de estudiante1 (heredado de Persona)
print(estudiante1.nombre)  # Salida: Gerard

# Accedemos al atributo universidad de estudiante1 (definido en Estudiante)
print(estudiante1.universidad)  # Salida: ConquerBlocks