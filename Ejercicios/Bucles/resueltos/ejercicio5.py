"""
Escribir un programa que pregunte al usuario una cantidad a invertir,
el interés anual y el número de años, y muestre por pantalla el capital
obtenido en la inversión cada año que dura la inversión.
"""

capital = float(input("Cantidad a invertir: "))

interes = float(input("Interes anual: "))

tiempo = int(input("Cantidad de años: "))

print(f"capital : {capital}  -- intereses: {interes}  -- años: {tiempo}")

print("Calculo de intereses año a año")
for i in range(tiempo):
    capital = capital + capital * interes * 0.01
    print(f"capital: {capital}  -- luego del {i+1}  año")
