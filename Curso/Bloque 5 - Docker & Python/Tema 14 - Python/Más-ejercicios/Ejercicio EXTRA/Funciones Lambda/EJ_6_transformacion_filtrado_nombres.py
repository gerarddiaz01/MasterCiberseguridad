# Ejercicio 6: Problema de Transformación y Filtrado de Nombres:

# Imagina que te encuentras desarrollando una herramienta de procesamiento de nombres para una aplicación de gestión de contactos. Tienes una lista de nombres en el formato "Apellido, Nombre", realiza las siguientes tareas:

# Utiliza la función lambda para transformar una lista de nombres completos al nuevo formato.
# Filtra la lista para incluir solo los nombres que contienen al menos dos vocales y tienen una longitud mayor a 10 caracteres.

lista_nombres = ["Pérez,Juan", "López,María", "García,José", "Martín,Ana","Lea,Kho","Zerrano, Xavier"]

#Funcion para filtrado de nombres transformados
def filtrar_nombres(lista_nombres_transformados):
  def nombre_valido(nombre):
    vocales= "aeiouáéíóúAEIOUÁÉÍÓÚ"
    return sum(1 for letra in nombre if letra in vocales) >=2 and len(nombre)>10
  return [nombre for nombre in lista_nombres_transformados if nombre_valido(nombre)]

#Lista de nombres transformados a un nuevo formato
lista_nombres_transformados = [(lambda nombre_original:nombre_original.split(",")[1]+" "+nombre_original.split(",")[0])(nombre_original) for nombre_original in lista_nombres]

lista_nombres_filtrados=filtrar_nombres(lista_nombres_transformados)
print(lista_nombres_filtrados)