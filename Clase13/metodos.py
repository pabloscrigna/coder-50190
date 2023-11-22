"""
Agregar metodos para leer y escribir los atributos

Calcular impuesto = 0,21 * saldo
"""


class Cuenta:

    def __init__(self, dni, numero, saldo):
        self.dni = dni
        self.numero = numero
        self.saldo = saldo
