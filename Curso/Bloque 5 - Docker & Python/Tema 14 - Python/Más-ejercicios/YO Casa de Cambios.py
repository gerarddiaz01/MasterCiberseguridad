# cantidad_euros = float(input("Ingresa cuantos euros deseas cambiar: "))
# cambio_dolares = cantidad_euros * 1.2
# tasa_gestion = cambio_dolares * 0.1
# cantidad_final = cambio_dolares - tasa_gestion
# print("Te damos " + str(cantidad_final) + " dolares")
# print("La tasa de gestión es ", str(tasa_gestion))
# print("La cantidad en dolares antes de las comisones es ", cambio_dolares)

#Pedir al usuaro que ingrese la cantidad de euros que desea cambiar
euros = input("Ingresa la cantidad de euros que deseas cambiar: ")

#Convertir la cantidad ingresada a float
euros = float(euros)

#Convertir la cantidad de euros a dolares
dolares = euros * 1.2

#Imprimir el resultado de la conversion
# print("euros, "euros son", dolares, "dolares")
      
#Calculamos la tasa de gestion
tasa_gestion = dolares * 0.1

#Calculamos la cantidad de dolares que recibe el usuario
cantidad_final = dolares - tasa_gestion

#Imprimimos el desglose de la operacion
print("Monto ingresado: ", euros, "euros")
print("Cambio en dolares", dolares, "dolares")
print("Tasa de gestion: ", tasa_gestion, "dolares")
print("Monto recibido: ", cantidad_final, "dolares")