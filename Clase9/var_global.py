# Alcance de las variables en las funciones


var_global = "Global"


def var_function():
    print(f"Adentro de la funcion: var_blobal: {var_global}")
    return



print("Programa principal")

var_function()

print("Continua el programa")

print(f"Afuera de la funcion -- var_blobal: {var_global}")