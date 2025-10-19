#Preguntar al usuario cuantos coches de cada tipo ha vendido
serie_1_vendidos = int(input("Ingrese la cantidad de coches RBM Serie 1 vendidos: "))
serie_plus_vendidos = int(input("Ingrese la cantidad de coches RBM Serie Plus vendidos: "))
todoterreno_vendidos = int(input("Ingrese la cantidad de coches RBM Todoterreno vendidos: "))

#Guardamos los datos en variables
serie_1 = 20000
serie_plus = 35000
todoterreno = 60000
comision_serie_1 = 0.3
comision_serie_plus = 0.5
comision_todoterreno = 0.7

#Calcular la comisión
beneficio_serie_1 = serie_1 * comision_serie_1 * serie_1_vendidos
beneficio_serie_plus = serie_plus * comision_serie_plus * serie_plus_vendidos
beneficio_todoterreno = todoterreno * comision_todoterreno * todoterreno_vendidos

beneficio_total = beneficio_serie_1 + beneficio_serie_plus + beneficio_todoterreno

#Imprimir la comisión por pantalla
print("La comisión por la venta de coches RBM Serie 1 es de: ", beneficio_serie_1)
print("La comisión por la venta de coches RBM Serie Plus es de: ", beneficio_serie_plus)
print("La comisión por la venta de coches RBM Todoterreno es de: ", beneficio_todoterreno)
print("La comisión total es de: ", beneficio_total)       
