from fastapi import FastAPI
from app.database.configuration import engine
from app.api.models.SQLtables import Base
from app.api.routes.endpoints import rutas

from starlette.responses import RedirectResponse

#metadata de las tablas es toda la info de las tablas. 
#Crear las tablas de sql desde python
Base.metadata.create_all(bind=engine)

#Variable para administrar la aplicacion
app = FastAPI()

#Activar el api
@app.get("/")
def main():
    return RedirectResponse(url="/docs")

app.include_router(rutas)