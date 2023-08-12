from typing import Optional
from pydantic import BaseModel

class cafes(BaseModel):
    id: Optional[str]
    Nombre: str
    Descripción: str
    Precio: str
    Tipo: str
