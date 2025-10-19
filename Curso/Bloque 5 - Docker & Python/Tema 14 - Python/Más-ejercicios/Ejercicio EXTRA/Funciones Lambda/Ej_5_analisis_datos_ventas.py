""" Ejercicio 5:

Problema de Análisis de Datos de Ventas:

Imagina que eres parte de una empresa de comercio electrónico y tienes información detallada sobre las ventas de productos. Cada venta se representa como un diccionario, que incluye el nombre del producto, la fecha de venta, el monto de la venta y la ubicación del comprador. Realiza un análisis avanzado de estas ventas.

Filtra las ventas realizadas en el último trimestre del año.
Selecciona solo las ventas de productos con un monto superior a $500.
Agrupa las ventas por ubicación del comprador.
Calcula el promedio del monto de venta para cada ubicación.
Ordena las ubicaciones por el promedio del monto de venta de forma descendente. Utiliza funciones lambda. """

from datetime import datetime
#Funcion principal
def analizar_ventas(ventas):

  # 1. Filtramos el ultimo trimestre de ventas
  ventas_filtradas = [venta for venta in ventas if datetime.strptime(venta['fecha_venta'],"%Y-%m-%d").month>=10]

  #2. Seleccionamos solo las ventas mayores a $500
  ventas_filtradas = [venta for venta in ventas_filtradas if venta['monto']>500]

  #3. Agrupar ventas por ubicacion del comprador
  ventas_agrupadas={}

  for venta in ventas_filtradas:
    ubicacion=venta['ubicacion']
    if ubicacion not in ventas_agrupadas:
      ventas_agrupadas[ubicacion]=[]
    ventas_agrupadas[ubicacion].append(venta)
  #4 Calculamos el promedio de monto de ventas para cada ubicacion

  promedio_ventas={}
  for ubicacion in ventas_agrupadas:
    ventas_por_ubicacion = ventas_agrupadas[ubicacion]
    promedio_ventas[ubicacion]=sum(venta['monto'] for venta in ventas_por_ubicacion )/len(ventas_por_ubicacion)

  #5 Ordenar de forma descendente las ubicaciones por promedio de ventas
  ubicaciones_ordenadas = sorted(promedio_ventas,key= lambda ubicacion:promedio_ventas[ubicacion],reverse=True)

  #Muestre la ubicacion y sus promedios
  for ubicacion in ubicaciones_ordenadas:
    print(f'{ubicacion}:{promedio_ventas[ubicacion]}')



ventas = [
    {"nombre_producto": "iPhone 13", "fecha_venta": "2023-10-01", "monto": 1000, "ubicacion": "Ecuador"},
    {"nombre_producto": "MacBook Pro", "fecha_venta": "2023-11-01", "monto": 2000, "ubicacion": "Argentina"},
    {"nombre_producto": "MacBook Pro 4", "fecha_venta": "2023-12-01", "monto": 3000, "ubicacion": "Argentina"},
    {"nombre_producto": "Samsung Galaxy S22", "fecha_venta": "2023-12-01", "monto": 500, "ubicacion": "Bolivia"},
    {"nombre_producto": "Samsung Galaxy S12", "fecha_venta": "2024-01-12", "monto": 300, "ubicacion": "Chile"},
]
analizar_ventas(ventas)