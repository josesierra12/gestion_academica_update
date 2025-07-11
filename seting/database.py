
from sqlmodel import SQLModel, create_engine, Session
from models.models import Persona, Curso, Asignatura, CursoAsignatura, TipoCurso, HorarioClase


DATABASE_URL = (
  # "mssql+pyodbc://talento:cartagena@nodossolutions.com:1435/gestion_academica?driver=ODBC+Driver+17+for+SQL+Server"
   "mssql+pyodbc://talento:cartagena@nodossolutions.com:1435/gestion_academica_01?driver=ODBC+Driver+17+for+SQL+Server"

)

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session


