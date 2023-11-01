"""
Escritura de un archivo de texto -- modo create: "x"
"""


file =open("create_archivo.txt", "x")

texto = "Text a agregar en el archivo X\n"

file.write(texto)

file.close()