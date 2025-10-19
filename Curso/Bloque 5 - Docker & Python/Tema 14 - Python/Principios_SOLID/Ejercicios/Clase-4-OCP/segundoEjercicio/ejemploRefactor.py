'''Open/Close Principle: Si queremos añadir un nuevo tipo de ataque, simplemente creamos una nueva clase que herede de attackManager() y la implementamos.
El sistema está abierto para extensión (nuevos ataques) y cerrado para modificación (no cambiamos el código existente)'''

from abc import ABC, abstractmethod


class attackManager(ABC):
    @abstractmethod # Garantizamos que cualquier tipo de ataque tendrá el mismo método, aunque la implementación sea distinta
    def attack(self, superhero):
        pass


# Implementaciones concretas, cada clase representa un ataque diferente
class PunchAttack(attackManager): # Open/Close Principle: podemos crear nuevos tipos de ataque sin modificar el resto del sistema
    def attack(self, superhero):
        return f"{superhero.name} attacks with a powerfull punch!!!! "


class LaserAttack(attackManager):
    def attack(self, superhero):
        return f"{superhero.name} attacks with a long laser!!!"


class FireballAttack(attackManager):
    def attack(self, superhero):
        return f"{superhero.name} attacks with a big fire ball!!!"


class IceballAttack(attackManager):
    def attack(self, superhero):
        return f"{superhero.name} attacks with a big ice ball!!!"
# Para ampliar el código simplemente creamos una nueva clase aqui con un nuevo ataque, sin modificar Superhero() ni Game()


class Superhero:
    def __init__(self, name, health, attackManager) -> None:
        self.name = name
        self.health = health
        self.attackManager = attackManager

    def attack(self): # Éste método delega la acción al tipo de ataque que tenga asignado
        return self.attackManager.attack(self) # El comportamiento de ataque de cada superhéroe depende del objeto de ataque que se le pase al crearlo


class Game: # Mantiene la lista de superhéroes
    def __init__(self) -> None:
        self.superheroes = []

    def add_superheroes(self, superhero): # Podemos añadir superhéroes
        self.superheroes.append(superhero)

    def superheroe_action(self): # Recorremos la lista de superhéroes y ejecutamos su ataque, imprimiendo el resultado
        for superhero in self.superheroes:
            print(superhero.attack())


game = Game() # Creamos un juego
superman = Superhero("Superman", 100, PunchAttack()) # Se crean instancias de varios superhéroes, cada uno con un tipo de ataque diferente
cyclops = Superhero("Cyclops", 80, LaserAttack())
fireman = Superhero("Fireman", 120, PunchAttack())
iceman = Superhero("Iceman", 120, IceballAttack())

game.add_superheroes(superman) # Añadimos las instancias de los superhéroes al juego
game.add_superheroes(cyclops)
game.add_superheroes(fireman)
game.add_superheroes(iceman)

game.superheroe_action() # Llamamos éste método para que cada superhéroe ataque usando su propio tipo de ataque

""" 
Es cómo tener matrioshkas: Hay diferentes niveles que cada uno delega responsabilidades al siguiente de forma ordenada y jerárquica. 
  - Dentro de Game() tenemos la lista de superhéroes y su acción
  - Dentro de Superhero() tenemos attack() que llama al tipo de ataque (attackManager) según la instancia de heroe creada
  - Dentro de attackManager() tenemos los tipos de ataques y su comportamiento (se añaden aqui los nuevos ataques sin tocar el resto)
  - En la acción dentro de Game() se llama al attack() de dicho superhéroe, y el attack() del superhero llama al tipo de ataque de attackManager() y el tipo
   de ataque depende del attackManager() que se ha especificado al crear la instancia del superheroe 
"""