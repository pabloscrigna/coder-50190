"""
Partir de la clase CalculadoraCientifica(Calculadora)

En CalculadoraCientifica agregar un atributo mas

modo: "Decimal" / "Binario"

Ver:

Las dos formas de init
Extender el metodo suma

"""

class Calculadora:

    def __init__(self, numero1, numero2):
        print("Init calculadora")
        self.numero1 = numero1
        self.numero2 = numero2
        


    def suma(self):
        print("Metodo  suma calculadora")
        resultado = self.numero1 + self.numero2
        return resultado
    

    def resta(self):
        resultado = self.numero1 - self.numero2
        return resultado



class CalculadoraCientifica(Calculadora):


    #def __init__(self, numero1, numero2, modo):
    #    self.numero1 = numero1
    #    self.numero2 = numero2
    #    self.modo = modo

    def __init__(self, numero1, numero2, modo):
        print("Init cientifica")
        self.modo = modo
        super().__init__(numero1, numero2)


    def suma(self):
        print("Metodo suma clase cientifica")
        resultado = super().suma()
        return resultado

calculo = CalculadoraCientifica(10, 2, "Decimal")

print(f"suma: {calculo.suma()}")









