"""
Escribir un programa que pida al usuario una palabra y la muestre por
pantalla 10 veces.
"""
CANTIDAD = 10

palabra = input("Ingrese una palabra: ")

for i in range(CANTIDAD):
    print(f"{i+1} -- {palabra}")
