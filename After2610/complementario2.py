"""
2)  Escribe un programa que lea un número impar por teclado. 
Si el usuario no introduce un número impar, debe repetirse el 
proceso hasta que lo introduzca correctamente.
"""

condicion = True

while condicion: 
    numero = int(input("Ingrese un numero: "))

    if numero % 2 == 1:
        condicion = False 


print(f"el numero ingresado es {numero}")

