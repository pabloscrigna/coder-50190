"""
Escribir un programa que pida al usuario un número entero y muestre por
pantalla un triángulo rectángulo como el de más abajo.

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1

"""


impares = []

numero = int(input("Ingresar un numero: "))


print(f"el numero ingresado es {numero}")


linea = ""

for i in range(1, numero+1, 2):
    linea = f"{i} {linea}"
    print(linea)
