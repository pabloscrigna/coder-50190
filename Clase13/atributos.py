"""
Leer y modificar los atributos
"""


class Cuenta:

    def __init__(self, dni, numero, saldo):
        self.dni = dni
        self.numero = numero
        self.saldo = saldo


cuenta_1 = Cuenta(123456788, 221133445566778899, 0.0)
cuenta_2 = Cuenta(123456789, 112233445566778899, 0.0)


# Ejemplos de acceder a los atributos directamente


# Ejemplos de modificar los atributos directamente