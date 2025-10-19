'''Encuentra o crea algunos textos que te gustaría analizar (puedes visitar
Project Gutenberg (http://gutenberg.org/) o crear textos usando ChatGPT).
Copia el texto sin formato desde tu navegador en un archivo de texto en tu
computadora (o descarga los archivos). Averigua cuántas veces aparece una
palabra o frase en el texto (puedes usar el método count())'''

# Definimos una función para contar cuántas veces aparece una palabra en un archivo de texto
def contar_palabras(file, palabra):
    # Abrimos el archivo en modo lectura ("r")
    # El modo "r" permite leer el contenido del archivo, pero no modificarlo
    with open(file, "r") as file:
        # Leemos todo el contenido del archivo como una cadena de texto
        content = file.read()
        # Usamos el método count() para contar cuántas veces aparece la palabra en el texto
        recuento = content.count(palabra)
    # Devolvemos el número de veces que aparece la palabra
    return recuento

# Nombre del archivo que queremos analizar
archivo1 = "texto1.txt"

# Palabra que queremos buscar en el archivo
word = "curiosidad"

# Llamamos a la función contar_palabras y guardamos el resultado en la variable recuento
# Esto nos dice cuántas veces aparece la palabra en el archivo
recuento = contar_palabras(archivo1, word)

# Imprimimos el resultado en la consola
# Mostramos cuántas veces aparece la palabra en el archivo
print(f"La palabra '{word}' aparece {recuento} veces en {archivo1}.")