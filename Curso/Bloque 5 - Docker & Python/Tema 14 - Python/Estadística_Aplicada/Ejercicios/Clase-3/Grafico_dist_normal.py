import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Parámetros de la distribución normal
mu = 170  # Media
sigma = 12  # Desviación estándar

# Definir los límites del intervalo
x1 = 189  # Límite inferior del intervalo
x2 = 190  # Límite superior del intervalo

# Calcular la probabilidad P(x1 < X < x2) donde X ~ N(mu, sigma)
prob = stats.norm.cdf(x2, mu, sigma) - stats.norm.cdf(x1, mu, sigma)

# Imprimir el resultado
print(f"La probabilidad de que un alumno mida entre {x1} cm y {x2} cm es aproximadamente {prob*100:.4f} %")

# Crear un rango de valores para X
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)  # Valores entre [mu - 4*sigma, mu + 4*sigma]
y = stats.norm.pdf(x, mu, sigma)  # Función de densidad de probabilidad (PDF)

# Crear el gráfico
plt.figure(figsize=(10, 6)) # Crea una nueva figura en el grafico, (figsize = width, height) en pulgadas
sns.lineplot(x=x, y=y, color='blue', label='Distribución Normal')  # Curva de Gauss
plt.fill_between(x, y, where=(x >= x1) & (x <= x2), color='orange', alpha=0.5, label=f'Área entre {x1} y {x2}')  # Resaltar el área bajo la curva
plt.title('Distribución Normal (Campana de Gauss)', fontsize=16) # Titulo descriptivo del grafico
plt.xlabel('Altura (cm)', fontsize=12) # Etiqueta del eje X
plt.ylabel('Densidad de Probabilidad', fontsize=12) # Etiqueta del eje Y
plt.axvline(mu, color='red', linestyle='--', label=f'Media ({mu} cm)')  # Línea vertical en la media
plt.legend() # Añade una leyenda para identificar los elementos del gráfico
plt.grid(alpha=0.3) # Activa una cuadrícula en el fondo del gráfico, con alpha definimos la transparencia de las líneas del grid
plt.show()

''' Explicación del codigo:
stats.norm.cdf(x2, mu, sigma) - stats.norm.cdf(x1, mu, sigma)
    cdf significa "Cumulative Distribution Function", o Función de Distribución Acumulada: Calcula la probabilidad acumulada de que un 
    valor aleatorio (X) de una distribución normal con media (\mu) y desviación estándar sea menor o igual a (x).
    En este caso:
        stats.norm.cdf(x2, mu, sigma) calcula la probabilidad acumulada hasta (x2 = 190).
        stats.norm.cdf(x1, mu, sigma) calcula la probabilidad acumulada hasta (x1 = 189).
    Se hace la resta de las probabilidades: la diferencia entre estas dos probabilidades da la probabilidad de que (X) esté entre (x1) y (x2).

x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000):
    np.linspace(start, stop, num): Genera un array de num(1000) valores equidistantes entre start(\mu - 4\sigma) y stop(\mu + 4\sigma), 
    que cubren el rango típico de una distribución normal.
        start = mu - 4*sigma: El rango comienza 4 desviaciones estándar por debajo de la media.
        stop = mu + 4*sigma: El rango termina 4 desviaciones estándar por encima de la media.
    Esto crea un rango de valores (x) que cubre la mayor parte de la distribución normal (aproximadamente el 99.99% de los datos).

y = stats.norm.pdf(x, mu, sigma):
    pdf significa "Probability Density Function", o Función de Densidad de Probabilidad. 
    Calcula la altura de la curva de Gauss (o distribución normal) para cada valor de (x), dada su media (\mu) y desviación estándar (\sigma).
    En este caso:
        Para cada valor en el arreglo x (generado con np.linspace), se calcula la densidad de probabilidad correspondiente.
        El resultado es un arreglo y que contiene las alturas de la curva de Gauss en los puntos definidos por x.

sns.lineplot():
    Es una función de Seaborn que dibuja un gráfico de líneas.
    Dibuja la curva de la distribución normal con los parámetros de color, ejes y etiquetas indicados.
    Parámetros:
        x=x: Valores en el eje X (los puntos generados con np.linspace).
        y=y: Valores en el eje Y (las alturas de la curva calculadas con stats.norm.pdf).
        color='blue': Define el color de la línea (azul).
        label='Distribución Normal': Agrega una etiqueta para identificar la línea en la leyenda.

plt.fill_between(x, y, where=(x >= x1) & (x <= x2), color='orange', alpha=0.5, label=f'Área entre {x1} y {x2}'):
    Rellena el área bajo la curva entre (x1) y (x2) para visualizar la probabilidad calculada.
    plt.fill_between(): Es una función de Matplotlib que rellena el área entre una curva y el eje X.
    Parámetros principales:
        x: Valores en el eje X (en este caso, el rango generado con np.linspace).
        y: Valores en el eje Y (las alturas de la curva calculadas con stats.norm.pdf).
        where=condición: Define la condición para rellenar el área. Solo se rellena el área donde la condición es True.
    where=(x >= x1) & (x <= x2):
        (x >= x1): Evalúa si cada valor de x es mayor o igual a x1.
        (x <= x2): Evalúa si cada valor de x es menor o igual a x2.
        &: Operador lógico "AND". Combina ambas condiciones.
        Resultado: Se rellena el área bajo la curva solo para los valores de x que están entre x1 y x2.
    Se añade el color "orange", se hace semitransparente con "alpha=0.5" y se añade una etiqueta para la leyenda con "label=f'Área entre {x1} y {x2}'"

plt.axvline(mu, color='red', linestyle='--'):
    Dibuja una línea vertical en la media ((\mu)) para destacar el centro de la distribución.
    Indicamos cómo parámetros la posición de la línea en el eje X (mu), el color, el estilo de la línea (discontinua) y una etiqueta para
    identificar la línea en la leyenda.

El gráfico mostrará:
Una curva simétrica en forma de campana (distribución normal).
Un área sombreada entre (x1 = 189) y (x2 = 190), que representa la probabilidad calculada.
Una línea vertical roja en la media ((\mu = 170)).
'''