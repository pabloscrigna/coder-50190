

class Persona:

    def __init__(self, nombre, edad, apellido):
        self.nombre = nombre
        self.edad = edad
        self.apellido = apellido



empleado_1 = Persona("Juan", "45", "Stier")
empleado_2 = Persona("Pedro", "24", "Aznar")


print(empleado_1.nombre)
print(empleado_2.edad)
print(empleado_1.apellido)