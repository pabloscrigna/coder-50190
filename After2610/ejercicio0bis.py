"""
Dado un string .....solicitar al usuario el ingreso de una letra e informar la cantidad de veces 
que aparece esa letra en el string
"""

frase = "Hoy es un dia perfecto, todos hablan de eso"

contador = 0

letra_a_buscar = input("ingresar letra: ")


for letra in frase:
    if letra_a_buscar == letra:
        contador += 1

print(f"la letra {letra_a_buscar} aparece {contador} veces en la frase")



