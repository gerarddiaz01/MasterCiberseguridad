import numpy as np
import matplotlib.pyplot as plt

''' Error estándar:
Mide la variabilidad de las medias muestrales respecto a la media poblacional.
Ley de los grandes números:
A medida que aumenta el tamaño de la muestra, la media de las muestras se aproxima a la media poblacional.
'''


# Crear una población con distribución normal (media=50, desviación estándar=10)
np.random.seed(42) # Fija la semilla para la generación de números aleatorios. Cada vez que se reproduce el script son los mismos numeros random.
poblacion = np.random.normal(50, 10, 10000) # Genera un array con 10.000 numeros aleatorios que representan la población (con distribución normal).
    # loc = 50: Media de la distribución.
    # scale = 10: Desviación estándar de la distribución.
    # size = 10000: Número de elementos en la población.

# Calcular la media real de la población
media_poblacion = np.mean(poblacion)
print(f"Media de la población: {media_poblacion:.2f}")




#TOMAMOS MUESTRAS DE LA POBLACIÓN

# Tamaño de la muestra
tamaño_muestra = 50 #PROBAR A BAJAR EL VALOR

# Número de muestras
num_muestras = 100 #DISMINUIR EL NUMERO DE MUESTRAS

# Calcular las medias de las muestras
medias_muestras = [np.mean(np.random.choice(poblacion, tamaño_muestra, replace=False)) for _ in range(num_muestras)]
    # np.mean(...): Calcula la media de los elementos seleccionados en cada muestra.
    # np.random.choice(array, size, replace): Selecciona aleatoriamente elementos de un arreglo.
    # Parámetros:
        #array=poblacion: Selecciona elementos de la población.
        #size=tamaño_muestra: Selecciona tamaño_muestra elementos.
        #replace=False: Los elementos no se pueden repetir en la misma muestra.
    # for _ in range(num_muestras): Genera una lista de medias, calculando una media para cada una de las num_muestras muestras.

# Calcular la media de las medias de las muestras
media_muestras = np.mean(medias_muestras)
print(f"Media de las medias de las muestras: {media_muestras:.2f}")

exit()

#CALCULO EL ERROR ESTANDAR DE LAS MUESTRAS

# Calcular la desviación estándar de las medias de las muestras (error estándar de la media)
error_estandar = np.std(medias_muestras, ddof=1)
    # Calcula la desviación estándar del arreglo array.
    # ddof=1: Ajusta los grados de libertad para calcular la desviación estándar muestral.
    # error_estandar: Representa el error estándar de la media, que mide la variabilidad de las medias de las muestras.

print(f"Error estándar de la media: {error_estandar:.2f}")


#GRAFICO LOS RESULTADOS

# Graficar la distribución de las medias de las muestras
plt.figure(figsize=(10, 6))
plt.hist(medias_muestras, bins=30, edgecolor='k', alpha=0.7)
plt.axvline(media_poblacion, color='red', linestyle='dashed', linewidth=2, label='Media Poblacional')
plt.axvline(media_muestras, color='blue', linestyle='dashed', linewidth=2, label='Media de las Muestras')
plt.title('Distribución de las Medias de las Muestras')
plt.xlabel('Media de las Muestras')
plt.ylabel('Frecuencia')
plt.legend()
plt.grid(True)
plt.show()

# plt.figure(figsize=(10, 6)):
    # Crea una nueva figura para el gráfico.
    # figsize=(10, 6):
        # Define el tamaño de la figura (10 pulgadas de ancho por 6 pulgadas de alto).

# plt.hist(medias_muestras, bins=30, edgecolor='k', alpha=0.7):
    # Crea un histograma de las medias de las muestras.
    # Parámetros:
        # medias_muestras: Datos a graficar.
        # bins=30: Divide los datos en 30 intervalos.
        # edgecolor='k': Define el color de los bordes de las barras (negro).
        # alpha=0.7: Ajusta la transparencia de las barras.
# plt.axvline(media_poblacion, color='red', linestyle='dashed', linewidth=2, label='Media Poblacional'):
    # Dibuja una línea vertical en la media de la población.
        # Parámetros:
            # color='red': Color de la línea (rojo).
            # linestyle='dashed': Estilo de la línea (discontinua).
            # linewidth=2: Grosor de la línea.
            # label='Media Poblacional': Etiqueta para la leyenda.

# plt.axvline(media_muestras, color='blue', linestyle='dashed', linewidth=2, label='Media de las Muestras'):
    # Dibuja una línea vertical en la media de las medias de las muestras.
    # Parámetros similares a la línea anterior, pero con color azul.

# plt.title('Distribución de las Medias de las Muestras'): Agrega un título al gráfico.

# plt.xlabel('Media de las Muestras'): Etiqueta el eje X.

# plt.ylabel('Frecuencia'): Etiqueta el eje Y.

# plt.legend(): Muestra la leyenda con las etiquetas definidas en las líneas verticales.

# plt.grid(True): Activa una cuadrícula en el fondo del gráfico.

# plt.show(): Muestra el gráfico.