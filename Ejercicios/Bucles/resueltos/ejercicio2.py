"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla
todos los años que ha cumplido (desde 1 hasta su edad).
"""

edad = int(input("Ingrese su edad: "))

for i in range(1, edad+1):
    print(f"Usted cumplio {i} año/s")
