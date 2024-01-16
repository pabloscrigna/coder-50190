import pytest

from sample01_new import numero_de_elementos, obtener_valor_maximo, obtener_valor_minimo


def test_obtener_numero_elementos_ok():
    lista_prueba = [1,2,3,4,5,6,7]
    esperado = 7

    cantidad = numero_de_elementos(lista_prueba)

    assert esperado == cantidad, 'La cantidad de elementos no es correcta'


def test_obtener_elementos_con_error():
    lista_valores = None
    with pytest.raises(TypeError):
            valor = numero_de_elementos(lista_valores)


def test_obtener_valor_minimo_ok():
    lista_prueba = [10,24,3,47,5,6,7]
    esperado_minimo = 3
    
    minimo = obtener_valor_minimo(lista_prueba)

    assert esperado_minimo == minimo, 'Ocurrio un error en el minimo'


def test_obtener_valor_minimo_error():
    lista_prueba = "Hola"
    
    with pytest.raises(AttributeError):
        minimo = obtener_valor_minimo(lista_prueba)


def test_obtener_valor_minimo_error():
    lista_prueba = []
    
    with pytest.raises(IndexError):
        minimo = obtener_valor_minimo(lista_prueba)
