"""
Hacer una funcion que calcule el promedio de positividad de un texto


def positividad(texto: str, palabras: dict)->float:


palabras = {
    "si" : 10,
    "no" : -10,
    "alegria" : 8
}

si la palabra del texto no esta en eñ diccionario considerar 0
"""


def positividad(texto:str, diccionario: dict)->float:

    suma_acumulada = 0
    contador = 0

    palabras = texto.split()
    cantidad_palabras = len(palabras)
    print(f"cantidad palabras: {cantidad_palabras}")
    print(palabras) 

    for palabra in palabras:
        print(palabra)
        if palabra in diccionario:
            contador += 1 
            print(f"la palabra {palabra} esta en el diccionario")
            suma_acumulada += diccionario.get(palabra)
            print(f"suma_acumulada = {suma_acumulada}")    

    promedio = suma_acumulada / cantidad_palabras
    print(f"contador {contador}")


    return promedio


diccionario = {
    "si" : 10,
    "no" : -10,
    "alegria" : 8
}

frase = "si no alegria python programacion"


print(positividad(frase, diccionario))
