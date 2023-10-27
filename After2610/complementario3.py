""""
5) Escribe un programa que pida al usuario un número entero del 0 al 9, 
y que mientras el número no sea correcto se repita el proceso. 
Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:
Ayuda: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista (devuelve True o False).

"""

lista_numeros = [0,1,2,3,4,5,6,7,8,9]

numero = int(input("Ingrese un numero: "))

print(f"numero: {numero}")

while not  numero in lista_numeros: 
    numero = int(input("Ingrese un numero: "))
    print(f"numero dentro while: {numero}")    











