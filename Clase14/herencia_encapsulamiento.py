"""
Ver el comportamiento de los atributos en la clase heredada

"""


class Persona:

    def __init__(self, nombre, dni, sueldo):
        self.nombre = nombre
        self._dni = dni
        self.__sueldo = sueldo

    def imprimir(self):
        print(f"nombre: {self.nombre}")
        print(f"dni: {self._dni}")
        print(f"sueldo: {self.__sueldo}")



class Profesor(Persona):

    def __init__(self, curso, nombre, dni, sueldo):
        self.curso = curso
        super().__init__(nombre, dni, sueldo)

    def imprimir(self):
        print(f"nombre: {self.nombre}")
        print(f"dni: {self._dni}")
        print(f"sueldo: {self.__sueldo}")


persona = Persona("Juan", 245678234, 500000)
persona.imprimir()

profesor = Profesor("Python", "juan", 23456789, 500000)
profesor.imprimir()
