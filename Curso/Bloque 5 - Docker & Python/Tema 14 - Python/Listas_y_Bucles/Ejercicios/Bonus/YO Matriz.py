'''
Crea un script que dada una lista de listas M (numérica), identifique si se trata de una matriz y en
ese caso imprima dos listas correspondientes a:
1. La fila cuyos elementos suman el máximo
2. La columna cuyos elementos suman el máximo
Si no se trata de una matriz devolverá dos listas vacías.
Por ejemplo:
M1=[[2,5,3],[6,1,8],[7,5,4]] devolverá: L1 = [7,5,4] y L2 = [2,6,9,7]
M2 = [[4,2,3],[4,5],[6,8,2]] devolverá: L1 = [] y L2 = []
(Nota: Definimos matriz como una lista de listas donde todas las listas internas tienen el mismo
numero de objetos) 
'''

#Definir la lista de listas (matriz)
M = [[2,5,3],
     [6,1,8],
     [2,5,4]]

#Verificar si M es una matriz
n_columnas = len(M[0])
n_filas = len(M)
es_matriz = True

#Recorrer M para comparar la longitud de la lista de referencia con las demás
for i in range(0, n_filas):
    if len(M[i]) != n_columnas:
        es_matriz = False
        break

#Parte 1: Tengo que encontrar la fila cuyos numeros suman el máximo

if es_matriz == True:
    sum_max = 0
    for i in range(0, n_filas):
        suma_fila = sum(M[i])
        if suma_fila > sum_max:
            sum_max = suma_fila
            num_fila = i

print(f"La fila cuyos numeros suman el máximo es la fila {num_fila}, y suman {sum_max}")

#Parte 2: Tengo que encontrar la columna cuyos numeros suman el maximo

'''
M = [[2,5,3],
     [6,1,8],
     [2,5,4]]
'''
if es_matriz == True:
    suma_max = 0
    for j in range(0, n_columnas):
        columna = []
        suma_columna = 0
        for fila in M:
            columna.append(fila[j])
            suma_columna = suma_columna + fila[j]
            if suma_columna > suma_max:
                suma_max = suma_columna
                num_columna = j
            
print(f"La columna cuyos numeros suman el máximo es la columna {num_columna}, y suman {suma_max}")
