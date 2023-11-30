"""
Hacer un script que reciba el nombre de un archivo y un dato para grabar en el archivo.  
Verificar que se reciban los dos argumentos

usage: python3 script.py invitados.txt Juan 247893456
"""

import sys

print(f"Los argumentos son: {sys.argv}")


argumentos = sys.argv

#if len(argumentos) < 4:
#    print("Error -- faltan argumentos")
#    exit(1)


for arg in argumentos:
    print(arg)

""""
file = open(argumentos[1], "a")
file = open("invitados.txt")
file.write(f"{argumentos[2]}:{argumentos[3]}\n")
file.close()
"""

