'''Enunciado: Escribe un programa que solicite al usuario dos números (un numerador y un denominador) y 
muestre el resultado de la división del numerador por el denominador. Si el usuario ingresa un valor que 
no es numérico, el programa debe detectar el error y avisar con un mensaje sin terminar abruptamente. Si 
el denominador es cero, el programa no debe intentar dividir (ya que causaría un error); en su lugar, debe 
imprimir un mensaje indicando que la división por cero no es posible.'''

def procesar_operacion(numerador, denominador):
    try:
        resultado = int(numerador) / int(denominador)
        return resultado
    except ValueError:
        print(f"Error: El valor ingresado no es numérico.")
    except ZeroDivisionError:
        print(f"Error: No se puede dividir por 0")
    
def main():
    numerador = input("Ingrese el numerador: ")
    denominador = input("Ingrese el denominador: ")
    resultado = procesar_operacion(numerador, denominador)
    print(f"El resultado es: {resultado}")

main()

# Separación de responsabilidades: cada función tiene una responsabilidad específica, importante no mezclarlas
#   main() es el punto de entrada del programa y se ocupa de interactuar con el usuario, solicitar datos y mostrar mensajes
#   procesar_operacion() se ocupa de realizar el cálculo de la división y manejar los errores relacionados con la operación
# el print podríamos ponerlo con un else en procesar_operacion() pero está más organizado así