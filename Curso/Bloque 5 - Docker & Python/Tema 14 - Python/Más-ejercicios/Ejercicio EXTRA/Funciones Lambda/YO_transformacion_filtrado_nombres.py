'''Problema de Transformación y Filtrado de Nombres:

Imagina que te encuentras desarrollando una herramienta de procesamiento de nombres para una 
aplicación de gestión de contactos. Tienes una lista de nombres en el formato "Apellido, Nombre", 
realiza las siguientes tareas:
Utiliza la función lambda para transformar una lista de nombres completos al nuevo formato.
Filtra la lista para incluir solo los nombres que contienen al menos dos vocales y tienen una 
longitud mayor a 10 caracteres.'''

lista_nombres = ["Pérez,Juan", "López,María", "García,José", "Martín,Ana","Lea,Kho","Serrano,Xavier"]

# Transformar nombres al formato "Nombre Apellido"
def transformar_nombres(lista):
    nombres_transformados = list(map(lambda nombre: f"{nombre.split(',')[1]} {nombre.split(',')[0]}", lista))
    return nombres_transformados
    
    
# Filtrar nombres con al menos dos vocales y longitud mayor a 10 caracteres
def filtrar_nombres(lista_transformada):
    vocales= "aeiouáéíóúAEIOUÁÉÍÓÚ"
    nombres_filtrados = list(filter(lambda nombre: sum(1 for letra in nombre if letra in vocales) >= 2 and len(nombre) > 10, lista_transformada))
    return nombres_filtrados

lista_transformada = transformar_nombres(lista_nombres)
lista_definitiva = filtrar_nombres(lista_transformada)

for nombre in lista_definitiva:
    print(nombre)