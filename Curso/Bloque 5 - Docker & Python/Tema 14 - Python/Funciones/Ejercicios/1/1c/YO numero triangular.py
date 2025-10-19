'''Crea una función recursiva llamada numero_triangular que calcule el n-ésimo
número triangular. Un número triangular se obtiene al sumar todos los
números naturales desde 1 hasta n'''

def numero_triangular(n):
    ''' Calcular el valor del numero triangular de n'''
    #input: int positivo
    #output: resultado int positivo

    # caso base
    if n == 1:
        return 1
    
    # sentencia recursiva
    else:
        return n + numero_triangular(n-1)
    
print(numero_triangular(4))

# Ejemplo de cómo debería funcionar:

# Si n = 4, el cálculo sería:
# numero_triangular(4) = 4 + numero_triangular(3)
# numero_triangular(3) = 3 + numero_triangular(2)
# numero_triangular(2) = 2 + numero_triangular(1)
# numero_triangular(1) = 1 (caso base).
# Resolviendo:
# numero_triangular(1) = 1
# numero_triangular(2) = 2 + 1 = 3
# numero_triangular(3) = 3 + 3 = 6
# numero_triangular(4) = 4 + 6 = 10