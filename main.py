from fastapi import FastAPI
from fastapi.params import Depends
from fastapi.security import HTTPBearer
from models.models import  SQLModel
from seting.database import engine
from fastapi.middleware.cors import CORSMiddleware

# Impotracionees modulos de la api
from routers.persona_router import router as persona_router
from routers.asignatura_router import router as asignatura_router
from routers.curso_router import router as curso_router
from routers.curso_asignatura_router import router as curso_asignatura_router
from routers.horario_clase_router import router as horario_clase_router
from routers.tipo_curso_router import router as tipo_curso_router
from routers.auth_router import router as auth_router

security = HTTPBearer()

tags_metadata = [
    
    {
        "name": "Personas",
        "description": "Permite gestionar las personas en la api"
    },
    {
        "name": "Autenticación",
        "description": "Permite gestionar las autenticaciones"
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
    title="API gestion Academica",
    description="Permite gestionar los curso academicos",
    version="1.0.0",
    openapi_tags= tags_metadata,
    dependencies=[Depends(security)]
     
)

# Permitir acceso desde Angular
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Cambia según tu entorno
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Crear las tablas en la base de datos

SQLModel.metadata.create_all(engine)


# inculir cada router por separado
app.include_router(persona_router)
app.include_router(auth_router)
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