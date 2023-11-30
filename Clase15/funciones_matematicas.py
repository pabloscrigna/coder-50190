"""
importar modulo math
"""
import math


"""
variable PI
"""
PI = 3.14

pi = math.pi 

"""
funcion suma
"""

def suma(a, b):
    return a + b

"""
funcion resta
"""

def resta(a, b):
    return a - b


class Alumno:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota



    def imprimir(self):
        print(f"El alumno se llama {self.nombre}, y tiene la nota {self.nota}")
        




if __name__ == "__main__":
    print(f"suma: {suma(10, 10)}")
    print(f"resta: {resta(10,5)}")
