"""
Escritura de un archivo de texto -- modo append: "a"
"""


file =open("archivo_prueba.txt", "a")

texto = "Agregando texto en el archivo\n"

file.write(texto)

file.close()