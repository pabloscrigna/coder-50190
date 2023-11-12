"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla
si es mayor de edad o no.
"""

MAYOR = 18

edad = int(input("Ingrese su edad: "))


if edad >= MAYOR:
    print("El usuario es mayor de edad")
else:
    print("El usuario es menor de edad")
