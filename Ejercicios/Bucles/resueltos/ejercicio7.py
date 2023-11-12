"""
Escribir un programa que muestre por pantalla la tabla de multiplicar
del 1 al 10.
"""

tabla = ""

for i in range(1, 11):
    for j in range(1, 11):
        tabla = f"{tabla} {i*j}\t"
    print(tabla)
    tabla = ""
