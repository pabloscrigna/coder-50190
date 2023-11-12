"""
Escribir un programa que muestre el eco de todo lo que el usuario introduzca
hasta que el usuario escriba “salir” que terminará.
"""

palabra = input("")

while palabra != "salir":
    print(palabra)

    palabra = input("")
