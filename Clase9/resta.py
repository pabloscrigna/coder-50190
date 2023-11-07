
# Reciba dos numeros y retorne la resta del primero menos el segundo


def resta(numero1, numero2, numero3):
    print(f"El valor del numero1 es {numero1}")
    print(f"El valoe del numero2 es {numero2}")
    print(f"El valoe del numero2 es {numero3}")

    resultado = numero1 - numero2 - numero3

    return resultado


nro1 = 10
nro2 = 5
nro3 = 2

resultado_resta = resta(nro1, nro2, nro3)

print(f"el resultado de la resta es {resultado_resta}")


resultado = resta(20,10,5)

if resultado >= 0:
    print("numero1 mayor")
