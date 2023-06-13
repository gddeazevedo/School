from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from ..config.base import Base


class Curso(Base):
    __tablename__ = 'cursos'

    cod_curso = Column(Integer, primary_key=True)
    nome = Column(String(length=50), nullable=False, unique=True)
    ano_inicio = Column(Integer, nullable=False)

    professores = relationship('Professor', back_populates='curso', lazy='joined')
    alunos = relationship('Aluno', back_populates='curso', lazy='joined')

    def __repr__(self) -> str:
        return f'Curso(cod_curso={self.cod_curso}, nome={self.nome}, ano_inicio={self.ano_inicio})'
