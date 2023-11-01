"""
Lectura de un archivo de texto -- Funcion: readlines
"""

file = open("prueba_lectura.txt", "r")

for line in file.readlines():
    print(line)

file.close()