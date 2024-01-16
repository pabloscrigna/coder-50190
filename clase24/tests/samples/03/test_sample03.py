import requests
import pytest

from sample_03 import get_url

class GetResponseDummy:

    def __init__(self, status_code, text):
        self.status_code = status_code
        self.text = text

def test_get_url_status_code_ok(mocker):

    response_esperado = GetResponseDummy(200, "Hola mundo!!!")
    mocker.patch.object(requests, "get", return_value=response_esperado)

    status_code, _ = get_url("http://midominio.com")
    status_code_esperado = 200

    assert status_code == status_code_esperado, "No coincide el status code"


def test_get_url_text_ok(mocker):

    response_esperado = GetResponseDummy(200, "Hola mundo!!!")
    mocker.patch.object(requests, "get", return_value=response_esperado)

    _, text = get_url("http://midominio.com")
    text_esperado = "Hola mundo!!!"

    assert text_esperado == text, "No coincide el texto"



