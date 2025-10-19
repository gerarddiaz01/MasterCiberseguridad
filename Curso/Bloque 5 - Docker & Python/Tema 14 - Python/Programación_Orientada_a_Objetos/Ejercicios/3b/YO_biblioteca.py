'''SISTEMA DE GESTION DE BIBLIOTECA
Crea un sistema de gestión de una biblioteca utilizando clases en Python.
Debes implementar las siguientes clases:
1. “Libro”: Representa un libro con atributos como título, autor y número de
ejemplares disponibles.
2. “Usuario”: Representa a un usuario de la biblioteca con atributos como
nombre, número de identificación y lista de libros prestados.
3. “Biblioteca”: Representa la biblioteca en sí, con métodos para agregar
libros, prestar libros a usuarios, devolver libros y mostrar el inventario.'''

# Clase que representa un libro
class Libro:
    def __init__(self, titulo, autor, ejemplares_disponibles):
        # Inicializamos los atributos del libro
        self.titulo = titulo
        self.autor = autor
        self.ejemplares_disponibles = ejemplares_disponibles

# Clase que representa a un usuario de la biblioteca
class Usuario:
    def __init__(self, nombre, num_identif):
        # Inicializamos los atributos del usuario
        self.nombre = nombre
        self.num_identif = num_identif
        self.libros_prestados = []  # Lista de libros que el usuario tiene prestados

# Clase que representa la biblioteca
class Biblioteca:
    def __init__(self):
        # Inicializamos el inventario como una lista vacía
        self.inventario = []

    def agregar_libro(self, nuevo_libro):
        # Agregamos un libro al inventario
        self.inventario.append(nuevo_libro)
        print(f"Libro '{nuevo_libro.titulo}' agregado al inventario.")

    def prestar_libro(self, titulo_libro, usuario):
        # Buscamos el libro en el inventario
        for libro in self.inventario:
            if libro.titulo == titulo_libro:
                # Verificamos si hay ejemplares disponibles
                if libro.ejemplares_disponibles > 0:
                    libro.ejemplares_disponibles -= 1
                    usuario.libros_prestados.append(libro)
                    print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
                    return
                else:
                    print(f"No hay ejemplares disponibles del libro '{titulo_libro}'.")
                    return # hacemos return para parar el bucle aqui y que se complete el for
        print(f"El libro '{titulo_libro}' no está en el inventario.") # si se completa el for aparece este mensaje

    def devolver_libro(self, titulo_libro, usuario):
        # Verificamos si el usuario tiene el libro prestado
        for libro in usuario.libros_prestados:            
            if libro.titulo == titulo_libro:
                usuario.libros_prestados.remove(libro)
                libro.ejemplares_disponibles += 1
                print(f"Libro '{titulo_libro}' devuelto por {usuario.nombre}.")
                return
        print(f"El usuario {usuario.nombre} no tiene el libro '{titulo_libro}' prestado.")

    def mostrar_inventario(self):
        # Mostramos todos los libros en el inventario
        print("Inventario de la biblioteca:")
        for libro in self.inventario:
            print(f"Titulo: {libro.titulo}, Autor: {libro.autor}, Ejemplares disponibles: {libro.ejemplares_disponibles}")

# Ejemplo de uso del sistema de gestión de biblioteca

# Creamos una instancia de la biblioteca
biblioteca = Biblioteca()

# Creamos algunos libros
libro1 = Libro("El nombre del viento", "Patrick Rothfuss", 3)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 2)
libro3 = Libro("1984", "George Orwell", 5)

# Agregamos los libros al inventario de la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# Mostramos el inventario inicial
biblioteca.mostrar_inventario()

# Creamos un usuario
usuario1 = Usuario("Gerard", 123)

# Prestamos un libro al usuario
biblioteca.prestar_libro("El nombre del viento", usuario1)

# Mostramos el inventario después del préstamo
biblioteca.mostrar_inventario()

# El usuario devuelve el libro
biblioteca.devolver_libro("El nombre del viento", usuario1)

# Mostramos el inventario después de la devolución
biblioteca.mostrar_inventario()
