'''
Supongamos que trabajas en una empresa que fabrica dispositivos electrónicos y quieres
analizar los datos de calidad de los componentes utilizados en la producción de dichos
dispositivos. Tienes un conjunto de datos que contiene información sobre la fecha de
producción, el tipo de componente, el lote al que pertenece el componente y la
puntuación de calidad del componente (un número entre 0 y 100). Quieres analizar estos
datos para determinar cuál es el tipo de componente con la puntuación de calidad más
alta, cuántos componentes se produjeron en cada mes y cuál es la puntuación de calidad
promedio de cada tipo de componente.
'''
# Importar los módulos
import numpy as np

# Crear un array con los datos
datos = np.array([['2022-01-01', 'Componente 1', 'Lote A', 80],
                  ['2022-01-15', 'Componente 1', 'Lote B', 90],
                  ['2022-02-01', 'Componente 2', 'Lote C', 85],
                  ['2022-02-15', 'Componente 2', 'Lote D', 95],
                  ['2022-03-01', 'Componente 1', 'Lote E', 75],
                  ['2022-03-15', 'Componente 2', 'Lote F', 90]])

# ---Determinar el tipo de componente con la puntuación de calidad más alta---
# extraer los datos de la base de datos: el tipo de componente y la puntuación de calidad
tipo_componente = datos[:,1]
puntuacion = datos[:,3].astype(float) #sino cambiamos a float en el promedio nos dará error

# ordenar los indices de la columna de puntuaciones de mayor a menor
puntuacion_ordenada = np.argsort(datos[:,3])[::-1]

# crear la variable con el tipo de componente con mejor puntuación
componente_mejor_puntuacion = tipo_componente[puntuacion_ordenada[0]]

# ordenar de mayor a menor la columna de puntuaciones para nombrar cual es la puntuacion mas alta en el print
puntuacion_mas_alta = np.sort(puntuacion)[::-1]

print(f"El tipo de componente con mayor puntuación de calidad es {componente_mejor_puntuacion}, con {puntuacion_mas_alta[0]}" )
print("----------")

# ---Determinar cuántos componentes se produjeron en cada mes---
# extraer las fechas de la base de datos y los meses de las fechas
fechas = datos[:,0]
meses = np.array([fecha[5:7] for fecha in fechas])

# inicializar un array vacío (diccionario) para almacenar los datos del conteo
conteo_componentes_producidos = {}

# hacer un array con los meses únicos distintos que hay en datos, sin duplicados
meses_unicos = np.unique(meses)

# contar los componentes producidos en cada mes
for mes in meses_unicos:
    conteo_componentes_producidos[mes] = np.count_nonzero(meses == mes)
    print(f"En el mes {mes} se produjeron {conteo_componentes_producidos[mes]} componentes")
print("----------")

# ---Determinar la puntuación de calidad promedio de cada tipo de componente---
# obtener una lista de todos los tipos de componentes sin duplicados
componentes_unicos = np.unique(tipo_componente)

# crear un array de ceros con una longitud igual al numero de tipos de componentes únicos
puntuacion_promedio = np.zeros(len(componentes_unicos))

# calcular el promedio suando un bucle
for i in range(len(componentes_unicos)):
    puntuacion_promedio[i]= np.mean(puntuacion[tipo_componente==componentes_unicos[i]])
    print(f"La puntuación de calidad promedio de {componentes_unicos[i]} es {puntuacion_promedio[i]}")
