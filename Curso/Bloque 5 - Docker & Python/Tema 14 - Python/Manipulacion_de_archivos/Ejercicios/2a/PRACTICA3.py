'''Enunciado: Crea un programa que le pida al usuario el nombre de un archivo de texto a abrir. 
Intenta abrir el archivo y leer su contenido. Si el archivo no existe (FileNotFoundError), 
el programa debe informar al usuario y darle otra oportunidad de ingresar un nombre de archivo, en lugar de terminar con error. 
Si el archivo se abre correctamente, muestra en pantalla la primera línea del archivo (o todo su contenido, como prefieras) y termina.'''

# Ésta función es la correción del ejercicio, aunque ya era correcto cómo lo he hecho abajo sin función
# es para ver otra manera de hacerlo, usando .readlines(), continue y .strip()
def correccion_gpt():
    while True:
        nombre = input("Ingrese el nombre del archivo a abrir: ")
        try:
            with open(nombre, "r", encoding="utf-8") as archivo:
                contenido = archivo.readlines()
            # Si llego aquí, se abrió y leyó el archivo correctamente
        except FileNotFoundError:
            print(f"El archivo {nombre} no existe. Por favor, ingrese un nombre de archivo válido.")
            continue # Vuelve al comienzo del while para pedir el nombre del archivo otra vez, no pasará de aquí hasta que el open() funcione
        except Exception as e: # Captura cualquier otro error inesperado de manera genérica
            print(f"Error inesperado: {e}. Por favor, intente de nuevo.")
            continue
        # Si no hubo excepciones, salimos del bucle
        break # rompemos el bucle while, ya que el archivo se abrió correctamente

    # Ahora "contenido" contiene todas las líneas del archivo leído
    if contenido: # Verificamos si el archivo no está vacío
        print("El contenido de la primera línea del archivo seleccionado es:")
        print(contenido[0].strip()) # .strip() elimina los espacios en blanco al principio y al final de la línea
    else:
        print("El archivo está vacío. No hay contenido para mostrar.")

# Mi versión empieza aquí, es más simple y no usa funciones, pero es correcto también
while True: #bucle infinito
    archivo = input("Ingrese el nombre del archivo a abrir: ")
    try:
        with open(archivo, "r") as file:
            content = file.read()
        break
    except FileNotFoundError:
        print(f"El archivo no existe, porfavor ingrese el nombre de un archivo válido.")

primera_linea = content.splitlines()[0]

print("El contenido de la primera linea del archivo seleccionado es...")
print("")
print(primera_linea)
