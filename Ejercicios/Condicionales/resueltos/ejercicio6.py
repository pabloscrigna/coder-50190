"""
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo
y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a
la M y los hombres con un nombre posterior a la N y el grupo B por el resto.
Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por
pantalla el grupo que le corresponde.
"""


nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo F o M: ")

print(f"Su nombre es: {nombre} , sexo: {sexo}")

condicion1 = nombre < "M" and sexo == "F"
condicion2 = nombre > "N" and sexo == "M"

if condicion1 or condicion2:
    print("Grupo: A")
else:
    print("Grupo B")
