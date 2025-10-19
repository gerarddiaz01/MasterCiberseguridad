def contar_palabras(filename):
    """
    Cuenta el número de palabras y líneas en un archivo de texto.
    
    :param filename: Nombre del archivo a leer.
    :return: Tupla con el número de palabras y líneas.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
        
    except FileNotFoundError:
        print(f"Error: El archivo {filename} no se encontró.") # podemos poner un except silencioso con pass y no aparecerá un mensaje de error
    
    else:
        word_count = len(content.split()) # .split sirve para dividir el documento por los espacios, así que será palabra a palabra
        line_count = len(content.splitlines()) # .splitlines divide el documento en líneas y con len contamos cuántas hay
        return print(f"El archivo {filename} tiene {word_count} palabras y {line_count} lineas.")

filenames = ["texto1.txt", "texto2.txt", "mobydick.txt", "texto4.txt"] # Lista de archivos a procesar, mobydick.txtno existe, veremos como manejamos la excepción

for filename in filenames:
    print(f"Contando palabras en {filename}:")
    contar_palabras(filename)
    print("-" * 40) # ésta línea sirve para separar los resultados de cada archivo

# Explicación del script paso a paso:
# 1. Definimos una función llamada contar_palabras que toma un nombre de archivo como argumento.
# 2. Dentro de la función, intentamos abrir el archivo en modo lectura ('r') utilizando un bloque try.
# 3. Si el archivo se abre correctamente, leemos su contenido y lo almacenamos en la variable content.
# 4. Si el archivo no se encuentra, se lanza una excepción FileNotFoundError y se imprime un mensaje de error.
# 5. Si no hay excepciones, contamos el número de palabras y líneas en el contenido del archivo.
# 6. La función devuelve el conteo de palabras y líneas en el archivo.
# 7. Creamos una lista de nombres de archivos para procesar.
# 8. Iteramos sobre cada nombre de archivo en la lista y llamamos a la función contar_palabras para cada uno.
# 9. Imprimimos una línea de separación entre los resultados de cada archivo.
# 10. El script cuenta el número de palabras y líneas en varios archivos de texto y maneja excepciones si alguno de los archivos no se encuentra.
# 11. La función contar_palabras se puede reutilizar para contar palabras en diferentes archivos de texto.
# 12. La función utiliza bloques try, except y else para manejar excepciones y separar el código de manejo de errores del código normal.
# 13. El bloque finally no se utiliza en este caso, pero se podría agregar si se desea ejecutar código adicional al final, independientemente de si hubo excepciones o no.
# 14. El script es útil para analizar archivos de texto y obtener estadísticas sobre su contenido.
# 15. Se puede ampliar para incluir más estadísticas, como el número de caracteres o la longitud promedio de las palabras.
# 16. El script es un ejemplo de cómo manejar excepciones y realizar operaciones de archivo en Python.
# 17. Se puede adaptar para trabajar con diferentes tipos de archivos o formatos de datos.