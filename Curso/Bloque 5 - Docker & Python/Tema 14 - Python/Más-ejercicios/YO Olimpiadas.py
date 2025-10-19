# #Pedir los tiempos por pantalla
# print("Introduce el tiempo de Hannah Neise")
# minutos = int(input("Minutos: "))
# segundos = int(input("Segundos: "))
# centesimas = int(input("Centesimas: "))
# hannah = minutos*60 + segundos + centesimas/100

# print("Introduce el tiempo de Jackie Narracott")
# minutos = int(input("Minutos: "))
# segundos = int(input("Segundos: "))
# centesimas = int(input("Centesimas: "))
# jackie = minutos*60 + segundos + centesimas/100

# print ("Introduce el tiempo de Kimberly Bos")
# minutos = int(input("Minutos: "))
# segundos = int(input("Segundos: "))
# centesimas = int(input("Centesimas: "))
# kimberly = minutos*60 + segundos + centesimas/100

# #Calcular la velocidad media
# distancia = 100
# velocidad_hannah = distancia/hannah
# velocidad_jackie = distancia/jackie
# velocidad_kimberly = distancia/kimberly

# #Imprimir los resultadosç
# print("La velocidad media de Hannah Neise es de ", velocidad_hannah, "m/s")
# print("La velocidad media de Jackie Narracott es de ", velocidad_jackie, "m/s")
# print("La velocidad media de Kimberly Bos es de ", velocidad_kimberly, "m/s")

#Pedir los tiempos por pantalla
tiempo_hannah = input("Introduce el tiempo de Hannah Neise (formato: minutos segundos centésimas): ")
tiempo_jackie = input("Introduce el tiempo de Jackie Narracott (formato: minutos segundos centésimas): ")
tiempo_kimberly = input("Introduce el tiempo de Kimberly Bos (formato: minutos segundos centésimas): ")

#Separar los tiempos en minutos, segundos y centésimas
minutos_hannah, segundos_hannah, centesimas_hannah = tiempo_hannah.split(" ") #split separa los elementos de una cadena de texto, en éste caso siguiendo los espacios cómo referencia
minutos_jackie, segundos_jackie, centesimas_jackie = tiempo_jackie.split(" ")
minutos_kimberly, segundos_kimberly, centesimas_kimberly = tiempo_kimberly.split(" ")

#Convertimos los tiempos a segundos
tiempo_hannah = float(minutos_hannah)*60 + float(segundos_hannah) + float(centesimas_hannah)*0.01
tiempo_jackie = float(minutos_jackie)*60 + float(segundos_jackie) + float(centesimas_jackie)*0.01
tiempo_kimberly = float(minutos_kimberly)*60 + float(segundos_kimberly) + float(centesimas_kimberly)*0.01

#Calcular la velocidad media
velocidad_hannah = 100/tiempo_hannah
velocidad_jackie = 100/tiempo_jackie
velocidad_kimberly = 100/tiempo_kimberly

#Imprimir los resultados por pantalla
print("La velocidad media de Hannah Neise fue de ", velocidad_hannah, "metros por segundo")
print("La velocidad media de Jackie Narracott fue de ", velocidad_jackie, "metros por segundo")
print("La velocidad media de Kimberly Bos fue de ", velocidad_kimberly, "metros por segundo")

