import pandas as pd # nos permite trabajar con dataframes y series
import numpy as np
from scipy.stats import skew, kurtosis # importamos Scipy que es una librería de datascience con herramientas estadisticas avanzadas

def normal_dist(): # se generan datos aleatorios con una distribución normal y calcula su curtosis usando pandas
    '''Por qué hacemos ésto? para verificar cómo pandas o scipy calcula la curtosis, ya que pandas o scipy devuelven el exceso de 
    curtosis (no es necesario restar 3) lo comparamos con un valor 0, sabiendo que 0 es el equivalente de una distribución normal.
    Es sólo para entender cómo pandas o scipy manejan el exceso de curtosis'''
    
    # Parámetros de la distribución normal, donde la curtosis será 3
    media = 0
    desviacion_estandar = 1
    tamaño = 100000

    # Generar datos aleatorios con distribución normal
    datos = np.random.normal(loc=media, scale=desviacion_estandar, size=tamaño)

    Data = pd.Series(datos)

    print(Data.kurtosis())
    

# Cargamos los datos desde el archivo csv y accedemos a la columna de salarios
df = pd.read_csv('salary_data.csv',sep = ';')
salaries = df["income"]

# Calculo ASIMETRIA (skewness en inglés)

print(df.head())

# Calcular la asimetría con pandas
skewness_pandas = df.income.skew() # o salaries.skew()
print('Asimetria de Salarios con pandas', skewness_pandas)

# Calcular la asimetría con scipy
skewness_scipy = skew(df.age) # o skew(salaries)
print('Asimetria de Salarios con scipy', skewness_scipy)

# Calculo CURTOSIS

# Calcular la curtosis con pandas: calcula la exceso de curtosis, que es la curtosis menos 3 
# (para que una distribución normal tenga un valor de 0).
kurtosis_pandas = df.income.kurtosis() # o salaries.kurtosis()
print("Curtosis con pandas:", kurtosis_pandas)

# Calcular la curtosis con scipy: por defecto, devuelve el exceso de curtosis (igual que pandas) con fisher=True (oculto)
kurtosis_scipy = kurtosis(df.income) # si ponemos fisher=False nos sumará 3 porque lo comparamos a una curtosis de 3 no de 0
print("Curtosis con scipy:", kurtosis_scipy)
kurtosis_scipy_clasica = kurtosis(df.income, fisher=False)
print("Curtosis con scipy:", kurtosis_scipy_clasica)


# Calculo curtosis de la distribución normal para ver si se le resta 3 o vale 0
normal_dist()

'''Interpretaciones:
Asimetria: Asimetría con pandas: 0.90, Asimetría con scipy: 0.89
    La asimetría es positiva y cercana a 1, lo que indica que la distribución de los salarios tiene una cola derecha más larga. 
    Esto significa que hay algunos salarios muy altos que están "empujando" la distribución hacia la derecha.

Curtosis: Exceso de Curtosis con pandas o scipy: 7.16, Exceso de Curtosis de una distribución normal: 0.009 (muy cercana a 0).
    La curtosis de los salarios (7.16) es mucho mayor que la de una distribución normal (0). Esto indica 
    que la distribución de los salarios tiene colas más pesadas, es decir, hay más valores extremos (muy altos o muy bajos)
    en comparación con una distribución normal.
    Exceso de curtosis: en una distribución normal la curtosis es 3, y cómo queremos compararlo con un valor de 0 restamos 3 y nos
    sale el exceso de curtosis, en una distribución normal será muy cercano a 0. Con las funciones de pandas o scipy calculamos 
    directamente el exceso de curtosis (no es necesario restar 3) y lo comparamos con 0. 
    Si el exceso es...:
        - 0: La distribución tiene colas similares a una distribución normal.
        - Mayor que 0: La distribución tiene colas más pesadas (más valores extremos).
        - Menor que 0: La distribución tiene colas más ligeras (menos valores extremos).

En resumen, los salarios no están distribuidos de manera simétrica ni normal. Hay una tendencia hacia salarios altos 
(asimetría positiva) y una mayor presencia de valores extremos (alta curtosis). Esto es común en datos de ingresos, 
donde una pequeña proporción de personas gana significativamente más que el resto.

'''