from typing import List
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from db import Base, SessionLocal, get_session
from sqlalchemy import Column, String, Date, Integer
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from pydantic import BaseModel
from datetime import date


""" Definição da classe 'Pessoa' """
class Pessoa(Base):
    __tablename__ = "funcionario"
    id = Column(Integer, primary_key=True)
    nome = Column(String(255))
    data_nasc = Column(Date)
    endereco = Column(String(255))
    cpf = Column(String(255), unique=True)
    estado_civil = Column(String(255))


""" Criação do Schema 'PessoaBase' """
class PessoaBase(BaseModel):
    id: int
    nome: str
    data_nasc: date
    endereco: str
    cpf: str
    estado_civil: str

    class Config:
        orm_mode = True

""" Definição do recurso de usuários """
router = APIRouter(prefix="/v1/users")

#CRUD

"""Definindo o comando de leitura"""
@router.get("/")
def list_users(session: Session=Depends(get_session) -> List[PessoaBase]):
    return session.query(Pessoa).all()

"""Definindo o comando de criação"""
@router.post("/")
def create_user(pessoa: PessoaBase, session: Session=Depends(get_session)):
    try:
        new_pessoa = Pessoa(
            nome=pessoa.nome,
            data_nasc=pessoa.data_nasc,
            endereco=pessoa.endereco,
            cpf=pessoa.cpf,
            estado_civil=pessoa.estado_civil,
        )

        session.add(new_pessoa)
        session.commit()
    
    except IntegrityError:
        return JSONResponse(status_code=400, content={"msg" : "CPF Duplicado"})

"""Definindo o comando de exclusão"""
@router.delete("/{user_id}")
def delete_user(user_id: int, session: Session=Depends(get_session)):
        pessoa = session.get(Pessoa, user_id)
        session.delete(pessoa)

        session.commit()

"""Definindo o comando de atualização completa (put)"""
@router.put("/")
def put_user(pessoa: PessoaBase, session: Session=Depends(get_session)):
    try:    
        att_pessoa = session.get(Pessoa, pessoa.id)
        att_pessoa.nome = pessoa.nome 
        att_pessoa.data_nasc = pessoa.data_nasc 
        att_pessoa.endereco = pessoa.endereco 
        att_pessoa.estado_civil = pessoa.estado_civil 

        session.commit()

    except IntegrityError as error:
        return JSONResponse(status_code=400, content={"msg" : "CPF Duplicado"})
