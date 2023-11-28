
class Perro:

    def hablar(self):
        print("Gua gua")


class Pato:

    def hablar(self):
        print("cuak cuak")


class Gato:

    def hablar(self):
        print("miua miua")


def llamar_hablar(x):
    x.hablar()


llamar_hablar(Perro())
llamar_hablar(Gato())
llamar_hablar(Pato())
