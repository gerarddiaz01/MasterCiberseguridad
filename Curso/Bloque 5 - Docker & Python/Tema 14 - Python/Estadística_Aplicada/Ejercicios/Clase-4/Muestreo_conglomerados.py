import numpy as np
import pandas as pd

''' Muestreo por conglomerados:
Es un método de muestreo en el que la población se divide en grupos (conglomerados).
Se seleccionan aleatoriamente algunos conglomerados, y todos los individuos de los conglomerados seleccionados forman parte de la muestra.
'''

# Creación de la población
data = {
    'individuos': np.arange(1, 51),
    'conglomerados': np.repeat(np.arange(1, 11), 5)  # 10 conglomerados con 5 individuos cada uno
}
    # 'individuos':
        # np.arange(1, 51): Genera un arreglo con los números del 1 al 50 (representa los individuos de la población).
    # 'conglomerados':
        # np.repeat(np.arange(1, 11), 5): Genera un arreglo que repite los números del 1 al 10, 5 veces cada uno.
            # Esto asigna a cada individuo un conglomerado (grupo) de manera uniforme.
            # Resultado: 10 conglomerados, cada uno con 5 individuos.

# Creación del DataFrame
poblacion = pd.DataFrame(data)
    # pd.Dataframe(): Convierte el diccionario data en un DataFrame de pandas.
    # población es un DataFrame que representa la población con dos columnas, los individuos (1 al 50) y los conglomerados (1 al 10).

# Impresión de la población
print(poblacion)

# Selección aleatoria de conglomerados
conglomerados_seleccionados=np.random.choice(poblacion['conglomerados'].unique(),size=2,replace=False)
    # poblacion['conglomerados'].unique(): Obtiene los valores únicos de la columna 'conglomerados' (en este caso, los números del 1 al 10).
    # np.random.choice(array, size, replace): Selecciona aleatoriamente elementos de un arreglo.
        # array: El arreglo del que se seleccionarán los elementos (en este caso, los conglomerados únicos).
        # size=2: Selecciona 2 conglomerados.
        # replace=False: Indica que los conglomerados no se pueden repetir en la selección.
    # conglomerados_seleccionados: Contiene los números de los 2 conglomerados seleccionados aleatoriamente.

# Selección de la muestra por conglomerados
muestra_por_conglomerados=poblacion[poblacion['conglomerados'].isin(conglomerados_seleccionados)]
    # poblacion['conglomerados'].isin(conglomerados_seleccionados): Verifica si cada valor de la columna 'conglomerados' pertenece 
    # a la lista conglomerados_seleccionados. Devuelve un arreglo booleano (True o False) indicando si cada fila pertenece a los 
    # conglomerados seleccionados.
    # poblacion[...]: Filtra las filas del DataFrame poblacion donde la condición es True.
    # muestra_por_conglomerados: Es un DataFrame que contiene los individuos pertenecientes a los conglomerados seleccionados.


print("Muestra por conglomerados \n",muestra_por_conglomerados)