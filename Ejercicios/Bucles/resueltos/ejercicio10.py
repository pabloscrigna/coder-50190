"""
Escribir un programa que pida al usuario un número entero y muestre
por pantalla si es un número primo o no.
"""

#  Cuando un numero es primo? cuando solo es divisible por si mismo y por el 1.
# 1, 3, 5, 7


numero = int(input("ingresar un numero: "))

contador = 2

while (numero % contador != 0):
    contador += 1


if contador == numero:
    print(f"El numero {numero} es primo")
else:
    print(f"El numero: {numero} no es primo")
