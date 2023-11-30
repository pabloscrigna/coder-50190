""""
Realiza la herencia múltiple respetando este diagrama de Clases UML.
Y crear dos Cetáceos.
"""


class Mamifero:

    def __init__(self, cantMamas, esperanzaDeVida):
        self.cantMamas = cantMamas
        self.esperanzaDeVida = esperanzaDeVida

    def mamar(self):
        print("Metodo mama clase Mamifero")
        return

    def nacer(self):
        print("Metodo nacer clase Mamifero")
        return


class AnimalMarino:

    def __init__(self, tieneBranqueas, especie):
        self.tieneBranquias = tieneBranqueas
        self.especie = especie

    def nadar(self):
        print("Metodo nadar clase AnimalMarino")
        return


class Cetaceo(Mamifero, AnimalMarino):

    def __init__(self, notas, viveEn, peso, cantMamas, esperanzaDeVida, tieneBranqueas, especie):

        self.notas = notas
        self.viveEn = viveEn
        self.peso = peso

        Mamifero.__init__(self, cantMamas, esperanzaDeVida)
        AnimalMarino.__init__(self, tieneBranqueas, especie)

    def nacer(self):
        print("Metodo nacer clase Cetaceo")
        # llama al metodo nacer de la clase Mamifero
        super().nacer()


    def nadar(self):
        print("Metodo nadar clase Cetaceo")
        # llama al metodo nadar de la clase AnimalMarino
        super().nadar()


ballena = Cetaceo("animal mas grande", "oceanos", 200, 2, 10, False, "ballena azul")


ballena.nacer()
ballena.nadar()

print(ballena.notas)
print(ballena.especie)
