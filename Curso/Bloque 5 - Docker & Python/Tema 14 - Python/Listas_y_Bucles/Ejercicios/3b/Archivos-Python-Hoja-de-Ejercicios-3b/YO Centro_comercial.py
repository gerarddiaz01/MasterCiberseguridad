'''
Eres un comercial trabajando para una compañía que vende diversos productos. Quieres crear un
programa para realizar un seguimiento de los productos que has vendido y el valor total de las
ventas. Supongamos que hay un total de 10 productos.
Tú has vendido 5 de estos productos en las siguientes cantidades:
Producto 1: 3 unidades
Producto 2: 1 unidad
Producto 5: 7 unidades
Producto 6: 2 unidades
Producto 9 : 4 unidades
Los precios de cada uno de estos productos son como siguen:
Producto 1: 30.0 EU	 	 Producto 6: 44.0 EU
Producto 2: 9.8 EU	 	 Producto 7: 21.2 EU
Producto 3: 42.5 EU	 	 Producto 8: 53.2 EU
Producto 4: 32.6 EU	 	 Producto 9: 25.3 EU
Producto 5: 71.5 EU	 	 Producto 10: 57.8 EU
Crea un script que dada una lista con los productos, sus precios y las unidades vendidas, imprima
la cantidad total de ventas, el dinero facturado por producto y el dinero total. 
'''

# --- lista de productos y precios
#+ lista de unidades vendidas de cada producto
precio_productos = [30.0, 9.8, 42.5, 32.6, 71.5, 44.0, 21.2, 53.2, 25.3, 57.8]
unidades_vendidas = [3, 1, 0, 0, 7, 2, 0, 0, 4, 0]
total_ventas = sum(unidades_vendidas)

# --- bucle que recorra los productos, lo que incluye los precios y las unidades vendidas
dinero_total = 0
for i in range(len(precio_productos)):
    dinero = precio_productos[i] * unidades_vendidas[i]
    dinero_total += dinero
    print(f"Dinero facturado por producto {i+1}: {dinero} EUR")
    
# --- imprimir resultados
print(f"Cantidad total de ventas: {total_ventas}")
print(f"Dinero total facturado: {dinero_total} EUR")

#output:
#cantidad total de ventas
#dinero facturado por producto
#dinero total