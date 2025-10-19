#pedir al usuario que introduzca su contraseña
password = input("Introduce la contraseña: ")

#crear límites de la contraseña segura
contains_a = "a" in password
contains_e = "e" in password
contains_i = "i" in password
contains_o = "o" in password
contains_u = "u" in password
contains_vowels = contains_a or contains_e or contains_i \
    or contains_o or contains_u
contains_asterisk = "*" in password
contains_hashtag = "#" in password
contains_special_characters = contains_asterisk and contains_hashtag

#comprobar si la contraseña es segura, si lo es print por pantalla
if contains_vowels and contains_special_characters:
    print("Contraseña segura")
else:
    print("Contraseña insegura")