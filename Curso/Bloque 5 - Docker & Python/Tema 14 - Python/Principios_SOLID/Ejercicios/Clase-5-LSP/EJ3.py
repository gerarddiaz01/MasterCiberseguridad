# Pregunta 1: ¿Se cumple LSP? ¿Qué problema ves con la clase Pinguino al usarla polimórficamente como Ave?

# class Ave:
#     def volar(self):
#         print("El ave vuela")

# class Golondrina(Ave):
#     pass

# class Pinguino(Ave):
#     def volar(self):
#         print("El pingüino intenta volar... pero no puede :-(")

'''En la jerarquía dada, Pinguino hereda de Ave y por tanto es tratable como un Ave. Sin embargo, conceptualmente un pingüino no puede volar. 
En la implementación propuesta, Pinguino.volar() imprime un mensaje indicando que no vuela (lo cual es una forma suave de violar LSP, al menos 
no rompe el código, pero sí contradice la expectativa). El código prueba_vuelo asume que cualquier Ave "vuela" efectivamente. Si bien aquí solo 
imprime mensajes, imagina que prueba_vuelo calculase tiempo de vuelo, distancia, etc. Con un pingüino, esos cálculos no tendrían sentido.
Esto es una violación del Principio de Sustitución de Liskov: un Pinguino no cumple con las mismas "propiedades" que otros Ave (no puede realizar la 
acción volar realmente). Aunque aquí no hay un fallo catastrófico en tiempo de ejecución, sí hay una ruptura del contrato: Ave.volar implica la capacidad 
de volar, Pinguino no la tiene. Hemos forzado una relación de herencia inapropiada.'''

# Pregunta 2: ¿Cómo arreglarías el diseño? (Pista: hay varias opciones: podrías eliminar o modificar el método volar de Ave, 
# segregar interfaces, o redefinir la jerarquía).

# def prueba_vuelo(ave: Ave):
#     # Esta función espera que el ave vuele de alguna forma
#     ave.volar()
#     print("Vuelo completado.\n")

# aves = [Golondrina(), Pinguino()]
# for ave in aves:
#     prueba_vuelo(ave)

'''Opción A: Segregar interfaces (ISP aplicado). Podemos reconocer que no todas las aves vuelan. Crear una interfaz (clase base abstracta) separada 
para aves voladoras. Por ejemplo, tener class Ave sin método volar, y luego class AveVoladora(Ave) con método abstracto volar(). Golondrina hereda 
de AveVoladora, pingüino hereda de Ave directamente o de una posible AveNoVoladora sin volar. 
En código:'''

# class Ave:
#     pass

# class AveVoladora(Ave):
#     def volar(self):
#         raise NotImplementedError

# class Golondrina(AveVoladora):
#     def volar(self):
#         print("La golondrina vuela bajo las nubes")

# class Pinguino(Ave):
#     def nadar(self):
#         print("El pingüino nada en el agua")

# Aquí ya no hacemos Pinguino.volar(). La función prueba_vuelo debería tiparse para AveVoladora en vez de Ave, así nunca se le pasaría un pingüino. 
# Esto cumple LSP porque todas las AveVoladora pueden volar, y un pingüino ya ni siquiera tiene volar() en su interfaz.

'''Opción B: Composición en lugar de herencia para comportamientos. Podríamos mantener Ave con un atributo que denote su estrategia de movimiento 
(volar, nadar, correr). Por ejemplo, un pingüino podría tener una estrategia de "no vuela / camina y nada", mientras una golondrina tiene estrategia 
de "volar". Así, la clase Ave podría llamar a su estrategia de movimiento. Esto se parece a Strategy pattern y también solucionaría el problema separando 
el comportamiento en objetos distintos.'''

'''Opción C: Herencia múltiple / mixins (no muy necesario aquí): Python permitiría hacer algo como class Volador: def volar(): ... y luego 
class Pinguino(Ave): pass y class Golondrina(Ave, Volador): .... Pero esto se complica y realmente es similar a la opción A conceptualmente.'''

# Veamos cómo implementar la opción A:

from abc import ABC, abstractmethod

class Ave:
    def comer(self):
        print("El ave come")

class AveVoladora(Ave):
    @abstractmethod
    def volar(self):
        pass

class Golondrina(AveVoladora):
    def volar(self):
        print("La golondrina vuela alto")

class Aguila(AveVoladora):
    def volar(self):
        print("El Aguila vuela y caza al mismo tiempo")

class Pato(AveVoladora):
    def volar(self):
        print("El pato sale del algo y vuela alto para migrar")
    
    def nadar(self):
        print("El pato nada pacíficamente")

class Pinguino(Ave):
    def nadar(self):
        print("El pinguino nada rápido")

def prueba_vuelo(ave: AveVoladora):
    ave.volar()
    print("Vuelo completado")

def prueba_nado(ave: Ave):
    ave.nadar()
    print("Nado completado")

aves_voladoras = [Golondrina(), Aguila(), Pato()]
for ave in aves_voladoras:
    prueba_vuelo(ave)

aves_nadando = [Pinguino(), Pato()]
for ave in aves_nadando:
    prueba_nado(ave)

'''
Ahora sí, la jerarquía respeta LSP: cualquier objeto pasado a prueba_vuelo es de tipo AveVoladora y ciertamente vuela. Un Pinguino ni siquiera puede 
ser pasado a prueba_vuelo porque no es subtipo de AveVoladora. Hemos segregado las interfaces de Ave en dos: las que vuelan y las que no (o al menos 
no nos interesa su vuelo).
Con este rediseño:
    - Cohesión: Mejor, cada clase tiene solo los métodos que puede cumplir.
    - Acoplamiento: prueba_vuelo solo conoce la abstracción AveVoladora.
    - LSP: Cumplido, ninguna subclase rompe las expectativas. Golondrina reemplaza a AveVoladora correctamente. Pingüino nunca promete volar, así que no 
    rompe nada.
    - ISP: Cumplido también, ya que no forzamos a Pingüino a implementar un método que no usa.
Este ejercicio muestra cómo detectar una violación de LSP (un subtipo que no puede cumplir el contrato del supertipo) y refactorizar el modelo para 
corregirlo. En general, si te encuentras escribiendo subclases que anulan métodos con comportamientos "vacíos" o contrarios a lo esperado (e.g., 
lanzando excepciones, o imprimiendo "no puedo hacer X"), es una señal de alarma de LSP/ISP: quizá la jerarquía de herencia no es adecuada y debes 
reconsiderar tu diseño.
'''