from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ..config.base import Base


class Aluno(Base):
    __tablename__ = 'alunos'

    cpf = Column(String(length=11), primary_key=True)
    nome = Column(String(length=50), nullable=False)
    telefone = Column(String(length=11), nullable=False)
    endereco = Column(String(length=100), nullable=False)
    ativo = Column(Boolean, nullable=False)
    cod_curso = Column(Integer, ForeignKey('cursos.cod_curso', ondelete='CASCADE'), nullable=False)

    curso = relationship('Curso', back_populates='alunos', lazy='joined')

    def __repr__(self) -> str:
        return f'Aluno(cpf={self.cpf}, nome={self.nome}, ativo={self.ativo}, curso={None})'
