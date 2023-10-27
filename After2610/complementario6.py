"""
Escribir un programa que le solicite al usuario su nombre, edad, dirección y que, 
posteriormente, lo muestre por pantalla:
Ejemplo del output solicitado: 
Juan tiene 25 años, y vive en Carrera 7 - Bogotá

persona = {
    "nombre" : "",
    "edad": 0,
    "direccion": "",
}



"""

persona = {}


persona["nombre"] = input("Ingrese su nombre: ") # nombre 
print(persona)

persona["edad"] = input("Ingrese su edad: ") # edad
print(persona)

persona["direccion"] = input("Ingrese su direccion: ") # direccion
print(persona)


print(f"{persona['nombre']} tiene {persona['edad']} años y vive en {persona['direccion']}")