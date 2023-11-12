"""
Escribir un programa que pida al usuario un número entero y muestre por
pantalla un triángulo rectángulo como el de más abajo, de altura el
número introducido.
"""

numero = int(input("Ingresar un numero: "))

caracter = "*"

for i in range(numero):
    caracter = f"{caracter} "
    print(caracter)
    caracter = f"{caracter} *"
