from fastapi import FastAPI
from app.database.configuration import engine
from app.api.models.SQLtables import Base
from app.api.routes.endpoints import rutas

from starlette.responses import RedirectResponse
from starlette.middleware.cors import CORSMiddleware

#metadata de las tablas es toda la info de las tablas. 
#Crear las tablas de sql desde python
Base.metadata.create_all(bind=engine)

#Variable para administrar la aplicacion
app = FastAPI()

#Configurar el protocolo CORS 
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"], #para que sea publico y pueda conectarse cualquiera desde cualquier origen, es decir, cualquier lugar
    allow_credentials = True,
    allow_methods = ["*"], #get, put, etc
    allow_headers = ["*"]
)

#Activar el api
@app.get("/")
def main():
    return RedirectResponse(url="/docs")

app.include_router(rutas)