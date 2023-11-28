"""
Definir una clase Calculadora:

Atributos:

numero1
numero2

Metodos:

suma
resta

"""


class Calculadora:

    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2


    def suma(self):
        resultado = self.numero1 + self.numero2
        return resultado
    

    def resta(self):
        resultado = self.numero1 - self.numero2
        return resultado



calculo = Calculadora(10, 2)

print(f"suma: {calculo.suma()}")
print(f"resta: {calculo.resta()}")


calculo = Calculadora(20, 2)

print(f"suma: {calculo.suma()}")
print(f"resta: {calculo.resta()}")