"""
Creamos un dic en python y lo pasamos a string json
Luego lo volvemos a convertir en un dict
"""
import json


datos = {
    "nombre": "Pedro",
    "edad": 56,
    "promedio": 7.8,
    "cursos": ["Python", "C++"],
    "curso": ("python", 50190),
    "notas": None,
    "activo" : True,
    "programas": {
        "OS": "Linux",
        12 : 12
    },
}

print(datos)
print(type(datos))

# datos_json = json.dumps(datos)

# print(datos_json)
# print(type(datos_json))

# datos_original = json.loads(datos_json)

# print(datos_original)
# print(type(datos_original))