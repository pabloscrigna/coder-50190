"""
Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña e imprima por pantalla si la
contraseña introducida por el usuario coincide con la guardada en la variable
sin tener en cuenta mayúsculas y minúsculas.
"""


CONTRASEÑA = "QwERTY"


contraseña = input("Ingrese su contraseña: ")


if contraseña.lower() == CONTRASEÑA.lower():
    print("La contraseña es correcta")
else:
    print("La contraseña es incorrecta")
