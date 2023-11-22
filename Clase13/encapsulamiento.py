
class Cuenta:

    def __init__(self, dni, numero, saldo=0):
        self.dni = dni
        self.numero = numero
        self.saldo = saldo

    def leer_dni(self):
        return self.dni
    
    def leer_saldo(self):
        return self.saldo


cuenta = Cuenta(25467845, 123456789, 4578)


# leer el atributo dni directo
print(f"leer dni atributo: {cuenta.dni}")

# leer el atributo dni utilizando un metodo
print(f"leer dni por metodo: {cuenta.dni}")


# Modificar el atributo dni directo
cuenta.dni = 987654321
print(f"Modificar dni atributo: {cuenta.dni}")

# leer el atributo dni utilizando un metodo
print(f"leer dni por metodo: {cuenta.dni}")




# Leer el atributo saldo directo   -- ponerlo privado


# leer el saldo utilizando un metodo


# Ver metodos privados
