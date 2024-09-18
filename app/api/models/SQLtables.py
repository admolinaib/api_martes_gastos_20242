from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship 
from sqlalchemy.ext.declarative import declarative_base

#llamado a la base para crear tablas 
Base = declarative_base()

#DEFINICION DE LAS TABLAS DE MI MODELO 

#usuario 
class User(Base):
    __tablename__='users'
    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String(50))
    dateOfBirth = Column(Date)
    location = Column(String(100))
    savingsTarget = Column(Float)

class Expenses(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key = True, autoincrement = True)
    description = Column(String(150))
    category = Column(String(50))
    amount = Column(Float)
    date = Column(Date)

class Category(Base):
    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String(50))
    description = Column(String(150))
    categoryPicture = Column(String(200))

class Income(Base):
    id = Column(Integer, primary_key = True, autoincrement = True)
    amount = Column(Float)
    description = Column(String(150))
    date = Column(Date)