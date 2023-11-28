"""
Hacer una clase Persona con los siguientes atributos


nombre: publico
dni : privado
sueldo : protegido

"""


class Persona:

    def __init__(self, nombre, dni, sueldo):
        # publico
        self.nombre = nombre
        # privado 
        self._dni = dni
        # protegido
        self.__sueldo = sueldo


    def mostrar_sueldo(self):
        return self.__sueldo

persona = Persona("Juan", 245678234, 500000)


print(persona.nombre)
print(persona._dni)
# print(persona.__sueldo)
print(persona.mostrar_sueldo())