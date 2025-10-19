import pandas as pd
import numpy as np
from scipy.stats import skew

def normal_dist():

    # Parámetros de la distribución normal
    media = 0
    desviacion_estandar = 1
    tamaño = 100000

    # Generar datos aleatorios con distribución normal
    datos = np.random.normal(loc=media, scale=desviacion_estandar, size=tamaño)

    Data=pd.Series(datos)

    print(Data.kurtosis())


df=pd.read_csv('salary_data.csv',sep=';')

#Calculo ASIMETRIA

print(df.head())

Asimetria=df.income.skew()
print('Asimetria de Salarios',Asimetria)

#Es decir, la asimetria es positiva, es decir la mayoria de salarios se encuentran en la parte izquierda, 
# es decir hay más salarios bajos que altos

#Numpy no tiene esa funcion por lo que podriamos utilzar otra libreria de datascience Scipy
from scipy.stats import skew
Asimetria=skew(df.age)
print('Asimetria de Salarios_scipy',Asimetria)
#Es decir, la asimetria es positiva, es decir la mayoria de las personas se encuentran en la parte izquierda, son mayores que la media

curtosis = df.income.kurtosis() 
print(curtosis)

# Calculo curtosis de la distribución normal para ver si se le resta 3 o vale 0
normal_dist()

