'''
Supongamos que tienes un conjunto de datos de clima que contiene información sobre la
temperatura, la humedad y la presión atmosférica en una ciudad durante un año. Quieres
analizar estos datos para determinar cuál fue la temperatura promedio de cada mes, cuál
fue la humedad promedio y la presión atmosférica promedio durante todo el año. Para
ello, puedes usar NumPy para cargar los datos en un array de 3 columnas y n filas, donde
n es el número de mediciones. Luego, puedes usar operaciones de NumPy para filtrar los
datos por mes y calcular las medias de temperatura, humedad y presión atmosférica
correspondientes

# importar modulos
import numpy as np

# Datos de clima
clima = np.array([
    [20, 70, 1009, 1],
    [18, 75, 1012, 2],
    [16, 72, 1011, 2],
    [19, 73, 1011, 2],
    [22, 65, 1008, 3],
    [25, 60, 1010, 4],
    [22, 60, 1013, 4],
    [24, 59, 1010, 4],
    [25, 61, 1011, 4],
    [28, 50, 1007, 5],
    [30, 45, 1005, 6],
    [10, 45, 1005, 6],
    [32, 40, 1002, 7],
    [30, 35, 1003, 8],
    [33, 35, 1001, 8],
    [32, 35, 1004, 8],
    [31, 45, 1003, 9],
    [28, 50, 1006, 10],
    [27, 48, 1008, 10],
    [25, 60, 1010, 11],
    [22, 70, 1011, 12]
])

#Guardar datos en arrays diferentes
temperaturas = clima[:,0]
humedad = clima[:,1]
presion = clima[:,2]
meses = clima[:,3]

# inicializamos arrays de valores promedio por mes
temp_mes = np.zeros(12)
humedad_mes = np.zeros(12)
presion_mes = np.zeros(12)

# recorrer los valores para cada mes
for i in range(12):
    # calculamos valores medios
    temp_mes[i] = np.mean(temperaturas[meses == i+1])
    humedad_mes[i] = np.mean(humedad[meses == i+1])
    presion_mes[i] = np.mean(presion[meses == i+1])

    # imprimimos resultados para cada mes
    print("La temperatura promedio en el mes", i+1, " fue de", temp_mes[i], "grados")
    print("La humedad promedio en el mes", i+1, " fue de", humedad_mes[i])
    print("La presion promedio en el mes", i+1, " fue de", presion_mes[i], "bar")
'''

# importar modulos
import numpy as np

# Datos de clima
clima = np.array([
    [20, 70, 1009, 1],
    [18, 75, 1012, 2],
    [16, 72, 1011, 2],
    [19, 73, 1011, 2],
    [22, 65, 1008, 3],
    [25, 60, 1010, 4],
    [22, 60, 1013, 4],
    [24, 59, 1010, 4],
    [25, 61, 1011, 4],
    [28, 50, 1007, 5],
    [30, 45, 1005, 6],
    [10, 45, 1005, 6],
    [32, 40, 1002, 7],
    [30, 35, 1003, 8],
    [33, 35, 1001, 8],
    [32, 35, 1004, 8],
    [31, 45, 1003, 9],
    [28, 50, 1006, 10],
    [27, 48, 1008, 10],
    [25, 60, 1010, 11],
    [22, 70, 1011, 12]
])

# guardamos datos en arrays independientes
temperatura = clima[:,0]
humedad = clima[:,1]
presion = clima[:,2]
meses = clima[:,3]

# inicializamos arrays de valores promedio por mes
temperatura_mes = np.zeros(12)
humedad_mes = np.zeros(12)
presion_mes = np.zeros(12)

# recorrer los valores para cada mes
for mes in range(1,13): #en indices tengo que poner -1, si pongo (12) tengo que poner mes+1 cuando hablo del mes en que estamos (0 al 11) pero los indices seria mes
    # calculamos valores medios
    temperatura_mes = np.mean(temperatura[meses==mes])
    humedad_mes = np.mean(humedad[meses==mes])
    presion_mes = np.mean(presion[meses==mes])

    # imprimimos resultados para cada mes
    print(f"La temperatura promedio en el mes {mes} fue de {temperatura_mes} grados")
    print(f"La humedad promedio en el mes {mes} fue de {humedad_mes}")
    print(f"La presion promedio en el mes {mes} fue de {presion_mes} bar")