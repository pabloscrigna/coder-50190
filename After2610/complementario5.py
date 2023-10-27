"""
4) Escribe un programa que pida al usuario cuantos números quiere introducir. 
Luego lee todos los números y realiza una media aritmética.

"""

cantidad_numeros = int(input("Cantidad de numeros a ingresar: "))
suma_acumulado = 0

cant = cantidad_numeros

while cantidad_numeros:
    numero = int(input("ingrese un numero: "))
    suma_acumulado += numero
    cantidad_numeros -= 1

promedio = suma_acumulado/cant

print(f"El promedio es igual a {promedio}")

