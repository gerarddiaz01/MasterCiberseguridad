import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression # Clase de Scikit-learn para realizar regresión lineal.
from scipy.stats import pearsonr, spearmanr # Funciones de Scipy para calcular los coeficientes de correlación de Pearson y Spearman.

# Para calcular la correlación necesitamos 4 elementos:
    # Variable independiente
    # Variable dependiente
    # Intersección de la línea de regresión en el eje X cuando es 0 (el valor Y cuando X = 0)
    # Pendiente de la línea de regresión

# Creación de los datos
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Variable independiente (predictora)
Y = np.array([2, 3, 5, 7, 11])  # Variable dependiente (respuesta)
    # hacemos el reshape porque Scikit-learn requiere una matriz columna, con reshape lo transformamos a columna
        # -1 significa que np calcula automáticamente el numero de filas
        # 1 indica que la matriz tendrá una sola columna

# Creación y ajuste del modelo de regresión lineal
modelo = LinearRegression() # Crea un modelo de regresión lineal.

modelo.fit(X,Y) # Ajusta el modelo a los datos (X e Y) y Calcula los parámetros de la línea de regresión (pendiente y ordenada al origen).

# Predicción con el modelo
Y_pred = modelo.predict(X) # Predice los valores de Y (variable dependiente) para los valores de X usando el modelo ajustado.
    # Devuelve un arreglo con los valores predichos en la variable Y_pred

# Obtención de los dos últimos parámetros del modelo
a = modelo.intercept_ # Devuelve la intersección (ordenada al origen) de la línea de regresión en X = 0. Es el valor de Y cuando X = 0.
b = modelo.coef_[0] # Devuelve la pendiente de la línea de regresión. Es un arreglo, por lo que se accede al primer elemento con [0].

print(f"Intersección (a): {a}")
print(f"Pendiente (b): {b}")

# Cálculo del coeficiente de correlación de Pearson

correlacion_pearson, _ = pearsonr(X.flatten(),Y)
    # X.flatten(): Convierte X de una matriz columna a un arreglo unidimensional (necesario para pearsonr). La aplanamos para que no importe
    # si es una fila o una columna.
    # Devuelve dos valores: el coeficiente de correlación de Pearson y el valor p (no se usa aqui por eso lo asignamos a _).
    # En este caso sale una correlación cercana a 1, muy buena correlación

# Cálculo del coeficiente de correlación de Spearman

correlacion_spearman = spearmanr(X.flatten(),Y)
    # Volvemos a aplanar la columna para que no importe la forma que tiene la variable X.
    # En este caso sale una correlación cercana a 1, los valores están bien correlacionados

print(f"Coeficiente de correlación de Pearson: {correlacion_pearson}")
print(f"Coeficiente de correlación de Spearman: {correlacion_spearman}")

plt.scatter(X,Y,color='blue')
    # Crea un gráfico de dispersión con los datos originales (X e Y).
plt.plot(X,Y_pred,color='red')
    # Dibuja la línea de regresión usando los valores predichos (Y_pred).
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regresión Lineal')
plt.show()

''' Interpretación de los coeficientes de Pearson y Spearman:
Indican la fuerza y dirección de la relación entre las variables (X) e (Y).
1. Coeficiente de correlación de Pearson: 0.97
    Pearson mide la relación lineal entre las variables.
    Un valor de 0.97 está muy cerca de 1, lo que indica:
        Una relación lineal muy fuerte entre (X) e (Y).
        A medida que (X) aumenta, (Y) también aumenta de manera casi proporcional.
    Interpretación:
        Los datos están muy bien alineados con una línea recta.
        La regresión lineal es un buen modelo para describir la relación entre (X) e (Y).

2. Coeficiente de correlación de Spearman: 0.99
    Spearman mide la relación monótona entre las variables (es decir, si una variable aumenta, la otra también aumenta o disminuye, 
    sin importar si la relación es lineal o no).
    Un valor de 0.99 está muy cerca de 1, lo que indica:
        Una relación monótona casi perfecta entre (X) e (Y).
        A medida que (X) aumenta, (Y) también aumenta consistentemente.
    Interpretación:
        Incluso si hubiera pequeñas desviaciones de la linealidad, la relación entre (X) e (Y) sigue siendo muy fuerte.
'''