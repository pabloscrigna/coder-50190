"""
En la clase ClaculadoraCientifica


Sobreescribir los metodos suma y __init__

"""


class Calculadora:

    def __init__(self, numero1, numero2):
        print("init calculadora")
        self.numero1 = numero1
        self.numero2 = numero2

    def suma(self):
        print("Metodo suma Calculadora")
        resultado = self.numero1 + self.numero2
        return resultado
    
    def resta(self):
        print("Resta Calculadora")
        resultado = self.numero1 - self.numero2
        return resultado




class CalculadoraCientifica(Calculadora):

    def __init__(self, numero1, numero2):
        print("metodo init cientifica")
        self.numero1 = numero1
        self.numero2 = numero2


    def multiplicacion(self):
        resultado = self.numero1 * self.numero2
        return resultado
    

    def division(self):
        resultado = self.numero1 / self.numero2
        return resultado
    

calculo = CalculadoraCientifica(10,2)


print(f"suma: {calculo.suma()}")
print(f"resta: {calculo.resta()}")
print(f"multiplicacion: {calculo.multiplicacion()}")
print(f"division: {calculo.division()}")