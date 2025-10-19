'''Busca si tu fecha de nacimiento esta en los primeros 10000 digitos de pi (y
en que posición. Puedes usar find()).
Puedes usar el archivo pi_10000.txt'''

# Nombre del archivo que contiene los primeros 10,000 dígitos de pi
archivo1 = "pi_10000.txt"

# Abrimos el archivo en modo lectura ("r")
# El modo "r" permite leer el contenido del archivo, pero no modificarlo
with open(archivo1, "r") as file:
    # Leemos todo el contenido del archivo como una cadena de texto
    content = file.read()

# Definimos la fecha de nacimiento que queremos buscar en los dígitos de pi
# En este caso, la fecha está representada como una cadena de texto
fecha_nacimiento = "1208"  # Ejemplo: 12 de agosto

# Usamos el método find() para buscar la posición de la fecha en los dígitos de pi
# Si la fecha se encuentra, find() devuelve el índice donde comienza la subcadena
# Si no se encuentra, find() devuelve -1
posicion = content.find(fecha_nacimiento)

# Verificamos si la fecha de nacimiento se encuentra en los dígitos de pi
if posicion != -1:
    # Si la posición no es -1, significa que la fecha fue encontrada
    # Imprimimos la posición donde comienza la fecha en los dígitos de pi
    print(f"La fecha {fecha_nacimiento} se encuentra en los digitos de pi, comenzando en la posicion {posicion}.")
else:
    # Si la posición es -1, significa que la fecha no fue encontrada
    # Imprimimos un mensaje indicando que la fecha no está en los dígitos de pi
    print(f"La fecha {fecha_nacimiento} no se encuentra en los dígitos de pi.")


