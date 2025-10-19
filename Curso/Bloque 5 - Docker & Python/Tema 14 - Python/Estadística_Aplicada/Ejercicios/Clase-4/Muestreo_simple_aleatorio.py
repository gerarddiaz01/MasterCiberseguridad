import numpy as np

''' Muestreo aleatorio simple:
Es un método de muestreo en el que cada elemento de la población tiene la misma probabilidad de ser seleccionado.
En este caso: Cada número del 1 al 100 tiene la misma probabilidad de ser incluido en la muestra de 10 elementos.
'''

# Generación de la población
poblacion = np.arange(1,101) # Poblacion del 1 al 100
    # np.arange(start, stop): Genera un arreglo de números enteros desde start hasta stop - 1.

# Definición del tamaño de la muestra
tamaño_muestra = 10

# Selección de la muestra aleatoria simple
muestra_aleatoria_simple=np.random.choice(poblacion,tamaño_muestra,replace=False)
    # Selecciona aleatoriamente elementos de un arreglo (choice para seleccionar)
    # Parámetros:
        # array: El arreglo del que se seleccionarán los elementos (en este caso, poblacion).
        # size: El número de elementos a seleccionar (en este caso, tamaño_muestra = 10).
        # replace=False:
            # Indica que los elementos no se pueden repetir en la muestra.
            # Si fuera True, los elementos podrían seleccionarse más de una vez.
    # Resultado: Una muestra aleatoria de 10 elementos seleccionados de la población.


print('Muestra aleatoria simple:',muestra_aleatoria_simple)