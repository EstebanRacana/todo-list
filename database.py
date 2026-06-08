from sqlmodel import SQLModel, create_engine, Session

URL_DATABASE = "sqlite:///./database.db" #De la variable URL_DATABASE USA EL MOTOR SQLITE Y CREA EL ARCHIVO EN EL PROYECTO PRINCIPAL.

conexion_bdd = create_engine(URL_DATABASE, echo=True) #Conexion Real a esa BD #True=IMPRIME CADA QUERY SI ESTO ES TRUE

def create_tables(): 
    SQLModel.metadata.create_all(conexion_bdd) #Guardar toda informacion de la BD, si existen, no hace nada, si existen, crea tablas.

def get_sessions():
    with Session(conexion_bdd) as session: #Sesion activa con la se
        yield session #Pausa, devuelve y solo finaliza cuando el endpoint lo pida internamente.

        

