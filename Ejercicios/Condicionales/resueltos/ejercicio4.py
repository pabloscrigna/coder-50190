"""
Escribir un programa que pida al usuario un número entero y muestre
por pantalla si es par o impar.
"""

mensaje = "El numero ingresado es"
par = "par"
impar = "impar"


numero = int(input("Ingrese un numero entero: "))

if numero % 2:
    print(f"{mensaje} {impar}")
else:
    print(f"{mensaje} {par}")
