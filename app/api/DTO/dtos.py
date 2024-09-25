from pydantic import BaseModel, Field 
from datetime import date

#Los DTO son clases que establecen el modelo de transferencia de datos. Se deben crear siempre dos DTO; uno de petición y otro de respuesta
class UsuarioDTOPeticion(BaseModel): 
    name: str
    dateOfBirth: date
    location: str
    savingsTarget: float
    class Config:
        orm_mode=True

class UsuarioDTORespuesta(BaseModel):
    id: int
    name: str
    savingsTarget: float
    class Config:
        orm_mode=True

class GastoDTOPeticion(BaseModel):
    description =str
    category = str
    amount = float
    date = date
    orm_mode=True

class GastoDTORepuesta(BaseModel):
    description =str
    category = str
    amount = float
    date = date
    orm_mode=True

class CategoriaDTOPeticion(BaseModel):
    name = str
    description = str
    categoryPicture = str
    orm_mode=True

class CategoriaDTORepuesta(BaseModel):
    name = str
    description = str
    categoryPicture = str
    orm_mode=True

class ingresoDTOPeticion(BaseModel):
    amount = float
    description = str
    date = date
    orm_mode=True

class ingresoDTORepuesta(BaseModel):
    amount = float
    description = str
    date = date
    orm_mode=True