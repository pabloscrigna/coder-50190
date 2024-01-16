
def leer_archivo(path_archivo):
    with open(path_archivo, 'r') as file:
        return file.read()
    

def agregar_archivo(path_archivo, texto):
    with open(path_archivo, 'a') as file:
        file.write(texto)
