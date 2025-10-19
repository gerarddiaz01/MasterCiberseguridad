'''Ejercicio 1: Tienes una clase Rueda y quieres crear una clase Coche. Decide cómo relacionarlas:
Opción A: Coche hereda de Rueda.
Opción B: Coche tiene instancias de Rueda.
¿Cuál crees que es correcta y por qué? Luego, implementa la solución elegida:
La clase Rueda puede tener un atributo diámetro (por ejemplo, 16 pulgadas) y quizás un método rodar() que imprime algo como "Rueda rodando...".
La clase Coche debe, en su constructor, crear 4 objetos Rueda (asígnalos a una lista o a atributos como rueda1, rueda2, ...). Añade un método mover() en Coche que haga 
que sus ruedas rueden (llamando al método correspondiente de cada rueda) y que imprima "Coche avanzando...".'''

class Rueda:
    def __init__(self, diametro):
        self.diametro = diametro
    
    def rodar(self):
        print("Rueda rodando...")
    
class Coche:
    def __init__(self, marca, diametro_ruedas):
        self.marca = marca
        self.ruedas = [Rueda(diametro_ruedas) for _ in range(4)]

    def mover (self):
        for rueda in self.ruedas:
            rueda.rodar()
        print(f"El coche {self.marca} está avanzando")

coche1 = Coche("Toyota", 16)
coche1.mover()
# "python.defaultInterpreterPath": "C:\\Users\\gerar\\miniconda3\\envs\\Conquer\\python.exe",