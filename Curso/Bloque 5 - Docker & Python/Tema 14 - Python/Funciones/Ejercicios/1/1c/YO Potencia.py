'''Implementa una función recursiva llamada potencia que calcule el resultado
de elevar un número a una potencia dada. Puedes asumir que tanto el
número como la potencia son enteros no negativos.'''

def potencia(base, exponente):
    '''Calcula la potencia de un numero'''
    # input: base (int positivo), exponente (int positivo)
    # output: int positivo

    # caso base
    if exponente == 0:
        return 1
    
    # sentencia recursiva
    else:
        return base * potencia(base, exponente - 1)

print(potencia(2, 3))

'''
2 * potencia(2, 2)
2 * 2 * potencia(2, 1)
2 * 2 * 2 * potencia(2, 0) # aqui al ser el exponente 0 se hace un return de 1 y termina la recursividad
2 * 2 * 2 * 1 = 8
'''
# the function will compute 2 * potencia(2, 2), which in turn computes 2 * potencia(2, 1)
# and so on, until it reaches potencia(2, 0).