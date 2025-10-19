'''Crea dos archivos, cats.txt y dogs.txt. Almacena al menos tres nombres de
gatos en el primer archivo y tres nombres de perros en el segundo archivo.
Escribe un programa que intente leer estos archivos e imprima el contenido
de cada archivo en la pantalla. Envuelve tu código en un bloque try-except
para capturar el error de FileNotFoundError, e imprime un mensaje amigable
si falta algún archivo. Mueve uno de los archivos a una ubicación diferente
en tu sistema y asegúrate de que el código en el bloque except se ejecute
correctamente. Modifica tu bloque except para que falle en silencio si falta
alguno de los archivos'''

# Crear el archivo "cats1.txt" en modo escritura ("w")
# El modo "w" (write) crea un archivo nuevo si no existe o sobrescribe el contenido si ya existe.
# Esto significa que si el archivo ya tiene contenido, este será eliminado.
with open("cats1.txt", "w") as file1:
    # Escribimos tres nombres de gatos en el archivo
    file1.write("Gato1\nGato2\nGato3\n")

# Crear el archivo "dogs1.txt" en modo escritura ("w")
# Al igual que con "cats1.txt", el modo "w" sobrescribirá el archivo si ya existe.
with open("dogs1.txt", "w") as file2:
    # Escribimos tres nombres de perros en el archivo
    file2.write("Perro1\nPerro2\nPerro3\n")

# Definimos los nombres de los archivos que queremos leer
archivo1 = "cats1.txt"  # Archivo que contiene nombres de gatos
archivo2 = "dogs2.txt"  # Archivo que contiene nombres de perros

# Intentamos abrir y leer el archivo "cats.txt"
try:
    # Abrimos el archivo en modo lectura ("r")
    with open(archivo1, "r") as file1:
        # Leemos todo el contenido del archivo
        content_file1 = file1.read()
        # Imprimimos el contenido del archivo en la consola
        print(content_file1)
except FileNotFoundError:
    # Si el archivo no se encuentra, mostramos un mensaje amigable
    print(f"El archivo {archivo1} no se encontró.")

# Separador visual para diferenciar el contenido de los archivos
print("-" * 30)

# Intentamos abrir y leer el archivo "dogs.txt"
try:
    # Abrimos el archivo en modo lectura ("r")
    with open(archivo2, "r") as file2:
        # Leemos todo el contenido del archivo
        content_file2 = file2.read()
        # Imprimimos el contenido del archivo en la consola
        print(content_file2)
except FileNotFoundError:
    # Si el archivo no se encuentra, fallamos en silencio (no hacemos nada)
    pass
    # Si quisieras mostrar un mensaje, puedes descomentar la línea siguiente:
    # print(f"El archivo {archivo2} no se encontró.")
