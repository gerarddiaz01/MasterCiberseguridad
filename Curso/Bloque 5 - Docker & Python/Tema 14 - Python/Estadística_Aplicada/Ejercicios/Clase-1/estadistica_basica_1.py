
def calculo(vector):
    # Media

    suma = 0 # para almacenar la suma de todos los números en el vector
    n = 0 # para contasr cuántos números hay en el vector

    for elemento in vector: # recorremos cada número de la lista vector
        suma += elemento # el número actual elemento se suma a suma
        n += 1 # se incrementa n en 1 para saber cuantos elementos se han procesado
    # cuando el bucle termina, suma contiene la suma total de los numeros y n contiene la cantidad de numeros
    media = (1/n) * suma # formula de la media en Python
    print("media", media)

    # Alternativa para calcular la media
    suma = sum(vector)
    n = len(vector)

    media = (1/n) * suma
    print("media2", media)

    # Moda

    moda = 0
    repeticiones = 0 # almacena la cantidad maxima de veces que un numero se repite
    diccionario={} # diccionario vacío para contar cuantas veces aparece cada numero en el vector

    for elemento in vector:
        if not diccionario.get(elemento): # si el numero no esta en el diccionario...
            diccionario[elemento] = 1 # ...se agrega al diccionario con un valor inicial de 1, indicando que ha aparecido una vez
        else: # si el numero ya está en el diccionario...
            diccionario[elemento] += 1 # ...se incrementa su valor en 1, ya que estará en el diccionario con su nombre de apariciones
        
        if diccionario[elemento] > repeticiones: # si elemento tiene más repeticiones que el valor almacenado en repeticiones...
            moda = elemento # ...actualizamos la moda con el valor de elemento
            repeticiones = diccionario[elemento] # actualizamos repeticiones con el numero de veces que aparece elemento
            # repeticiones empieza en 0 y se va actualizando elemento a elemento, sube a 1 con el primer numero y se queda en 1
            # hasta que encuentra un numero repetido (porque if diccionario[elementoNoRepetido] > repeticiones → 1 > 1 (falso))
            # de momento todos los numeros tienen una sola repeticion, cuando llegamos a un numero repetido la variable repeticiones...
            # ... se actualiza a 2 porque hemos encontrado un numero que ya estaba en la lista y la moda se actualiza a ése elemento...
            # ... porque es el mas repetido de momento.
    
    print("Moda es", moda)

    # Mediana

    vector.sort(reverse=False) # ordenamos el vector de menor a mayor
    # vector = [1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9]

    punto_medio = int(len(vector) / 2) # calculamos el indice del punto medio de la lista ordenada del vector (len = 14, entonces es 7)

    if len(vector) % 2 == 0: # si la longitud de la lista es par, la mediana se calcula como el promedio de los dos valores centrales
        mediana = (vector[punto_medio] + vector[punto_medio - 1]) / 2 # en Python ponemos - 1 porque el indice empieza en 0 no en 1...
    # ... hay dos valores centrales : punto_medio - 1 (El índice del primer valor central, que en nuestro vector es el septimo ...
    # ... numero con indice [6] que corresponde a 5) y punto_medio (El índice del segundo valor central, que en nuestro ...
    # ... vector es el octavo numero con indice [7] que corresponde a 6). 5 + 6 / 2 = 5.5
    else: 
        mediana = vector[punto_medio] # si la longitud es impar es simplemente el punto medio de la lista
    
    print("mediana es ", mediana)



vector = [1,2,3,4,5,6,7,8,9,8,6,5,7,5]

calculo(vector)

