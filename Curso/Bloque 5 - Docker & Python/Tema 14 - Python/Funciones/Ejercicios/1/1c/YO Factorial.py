'''Implementa una función recursiva llamada factorial que calcule el factorial de
un número entero positivo. El factorial de un número n se define como el
producto de todos los números enteros positivos desde 1 hasta n.
(El factorial de 0 y de 1 es igual a 1)'''

def factorial(n):
    ''' Calcula el factorial de n'''
    # input: n: int
    # output: resultado: int
    if n == 0 or n == 1:
        return 1
    else: 
        resultado = n * factorial(n-1)
    return resultado

print(factorial(4))

'''
4 * factorial(3)
4 * 3 * factorial(2)
4 * 3 * 2 * factorial(1)
4 * 3 * 2 * 1
'''
# If n is greater than 1, the function proceeds to the else block. Here, it calculates the factorial by multiplying n by the result 
# of a recursive call to factorial(n-1). This recursive call reduces the value of n by 1 in each step, 
# gradually working its way toward the base case.
# For example, if n = 4, the function computes 4 * factorial(3), which in turn computes 3 * factorial(2), and so on, 
# until it reaches factorial(1).