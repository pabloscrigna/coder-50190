"""
Escribir un programa que almacene la cadena de caracteres contraseña
en una variable, pregunte al usuario por la contraseña hasta que introduzca
la contraseña correcta.
"""

clave = "contraseña"

contraseña = ""

while contraseña != clave:
    contraseña = input("Introduce la contraseña: ")

print("Contraseña correcta")
