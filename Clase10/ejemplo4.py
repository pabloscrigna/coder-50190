"""
Realiza una función llamada intermedio() que, a partir de dos números, devuelva su punto intermedio:

Ayuda: El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2

Comprueba el punto intermedio entre -12 y 24

"""

# Definis la funcion
def intermedio(*args):

    for valor in args:
        print(valor)

    inter = (args[0] + args[1]) / 2

    return inter



nro1 = int(input("primer numero: "))
nro2 = int(input("segundo numero: "))

print(intermedio(nro1, nro2, nro1))


