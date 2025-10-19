def procesar_archivo(nombre):
    """
    Procesa un archivo de texto y cuenta el número de palabras y líneas.
    param nombre: Nombre del archivo a procesar.
    return: Tupla con el número de palabras y líneas.
    """
    try:
        with open(nombre, "r", encoding="utf-8") as f: # encoding="utf-8" para evitar problemas con caracteres especiales
            contenido = f.read()
        palabras = contenido.split()
        lineas = contenido.splitlines()
        return len(palabras), len(lineas)
    except FileNotFoundError:
        print(f"Avertencia: el archivo {nombre} no fue encontrado. Se omitirá este archivo.")
        return 0, 0
    except PermissionError:
        print(f"Error: No tienes permisos para leer el archivo {nombre}.")
        return 0, 0
    except Exception as e: # Captura cualquier otro error inesperado
        print(f"No se pudo procesar {nombre} debido a un error inesperado: {e}")
        return 0, 0
# La función procesar_archivo() recibe el nombre de un archivo, intenta abrirlo y leer su contenido.
# Si el archivo se abre correctamente, cuenta el número de palabras y líneas y devuelve estos valores.
# Si el archivo no se encuentra o hay un error al abrirlo, maneja la excepción y devuelve 0 para ambos conteos.

def main():
    """
    Función principal que define la lista de archivos a procesar y llama a la función procesar_archivo().
    """
    archivos = ["texto1.txt", "texto2.txt", "inexistente.txt", "texto3.txt", "texto4.txt"]
    total_palabras = 0
    total_lineas = 0

    if not archivos: # Verifica si la lista de archivos está vacía
        print("No hay archivos para procesar.")
        return

    for nombre in archivos:  # Recorre la lista de archivos aplicando la función procesar_archivo()
        num_palabras, num_lineas = procesar_archivo(nombre)
        print(f"{nombre:<20} {num_palabras:>10} palabras, {num_lineas:>10} líneas")
        total_palabras += num_palabras # Almacena el número de palabras en la variable total_palabras para cada archivo
        total_lineas += num_lineas

    print(f"\nTotal de palabras procesadas: {total_palabras}")
    print(f"Total de líneas procesadas: {total_lineas}")
# La función main() es el punto de entrada del programa.
# Se encarga de definir la lista de archivos a procesar, inicializar los contadores de palabras y líneas,
# y llamar a la función procesar_archivo() para cada archivo en la lista.
# También imprime el resultado de cada archivo y el total al final.

if __name__ == "__main__":
    main()
# Convención en Python que permite que un archivo se ejecute como un script independiente 
# o se importe como un módulo sin ejecutar el código de la sección principal.
