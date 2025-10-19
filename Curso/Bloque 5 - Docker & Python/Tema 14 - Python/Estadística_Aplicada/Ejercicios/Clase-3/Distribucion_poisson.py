import numpy as np # librería para cálculos numéricos en Python, aqui usamos la suma y el cálculo de la media (mean)
import matplotlib.pyplot as plt # librería para crear gráficos en Python. Aquí se usa para graficar un histograma que muestra la distribución de neuronas desactivadas.
from scipy.stats import poisson # permite trabajar con la distribución de Poisson. Aquí se usa para simular el número de neuronas desactivadas en cada iteración.

# Distribución de Poisson:
# Modela el numero de eventos que pasan en un intervalo fijo de tiempo o espacio, bajo unas condiciones:
    # Eventos independientes: la ocurrencia de un evento no afecta a la probabilidad de ocurrencia de otro evento
    # Tasa de ocurrencia de eventos constante: la tasa promedio de eventos o lambda no cambia durante el intervalo considerado
    # Eventos ocurren de uno en uno: No ocurren simultáneamente

# 1. Simulación del proceso de dropout
# En una red neuronal, el dropout es una técnica que se utiliza para prevenir el sobreajuste.
# Consiste en desactivar aleatoriamente una fracción de neuronas durante el entrenamiento.
# En este caso suponemos que la probabilidad de que una neurona sea desactivada sigue una distribución de Poisson con una tasa de 0.5
# Aplicamos la distribución de Poisson a ésta simulación: nos permite saber cuantas neuronas se desactivan durante un numero fijo de iteraciones

# Parámetros
num_neuronas = 100 # número total de neuronas en la capa
lambda_poisson = 0.5 # representa la tasa promedio de eventos (en este caso, la probabilidad de que una neurona sea desactivada)
num_iteraciones = 1000 # número de iteraciones en las que se simulará el proceso de dropout

# Función para simular el proceso de dropout para una capa de neuronas usando distribución de Poisson
def simular_dropout(num_neuronas, lambda_poisson): # Nos da un array de 100 neuronas y nos dice si cada neurona está activada o desactivada
    return poisson.rvs(mu=lambda_poisson, size=num_neuronas)
    # size=num_neuronas: Genera un número aleatorio de eventos (neuronas desactivadas) para cada una de las 100 neuronas.
    # Esta función se llama para cada una de las 100 neuronas, y así determinamos cuántas de ellas se desactivan en cada iteración.

# Simular el dropout en 1000 iteraciones
neurons_off_counts = [] # Es una lista que almacenará el número total de neuronas desactivadas en cada iteración.

for _ in range(num_iteraciones): # Bucle de 1000 iteraciones y en cada iteración miramos cuantas neuronas estan desactivadas (randomly se desactivan)
    dropout_mask = simular_dropout(num_neuronas, lambda_poisson) # Nos da un arreglo donde cada valor indica si una neurona fue desactivada o no
    num_neurons_off = np.sum(dropout_mask) # Suma los valores del arreglo para obtener cuántas neuronas están desactivadas en ésta iteración
    neurons_off_counts.append(num_neurons_off) # agregamos el numero de neuronas desactivadas a la lista

# 2. Calcular y mostrar el número medio de neuronas desactivadas
mean_neurons_off = np.mean(neurons_off_counts)
print(f'Número medio de neuronas desactivadas en {num_iteraciones} iteraciones: {mean_neurons_off:.2f}')

# 3. Graficar la distribución de neuronas desactivadas
plt.hist(neurons_off_counts, bins=30, density=True, alpha=0.6, color='g', edgecolor='black')
plt.title('Distribución de Neuronas Desactivadas en 1000 Iteraciones')
plt.xlabel('Número de Neuronas Desactivadas') # El eje X muestra los posibles valores del número de neuronas desactivadas (por ejemplo, 45, 50, 55, etc.).
plt.ylabel('Frecuencia') # El eje Y muestra qué tan común es cada valor (o rango de valores) en las 1000 iteraciones.
plt.show()

# plt.hist(): Crea un histograma que muestra la distribución de neuronas desactivadas en las 1000 iteraciones.
    # neurons_off_counts: Datos a graficar (número de neuronas desactivadas en cada iteración).
    # bins=30: Divide los datos en 30 intervalos.
    # density=True: Normaliza el histograma para que las frecuencias sumen 1. Esto significa que la altura de cada barra no representa 
    # el número absoluto de iteraciones, sino la proporción relativa de iteraciones en las que el número de neuronas desactivadas cae 
    # dentro de ese intervalo.
    # alpha=0.6: Ajusta la transparencia del color.
    # color='g': Define el color de las barras (verde).
    # edgecolor='black': Agrega bordes negros a las barras.
# plt.title(): Agrega un título al gráfico.
# plt.xlabel() y plt.ylabel(): Etiquetan los ejes X e Y.
# plt.show(): Muestra el gráfico.