from fastapi import FastAPI
from database import create_tables
from contextlib import asynccontextmanager
from app.models.todo import Todo
from app.routers.todo import router
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager #Llamamos a la asincronica de libreria estandar de python
async def server_lifecycle(app: FastAPI): #Funcion asincronica de la variable asignada
    create_tables() ##Llama al metodo
    yield        #Pausa, llama al metodo y solo se apaga cuando el servidor se apague, diferente a la sesion.
                           
app=FastAPI(lifespan=server_lifecycle)
#Middlware, intermediario para cada request a los endpoints
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #A traves de estas URL, se conectara el frontend y llegara a la API
    allow_methods=["*"], #Permite todos los HTTP 
    allow_headers=["*"], #permite headers en los request
)


app.include_router(router=router)
@app.get("/")
def home():
    return "Hola mundo"
