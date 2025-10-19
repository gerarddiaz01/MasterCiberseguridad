# Clase base: Define la interfaz común para todas las figuras
class Figura:
    def obtener_area(self):
        pass

# Subclases
class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def obtener_area(self):
        return self.ancho * self.alto

    def set_ancho(self, ancho): # función para modificar el valor de ancho del rectangulo sin crear una nueva instancia, reutilizamos el mismo objeto
        self.ancho = ancho

    def set_alto(self, alto): # función para modificar el valor de alto del rectangulo sin crear una nueva instancia, actualizamos el valor
        self.alto = alto


class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def obtener_area(self):
        return self.lado * self.lado
    
    def set_lado(self, lado): # función para modificar el valor de lados del cuadrado sin crear una nueva instancia, simplemente le atribuimos otro valor
        self.lado = lado

# Función de alto nivel
def imprimir_area(figura: Figura): # se le pasa una figura (que tiene atribuidos unos detalles)
    print(f"Area:{figura.obtener_area()}") # llama al método obtener_area() concreto de la figura y usa los detallos para calcular el área


rectangulo = Rectangulo(4, 5)
cuadrado = Cuadrado(4)

imprimir_area(rectangulo)
imprimir_area(cuadrado)

rectangulo.set_alto(6)
rectangulo.set_ancho(7)
imprimir_area(rectangulo)

cuadrado.set_lado(2)
imprimir_area(cuadrado)

'''
Aplicación del LSP: a la función imprimir_area() podemos pasarle un Rectangulo() o un Cuadrado(), funcionará igual de bien porqué ambas clases implementan
el método obtener_area(). Si tenemos una función o clase que espera un objeto de la clase base, podemos darle una subclase y todo seguirá funcionando.
Las subclases no deben cambiar el comportamiento esperado de la clase base, solo pueden extenderlo o especializarlo.
Si una subclase rompe el comportamiento esperado (por ejemplo, no implementa bien un método o cambia cómo funciona), el programa puede tener errores o 
comportarse de forma inesperada cuando usemos esa subclase en lugar de la clase base.

Buenas prácticas: utilización de métodos set_():
    - Evitar crear nuevas instancias: Podemos cambiar el tamaño de un rectángulo o cuadrado ya existente sin tener que crear uno nuevo cada vez.
    - Facilitar la reutilización: Si tenemos un objeto que representa una figura y necesitamos cambiar sus dimensiones varias veces 
    (por ejemplo, en un programa interactivo o en un bucle), podemos hacerlo fácilmente.
    - Encapsulamiento: Usar métodos set_ es una buena práctica de programación orientada a objetos porque nos permite controlar cómo se modifican los atributos.
    Si en el futuro queremos añadir validaciones (por ejemplo, que el lado no sea negativo), podemos hacerlo dentro del método set_lado o set_ancho/set_alto.
'''