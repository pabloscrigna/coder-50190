"""
Escribe un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:


Mostrar una suma de los dos números
Mostrar una resta de los dos números (el primero menos el segundo)
Mostrar una multiplicación de los dos números
Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
En caso de no introducir una opción válida, el programa informará de que no es correcta.

"""

numero1 = int(input("nro1: "))
numero2 = int(input("nro2: "))

condicion = True

while condicion:

    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Salir")   
    codigo = input("Ingrese opcion")    
    if codigo == "1":
        resultado = numero1 + numero2
        print(f"el resultado de la suma es : {resultado}")
        condicion = False
    elif codigo == "2":
        resultado = numero1 - numero2
        print(resultado)
        condicion = False
    elif codigo == "3":
        resultado = numero1 * numero2
        print(resultado)
        condicion = False
    elif codigo == "4":
        condicion = False
    else:
        print("Codigo incorrecto")


print("Fin del programa")