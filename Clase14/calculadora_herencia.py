"""
Definir una clase Calculadora

Atributos

numero1
numero2

Metodos

constructor
suma
resta


Definir una clase CalculadoraCientifica

Herede de Calculadora

Metodos

multiplicacion
division

"""


class Calculadora:

    def __init__(self, numero1, numero2):
        print("Init calculadora")
        self.numero1 = numero1
        self.numero2 = numero2


    def suma(self):
        resultado = self.numero1 + self.numero2
        return resultado
    

    def resta(self):
        resultado = self.numero1 - self.numero2
        return resultado
    


class CalculadoraCientifica(Calculadora):
    
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
print(f"division: {calculo.division()}")


# calculo_1 = Calculadora(5,5)

# print(calculo_1.suma())


# print("metodos Calculadora")
# print(dir(calculo_1))


# print("metodos Calculadora Cientifica")
# print(dir(calculo))
