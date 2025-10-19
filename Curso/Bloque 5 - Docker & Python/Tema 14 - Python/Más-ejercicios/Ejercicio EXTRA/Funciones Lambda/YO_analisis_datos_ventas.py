""" Ejercicio 5:
Problema de Análisis de Datos de Ventas:
Imagina que eres parte de una empresa de comercio electrónico y tienes información detallada 
sobre las ventas de productos. Cada venta se representa como un diccionario, que incluye el 
nombre del producto, la fecha de venta, el monto de la venta y la ubicación del comprador. 
Realiza un análisis avanzado de estas ventas.
Filtra las ventas realizadas en el último trimestre del año.
Selecciona solo las ventas de productos con un monto superior a $500.
Agrupa las ventas por ubicación del comprador.
Calcula el promedio del monto de venta para cada ubicación.
Ordena las ubicaciones por el promedio del monto de venta de forma descendente. Utiliza funciones lambda. """

from datetime import datetime

def analizar_ventas(ventas):
    # Paso 1: Filtrar ventas del último trimestre
    ventas_ultimo_trimestre = list(filter(lambda venta: int(venta["fecha_venta"].split("-")[1]) in [10, 11, 12], ventas))
    
    # Paso 2: Filtrar ventas con monto superior a $500
    ventas_monto_mayor_500 = list(filter(lambda venta: venta["monto"] > 500, ventas_ultimo_trimestre))
    
    # Paso 3: Agrupar ventas por ubicación
    ventas_por_ubicacion = {}
    for venta in ventas_monto_mayor_500:
        pais = venta["ubicacion"]
        if pais not in ventas_por_ubicacion:
            ventas_por_ubicacion[pais] = []
        ventas_por_ubicacion[pais].append(venta["monto"])
    
    # Paso 4: Calcular el promedio del monto de venta por ubicación
    promedio_por_ubicacion = {pais: sum(montos) / len(montos) for pais, montos in ventas_por_ubicacion.items()}
    
    # Paso 5: Ordenar las ubicaciones por promedio de venta (descendente)
    ubicaciones_ordenadas = sorted(promedio_por_ubicacion.items(), key=lambda x: x[1], reverse=True)
    
    return ubicaciones_ordenadas

# Lista de ventas
ventas = [
    {"nombre_producto": "iPhone 13", "fecha_venta": "2023-10-01", "monto": 1000, "ubicacion": "Ecuador"},
    {"nombre_producto": "MacBook Pro", "fecha_venta": "2023-11-01", "monto": 2000, "ubicacion": "Argentina"},
    {"nombre_producto": "MacBook Pro 4", "fecha_venta": "2023-12-01", "monto": 3000, "ubicacion": "Argentina"},
    {"nombre_producto": "Samsung Galaxy S22", "fecha_venta": "2023-12-01", "monto": 500, "ubicacion": "Bolivia"},
    {"nombre_producto": "Samsung Galaxy S12", "fecha_venta": "2024-01-12", "monto": 300, "ubicacion": "Chile"},
]

# Analizar ventas
resultado = analizar_ventas(ventas)
print("Ubicaciones ordenadas por promedio de venta:")
for ubicacion, promedio in resultado:
    print(f"{ubicacion}: ${promedio:.2f}")