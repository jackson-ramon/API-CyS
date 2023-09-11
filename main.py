from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Libro(BaseModel):
    titulo: str
    autor: str
    paginas: int
    editorial: Optional[str]

# Base de datos de libro temporal
base_de_datos = [
    {
        "titulo": "El Gran Gatsby",
        "autor": "F. Scott Fitzgerald",
        "paginas": 218,
        "editorial": "Scribner",
    },
    {
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "paginas": 417,
        "editorial": "Editorial Sudamericana",
    },
    {
        "titulo": "1984",
        "autor": "George Orwell",
        "paginas": 328,
        "editorial": "Secker & Warburg",
    },
    {
        "titulo": "Matar a un ruiseñor",
        "autor": "Harper Lee",
        "paginas": 324,
        "editorial": "J.B. Lippincott & Co.",
    },
]


# Ruta para crear un nuevo libro
@app.post("/libros/", response_model=Libro)
def crear_libro(libro: Libro):
    base_de_datos.append(libro)
    return libro

# Ruta para obtener un libro por su índice en la base de datos
@app.get("/libros/{indice}", response_model=Libro)
def obtener_libro(indice: int):
    if indice < 0 or indice >= len(base_de_datos):
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return base_de_datos[indice]

# Ruta para actualizar un libro por su índice en la base de datos
@app.put("/libros/{indice}", response_model=Libro)
def actualizar_libro(indice: int, libro: Libro):
    if indice < 0 or indice >= len(base_de_datos):
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    
    base_de_datos[indice] = libro
    return libro

# Ruta para eliminar un libro por su índice en la base de datos
@app.delete("/libros/{indice}", response_model=Libro)
def eliminar_libro(indice: int):
    if indice < 0 or indice >= len(base_de_datos):
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    
    libro_eliminado = base_de_datos.pop(indice)
    return libro_eliminado
