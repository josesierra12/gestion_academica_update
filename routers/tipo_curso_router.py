from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from models.models import TipoCurso
from seting.database import get_session
from seting.ResponseDTO import ResponseDTO

router = APIRouter(
    prefix="/tipo_cursos",
    tags=["Tipo_Cursos"],
    #dependencies=[Depends(get_current_user)]
)

@router.post("/guardar")
def create(item: TipoCurso, session: Session = Depends(get_session)):
    session.add(item)
    session.commit()
    session.refresh(item)
    return  ResponseDTO(status="success", message="Guardado correctamente", data=item)

@router.get("/listar")
def get_all(session: Session = Depends(get_session)):
    return  ResponseDTO(status="success", message="", data=session.exec(select(TipoCurso)).all()) 

@router.get("/consultar/{id}")
def get(id: str, session: Session = Depends(get_session)):
    item = session.get(TipoCurso, id)
    if not item:
        raise HTTPException(status_code=404, detail="Registro no encontrada")
    return  ResponseDTO(status="success", message="", data=item)

@router.put("/actualizar/{id}")
def update(id: str, updated: TipoCurso, session: Session = Depends(get_session)):
    item = session.get(TipoCurso, id)
    if not item:
        raise HTTPException(status_code=404, detail="No encontrada")
    for key, value in updated.dict(exclude_unset=True).items():
        setattr(item, key, value)
    session.add(item)
    session.commit()
    return  ResponseDTO(status="success", message="Registro actualizado", data=item) 

@router.delete("/eliminar/{id}")
def delete(id: str, session: Session = Depends(get_session)):
    item = session.get(TipoCurso, id)
    if not item:
        raise HTTPException(status_code=404, detail="No encontrada")
    session.delete(item)
    session.commit()
    return  ResponseDTO(status="success", message="", data=True) 