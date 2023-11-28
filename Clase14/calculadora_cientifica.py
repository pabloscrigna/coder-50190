"""
Definir una clase CalculadoraCientifica

Atributos

numero1
numero2

Metodos

suma
resta
multiplicacion
division

"""


class CalculadoraCientifica:

    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2


    def suma(self):
        resultado = self.numero1 + self.numero2
        return resultado
    

    def resta(self):
        resultado = self.numero1 - self.numero2
        return resultado

    def multiplicacion(self):
        resultado = self.numero1 * self.numero2
        return resultado
    
    def division(self):
        resultado = self.numero1 / self.numero2
        return resultado
    


calculo = CalculadoraCientifica(10, 2)

print(f"suma: {calculo.suma()}")
print(f"resta: {calculo.resta()}")
print(f"multiplicacion: {calculo.multiplicacion()}")
print(f"Division: {calculo.division()}")
