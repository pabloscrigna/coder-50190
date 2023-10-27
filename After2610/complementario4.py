"""
Utilizando la función range() y la conversión a listas, genera las siguientes listas dinámicamente:





🖐 Ayuda: la conversión de listas es mi_lista=list(range(inicio,fin,salto))
"""


mi_lista = []

# Todos los números del 0 al 10 [0, 1, 2, ..., 10]
mi_lista = list(range(11))
print(mi_lista)


# Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
mi_lista = list(range(-10,1))
print(mi_lista)


# Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
mi_lista = list(range(2,21,2))
print(mi_lista)


# Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]

mi_lista = list(range(-19,0,2))
print(mi_lista)

# Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
mi_lista = list(range(0,51,5))
print(mi_lista)