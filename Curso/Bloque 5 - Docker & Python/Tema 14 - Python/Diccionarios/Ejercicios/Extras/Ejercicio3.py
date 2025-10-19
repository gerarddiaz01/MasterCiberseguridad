'''Crea un diccionario menu con platos como claves y precios como valores. Luego:
Pregunta al usuario qué plato quiere pedir.
Muestra el precio si existe, o indica que no está disponible.
Agrega un nuevo plato llamado sopa con precio 5.0.'''

menu = {
    "pasta": 10.0,
    "pizza": 12.5,
    "ensalada": 8.0
}
menu["sopa"] = 5.0

plato = input("\nQue plato desea pedir?: ").lower()
precio = menu.get(plato)

if precio: # si precio existe then continuamos, es lo mismo que comprobar si el plato existe o no
    print(f"El precio de {plato} es ${precio}")
else:
    print("Lo sentimos, ese plato no está disponible.")