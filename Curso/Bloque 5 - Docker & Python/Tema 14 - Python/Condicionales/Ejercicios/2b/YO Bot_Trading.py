#Pedir precio al usuario
precio = float(input("Introduce el precio del producto: "))

#Crear ordenes para el bot según el precio
if precio < 100:
    print("Comprar")
elif precio >= 100 and precio <= 150:
    print("Hold")
else:
    print("Vender")


