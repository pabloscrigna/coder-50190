"""
Escritura de un archivo de texto -- modo: "w"
"""


file = open("archivo_prueba.txt", "w")

texto = "Probando la escritura en un archivo\n"

file.write(texto)


file.close()


# Que pasa si se vuelve a ejecutar? Cambiar texto


