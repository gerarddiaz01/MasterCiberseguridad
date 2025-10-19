# Atributos privados
class Ejemplo:
    def __init__(self):
        self.__atributo_privado = 10

    def get_atributo(self):
        print(f"{ self.__atributo_privado*2}")


valor = Ejemplo()
valor.get_atributo()
valor.__atributo_privado = 20


# Atributos protegidos
class Ejemplo:
    def __init__(self):
        self._atributo_protegido = 20

    def get_atributo(self):
        print(self._atributo_protegido)


valor = Ejemplo()
print(valor._atributo_protegido)  # no es correcto / se puede lograr
valor.get_atributo()
