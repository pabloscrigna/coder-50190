"""
Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. 
La primera con los números pares, y la segunda con los números impares.

Ayuda: Para ordenar una lista automáticamente puedes usar el método .sort()


"""


numeros = [2,1,5,3,9,6,7,8,4]

def separar(lista_numeros):
    lista_par = []
    lista_impar = []

    for numero in lista_numeros:

        if numero % 2 == 0:     # 4 % 2 = 0 --> Falso Par -- Verdadero Impar
            lista_par.append(numero)
        else:
            lista_impar.append(numero)

    lista_impar.sort()
    lista_par.sort()

    return lista_par, lista_impar

lista_pares, lista_impares = separar(numeros)

print(f"pares: {lista_pares} *** impares: {lista_impares}")