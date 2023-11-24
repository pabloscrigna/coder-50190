
"""

numero: str
banco : str
CVV : str
dni : str


"""

class Tarjeta:

    def __init__(self, numero, banco, cvv, dni):
        self.numero = numero        
        self.banco = banco
        self.cvv = cvv
        self.dni = dni
        self.activa = False


    def estado(self):
        return self.activa
    
    
    def cambiar_estado(self, estado):
        self.activa = estado


tarjeta_pablo = Tarjeta("123456789", "HSBC", "123", "123456")
tarjeta_julieta = Tarjeta("6666666", "Santander", "906", "99999999")


print(f"tarjeta pablo {tarjeta_pablo.activa} -- {tarjeta_pablo.banco}")

print(tarjeta_pablo.estado())

print(f"El estado de la tarjeta_julieta es {tarjeta_julieta.estado()}")


tarjeta_julieta.cambiar_estado(True)

print(f"El estado de la tarjeta_julieta es {tarjeta_julieta.estado()}")
print(f"El estado de la tarjeta_pablo es {tarjeta_pablo.estado()}")


tarjeta_pablo.cambiar_estado(True)

print(f"El estado de la tarjeta_pablo es {tarjeta_pablo.estado()}")
