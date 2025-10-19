'''El gobierno quiere otorgar becas de excelencia a los estudiantes con un mínimo 
de un 8 de media. Además para acceder a la beca el estudiante debe tener entre 17 
y 21 años. Crea un script que pida el nombre, la edad y la nota media del estudiante 
e indique si puede optar a la beca o no'''

#Pedir el nombre del estudiante
name = input("Introduce tu nombre: ")

#Pedir la edad del estudiante
age = int(input("Introduce tu edad: "))

#Pedir la nota media del estudiante
average = float(input("Introduce tu nota media: "))

#Verificar si el estudiante puede optar a la beca
if 17 <= age <= 21 and average >= 8:
    print(f"{name}, puedes optar a la beca de excelencia.")
else:
    print(f"{name}, no puedes optar a la beca de excelencia.")

          