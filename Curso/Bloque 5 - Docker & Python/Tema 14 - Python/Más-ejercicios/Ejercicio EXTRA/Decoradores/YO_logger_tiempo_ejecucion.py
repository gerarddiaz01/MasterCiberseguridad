'''Logger con Tiempo de Ejecución
Imagina que estás desarrollando un sistema complejo que incluye múltiples
funciones críticas. Para asegurarte de que todo funcione correctamente y para
realizar un seguimiento del tiempo de ejecución de estas funciones, decides
implementar un decorador de registro (logger) con tiempo de ejecución.
El decorador debería realizar las siguientes acciones:
1. Antes de llamar a la función original (puedes incluir cualquier función),
debe imprimir un mensaje indicando que la función está a punto de
ejecutarse.
2. Después de que la función se haya ejecutado, debe imprimir un mensaje
que incluya el tiempo que tardó la función en ejecutarse.
3. Si la función original arroja una excepción, el decorador debe manejarla e
imprimir un mensaje adecuado, indicando que se ha producido una
excepción.
'''

import time

def logger_con_tiempo(func):
    def wrapper(*args, **kwargs):
        print(f"[INFO] A punto de ejecutar '{func.__name__}'...")
        start_time = time.time()
        
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print(f"[ERROR] Se produjo una excepción en '{func.__name__}': {e}")
            return None
        else:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"[INFO] '{func.__name__}' ejecutada en {elapsed_time:.4f} segundos.")
            return result
        
    return wrapper

@logger_con_tiempo
def mi_funcion(x, y):
    time.sleep(2)  # Simula una operación que tarda 2 segundos
    return x + y

resultado = mi_funcion(5, 10)
print(f"Resultado: {resultado}")