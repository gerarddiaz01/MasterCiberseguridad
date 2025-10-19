#pedimos el nombre del usuario
nombre = input("Introduce tu nombre: ")

#saludar al usuario
print("Hola", nombre)

#pedimos el salario por hora y el número de horas trabajadas
salario_hora = float(input("Introduce tu salario por hora: "))
horas_trabajadas = float(input("Introduce el número de horas trabajadas: "))

#calculamos el salario semanal, mensual y anual
salario_semanal = salario_hora * horas_trabajadas
salario_mensual = salario_semanal * 4
salario_anual = salario_mensual * 12

#imprimimos el salario anual
print(nombre.title(), "tus ganancias anuales son de", salario_anual, "euros")

#pedimos los gastos semanales
gastos_semanales = float(input("Introduce tus gastos semanales: "))

#calculamos los gastos mensuales y anuales
gastos_mensuales = gastos_semanales * 4
gastos_anuales = gastos_mensuales * 12

#calculamos los ahorros anuales
ahorros_anuales = salario_anual - gastos_anuales

#imprimimos los ahorros anuales
print(nombre.title(), "tus ahorros anuales son de", ahorros_anuales, "euros")

