'''Escribe un programa que solicite al usuario su número favorito. Utiliza
json.dump() para almacenar este número en un archivo. Escribe un
programa separado que lea este valor e imprima el mensaje: "Sé cuál es tu
número favorito… Es ____.” Combina ambos programas en un solo archivo
(puedes crear tantas funciones como necesites). Si el número ya está
almacenado, muestra el número favorito al usuario. Si no lo está, solicita al
usuario su número favorito y guárdalo en un archivo. Ejecuta el programa al
menos dos veces para asegurarte de que funciona correctamente'''

import json, os  # Importamos json para manejar archivos JSON y os para verificar la existencia de archivos

# Función para guardar un nuevo número favorito en un archivo JSON
def nuevo_numero_favorito():
    # Solicitamos al usuario que ingrese su número favorito
    numero = int(input("Ingrese su numero favorito: "))
    
    # Creamos un diccionario para almacenar el número favorito
    info = {
        "numero favorito": numero  # Clave: "numero favorito", Valor: el número ingresado por el usuario
    }
    
    # Abrimos (o creamos) el archivo "info.json" en modo escritura ("w")
    # Es importante poner "info.json" entre comillas porque es una cadena de texto que representa el nombre del archivo.
    # Si no lo ponemos entre comillas, Python intentará interpretar `info.json` como una variable, lo que generará un error.
    with open("info.json", "w") as file:
        # Usamos json.dump() para guardar el diccionario en el archivo JSON con formato legible (indentación de 4 espacios)
        json.dump(info, file, indent=4)
    
    # Informamos al usuario que la información se ha guardado correctamente
    print("Información guardada en info.json")

# Función para leer el número favorito desde el archivo JSON
def leer_numero_favorito():
    # Abrimos el archivo "info.json" en modo lectura ("r")
    # Aquí también usamos "info.json" entre comillas porque es el nombre del archivo que queremos abrir.
    with open("info.json", "r") as file:
        # Usamos json.load() para cargar el contenido del archivo JSON en un diccionario
        info_loaded = json.load(file)
    
    # Mostramos al usuario el número favorito almacenado en el archivo
    print(f"Sé cuál es tu número favorito, es {info_loaded['numero favorito']}.")
    ''' Puedes añadir en ésta función un try-except para manejar el FileNotFound error
    en lugar de hacer el if else con os.path.exists() '''

# Verificamos si el archivo "info.json" existe usando os.path.exists
# os.path.exists("info.json") devuelve True si el archivo existe, y False si no existe.
if os.path.exists("info.json"):
    # Si el archivo existe, llamamos a la función leer_numero_favorito para mostrar el número favorito al usuario
    leer_numero_favorito()
else:
    # Si el archivo no existe, llamamos a la función nuevo_numero_favorito para solicitar y guardar un nuevo número
    nuevo_numero_favorito()