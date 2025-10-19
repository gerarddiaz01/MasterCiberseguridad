'''
Supongamos que tienes un conjunto de datos de películas que contiene información
sobre su título, género, duración, año de lanzamiento y calificación. Quieres analizar
estos datos para determinar cuál es el género de película más popular, cuántas películas
se lanzaron en cada década y cuál es la duración promedio de cada género de película.
'''

# import modules
import numpy as np

# array con datos de peliculas
peliculas = np.array([    
    ['Peli 1', 'Comedia', 120, 1990, 8.5],
    ['Peli 2', 'Acción', 110, 2005, 7.8],
    ['Peli 3', 'Drama', 95, 2010, 6.9],
    ['Peli 4', 'Comedia', 100, 1985, 7.5],
    ['Peli 5', 'Acción', 130, 2015, 8.1],
    ['Peli 6', 'Drama', 115, 2000, 6.7],
    ['Peli 7', 'Comedia', 90, 1995, 8.2],
    ['Peli 8', 'Acción', 105, 2010, 7.4],
    ['Peli 9', 'Drama', 125, 1980, 6.8],
    ['Peli 10', 'Comedia', 95, 2000, 8.0]
])

# --- pelicula mas popular ---
# obtener generos y apariciones en la base de datos
todos_generos = peliculas[:,1]
generos_unicos, conteo = np.unique(todos_generos, return_counts=True)


# ordenamos los conteos de mayor a menor
conteo_ordenado_inverso = np.argsort(conteo)[::-1]

# extraemos el genero mas popular
genero_mas_popular = generos_unicos[conteo_ordenado_inverso[0]]
print(f"El genero mas popular es {genero_mas_popular}")
print("----------")

# --- pelicula con mejor rating --- (EXTRA HOMEWORK TO PRACTICE NP.ARGSORT E INDICES)
# obtener la columna de las calificaciones
calificaciones = peliculas[:,4]
pelis = peliculas[:,0]
rating_ordenados = np.argsort(calificaciones)[::-1]
pelicula_mejor = pelis[rating_ordenados[0]]
print(f"La pelicula con mejor calificaciones es {pelicula_mejor}")
print("----------")

# --- agrupamos las peliculas por decada ---
# creamos array con las decadas a tratar
decadas = np.unique(peliculas[:,3].astype(int) // 10 * 10)
    #Ej: (int)1985//10 = 198 * 10 = 1980

# contamos las peliculas en cada decada
for decada in decadas:
    conteo = np.count_nonzero((peliculas[:,3].astype(int) >= decada) & (peliculas[:,3].astype(int) < decada + 10))
    # traducción: quiero que cuentes cuántas películas se han hecho en ésta década.
    # se ha usado la función para contar de numpy poniéndole una condición para que sea True: que vaya del año 0
    # de la década al año 9 de la década. Ej: 1980 al 1989
    # peliculas[:,3].astype(int) = año de la película en la base de datos (Ej: 1985)
    # >= decada, es para indicar que sea igual o mayor al año 0 de la década (Ej: >+ 1980)
    # < decada + 10, es para indicar que sea menor al año 10 de la década (Ej: < 1990(1980 + 10))
    print(f"En la década {decada} se han hecho {conteo} películas")
print("----------")

# --- duracion promedio por genero ---
duracion = peliculas[:,2].astype(int)
duracion_media = {}

# duracion media
for i in range(len(generos_unicos)):
    duracion_media[i] = np.mean(duracion[todos_generos==generos_unicos[i]])
    print(f"Duracion media de las peliculas de {generos_unicos[i]}, es de {duracion_media[i]} minutos")