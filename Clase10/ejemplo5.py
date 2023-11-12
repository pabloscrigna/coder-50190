"""
Realiza una función llamada recortar() que reciba tres parámetros. 
El primero es el número a recortar, el segundo es el límite inferior y el tercero 
el límite superior. La función tendrá que cumplir lo siguiente:

Devolver el límite inferior si el número es menor que éste
Devolver el límite superior si el número es mayor que éste.
Devolver el número sin cambios si no se supera ningún límite.
Comprueba el resultado de recortar 15 entre los límites 0 y 10


      0    ------- 10

  3 --> 5
  7 --> 7
  20 --> 20    

"""


def recortar(numero, limite_inferior, limite_superior):

    if limite_inferior < numero < limite_superior:
       return numero

    numero1 = limite_superior
    if numero < limite_inferior:
        numero1 = limite_inferior
        

    return numero1


print(recortar(-2, 0, 10))
print(recortar(5, 0, 10))
print(recortar(20, 0, 10))
