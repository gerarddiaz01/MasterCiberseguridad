archivos = ["texto1.txt", "texto2.txt", "inexistente.txt", "texto3.txt", "texto4.txt"]
total_palabras = 0 # inicializamos el total de palabras a 0, para que no de error al sumar
total_lineas = 0 # inicializamos el total de lineas a 0, para que no de error al sumar

# Creamos un bucle for para recorrer la lista de archivos, almacenando el numero de palabras y lineas de cada uno en cada iteración
# y luego imprimiendo el resultado de cada archivo, y al final imprimiendo el total de palabras y lineas procesadas
for nombre in archivos:
    try:
        with open(nombre, "r", encoding="utf-8") as f:
            contenido = f.read()
    except FileNotFoundError:
        print(f"Avertencia: el archivo {nombre} no fue encontrado. Se omitirá éste archivo.")
        continue # pasa al siguiente archivo en la lista, porqué si no existe el archivo, no se puede contar nada, así que no tiene sentido seguir con el resto del código
    except Exception as e:
        print(f"No se pudo procesar {nombre} debido a un error inesperado: {e}")
        continue
    # Si llegamos aqui, la lectura fue exitosa
    palabras = contenido.split() # separa por espacios
    lineas = contenido.splitlines() # separa por líneas
    num_palabras = len(palabras)
    num_lineas = len(lineas)
    print(f"{nombre}: {num_palabras} palabras, {num_lineas} lineas")
    total_palabras += num_palabras # almacenamos el número de palabras en la variable total_palabras para cada archivo
    total_lineas += num_lineas # almacenamos el número de lineas en la variable total_lineas para cada archivo

print(f"\nTotal de palabras procesadas: {total_palabras}")
print(f"Total de lineas procesadas: {total_lineas}")