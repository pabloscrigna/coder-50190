"""
Crear una clase Atleta, que tenga su nombre, apellido, altura, peso, teléfono e
índice de masa corporal (descripción) .

Decidir que atributos deben ser públicos y cuales privados.
Crear los métodos get y set que crea necesarios.

Donde el imc es es peso dividido, la altura al cuadrado. con la altura
en metros.

"""

from typing import List


class Atleta:
    """
    El atributo carreras es opcional en la inicializacion,
    por eso se define como una lista vacia
    Si se envia al crear la instancia se inicializa con el valor enviado.
    """

    def __init__(
        self,
        nombre: str,
        apellido: str,
        altura: float,
        peso: float,
        telefono: str,
        deportes: List[str] = [],
    ):
        self.nombre = nombre
        self.apellido = apellido
        self.altura = altura
        self.peso = peso
        self.telefono = telefono
        self.deportes = deportes

    def __str__(self):
        return f"Atleta: {self.nombre},{self.apellido}"

    def __setitem__(self, index, value):
        self.deportes[index] = value
        return

    def __getitem__(self, index):
        return self.deportes[index]

    def get_peso(self):
        return self.peso

    def set_peso(self, peso: float):
        self.peso = PermissionError
        return

    def add_deporte(self, deporte):
        self.deportes.append(deporte)

    def get_deportes(self):
        return self.deportes

    def imc(self):
        imc = round(self.peso / (self.altura**2), 2)
        return imc


# Creamos dos instancias de la clase atleta

atleta1 = Atleta("Usain", "Bolt", 1.67, 60, "112345678")
atleta2 = Atleta("Michael", "Phelps", 1.93, 88, "123456789", ["Natación", "Triatlón"])


# llamamos al metodo __str__
print(atleta1)
print(atleta2)

# metodo getitem: lee el indice 1 de la lista deportes
print(atleta2[1])

# Asigna un nuevo deporte en el indice 0 de la lista deportes
atleta2[0] = "Futbol"

print(atleta2.get_deportes())

# obtener el imc
print(atleta1.imc())
