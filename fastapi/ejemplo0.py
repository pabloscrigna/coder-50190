from fastapi import FastAPI
from pydantic import BaseModel

from typing import Union


class Item(BaseModel):
    nombre: str
    precio: float
    descripcion : Union[str, None] = None


# levantamos una instancia de la clase FASTAPI
app = FastAPI()


@app.get("/")
def hola_mundo():
    return {"detail": "Hola mundo!!!"}


@app.get("/items/{id}")
def leer_items(id: int, cantidad: int):

    return {"detail": f"Se envio el : {id}, cantidad: {cantidad}"}


@app.post("/items/")
def crear_item(item: Item):
    print(item)
    return {"detail": "Se creo el item"}
