#pedir al usuario si cobra mas de 1000 euros al mes
salario_mensual = float(input("¿Cuánto cobras al mes? "))
salario_anual = salario_mensual * 12

#pedir si el usuario es mayor de edad
edad = int(input("¿Cuántos años tienes? "))

#calcular que tipo impositivo tiene que pagar
if edad < 18 and salario_mensual < 1000:
    print("No puedes declarar la renta")
elif edad >= 18 and salario_mensual < 1000:
    if salario_anual < 15000:
        print("Te toca pagar el 5% de tu salario anual cómo tipo impositivo")
    elif salario_anual >= 15000 and salario_anual < 25000:
        print("Te toca pagar el 15% de tu salario anual cómo tipo impositivo")
    elif salario_anual >= 25000 and salario_anual < 35000:
        print("Te toca pagar el 20% de tu salario anual cómo tipo impositivo")
    elif salario_anual >= 35000 and salario_anual < 60000:
        print("Te toca pagar el 30% de tu salario anual cómo tipo impositivo")
    elif salario_anual >= 60000:
        print("Te toca pagar el 45% de tu salario anual cómo tipo impositivo")


