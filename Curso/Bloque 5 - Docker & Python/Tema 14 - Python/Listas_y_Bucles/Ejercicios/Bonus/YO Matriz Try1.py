'''
Crea un script que dada una lista de listas M (numérica), identifique si se trata de una matriz y en
ese caso imprima dos listas correspondientes a:
1. La fila cuyos elementos suman el máximo
2. La columna cuyos elementos suman el máximo
Si no se trata de una matriz devolverá dos listas vacías.
'''


M = [[2,5,3],
     [6,1,8],
     [2,5,4]]

#Verificar que M sea una matriz
n_columnas = len(M[0])
n_filas = len(M)
es_matriz = True

for i in range(0, n_filas):
    if n_columnas != len(M[i]):
        es_matriz = False
if es_matriz == True:
    print("Es una matriz, podemos continuar con el ejercicio")
print("----------")

#Parte 1
sum_max = 0
for i in range(0, n_filas):
    suma_fila = sum(M[i])
    if suma_fila > sum_max:
        sum_max = suma_fila
        num_fila_max = i
print("La fila que mas suma es la fila", num_fila_max, "que suma un total de", sum_max)
print("----------")

'''
M = [[2,5,3],
     [6,1,8],
     [2,5,4]]
     '''

#Parte 2
suma_max = 0
for j in range(0, n_columnas):
    columna=[]
    suma_columna = 0
    for fila in M:
        columna.append(fila[j])
        suma_columna = suma_columna + fila[j]
        if suma_columna > suma_max:
            suma_max = suma_columna
            num_columna_max = j
print("La columna que mas suma es la columna", num_columna_max, "que suma un total de", suma_max)


