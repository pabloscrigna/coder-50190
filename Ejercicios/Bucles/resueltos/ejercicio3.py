"""
Escribir un programa que pida al usuario un número entero positivo y muestre
por pantalla todos los números impares desde 1 hasta ese número separados por
comas.
"""

numero = int(input("Ingrese un numero: "))

lista_impares = []

for i in range(1, numero+1):
    if i % 2:
        lista_impares.append(str(i))

print(",".join(lista_impares))
