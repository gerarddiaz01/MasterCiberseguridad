sexo = input('¿Eres chico o chica? ')
nombre = input('Introduce tu nombre: ')

if sexo.lower() == "chico" and nombre.upper()[0] in "ABCDEFGH" or nombre[0] in "RSTUVWXYZ":
    print('El grupo al que perteneces es el A')
elif sexo.lower() == "chico" and nombre.upper()[0] in "IJKLMNOPQ":
    print('El grupo al que perteneces es el B')

if sexo.lower() == "chica" and nombre.upper()[0] in "EFGHIJKLM":
    print('El grupo al que perteneces es el A')
elif sexo.lower() == "chica" and nombre.upper()[0] in "ABCD" or nombre.upper()[0] in "NOPQRSTUVWXYZ":
    print('El grupo al que perteneces es el B')

