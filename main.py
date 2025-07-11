from fastapi import FastAPI
from models.models import  SQLModel
from seting.database import engine

# Impotracionees modulos de la api
from routers.persona_router import router as persona_router
from routers.asignatura_router import router as asignatura_router
from routers.curso_router import router as curso_router
from routers.curso_asignatura_router import router as curso_asignatura_router
from routers.horario_clase_router import router as horario_clase_router
from routers.tipo_curso_router import router as tipo_curso_router

tags_metadata = [
    
    {
        "name": "Personas",
        "description": "Permite gestionar las personas en la api"
    },
    {
        "name": "Asignaturas",
        "description": "Permite gestionar las diferentes asignaturas"
    },
    {
        "name": "Cursos",
        "description": "Permite gestionar los diferentes cursos"
    },
    {
        "name": "Cursos_Asignaturas",
        "description": "Permite gestionar cursos con sus asignaturas"
    },
    {
        "name": "Horario_Clases",
        "description": "Permite gestionar el horario de clase"
    },
    {
        "name": "Tipo_Cursos",
        "description": "Permite gestionar los difere3ntes tipos de cursos"
    },


]



app = FastAPI(
    title="API gestion de Tarjetas",
    description="Permite gestionar los tipos de tarjetas",
    version="1.0.0",
    openapi_tags= tags_metadata,
    
)


# Crear las tablas en la base de datos

SQLModel.metadata.create_all(engine)


# inculir cada router por separado
app.include_router(persona_router)
app.include_router(asignatura_router)
app.include_router(curso_router)
app.include_router(curso_asignatura_router)
app.include_router(horario_clase_router)
app.include_router(tipo_curso_router)









'''
from contextlib import asynccontextmanager
from fastapi import FastAPI
from seting.database import create_db_and_tables

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🔧 Iniciando aplicación y creando tablas...")
    create_db_and_tables()
    yield
    print("✅ Aplicación cerrada.")

app = FastAPI(lifespan=lifespan)

@app.get("/")
def root():
    return {"message": "API Gestión Académica activa ✅"}
'''