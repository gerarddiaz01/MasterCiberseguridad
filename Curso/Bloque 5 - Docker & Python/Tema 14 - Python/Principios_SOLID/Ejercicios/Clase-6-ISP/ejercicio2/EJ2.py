'''Imagina un sistema para dispositivos de oficina. Inicialmente se definió una interfaz llamada Multifuncional con tres métodos: imprimir(), escanear()
 y enviarFax(). Dos clases implementan esta interfaz:
ImpresoraBasica que solo imprime, pero como implementa Multifuncional, se ve obligada a definir (aunque sea vacías) escanear() y enviarFax().
EquipoMultifuncional que sí realiza las tres operaciones (impresora+escáner+fax).
Este diseño claramente viola ISP, ya que ImpresoraBasica no necesita escanear ni enviar fax. Nuestra tarea es rediseñar las interfaces para corregir 
el problema:
Definimos interfaces segregadas para las funciones de imprimir, escanear y fax.
Ajustamos las clases para implementar solo las interfaces que requieran:
ImpresoraBasica debería implementar solo la interfaz de impresión.
EquipoMultifuncional debería implementar las necesarias para imprimir, escanear y faxear.
Finalmente, mostramos cómo instanciar y utilizar estos objetos en un código de ejemplo, asegurándonos de que cada clase tenga solo los métodos que usa'''

from abc import ABC, abstractmethod

# Creamos las tres interfaces abstractas, cada una con su función
class Impresion(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Escaneo(ABC):
    @abstractmethod
    def escanear(self):
        pass

class Fax(ABC):
    @abstractmethod
    def enviar_fax(self):
        pass

# Creamos los objetos con las funciones que necesitan tener heredando de las interfaces que les interesan
class ImpresoraBasica(Impresion):
    def imprimir(self, documento):
        print(f"Impresora básica imprimiendo: {documento}")
    # No implementa Escaneable ni Faxable, no los necesita.

class ImpresoraMultiFuncional(Impresion, Escaneo, Fax):
    def imprimir(self, documento):
        print(f"Multifuncional imprime: {documento}")

    def escanear(self) -> str:
        texto = "contenido escaneado"
        print("Multifuncional escaneando documento...")
        return texto

    def enviar_fax(self, numero):
        print(f"Multifuncional enviando fax al {numero}...")



dispositivos = [ImpresoraBasica(), ImpresoraMultiFuncional()]

for dispositivo in dispositivos:
    dispositivo.imprimir("Informe Anual.pdf")
    if isinstance(dispositivo, Escaneo): # isinstance verifica si dispositivo es una instancia de la clase Escaneo, si tiene la capacidad de escanear o no
        contenido = dispositivo.escanear()
        print(f"Contenido escaneado: {contenido}")
    if isinstance(dispositivo, Fax): # isinstance verifica si dispositivo es una instancia de la clase Fax, si tiene la capacidad de enviar un fax o no
        dispositivo.enviar_fax("12345")
    print("-----")

# Creamos los objetos con las funciones que necesitan tener heredando de las interfaces que les interesan
# class ImpresoraBasica(Impresion):
#     def imprimir(self):
#         print("La impresora básica está imprimiendo.")

# class ImpresoraMultiFuncional(Impresion, Escaneo, Fax):
#     def imprimir(self):
#         print("La impresora multifuncional está imprimiendo.")

#     def escanear(self):
#         print("La impresora multifuncional está escaneando un documento.")

#     def enviar_fax(self):
#         print("La impresora multifuncional está enviando un fax al jefe.")

# impresora_basica = ImpresoraBasica()
# impresora_basica.imprimir()

# impresora_multifuncional = ImpresoraMultiFuncional()
# impresora_multifuncional.imprimir()
# impresora_multifuncional.escanear()
# impresora_multifuncional.enviar_fax()