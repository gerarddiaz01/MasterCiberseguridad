""" Una biblioteca tiene una lista de libros y sus autores. Crea un programa que tome la lista
de libros y sus autores como una lista de tuplas, donde cada tupla contiene el título del
libro y el nombre del autor, y devuelva una nueva lista de tuplas que contenga el título del
libro y el apellido del autor."""

lista_libros = [('El aleph', 'Jorge Luis Borges'), ('Cien años de soledad', 'Gabriel Garcia Márquez'), ('La ciudad y los perros', 'Mario Vargas Llosa')]

""" titulos_apellidos = []

for tupla in lista_libros:
    titulos, autor = tupla
    apellido = autor.split()[-1]
    titulos_apellidos.append((titulos, apellido))
print(titulos_apellidos) """

titulos_apellidos = [(titulos, autor.split()[-1]) for titulos, autor in lista_libros]
# Explicación de la compresión de listas:
# (titulos, autor.split()[-1]) Es la expresión que genera cada elemento de la nueva lista
# titulos: es el titulo del libro
# autor.split()[-1] obtiene el apellido del autor dividiendo el nombre completo por palabras y seleccionando la última
# for titulos, autor in lista_libros: Itera sobre cada tupla en lista_libros, desempaquetando el titulo y el autor
