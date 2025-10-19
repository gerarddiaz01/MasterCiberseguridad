'''
ANALISIS DE DATOS - VENTAS POR MES
Supongamos que tienes un conjunto de datos de ventas de una tienda durante un año.
Cada fila representa una venta y tiene tres columnas: la fecha de la venta, el monto de la
venta y la categoría de producto vendido (por ejemplo, electrónicos, ropa, alimentos,
etc.). Quieres analizar estos datos para determinar cuánto fue el monto total de ventas en
cada mes. Para ello, puedes usar NumPy para cargar los datos en un array de 3
columnas y n filas, donde n es el número de ventas. Luego, puedes usar operaciones de
NumPy para filtrar los datos por mes y sumar los montos de venta correspondientes.
'''
'''
import numpy as np

#Crear un array de ejemplo con 10 filas y 3 columnas
#Columnas: [fecha (YYYY-MM-DD), monto de la venta, categoría de producto]
ventas = np.array([
    ['2022-01-01', 100, 'ropa'],
    ['2022-01-02', 200, 'alimentos'],
    ['2022-01-03', 150, 'ropa'],
    ['2022-02-01', 120, 'alimentos'],
    ['2022-02-02', 180, 'electrónicos'],
    ['2022-02-03', 200, 'alimentos'],
    ['2022-03-01', 90, 'ropa'],
    ['2022-03-02', 110, 'electrónicos'],
    ['2022-03-03', 100, 'alimentos']
])

#Convertir las fechas a un formato manejable, extraerlas de la lista del array
fechas = np.array([venta[0] for venta in ventas])
print(fechas)

#Crear un array para almacenar los totales por mes, extraer del array de fechas
meses = np.array([int(fecha[5:7]) for fecha in fechas])
print(meses)

#Sumar los montos de venta por mes usando un bucle
montos_mes = np.zeros(12)
for mes in range(1,13):
    ventas_mes = ventas[meses == mes]
    montos_mes[mes-1] = np.sum(ventas_mes[:,1].astype(int))

#Mostrar los resultados
print("Monto total de ventas por mes:", montos_mes)'
'''

# importar modulos
import numpy as np

# Datos de ventas de la tienda / input
ventas = np.array([
    ['2022-01-01', 100, 'ropa'],
    ['2022-01-02', 200, 'alimentos'],
    ['2022-01-03', 150, 'ropa'],
    ['2022-02-01', 120, 'alimentos'],
    ['2022-02-02', 180, 'electrónicos'],
    ['2022-02-03', 200, 'alimentos'],
    ['2022-03-01', 90, 'ropa'],
    ['2022-03-02', 110, 'electrónicos'],
    ['2022-03-03', 100, 'alimentos']
])

# Extraer las fechas
fechas = np.array([venta[0] for venta in ventas])

# Extraer el mes
meses = np.array([int(fecha[5:7]) for fecha in fechas])

montos_mes = np.zeros(12)
# sumar los montos de venta por mes
for mes in range(1,13):
    # ventas relacionadas con ese mes
    ventas_mes = ventas[meses == mes]
    # suma de las ventas del mes en cuestion
    montos_mes[mes-1] = np.sum(ventas_mes[:,1].astype(int))

#print
print(f"Monto total de ventas por mes {montos_mes}")
