'''Enunciado: Crea una clase Persona que tenga como atributos nombre y edad. 
Añade un método saludar que imprima un saludo incluyendo el nombre, y otro método 
cumplir_anio que aumente en 1 la edad de la persona. Prueba crear una instancia de 
Persona y utiliza sus métodos, mostrando antes y después la edad para verificar que 
el método cumplir_anio funciona correctamente'''

class Persona:
    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años, encantado.")
    
    def cumplir_años(self):
        self.edad += 1
        print(f"Woah es tu cumpleaños {self.nombre}, felicidades!")

gerard = Persona("Gerard", 30)
gerard.saludar()
gerard.cumplir_años()
print(gerard.edad)