"""
Escribir un programa que pida al usuario dos números y muestre por pantalla
su división. Si el divisor es cero el programa debe mostrar un error.
"""

numero1 = int(input("Ingrese un dividendo: "))
numero2 = int(input("Ingrese un divisor: "))


if numero2:
    resultado = numero1 / numero2
    print(f"El numero {numero1} dividido {numero2} es {resultado}")
else:
    print("No se puede dividir por 0")
