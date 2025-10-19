import pandas as pd
import numpy as np

df = pd.read_csv("salary_data.csv", sep = ";") # leemos el csv con la información

# calculamos el rango, que es la diferencia entre el valor maximo y el valor minimo, en éste caso el salario
rango = (df.income.max()) - (df.income.min())
print("El rango de los salarios del dataframe es:", rango)

# calculamos el rango con numpy
rango_numpy = (np.max(df.age)) - (np.min(df.age))
print("El rango de la edad del dataframe es:", rango_numpy)
print("")
# calculamos la varianza
varianza = df.age.var()
print("Varianza de edad:", varianza)
print("Media de edad:", df.age.mean()) 


# calculamos la varianza con numpy
varianza_numpy = np.var(df.age)
print("Varianza de edades con numpy:", varianza_numpy)
# nos sale una varianza ligeramente distinta, como más grande sea el muestreo mas ligera es la diferencia, razón:
#   con pandas se divide entre n: porque usa la varianza muestral
#   con numpy se divide entre n + 1: porque usa la varianza poblacional
# Vamos a parametrar ésta diferencia para que ambas sean poblacionales:
print("")
print("Varianza Poblacional:")
varianza_poblacional = df.age.var(ddof = 0)
print("Varianza Edad:", varianza_poblacional)
varianza_poblacional_numpy = np.var(df.age,ddof = 0)
print("Varianza Edad Numpy:", varianza_poblacional_numpy)
print("")
# Vamos a calcular la desciacion estandar (std en ingles, standard deviation):
# desviacion_estandar = (varianza)**0.5  elevarlo al cuadrado es equivalente a hacer la raiz cuadrada
ds = df.age.std()
print("Desviacion estandar de edad:", ds) # nos da un margen de 9 años parriba y pabajo de la media mas o menos
# desviacion estandar con np
ds_np = np.std(df.age)
print("Desviacion estandar de edad con np:", ds_np)

'''Interpretación:
Varianza: una varianza de 88 indica que las edades están distribuidas con cierta variabilidad alrededor de la media (32 años).
    Sin embargo, la varianza no es tan intuitiva porque está en unidades al cuadrado (en este caso, "años al cuadrado"). Por eso, 
    solemos usar la desviación estándar para una interpretación más directa.
Desviacion Estandar: La desviación estándar es la raíz cuadrada de la varianza y se mide en las mismas unidades que los datos 
    originales (en este caso, años). Una desviación estándar de 9 años significa que, en promedio, las edades se desvían 9 años de 
    la media (32 años). Esto implica que la mayoría de las edades están en el rango de [32 - 9, 32 + 9], es decir, entre 23 y 41 años.

'''