#Definir el precio de cada alimento
ensalada = 12
sopa = 10
dorada = 18
arroz = 14
lasaña = 15
brownie = 8
helado = 6
refresco = 5.5
cafe = 3.5

#Pedir al usuario la cantidad de cada alimento que ha consumido
cantidad_ensalada = int(input("Cuantas ensaladas has consumido? "))
cantidad_sopa = int(input("Cuantas sopas has consumido? "))
cantidad_dorada = int(input("Cuantas doradas has consumido? "))
cantidad_arroz = int(input("Cuantos arroces has consumido? "))
cantidad_lasaña = int(input("Cuantas lasañas has consumido? "))
cantidad_brownie = int(input("Cuantos brownies has consumido? "))
cantidad_helado = int(input("Cuantos helados has consumido? "))
cantidad_refresco = int(input("Cuantos refrescos has consumido? "))
cantidad_cafe = int(input("Cuantos cafes has consumido? "))

#Calcular el total a pagar de la cuenta
total = (ensalada*cantidad_ensalada) + \
    (sopa*cantidad_sopa) + \
    (dorada*cantidad_dorada) + \
    (arroz*cantidad_arroz) + \
    (lasaña*cantidad_lasaña) + \
    (brownie*cantidad_brownie) + \
    (helado*cantidad_helado) + \
    (refresco*cantidad_refresco) + \
    (cafe*cantidad_cafe)

print("El total a pagar es: ", total)
