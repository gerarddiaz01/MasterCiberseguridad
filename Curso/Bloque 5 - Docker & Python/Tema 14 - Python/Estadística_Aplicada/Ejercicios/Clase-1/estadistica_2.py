import pandas as pd
import numpy as np

# Vamos a calcular la media y la moda usando funciones de pandas y un documento csv (data externa)

df = pd.read_csv("salary_data.csv",sep=";") # almacenamos en una variable llamada dataframe con un separador ; para obtener los datos

print(df.head()) # para obtener las lineas del header del documento (cabecera)
print("\n-----\n")
print("La media de edad del dataframe es :", df.age.mean()) # para obtener la media de la columna edad
print("\n-----\n")
print("La moda de edad del dataframe es :", df.age.mode()) # para obtener la moda de la columna edad
print("\n-----\n")

# Vamos a calcular la media de un vector con numpy arrays
vector = [1,2,3,4,5,6,7,8,9,8,6,5,7,5]

v = np.array(vector) # ponemos el vector cómo función de numpy array
print("La media del vector usando numpy array es :", v.mean())