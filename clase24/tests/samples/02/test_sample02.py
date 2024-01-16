import pytest
import os

from sample02_new import leer_archivo, agregar_archivo



@pytest.fixture(autouse=True, scope='module')
def crear_archivo_prueba():
    file_name = 'test_file.txt'
    with open(file_name, 'w') as file:
        file.write("Hola mundo\n")
        file.write("prueba\n")

    yield

    os.remove(file_name)


def test_leer_archivo_ok():
    texto_esperado = "Hola mundo\nprueba\n"

    texto_leido = leer_archivo('test_file.txt')

    assert texto_esperado == texto_leido, 'No coincide el contenido'    


def test_leer_archivo_not_file():

    with pytest.raises(FileNotFoundError):
        texto_leido = leer_archivo('test_file_1.txt')


def test_agregar_texto_ok():
    texto_esperado = "Hola mundo\nprueba\nTexto agregado\n"

    agregar_archivo('test_file.txt', 'Texto agregado\n')

    texto_leido = leer_archivo('test_file.txt')

    assert texto_esperado == texto_leido, 'fallo agregar texto'    


""""
def test_agregar_texto_archivo_not_file():

    with pytest.raises(Exception):
        agregar_archivo('test_file_1.txt', 'Texto a agregar!!!')
"""