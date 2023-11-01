"""
seek: Acceder a una ubicación en particular, es decir, 
empezar la lectura desde la posición indicada.
"""


file = open("prueba_lectura.txt", "r")

file.seek(5)

contenido = file.read()

print(contenido)

file.close()