'''Veamos ahora un ejemplo integral para aplicar todo lo anterior. Supongamos que queremos hacer un pequeño analizador de textos: 
nuestro programa va a leer varios archivos de texto y contar cuántas palabras tiene cada uno, y al final dar un total de palabras procesadas. 
Este escenario nos permitirá ver manejo de excepciones con archivos (por si algún archivo no existe) y la decisión de reportar o no ciertos errores al usuario.
Imaginemos que tenemos una lista de nombres de archivos de texto (podrían ser archivos de libros obtenidos de Project Gutenberg u otra fuente). 
Algunos archivos pueden existir y otros no, para simular distintos casos. Queremos que el programa procese todos los archivos que pueda y no se detenga si uno falla.'''

filenames = "texto1.txt", "texto2.txt", "mobydick.txt", "texto4.txt"


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
        print(f"Error: El archivo {filename} no se encontró.")

    else:
        word_count = len(content.split())
        line_count = len(content.splitlines())
        return print(f"El archivo {filename} tiene {word_count} palabras y {line_count} lineas.")

for filename in filenames:
    print(f"Contando palabras en {filename}:")
    contar_palabras(filename)
    print("." * 40)


