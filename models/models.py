from datetime import datetime, time
from typing import Optional, List
from sqlalchemy import ForeignKey, String
from sqlmodel import Column, SQLModel, Field, Relationship

class Persona(SQLModel, table=True):
    id_persona: str = Field(sa_column=Column(String(50), primary_key=True))
    nombres: str
    apellidos: str
    direccion: str
    telefono: str
    fecha_nacimiento: str
    user_name: str
    password: str
    correo: str
    rol: str  # "estudiante", "instructor"
    curso_instructor: List["Curso"] = Relationship( back_populates="instructor", sa_relationship_kwargs={"foreign_keys": "[Curso.id_instructor]"})
    curso_estudiante: List["Curso"] = Relationship(back_populates="estudiante",sa_relationship_kwargs={"foreign_keys": "[Curso.id_estudiante]"})

class CursoAsignatura(SQLModel, table=True):
    id_curso: int = Field(foreign_key="curso.id_curso", primary_key=True)
    id_asignatura: int = Field(foreign_key="asignatura.id_asignatura", primary_key=True)

class Asignatura(SQLModel, table=True):
    id_asignatura: int = Field(primary_key=True)
    nombre_asignatura: str
    cursos: List["Curso"] = Relationship(back_populates="asignaturas",link_model=CursoAsignatura )

class Curso(SQLModel, table=True):
    id_curso: int = Field(primary_key=True)
    nombre: str
    fecha_inicio: str
    fecha_vencimiento: str
    status: str = Field(sa_column=Column(String(20)))

    id_estudiante: Optional[str] = Field(default=None, sa_column=Column(String(50), ForeignKey("persona.id_persona")))
    id_instructor: Optional[str] = Field(default=None, sa_column=Column(String(50), ForeignKey("persona.id_persona")))
    id_tipo: Optional[int] = Field(default=None, foreign_key="tipocurso.id_tipo")

    asignaturas: List["Asignatura"] = Relationship(back_populates="cursos",link_model=CursoAsignatura)
    instructor: Optional["Persona"] = Relationship(back_populates="curso_instructor",sa_relationship_kwargs={"foreign_keys": "[Curso.id_instructor]"})
    estudiante: Optional["Persona"] = Relationship(back_populates="curso_estudiante",sa_relationship_kwargs={"foreign_keys": "[Curso.id_estudiante]"})
    tipo: Optional["TipoCurso"] = Relationship(back_populates="curso")
    horarios: List["HorarioClase"] = Relationship(back_populates="curso")

class TipoCurso(SQLModel, table=True):
    id_tipo: int = Field(primary_key=True)
    nombre_tipo: str
    curso: List["Curso"] = Relationship(back_populates="tipo")

class HorarioClase(SQLModel, table=True):
    id_horario: int = Field(primary_key=True)
    dia_semana: str
    hora_inicio: time
    hora_fin: time
    aula: str
    id_curso: int = Field(foreign_key="curso.id_curso")
    curso: Optional["Curso"] = Relationship(back_populates="horarios")