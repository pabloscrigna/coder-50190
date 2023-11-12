"""
Para tributar un determinado impuesto se debe ser mayor de 18 años y tener unos
ingresos iguales o superiores a 1000000 $ mensuales. Escribir un programa que
pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla
si el usuario tiene que tributar o no.
"""

INGRESOS = 1000000
EDAD = 18


edad = int(input("Ingrese su edad: "))
ingresos = float(input("Ingree sus ingresos mensuales: "))


if edad > EDAD and ingresos >= float(INGRESOS):
    print("Tributa impuesto")
else:
    print("No tributa impuesto")
        