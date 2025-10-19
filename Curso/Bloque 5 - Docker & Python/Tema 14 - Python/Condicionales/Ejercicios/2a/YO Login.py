#pedir la contraseña al usuario
password = input("Introduce la contraseña: ")

#decir cual es la contraseña correcta
ok_password = "gerard1"

#verificar si la contraseña es correcta, sino lo es pedir de nuevo
if password.lower() == ok_password:
    print("¡Bienvenido, Gerard!")
else:
    print("¡Contraseña incorrecta!")
    again_password = input("Introduce la contraseña de nuevo: ")
    if again_password.lower() == ok_password:
        print("¡Bienvenido, Gerard!")
    else:
        print("¡Contraseña incorrecta, límite alcanzado!")

