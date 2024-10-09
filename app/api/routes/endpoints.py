from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends

from app.api.DTO.dtos import UsuarioDTOPeticion, UsuarioDTORespuesta, GastoDTOPeticion, GastoDTORespuesta, CategoriaDTOPeticion, CategoriaDTORespuesta, ingresoDTOPeticion, ingresoDTORespuesta
from app.api.models.SQLtables import User, Expenses, Category, Income
from app.database.configuration import sessionLocal, engine

rutas = APIRouter()

def conectarConBd():
    try: 
        baseDatos = sessionLocal()
        yield baseDatos #Activar la base de datos
    except Exception as error:
        baseDatos.rollback()
        raise error
    finally:
        baseDatos.close()

#CONSTRUYENDO NUESTROS SERVICIOS 

#Cada servicio (operación o transacción en BD) debe programarse como una funcion 
@rutas.post("/user", response_model=UsuarioDTORespuesta, summary="Registrar un usuario en la base de datos")
def guardarUsuario(datosUsuario: UsuarioDTOPeticion, database: Session = Depends(conectarConBd)):
    try:
        user = User(
            name = datosUsuario.name,
            dateOfBirth = datosUsuario.dateOfBirth,
            location = datosUsuario.location,
            savingsTarget = datosUsuario.savingsTarget
        )
        #Ordenandole a la BD
        database.add(user)
        database.commit()
        database.refresh(user)
        return user

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema {error}")
    
#En este no se tiene que llevar datos porque ya tenemos la conexión y son datos que ya existen
@rutas.get("/user", response_model=List[UsuarioDTORespuesta], summary="Buscar todos los uauarios en BD")
def buscarUsuarios(database: Session = Depends(conectarConBd)):
    try:
        user = database.query(User).all()
        return user
    
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"No se puede buscar los usuarios {error}")
    
@rutas.post("/expenses", response_model=GastoDTORespuesta, summary="Registrar los gastos en la base de datos")
def guardarGastos(datosGastos: GastoDTOPeticion, database: Session = Depends(conectarConBd)):
    try:
        expenses = Expenses(
            description = datosGastos.description,
            category = datosGastos.category,
            amount = datosGastos.amount,
            date = datosGastos.date
        )
        #Ordenandole a la BD
        database.add(expenses)
        database.commit()
        database.refresh(expenses)
        return expenses

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema {error}")
    
@rutas.get("/expenses", response_model=List[GastoDTORespuesta], summary="Buscar todos los gastos en BD")
def buscarGastos(database: Session = Depends(conectarConBd)):
    try:
        expenses = database.query(Expenses).all()
        return expenses
    
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"No se puede buscar los gastos {error}")
    
@rutas.post("/category", response_model=CategoriaDTORespuesta, summary="Categorizar y ampliar la información de los gastos en la base de datos")
def guardarCategorias(datosCateroria: CategoriaDTOPeticion, database: Session = Depends(conectarConBd)):
    try:
        category = Category(
            name = datosCateroria.name,
            description = datosCateroria.description,
            categoryPicture = datosCateroria.categoryPicture,
        )
        #Ordenandole a la BD
        database.add(category)
        database.commit()
        database.refresh(category)
        return category

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema {error}")
    
@rutas.get("/category", response_model=List[CategoriaDTORespuesta], summary="Buscar las categorías e información relacionada en BD")
def buscarCategorias(database: Session = Depends(conectarConBd)):
    try:
        category = database.query(Category).all()
        return category
    
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"No se puede buscar las categorías {error}")
    
@rutas.post("/income", response_model=ingresoDTORespuesta, summary="Registrar los ingresos en la base de datos")
def guardarIngreso(datosIngreso: ingresoDTOPeticion, database: Session = Depends(conectarConBd)):
    try:
        income = Income(
            amount = datosIngreso.amount,
            description = datosIngreso.description,
            date = datosIngreso.date,
        )
        #Ordenandole a la BD
        database.add(income)
        database.commit()
        database.refresh(income)
        return income

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema {error}")
    
@rutas.get("/income", response_model=List[ingresoDTORespuesta], summary="Buscar todos los ingresos en BD")
def buscarIngreso(database: Session = Depends(conectarConBd)):
    try:
        income = database.query(Income).all()
        return income
    
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"No se puede buscar los ingresos {error}")