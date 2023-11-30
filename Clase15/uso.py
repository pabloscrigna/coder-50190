"""
Mostrar las distintas formas de importar las funciones y variables del modulo 
funciones_matematicas.py
"""

# import funciones_matematicas

# print(funciones_matematicas.suma(5,5))
# print(funciones_matematicas.resta(10, 5))
# print(funciones_matematicas.pi)

# import funciones_matematicas as fm

# print(fm.suma(10, 5))
# print(fm.resta(10, 5))
# print(fm.PI)
#

# from funciones_matematicas import *

# print(suma(10, 5))
# print(resta(10, 5))
# print(pi)

from funciones_matematicas import suma, resta, Alumno

print(suma(10, 5))
print(resta(10, 5))

alumno = Alumno("Pablo", 10)

alumno.imprimir()