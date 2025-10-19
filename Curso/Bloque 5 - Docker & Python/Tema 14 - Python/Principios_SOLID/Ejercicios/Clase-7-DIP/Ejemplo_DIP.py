'''Estamos construyendo una aplicación y queremos implementar un módulo de reporte que toma datos de ventas y genera un informe, luego lo guarda y notifica 
a algún canal.'''

from abc import ABC, abstractmethod


# Definimos las abstracciones
class RepositorioReportes(ABC): # Para el almacenamiento del reporte
    @abstractmethod
    def guardar_reporte(reporte):
        pass

class Notificador(ABC): # Para notificar al destinatario
    @abstractmethod
    def enviar(destinatario, mensaje):
        pass

# Definimos las implementaciones de bajo nivel
class RepositorioDisco(RepositorioReportes): # Guarda el reporte en los archivos locales
    def guardar_reporte(self, reporte):
        print(f"{reporte} se ha guardado en los archivos locales.")

class RepositorioDB(RepositorioReportes): # Guarda el reporte en una base de datos
    def guardar_reporte(self, reporte):
        print(f"{reporte} se ha guardado en la base de datos.")

class EmailNotificador(Notificador): # Envía la notificación por email
    def enviar(self, destinatario, mensaje):
        print(f"El email {mensaje} se ha enviado correctamente a {destinatario}.")

class SMSNotificador(Notificador): # Envía la notificación por SMS
    def enviar(self, destinatario, mensaje):
        print(f"El SMS {mensaje} se ha enviado correctamente a {destinatario}.")

# Módulo de alto nivel:
class GeneradorReportes:
    def __init__(self, repositorio: RepositorioReportes, notificador: Notificador):
       self.repositorio = repositorio
       self.notificador = notificador

    def generar_y_procesar(self, datos, destinatario):
       print("Informe generado.")
       self.repositorio.guardar_reporte(datos)
       self.notificador.enviar(destinatario, "Reporte listo")

# main de la aplicación
datos_semanales = "12345"
repo = RepositorioDisco()
notif = EmailNotificador()
generador = GeneradorReportes(repo, notif) # Inyección de dependencias
generador.generar_y_procesar(datos_semanales, "gerente@empresa.com")

'''
GeneradorReportes no sabe aún si repo será RepositorioDisco o RepositorioDB o si notif será EmailNotificador o SMSNotificador, podemos cambiar éstas decisiones 
en un sólo lugar sin cambiar la lógica de GeneradorReportes. 
Éste diseño es flexible: podríamos fácilmente reutilizar GeneradorReportes en otro contexto guardando en la base de datos simplemente construyéndolo con RepositorioDB(). O para un segundo 
reporte podríamos instanciar otro GeneradorReportes con diferentes dependencias.
'''