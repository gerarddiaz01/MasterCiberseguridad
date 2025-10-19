'''Decorador de Control de Acceso:

Imagina que estás trabajando en el desarrollo de un sistema para una aplicación de gestión de documentos 
en un entorno empresarial.Deseas implementar un decorador llamado verificar_acceso_entorno que permita 
controlar el acceso a funciones según el entorno de ejecución.
El decorador debe realizar las siguientes acciones:
Antes de ejecutar la función, verificar si el entorno de ejecución es "producción".
Si el entorno es "producción", permitir la ejecución de la función y mostrar un mensaje indicando que 
el acceso fue permitido en el entorno de producción.Si el entorno no es "producción", evitar la ejecución 
de la función y mostrar un mensaje indicando que el acceso está restringido a entornos de producción.
Luego, aplica este decorador a dos funciones: subir_documento y eliminar_documento.
Intenta ejecutar estas funciones con diferentes entornos y observa el comportamiento del decorador.'''

def verificar_acceso_entorno(func):
    def wrapper(*args, **kwargs):
        if entorno == 'produccion':
            print(f"[ACCESO PERMITIDO] Ejecutando '{func.__name__}' en entorno de producción.")
            return func(*args, **kwargs)
        else:
            print(f"[ACCESO RESTRINGIDO] '{func.__name__}' solo puede ejecutarse en entorno de producción.")
    return wrapper

@verificar_acceso_entorno
def subir_documento(nombre):
    print(f"Documento '{nombre}' subido exitosamente.")

@verificar_acceso_entorno
def eliminar_documento(nombre):
    print(f"Documento '{nombre}' eliminado exitosamente.")

# Caso 1: Producción
entorno = 'produccion'
subir_documento("Documento1")
eliminar_documento("Documento1")

print("\n---\n")

# Caso 2: Desarrollo
entorno = 'desarrollo'
subir_documento("Documento2")
eliminar_documento("Documento2")
