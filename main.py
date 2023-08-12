from fastapi import FastAPI
from rutas.user import Cafes
from docs import tags_metadata
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
  title="CRUD con Fast API y MongoDB",
  description="Es un proyecto básico para crear el CRUD con APIS utilizando Fast API y MongoDB",
  version="0.1.1",
  openapi_tags=tags_metadata
)
origins = [
    "http://localhost",
    "http://localhost/Cafes",  # Asegúrate de incluir el puerto si lo estás usando
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(Cafes)