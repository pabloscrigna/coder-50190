"""
C:
R:
U:
D
"""

from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel


# Modelos
class Articulo(BaseModel):
    id: int
    nombre: str
    descripcion: str | None = None
    precio: float
    impuesto: float | None = None

    def to_dict(self):
        return {
            "id": self.id, 
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "impuesto": self.impuesto,
        }


app = FastAPI()


# simulacion de DB
lista_articulos = []


#endpoints
@app.post("/articulos")
def crear_articulo(articulo: Articulo):

    articulo_dict = articulo.to_dict()
    lista_articulos.append(articulo_dict)

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=articulo_dict)

@app.get("/articulos")
def leer_articulos():
    print(lista_articulos)
    return lista_articulos


@app.get("/articulos/{articulo_id}")
def leer_articulo(articulo_id: int):
    
    for i in range(len(lista_articulos)):
        if articulo_id == lista_articulos[i].get("id"):
            return JSONResponse(status_code=status.HTTP_200_OK, content=lista_articulos[i]) 

    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=f"No se encontro el articulo {articulo_id}")


@app.put("/articulos/{articulo_id}")
def update_articulo(articulo_id: int, mod_articulo: Articulo):

    for i in range(len(lista_articulos)):
        if articulo_id == lista_articulos[i].get("id"):
            articulo = mod_articulo.to_dict()
            lista_articulos[i] = articulo

            return JSONResponse(status_code=status.HTTP_200_OK, content=articulo)

    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=f"No se encontro el articulo {articulo_id}")


@app.delete("/articulos/{articulo_id}")
def eliminar_articulo(articulo_id: int):

    for i in range(len(lista_articulos)):
        if articulo_id == lista_articulos[i].get("id"):

            lista_articulos.pop(i)
            return JSONResponse(status_code=status.HTTP_200_OK, content=f"se elimino el id: {articulo_id}")
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No se encontro el id: {articulo_id}")   