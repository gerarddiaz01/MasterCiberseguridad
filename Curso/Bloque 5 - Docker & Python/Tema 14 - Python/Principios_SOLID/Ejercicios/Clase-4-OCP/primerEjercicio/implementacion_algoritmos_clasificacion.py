from abc import ABC, abstractmethod

class Classifier(ABC):
    @abstractmethod
    def train(self, data, labels):
        pass

    @abstractmethod
    def predict(self, data):
        pass

'''
Explicación en el contexto de algoritmos de clasificación y el principio Open/Closed (SOLID):
Este código define una clase abstracta llamada Classifier que representa la interfaz común para cualquier algoritmo de clasificación.

El método train(self, data, labels) es abstracto: todas las subclases deben implementar cómo se entrena el modelo con los datos y las etiquetas.
El método predict(self, data) también es abstracto: todas las subclases deben implementar cómo se hacen predicciones con nuevos datos.

¿Por qué es útil esto para el Open/Closed Principle?
Open/Closed Principle: El sistema está abierto para extensión (puedes crear nuevos clasificadores) pero cerrado para modificación 
(no necesitas cambiar la clase base ni el resto del sistema para añadir nuevos algoritmos).
Por ejemplo, puedes crear subclases como KNNClassifier, SVMClassifier, DecisionTreeClassifier, etc., cada una implementando su propia 
lógica de entrenamiento y predicción, sin modificar la clase Classifier ni el código que la usa.
Así, si el sistema necesita soportar un nuevo algoritmo, solo tenemos que crear una nueva subclase y la implementamos, cumpliendo el 
Open/Closed Principle del SOLID.
Esto hace nuestro código más flexible, modular y fácil de extender en el futuro.
'''

class NaiveBayesClassifier(Classifier):
    def train(self, data, labels):
        # Implementación del entrenamiento de Naive Bayes
        pass

    def predict(self, data):
        # Implementación de la predicción de Naive Bayes
        pass

class NeuralNetworkClassifier(Classifier):
    def train(self, data, labels):
        # Implementación del entrenamiento de Red Neuronal
        pass

    def predict(self, data):
        # Implementación de la predicción de Red Neuronal
        pass

class SVMClassifier(Classifier):
    def train(self, data, labels):
        # Implementación del entrenamiento de SVM
        pass

    def predict(self, data):
        # Implementación de la predicción de SVM
        pass

'''
Las tres clases heredan de la clase abstracta Classifier() y todas tienen que implementar los métodos train() y predict(), porqué son métodos 
abstractos.
Cada algoritmo tiene una implementación específica:
    - NaiveBayesClassifier implementará el entrenamiento y la predicción usando el algoritmo de Naive Bayes.
    - NeuralNetworkClassifier hará lo mismo pero usando una red neuronal.
    - SVMClassifier lo hará usando máquinas de soporte vectorial (SVM).
    Cada clase puede tener su propia lógica interna, pero todas comparten la misma interfaz (train y predict).
Open/Closed Principle:
    - Abierto para extensión: Si queremos añadir un nuevo algoritmo de clasificación, solo tenemos que crear una nueva subclase de 
    Classifier e implementar los métodos requeridos.
    - Cerrado para modificación: No necesitamos modificar la clase base Classifier ni las otras clases ya existentes.
Esto hace que el sistema sea flexible y fácil de mantener o ampliar.
Ventajas prácticas
    - Podemos usar cualquier clasificador de manera intercambiable en tu código, porque todos tienen los mismos métodos.
    - Si en el futuro surge un nuevo algoritmo, solo añadimos una nueva clase y el resto del sistema puede usarla sin cambios.
'''

from abc import ABC, abstractmethod

class RoutingAlgorithm(ABC):
    @abstractmethod
    def calculate_routes(self, network_topology):
        pass

    @abstractmethod
    def update_routes(self, network_event):
        pass

class DistanceVectorRouting(RoutingAlgorithm):
    def calculate_routes(self, network_topology):
        # Implementación del cálculo de rutas de vector de distancia
        pass

    def update_routes(self, network_event):
        # Implementación de la actualización de rutas de vector de distancia
        pass

class LinkStateRouting(RoutingAlgorithm):
    def calculate_routes(self, network_topology):
        # Implementación del cálculo de rutas de estado de enlace
        pass

    def update_routes(self, network_event):
        # Implementación de la actualización de rutas de estado de enlace
        pass

class PolicyBasedRouting(RoutingAlgorithm):
    def calculate_routes(self, network_topology):
        # Implementación del cálculo de rutas basado en políticas
        pass

    def update_routes(self, network_event):
        # Implementación de la actualización de rutas basada en políticas
        pass

'''
Clase abstracta como interfaz común:
    - RoutingAlgorithm es una clase abstracta que define dos métodos abstractos: calculate_routes y update_routes.
    - Esto obliga a que cualquier algoritmo de enrutamiento que herede de esta clase implemente estos métodos, asegurando una interfaz común 
    para todos los algoritmos.

Implementaciones concretas:
    - DistanceVectorRouting implementa la lógica específica para el algoritmo de vector de distancia.
    - LinkStateRouting implementa la lógica para el algoritmo de estado de enlace.
    - PolicyBasedRouting implementa la lógica para el enrutamiento basado en políticas.
    Cada clase puede tener su propia lógica interna, pero todas comparten la misma interfaz.

Relación con el Open/Closed Principle:
    - Abierto para extensión: Si necesitas agregar un nuevo algoritmo de enrutamiento, solo tienes que crear una nueva subclase de 
    RoutingAlgorithm e implementar los métodos requeridos.
    - Cerrado para modificación: No necesitas modificar la clase base ni las clases existentes para añadir nuevas funcionalidades.
    Esto hace que el sistema sea flexible, mantenible y fácil de ampliar.
Ventajas prácticas:
    - Puedes usar cualquier algoritmo de enrutamiento de manera intercambiable en tu sistema, porque todos tienen los mismos métodos.
    - Si surge un nuevo tipo de algoritmo, solo añades una nueva clase y el resto del sistema puede usarla sin cambios.

'''