"""

Clase Cilindro

Atributos

radio 
altura

Metodos

Volumen pi x radio **2 x altura

cambiar el radio y la altura

str : ver los datos del cilindro

"""

from math import pi

class Cilindro:

    figura = "Cilindro"

    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura


    def volumen(self):
        volumen = pi * self.radio**2 * self.altura
        return volumen

    def cambiar_valores(self, radio, altura):
        self.radio = radio
        self.altura = altura
        return
       

figura1 = Cilindro(10,5)
figura2 = Cilindro(5,10)

print(figura1.figura)
print(figura2.figura)
print(Cilindro.figura)

volumen = figura1.volumen()
print(round(volumen,2))

