'''
Crea un programa que valide un formulario de registro. Crea una función
llamada validar_formulario que reciba diferentes campos de un formulario
(nombre, correo electrónico y número de teléfono) y verifique si los valores
ingresados cumplen con los requisitos especificados, siendo estos:
1. Que el nombre tenga una longitud minima de 3 caracteres
2. Que el teléfono este conformado por dígitos y tenga una longitud de 9
caracteres
3. Que el email contenga un “@“ y un “.” '''

def validar_formulario(nombre, email, numero_telefono):
    if len(nombre) < 3:
        return False
    if "@" not in email or "." not in email:
        return False
    if not numero_telefono.isdigit() or len(numero_telefono) != 9:
        return False
    return True

name = input("Introduce tu nombre (mínimo 3 carácteres): ")
email = input("Introduce tu email (obligatorio que tenga @ y .): ")
phone = input("Introduce tu numero de telefono: ")

valido = validar_formulario(name, email, phone)

if valido:
    print("Formulario válido")
else:
    print("Formulario no válido")