import seaborn as sns # librería de visualización de datos basada en Matplotlib, proporciona gráficos
import matplotlib.pyplot as plt # librería para crear gráficos en python, se usa junto a seaborn
# Utilizamos Seaborn para gráficos estadísticos y Matplotlib para personalizar y mostrar los gráficos


datos = sns.load_dataset('iris')
    # sns.load_dataset('iris'): Carga el dataset iris, que es un conjunto de datos predefinido en Seaborn. 
    # Contiene información sobre tres especies de flores (setosa, versicolor, virginica) y sus características 
    # (sepal_length, sepal_width, petal_length, petal_width).

# Grafico de dispersion (scatterplot en inglés)

sns.scatterplot(data=datos, x='sepal_length', y='sepal_width') # Crea un gráfico de dispersión. Muestra la relación entre dos variables (sepal_length y sepal_width)
    # data=datos: Especifica el Dataset que contiene los datos
    # x='sepal_length': Define la variable para el eje X
    # y='sepal_width': Define la variable para el eje Y
plt.title('Grafico de dispersion de longitud del sepalo vs ancho') # Agrega un título al gráfico, tiene que ser descriptivo
plt.xlabel('sepal_length') # etiqueta del eje X
plt.ylabel('sepal_width') # etiqueta del eje 
plt.show() # ejecuta el gráfico

# Grafico de Barras

sns.barplot(data=datos, x='species', y='sepal_length') # Crea un gráfico de barras. Muestra la media de sepal_length para cada especie (species)
    # x='species': Define la variable categórica para el eje X
    # y='sepal_length': Define la variable numérica para el eje Y
plt.title('Grafico de barras longitud del sepalo por especie')
plt.xlabel('Specie')
plt.ylabel('sepal_length')
plt.show()

# Histograma

sns.histplot(datos['sepal_length'],bins=5) # Crea un histograma. Muestra la distribución de la variable sepal_length
    # datos['sepal_length']: Especifica la columna del dataset que se va a graficar
    # bins=5: Divide los datos en 5 intervalos (bins), los bins son la cantidad de divisiones que hay en nuestro gráfico
plt.title('Histograma de longitud del sepalo')
plt.show()

# Grafico de violin

sns.violinplot(data=datos,x='species',y='sepal_length') #  Crea un gráfico de violín
    # Combina un gráfico de caja (boxplot) con una estimación de densidad
    # Muestra la distribución de sepal_length para cada especie (species)
        # x='species': Define la variable categórica para el eje X
        # y='sepal_length': Define la variable numérica para el eje Y.
plt.title('Grafico de violin')
plt.show()

# Gráfico de pares (pairplot): Necesario para poder pintar el heatmap

sns.pairplot(data=datos,hue='species') # Crea un gráfico de pares. 
    # Muestra gráficos de dispersión para todas las combinaciones de variables numéricas en el dataset
    # data=datos: Especifica el DataFrame que contiene los datos
    # hue='species': Colorea los puntos según la especie (species)
plt.show()

# Mapa de calor (heatmap)

corr = datos.select_dtypes(include=['float64', 'int64']).corr()
#corr=datos.corr() # Calcula la matriz de correlación entre las variables numéricas del DataFrame
sns.heatmap(corr, annot=True, cmap='coolwarm') # Crea un mapa de calor para visualizar la matriz de correlación
    # Especifica la matriz de correlación
    # annot=True: Muestra los valores numéricos en cada celda del mapa
    # cmap='coolwarm': Define el esquema de colores
plt.title('Mapa de calor de las correlaciones')
plt.show()

'''
1. Explicación del gráfico de pares (pairplot):
El gráfico de pares muestra gráficos de dispersión para todas las combinaciones de variables numéricas en el dataset, 
junto con distribuciones univariadas (histogramas o densidades) en la diagonal. Es una herramienta útil para explorar 
relaciones entre múltiples variables numéricas en un dataset. 
En este caso, el dataset iris contiene las siguientes variables numéricas:
    sepal_length
    sepal_width
    petal_length
    petal_width
El gráfico de pares muestra gráficos de dispersión para cada combinación de estas variables.
Colorea los puntos según la variable categórica species (especies de flores: setosa, versicolor, virginica).
En la diagonal, muestra la distribución univariada de cada variable (estimación de densidad).

2. Interpretación:
-Ejes del gráfico
    Cada fila y columna corresponde a una variable numérica del dataset.
    Por ejemplo:
        La primera fila muestra cómo sepal_length se relaciona con las demás variables (sepal_width, petal_length, petal_width).
        La segunda fila muestra cómo sepal_width se relaciona con las demás variables, y así sucesivamente.
-Colores
    Los puntos están coloreados según la especie de flor (species):
        Azul: setosa
        Naranja: versicolor
        Verde: virginica
-Relaciones entre variables
    Gráficos de dispersión (fuera de la diagonal):
        Muestran la relación entre dos variables numéricas.
        Por ejemplo, en la primera fila y segunda columna, se observa la relación entre sepal_length (eje X) y sepal_width (eje Y).
    Distribuciones univariadas (diagonal):
        Muestran la distribución de cada variable para cada especie.
        Por ejemplo, en la primera celda de la diagonal, se observa la distribución de sepal_length para las tres especies.

3. Observaciones clave del gráfico
-Relación entre petal_length y petal_width
    Hay una relación lineal clara entre petal_length y petal_width.
    Las tres especies están bien separadas:
        setosa (azul) tiene valores bajos de ambas variables.
        versicolor (naranja) tiene valores intermedios.
        virginica (verde) tiene valores altos.
-Relación entre sepal_length y sepal_width
    La relación entre sepal_length y sepal_width no es tan clara como en el caso anterior.
    setosa (azul) parece estar más separada de las otras dos especies, con valores más altos de sepal_width y más bajos de sepal_length.
-Distribuciones univariadas
    En la diagonal, las distribuciones muestran que:
        setosa tiene distribuciones más concentradas (menos dispersión) para todas las variables.
        versicolor y virginica tienen distribuciones más dispersas y, en algunos casos, se superponen (por ejemplo, en sepal_length).

4. Conclusión
El gráfico de pares es útil para identificar patrones y relaciones entre las variables numéricas del dataset iris. 
Algunas conclusiones clave:
    petal_length y petal_width son las variables más útiles para separar las tres especies.
    setosa está claramente separada de las otras dos especies en la mayoría de las combinaciones de variables.
    versicolor y virginica tienen más superposición, lo que podría dificultar su separación en algunos casos.

'''