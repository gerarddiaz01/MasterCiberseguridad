import pandas as pd
import numpy as np

def calulo(vector):

    #Media

    suma=0
    n=0

    for elemento in vector:

        suma+=elemento
        n+=1

    media=(1/n)*suma
    
    print('media',media)

    #alternativas

    suma=sum(vector)
    n=len(vector)

    media=(1/n)*suma
    
    print('media_2',media)

    moda=0
    repeticiones=0

    diccionario={}

    for elemento in vector:

        if not diccionario.get(elemento):

            diccionario[elemento]=1
        else:
            diccionario[elemento]+=1

        if diccionario[elemento]>repeticiones:
            repeticiones = diccionario[elemento]  # Fe de erratas
            moda=elemento

    print('moda es:',moda)


    #Mediana

    vector.sort(reverse=False) #ordenar de menor a mayor

    punto_medio=int(len(vector)/2)

    if len(vector) % 2 ==0:

        mediana= (vector[punto_medio] + vector[punto_medio+1])/2

    else:
        mediana= vector[punto_medio]

    print('La mediana es:',mediana)


Vector =[1,2,3,4,5,6,7,8,9,8,6,5,7,5]

# calulo(Vector)

df=pd.read_csv('Salary_data.csv',sep=";")

# print(df.head())

print(df.age.mean())
print(df.age.mode())

V=np.array(Vector)
print(V.mean())