"""
 Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:

Si el primer número es mayor que el segundo, debe devolver 1.
Si el primer número es menor que el segundo, debe devolver -1.
Si ambos números son iguales, debe devolver un 0.

Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'

"""


def relacion(numero1, numero2):
    
    if numero1 > numero2:
        return 1

    if numero1 < numero2:
        return -1
    
    if numero1 == numero2:
        return 0



def relacion_1(numero1, numero2):

    resultado = 0

    if numero1 > numero2:
        resultado = 1

    elif numero1 < numero2:
        resultado = -1
    
    else: 
        resultado = 0


    return resultado


print(relacion(5, 10))
print(relacion(10, 5))
print(relacion(5, 5))
