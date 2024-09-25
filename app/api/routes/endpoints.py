from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends

from app.api.DTO.dtos import UsuarioDTOPeticion, UsuarioDTORespuesta
from app.api.models.SQLtables import User
from app.database.configuration import sessionLocal, engine

rutas = APIRouter()

def conectarConBd():
    try: 
        baseDatos = sessionLocal()
        yield baseDatos
    except Exception as error:
        baseDatos.rollback()
        raise error
    finally:
        baseDatos.close()