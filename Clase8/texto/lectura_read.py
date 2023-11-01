"""
Lectura de un archivo de texto -- Funcion: read
"""

file = open("prueba_lectura.txt", "r")

contenido = file.read()

file.close()


print(contenido)

# print(contenido[0])

 