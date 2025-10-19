""" Ejercicio de Memoización en Análisis de Texto
Imagina que estás trabajando en un sistema de análisis de texto que requiere calcular la frecuencia de 
ocurrencia de palabras en un conjunto de documentos. Implementa una función llamada calcular_frecuencia_palabras 
que tome como entrada un texto y devuelva un diccionario que muestre la frecuencia de cada palabra en el texto.
La función debe ser capaz de manejar textos y ser insensible a mayúsculas/minúsculas (por ejemplo, "Hola" y "hola" 
se consideran la misma palabra).
Se deben excluir las palabras comunes (artículos, preposiciones, etc.) que no aportan información relevante al análisis.
Utiliza memoización para evitar recalcular la frecuencia de palabras para el mismo texto y muestra el tiempo de ejecución 
con o sin memoización."""

import functools
import time
import string

# Lista de palabras comunes
palabras_comunes = set(["el", "la", "los", "las", "de", "en", "y", "a", "con", "es", "un", "una", "para"])

# Función para calcular la frecuencia de palabras con memoización
@functools.lru_cache(maxsize=None)
def calcular_frecuencia_palabras(texto):
    # Convertir el texto a minúsculas
    texto = texto.lower()

    # Eliminar puntuación usando string.punctuation
    texto = texto.translate(str.maketrans("", "", string.punctuation))

    # Dividir el texto en palabras
    palabras = texto.split()

    # Excluir palabras comunes
    palabras_filtradas = [palabra for palabra in palabras if palabra not in palabras_comunes]

    # Calcular la frecuencia de palabras
    # Obtenemos el valor de la llave palabra usando get, que sera 0 sino existe y se incrementa con cada encuentro de dicha llave
    frecuencia = {}
    for palabra in palabras_filtradas: # Busca la palabra en el diccionario frecuencia. Si no existe, devuelve 0 como valor
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1 # Incrementa el contador de la palabra en 1
    return frecuencia

# Función para medir el tiempo de ejecución
def medir_tiempo(func, *args):
    inicio = time.time() # Marca el tiempo inicial
    resultado = func(*args) # Llama a la función `func` con los argumentos `*args`
    final = time.time() # Marca el tiempo final
    tiempo = final - inicio # Calcula el tiempo transcurrido
    return resultado, tiempo # Devuelve el resultado de la función y el tiempo transcurrido

# Texto de entrada
texto_1 = """
En un lugar de la Mancha, de cuyo nombre no quiero acordarme,
no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero,
adarga antigua, rocín flaco y galgo corredor.
Una olla de algo más vaca que carnero, salpicón las más noches,
duelos y quebrantos los sábados, lentejas los viernes,
algún palomino de añadidura los domingos, consumían las tres partes de su hacienda.
El resto della concluían sayo de velarte, calzas de velludo para las fiestas con sus pantuflos de lo mismo,
los días de entre semana se honraba con su vellorí de lo más fino.
Tenía en su casa una ama que pasaba de los cuarenta y una sobrina que no llegaba a los veinte,
y un mozo de campo y plaza que así ensillaba el rocín como tomaba la podadera.
Frisaba la edad de nuestro hidalgo con los cincuenta años; era de complexión recia, seco de carnes,
enjuto de rostro, gran madrugador y amigo de la caza.
Quieren decir que tenía el sobrenombre de Quijada o Quesada (que en esto hay alguna diferencia en los autores que deste caso escriben),
aunque por conjeturas verosímiles se deja entender que se llama Quijana;
pero esto importa poco a nuestro cuento: basta que en la narración dél no se salga un punto de la verdad.
"""

# Función principal
def main():
    # Calcular frecuencia sin memoización
    calcular_frecuencia_palabras.cache_clear()  # Limpiar el caché
    resultado_sin_memo, tiempo_sin_memo = medir_tiempo(calcular_frecuencia_palabras, texto_1) # Asignación múltiple

    # Calcular frecuencia con memoización
    resultado_con_memo, tiempo_con_memo = medir_tiempo(calcular_frecuencia_palabras, texto_1) # Asignación múltiple

    # Imprimir resultados
    print("\nFrecuencia de palabras (sin memoización):")
    print(resultado_sin_memo)
    print(f"Tiempo sin memoización: {tiempo_sin_memo:.6f} segundos")

    print("\nFrecuencia de palabras (con memoización):")
    print(resultado_con_memo)
    print(f"Tiempo con memoización: {tiempo_con_memo:.6f} segundos")

    # Comparar tiempos
    tiempo_ganado = tiempo_sin_memo - tiempo_con_memo
    print(f"\nTiempo ganado con memoización: {tiempo_ganado:.6f} segundos")

if __name__ == "__main__":
    main()