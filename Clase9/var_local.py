# Alcance de las variables en las funciones


var_global = "Global"


def var_function():
    var_local = "Local"
    print(f"Adentro de la funcion: var_global: {var_global}")
    print(f"Adentro de la funcion: var_local: {var_local}")
    return



print("Programa principal")

var_function()

print("Continua el programa")

print(f"Afuera de la funcion -- var_global: {var_global}")
print(f"Adentro de la funcion: var_local: {var_local}")