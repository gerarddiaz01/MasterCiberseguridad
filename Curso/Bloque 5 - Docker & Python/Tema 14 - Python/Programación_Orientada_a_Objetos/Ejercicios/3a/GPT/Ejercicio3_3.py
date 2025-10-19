'''Ejercicio 3: Métodos especiales y polimorfismo
Enunciado: Construye una clase Libro con atributos titulo y autor. Implementa los métodos especiales __str__ 
y __repr__ para que las instancias se muestren de forma legible. En particular, __str__ debe devolver "<titulo>"
de <autor> (por ejemplo, "Cien años de soledad" de Gabriel García Márquez), mientras que __repr__ debe devolver 
Libro(titulo='<titulo>', autor='<autor>'). Añade también un método citar() que devuelva un texto simulando una 
cita del libro (por ejemplo: «Extracto de "titulo"...»). Luego, crea dos clases que hereden de Libro: Ebook y 
Audiolibro, que representen libros en formato electrónico y audiolibro respectivamente. Cada una debe sobreescribir 
el método citar() para reflejar su formato (por ejemplo, en Audiolibro.citar() la cita podría incluir que es narrada).
Crea instancias de Ebook y Audiolibro y muestra sus representaciones (usando print y repr) y sus citas para verificar
el polimorfismo'''

# Definimos la clase base Libro
class Libro:
    def __init__ (self, titulo, autor):
        # Inicializamos los atributos titulo y autor
        self.titulo = titulo
        self.autor = autor

    def __str__ (self):
        # Método especial __str__: devuelve una representación legible del objeto
        # Este método se usa cuando hacemos print(objeto)
        return f"{self.titulo} de {self.autor}."
    
    def __repr__ (self):
        # Método especial __repr__: devuelve una representación más técnica del objeto
        # Este método se usa cuando hacemos repr(objeto) o en la consola interactiva
        return f"Libro(titulo={self.titulo}, autor={self.autor})"
    
    def citar(self):
        # Método que imprime una cita genérica del libro
        print(f"Extracto del libro {self.titulo}: Y entonces escaló el arbol, dejando a los Chandrian con la boca abierta")

# Definimos la clase Ebook que hereda de Libro
# En la clase Libro ya inicializamos titulo y autor asi que no es necesario añadir un __init__ y super.()__init__
# Pero si quieres añadir un atributo adicional en ésta clase si tenemos que hacer __init__
class Ebook(Libro):
    def citar(self):
        # Sobrescribimos el método citar para reflejar que es un Ebook
        print(f"Extracto del Ebook {self.titulo}: Y entonces escaló el arbol, dejando a los Chandrian con la boca abierta")
    
# Definimos la clase Audiobook que hereda de Libro
class Audiobook(Libro):
    def citar(self):
        # Sobrescribimos el método citar para reflejar que es un Audiobook
        print(f"Extracto narrado de {self.titulo}: Y entonces escaló el arbol, dejando a los Chandrian con la boca abierta")

libro1 = Libro("El nombre del viento", "Patrick Rothfuss")
ebook1 = Ebook("El nombre del viento", "Patrick Rothfuss")

# Creamos una instancia de la clase Audiobook
audiobook1 = Audiobook("El nombre del viento", "Patrick Rothfuss")

# Mostramos la representación técnica del Libro usando repr
print(repr(libro1)) 

# Mostramos la representación legible del Libro usando str
print(libro1) 

# Llamamos al método citar del Libro (sobrescrito)
libro1.citar()

print("")  # Línea en blanco para separar las salidas

# Mostramos la representación técnica del Ebook usando repr
print(repr(ebook1))  

# Mostramos la representación legible del Ebook usando str
print(ebook1)  

# Llamamos al método citar del Ebook (sobrescrito)
ebook1.citar() 

print("")  # Línea en blanco para separar las salidas

# Mostramos la representación técnica del Audiobook usando repr
print(repr(audiobook1))  

# Mostramos la representación legible del Audiobook usando str
print(audiobook1)  

# Llamamos al método citar del Audiobook (sobrescrito)
audiobook1.citar() 