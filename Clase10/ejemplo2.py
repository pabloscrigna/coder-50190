"""
Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio.
Calcula el área de un círculo de 5 de radio

Ayuda: El área de un círculo se obtiene al elevar el radio a dos y multiplicando el resultado 
por el número pi. Puedes utilizar el valor 3.14159 como pi o importarlo del módulo math

"""
#from math import pi
import math

def area_circulo(radio):

    #area = pi * radio**2
    area = math.pi * radio**2
    return area


#print(pi)
print(math.pi)

area = area_circulo(5)

print(f"El area del circulo es  {round(area)}")