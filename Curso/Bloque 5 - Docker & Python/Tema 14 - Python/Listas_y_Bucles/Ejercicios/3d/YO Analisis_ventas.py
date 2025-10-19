'''
Supongamos que eres el propietario de una tienda en línea y tienes una lista de ventas de los
últimos 30 días. Quieres analizar las ventas por día de la semana para identificar los días de mayor
venta.
Pista 1: Puedes crear dos listas, una con las ventas por cada día del mes como por ejemplo…
ventas = [120, 80, 140, 200, 75, 100, 180, 220, 160, 110, 90, 120, 170, 190, 250, 300, 95, 110,
140, 180, 200, 160, 120, 80, 170, 150, 210, 190, 230, 250]
Y otra lista con los días de la semana:
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo“]
Después puedes crear una nueva lista con una entrada por cada día de la semana y usar un bucle
para añadir a esta lista la suma de las ventas correspondientes a cada uno de los días de la
semana.
Pista 2: Puede que necesites una variable que lleve la cuenta del día de la semana actual y se
reinicie a cero cuando llegue al séptimo día. 
'''

#Definir las listas de venta y la lista de los dias de la semana
ventas = [120, 80, 140, 200, 75, 100, 180, 220, 160, 110, 90, 120, 170, 190, 250, 300, 95, 110, 140, 180, 200, 160, 120, 80, 170, 150, 210, 190, 230, 250]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado","Domingo"]

#inicializar una lista para almacenar las ventas por dia de la semana
ventas_dia = [0, 0, 0, 0, 0, 0, 0]

#recorrer la lista de ventas y sumar las ventas correspondientes a cada dia de la semana
dia_semana = 0
for venta in ventas:
   ventas_dia[dia_semana] += venta
   dia_semana += 1
   if dia_semana == 7:
     dia_semana = 0

'''
dia_semana2 = 0
for dia in dias_semana:
    print(f"El {dia} se hicieron {ventas_dia[dia_semana2]} ventas")
    dia_semana2 += 1'
'''

for i in range(len(dias_semana)):
   print(dias_semana[i], ":", ventas_dia[i])
