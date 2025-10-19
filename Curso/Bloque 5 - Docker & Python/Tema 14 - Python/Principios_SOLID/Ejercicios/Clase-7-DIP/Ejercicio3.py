'''Tienes un código que maneja la generación de reportes en una aplicación:

class FileSaver:
    def save_to_file(self, data, filename):
        with open(filename, 'w') as f:
            f.write(data)

class ReportGenerator:
    def __init__(self):
        self.saver = FileSaver()
    def generate_report(self, text):
        report = f"*** Reporte ***\n{text}\n**************"
        self.saver.save_to_file(report, 'reporte.txt')
        print("Reporte generado y guardado.")

En esta versión, ReportGenerator (módulo de alto nivel encargado de crear el reporte) está dependiendo directamente de un módulo de bajo nivel concreto 
FileSaver para guardar el archivo. Esto viola DIP porque si quisiéramos guardar los reportes de otra forma (por ejemplo en una base de datos, o enviarlos 
por red) tendríamos que modificar ReportGenerator. Además, para pruebas, ReportGenerator siempre escribe en el sistema de archivos real, lo que no es ideal.

Tu tarea: Refactoriza el diseño para seguir el Principio de Inversión de Dependencias:
- Crea una abstracción Saver (por ejemplo una clase abstracta con un método save(data, destino) o similar) que represente el acto de guardar datos.
- Haz que ReportGenerator dependa de esa abstracción, recibiéndola por el constructor (inyección por constructor).
- Implementa al menos dos variantes concretas de Saver: una similar a FileSaver (guarda en archivo) y otra que guarde en memoria (por ejemplo 
almacenando el último reporte en un atributo o imprimiéndolo en pantalla simulando otra acción).
- Ajusta ReportGenerator.generate_report para usar la abstracción en lugar de la clase concreta.
- Muestra un ejemplo de uso creando un ReportGenerator con la implementación de archivo y otro con la de memoria, generando un reporte con cada uno.

'''
from abc import ABC, abstractmethod

# Abstracción
class Saver(ABC):
    @abstractmethod
    def save(data, nombre):
        pass

# Módulos de bajo nivel o Implementaciones concretas
class FileSaver(Saver):
    def __init__(self, filename):
        self.filename = filename
    def save(self, data):
        with open(self.filename, 'w') as f:
            f.write(data)
        print(f"Archivo guardado en {self.filename}.")

class MemorySaver(Saver):
    def __init__(self):
        self.last_data = None # Aqui almacenaremos el último dato guardado
    def save(self, data):
        self.last_data = data
        print(f"Datos guardados en memoria (atributo last_data)")

# Módulo de alto nivel
class ReportGenerator:
    def __init__(self, saver: Saver):
        self.saver = saver # Inyección de dependencia por constructor
    def generate_report(self, text):
        report = f"*** Reporte ***\n{text}\n**************"
        self.saver.save(report) # Usamos la abstracción Saver
        print("Reporte generado y guardado por Saver.")

# Usando FileSaver para guardar en disco
filesaver = FileSaver("report1.txt")
repgen1 = ReportGenerator(filesaver)
repgen1.generate_report("Guardamos en el archivo")

# Usando MemorySaver para guardar en memoria
memorysaver = MemorySaver()
repgen2 = ReportGenerator(memorysaver)
repgen2.generate_report("Guardamos en Memoria")
print("Último dato en memoria:", repgen2.saver.last_data)

'''
Explicación paso a paso:
- Crear la interfaz Saver: Usamos una clase abstracta Saver con un método save(self, data) que encapsula la acción de persistir datos de alguna forma. 
Esto es la abstracción que usará el código de alto nivel. Así, definimos el contrato: un Saver sabe guardar datos (sin especificar dónde).

- Implementar FileSaver concreto: Esta clase ahora implementa Saver. En lugar de save_to_file(data, filename), en su constructor tomamos filename una vez, 
y en el método save(data) escribimos a ese archivo. Notar que movimos el conocimiento del nombre de archivo al interior de FileSaver (podría haberse 
mantenido como parámetro de save, pero optamos por fijarlo en el init para simplificar el uso). Tras escribir, imprime un mensaje confirmando la ubicación.

- Implementar MemorySaver concreto: Como segunda implementación, MemorySaver también cumple Saver. Aquí decidimos simular un guardado "en memoria" 
simplemente almacenando los datos en un atributo last_data. En una situación real, esto podría ser un objeto que guarda en una estructura en memoria o 
base de datos en memoria. Imprimimos un mensaje para dejar constancia en este ejemplo.

- Modificar ReportGenerator: Ahora su __init__ espera un Saver. Guardamos esa referencia. Al generar el reporte, creamos la cadena formateada 
(añadiendo adornos "***"), y luego delegamos en self.saver.save(report). Nótese que ReportGenerator ya no sabe si eso lo guarda en un archivo, memoria u 
otro lado. Solo sabe que hay un objeto que tiene un método save y lo usa. Esto cumple DIP: ReportGenerator depende de la abstracción Saver, no de detalles 
(FileSaver).

- Inyección de dependencias en acción: En el uso, vemos cómo podemos crear diferentes configuraciones de ReportGenerator fácilmente. En gen1 inyectamos un 
FileSaver('reporte1.txt'), y en gen2 un MemorySaver(). Llamar generate_report en ambos funciona, guardando en destinos distintos. Importante: no modificamos
 ReportGenerator para lograr esto; solo cambiamos qué le inyectamos. Si en el futuro quisiéramos una variante que envíe el reporte por red, crearíamos otra 
 clase NetworkSaver que implemente Saver y la pasaríamos al constructor. ReportGenerator seguiría funcionando sin cambios.

- Verificación: Imprimimos gen2.saver.last_data para confirmar que efectivamente el reporte fue "guardado" en memoria. Vemos el contenido con el formato 
correcto. En un test unitario, podríamos hacer algo similar: usar MemorySaver o incluso un DummySaver que registre si fue llamado, para asegurarnos de que 
ReportGenerator invoca a save() apropiadamente. Esto antes era difícil porque ReportGenerator siempre usaba FileSaver interno. Ahora es muy sencillo gracias 
a la inversión de dependencias.

- Conclusión del ejercicio: Hemos separado la responsabilidad de guardar del generador de reportes. Cada pieza hace su trabajo y es intercambiable. 
ReportGenerator quedó más limpio y enfocado (responsabilidad única: formatear y delegar guardado). El diseño es extensible (nuevos Saver) y testeable. 
Así es como DIP mejora la arquitectura.
'''