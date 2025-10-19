import numpy as np
import pandas as pd

''' Muestreo estratificado:
Es un método de muestreo en el que la población se divide en grupos (estratos) y se selecciona una muestra de cada grupo.
La muestra es proporcional al tamaño de cada estrato, asegurando que todos los grupos estén representados.
'''

# Creación de los datos
data = {
    'individuos':np.arange(1,101),
    'estratos': np.repeat(['A','B','C','D'],25)
}
    # 'individuos':
        # np.arange(1, 101): Genera un arreglo con los números del 1 al 100 (representa los individuos de la población).
    # 'estratos':
        # np.repeat(['A', 'B', 'C', 'D'], 25): Repite los valores 'A', 'B', 'C', y 'D' 25 veces cada uno.
        # Esto asigna a cada individuo un estrato (grupo) de manera uniforme.

# Creación del DataFrame
poblacion = pd.DataFrame(data)
    # pd.DataFrame(data): Convierte el diccionario data en un DataFrame de pandas.
    # poblacion: Es un DataFrame que representa la población, con dos columnas:
        # individuos: Contiene los números del 1 al 100.
        # estratos: Contiene los estratos ('A', 'B', 'C', 'D').

# print(poblacion.head())

# Definición del tamaño de la muestra
Tamaño_muestra = 12
    # Define el número total de individuos que se seleccionarán en la muestra estratificada. En este caso, se seleccionarán 12 individuos.

# Muestreo estratificado
muestra_estratificada=poblacion.groupby('estratos',group_keys=False).apply(lambda x: x.sample(int(np.rint(Tamaño_muestra * len(x) / len(poblacion)))))
    # poblacion.groupby('estratos', group_keys=False): Agrupa el DataFrame poblacion por la columna 'estratos'. 
        # Cada grupo contiene los individuos pertenecientes a un estrato ('A', 'B', 'C', 'D').
        # group_keys=False: Evita que el nombre del grupo (el estrato) se agregue como un índice adicional en el resultado.
    # .apply(lambda x: ...): Aplica una función a cada grupo.
        # lambda x: x.sample(...): Selecciona una muestra aleatoria de individuos dentro de cada grupo.
    # x.sample(...): Selecciona una muestra aleatoria de filas del grupo x.
        # int(np.rint(...)): Calcula el número de individuos que se seleccionarán de cada grupo.
        # np.rint(...): Redondea el resultado al entero más cercano.
        # int(...): Convierte el resultado en un número entero.

print("Muestra Estratificada \n",muestra_estratificada)