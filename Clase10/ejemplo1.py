"""
Realiza una función llamada area_rectangulo() que devuelva el área del
rectángulo a partir de una base y una altura. 
Calcula el área de un rectángulo de 15 de base y 10 de altura

Ayuda: El área de un rectángulo se obtiene al multiplicar la base por la altura.

"""


# Definimos la funcion
def area_rectangulo(base, altura):

    # area = base * altura

    return base * altura


base = 15
altura = 10
area = area_rectangulo(base, altura)
print(f"El area del rectangulo de base {base} y altura {altura} es {area}")

print(f"El area del rectangulo de base {base} y altura {altura} es {area_rectangulo(base,altura)}")
