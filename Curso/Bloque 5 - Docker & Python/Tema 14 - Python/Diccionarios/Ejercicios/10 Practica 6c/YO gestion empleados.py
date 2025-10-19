'''
Imagina que eres el gerente de recursos humanos de una empresa y
necesitas gestionar la información de los empleados. Cada empleado
tiene un nombre, salario y departamento al que pertenece. Implementa
un programa en Python que permita agregar nuevos empleados,
actualizar el salario de un empleado existente, mostrar la lista completa
de empleados y calcular el promedio salarial por departamento.
'''

empleados = {}
condition = True

while condition == True:
    menu = input(f"MENU\n1.Agregar nuevo empleado\n2.Actualizar salario\n3.Mostrar lista de empleados\n4.Calcular promedio salarial por departamento\n5.Salir\nEscoge una de las siguientes opciones: ")
    print("")
    
    if menu == "1":  # Agregar nuevo empleado
        nuevo_empleado = input("Nombre: ")
        nuevo_salario = input("Salario: ")
        
        # Validar que el salario sea un número
        if not nuevo_salario.isdigit():
            print("Error: El salario debe ser un número.\n")
            continue
        
        nuevo_salario = int(nuevo_salario)
        nuevo_departamento = input("Departamento: ")
        empleados[nuevo_empleado] = {"salario": nuevo_salario, "departamento": nuevo_departamento}
        print("Empleado agregado correctamente.\n")
    
    elif menu == "2":  # Actualizar salario
        empleado_modif = input("De qué empleado desea actualizar el salario? ")
        if empleado_modif in empleados:
            new_salary = input("Introduce el nuevo salario: ")
            
            # Validar que el nuevo salario sea un número
            if not new_salary.isdigit():
                print("Error: El salario debe ser un número.\n")
                continue
            
            new_salary = int(new_salary)
            empleados[empleado_modif]["salario"] = new_salary
            print("Salario actualizado correctamente.\n")
        else:
            print("El empleado no está en la base de datos.\n")
    
    elif menu == "3":  # Mostrar lista de empleados
        if not empleados:
            print("No hay empleados registrados.\n")
        else:
            print("Lista de empleados:")
            for clave in empleados.keys():
                print(clave)
            print("")
    
    elif menu == "4":  # Calcular promedio salarial por departamento
        if not empleados:
            print("No hay empleados registrados.\n")
        else:
            salarios_departamento = {}
            for empleado, datos in empleados.items():
                departamento = datos["departamento"]
                salario = datos["salario"]
                if departamento not in salarios_departamento:
                    salarios_departamento[departamento] = []
                salarios_departamento[departamento].append(salario)
            
            for departamento, salarios in salarios_departamento.items():
                promedio = sum(salarios) / len(salarios)
                print(f"El promedio salarial del departamento {departamento} es {promedio:.2f}")
            print("")
    
    elif menu == "5":  # Salir del programa
        condition = False
        print("Saliendo del programa...")
    
    else:  # Opción no válida
        print("Ésta opción no está disponible, escoja otra opción.\n")

