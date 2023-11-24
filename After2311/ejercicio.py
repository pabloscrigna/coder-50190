"""
Aclaraciones Generales:

Crear una clase llamada __Alumno__, que posea como atributos de instancia el 

nombre y la nota del estudiante. 

Como métodos propios de la clase, se deberán definir correspondientemente el constructor, 
el método imprimir y resultado.


**Consigna**: Implementar la Clase de Alumno, creada en la actividad anterior, directamente en Python.

* El método imprimir, deberá mostrar por pantalla el nombre y la nota del estudiante.
* El método resultado, evalúa la nota correspondiente del estudiante. 
Si el estudiante saca menos de 5 puntos  desaprueba la materia, más de 5 puntos aprueba. 
Tip: Para la realización de este apartado, es necesario trabajar con estructuras condicionales.
* Se deberá instanciar, al menos, dos objetos pertenecientes a la clase Alumno.

"""

def imprimir(a,b):
    return a +b


class Alumno:

    def __init__(self, nombre_estudiante, nota_estudiante):
        self.nombre = nombre_estudiante
        self.nota = nota_estudiante
        self.activo = True
        return         

    def imprimir(self):
        print(f"El nombre del alumno es {self.nombre} y la nota es {self.nota}")
        return

    def resultado(self):
        if self.nota < 5:
            print("El alumno esta desaprobado")
        else:
            print("El alumno esta aprobado")
        return

    def actualizar_nota(self, nueva_nota):
        self.nota = nueva_nota
        #self.resultado()
        return
    
    def __str__(self):
        return f"El alumno se llama {self.nombre} y su nota es {self.nota}"


alumno = Alumno("Juan", 10)
alumno1 = Alumno("Pedro", 1)


alumno.imprimir()
alumno.resultado()

alumno1.imprimir()
alumno1.resultado()

print("Actualizando nota")
alumno.actualizar_nota(4)
print("Fin actualizacion de nota")
alumno.imprimir()

alumno.resultado()

print(alumno)
print(alumno1)

