"""
Hacer una clase Llamada

metodos: constructor - llamar - cortar


Hacer una clase Camara

metodos: constructor - foto - video

Hacer una clase Reproductor

metodos: constructor - reproducir



Hacer una clase Smartphone que herede de las anteriores
"""


class Llamadas:

    def __init__(self):
        print("init llamadas")

    def llamar(self):
        print("metodo llamar")


    def comun(self):
        print("Metodo comun llmadas")

class Camara:

    def __init__(self):
        print("Init Camara")


    def capturar(self):
        print("Metodo camara")


    def comun(self):
        print("Metodo comun camara")


class Smartphone(Camara, Llamadas):

    def __init__(self, modelo):
        print("Init smartphone")
        self.modelo = modelo
        Camara.__init__(self)
        Llamadas.__init__(self)



telefono = Smartphone("Samsung A3")


telefono.llamar()
telefono.capturar()
telefono.comun()