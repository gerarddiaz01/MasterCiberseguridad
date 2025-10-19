filename = "texto1.txt"

import os
print(os.getcwd())  # Muestra el directorio actual

try:
    with open(filename, 'r') as file:
        content = file.read()

except FileNotFoundError:
        print(f"Error: El archivo {filename} no se encontró.")
    
else:
     # Cuenta las palabras y las lineas del archivo
    word_count = len(content.split()) # .split me divide el documento por los espacios asi que será palabra a palabra
    line_count = len(content.splitlines())
    print(f"El archivo {filename} tiene {word_count} palabras y {line_count} lineas.")

finally:
    print("Fin del programa.")

# El programa cuenta el número de palabras y líneas en un archivo de texto.
# Si el archivo no se encuentra, se maneja la excepción y se imprime un mensaje de error.
# Al final, se imprime un mensaje indicando que el programa ha terminado.

# Explicación del "else":
# El bloque "else" se ejecuta si no se produce ninguna excepción en el bloque "try".
# Es útil para separar el código que maneja errores del código que se ejecuta normalmente.

# La sintaxis es la siguiente:
# try:
#     # Código que puede causar una excepción
# except ExceptionType:
#     # Manejo de la excepción
# else:
#     # Código que se ejecuta si no hay excepciones
# finally:
#     # Código que se ejecuta siempre, independientemente de si hubo excepciones o no
# En este caso, el bloque "else" se utiliza para contar las palabras y líneas del archivo solo si se abre correctamente.
# El bloque "finally" se ejecuta siempre, independientemente de si hubo excepciones o no.
# En este caso, se utiliza para imprimir un mensaje de finalización del programa.
# El bloque "try" contiene el código que intenta abrir y leer el archivo.
# Si se produce una excepción (como un archivo no encontrado), el bloque "except" maneja el error.
# Si no hay excepciones, el bloque "else" cuenta las palabras y líneas del archivo.
# Finalmente, el bloque "finally" imprime un mensaje de finalización del programa.



