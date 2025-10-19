'''Un problema común al solicitar una entrada numérica ocurre cuando las
personas ingresan texto en lugar de números. Cuando intentas convertir la
entrada a un entero (int), obtendrás un ValueError. Escribe un programa que
solicite dos números. Suma los números y muestra el resultado. Captura el
ValueError si alguno de los valores de entrada no es un número e imprime un
mensaje de error amigable. Prueba tu programa ingresando dos números y
luego ingresando texto en lugar de un número. Envuelve tu código del en un
bucle while para que el usuario pueda continuar ingresando números incluso
si comete un error ingresando texto en lugar de un número'''

while True:
    try:
        numero1 = int(input("Ingrese un numero: "))
        numero2 = int(input("Ingrese otro numero: "))
        print(numero1 + numero2)
        break
    except ValueError:
        print("Error inesperado: Has ingresado texto en lugar de numeros, vuelve a intentarlo.")
