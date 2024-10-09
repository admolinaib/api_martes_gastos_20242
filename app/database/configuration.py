from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine

#datos para la conexion a BD

dataBaseName = "gestorbd"
userName = "root"
userPassword = ""
connectionPort = 3306
server = "localhost"

#creando la conexion
dataBaseConnection=f"mysql+mysqlconnector://{userName}:{userPassword}@{server}:{connectionPort}/{dataBaseName}"

#creando el motor de conexion 
engine = create_engine(dataBaseConnection)

#abrir la sesion con la bd 
sessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
