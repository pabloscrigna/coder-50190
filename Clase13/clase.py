"""
Definir una clase Cuenta con 3 atributos
"""


class Cuenta:

    def __init__(self, dni, numero, saldo):
        self.dni = dni
        self.numero = numero
        self.saldo = saldo


cuenta_1 = Cuenta(123456788, 221133445566778899, 0.0)

print(f"cuenta es un instancia de la clase Cuenta: {type(cuenta_1)} ")
