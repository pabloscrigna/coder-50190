class ClaseExterna:

    def __init__(self, valor_exterior, valor_interior):
        self.valor_exterior = valor_exterior
        self.clase_interna = self.ClaseInterna(valor_interior)

    def mostrar_valores(self):
        print(f"Valor exterior: {self.valor_exterior}")
        self.clase_interna.mostrar_valor_interno()

    class ClaseInterna:
        def __init__(self, valor_interior):
            self.valor_interno = valor_interior

        def mostrar_valor_interno(self):
            print(f"Valor interno: {self.valor_interno}")


# Crear una instancia de la clase externa
instancia_externa = ClaseExterna(valor_exterior=10, valor_interior=20)

# Llamar al método que muestra los valores
instancia_externa.mostrar_valores()
