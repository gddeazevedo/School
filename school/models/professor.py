from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from ..config.base import Base


class Professor(Base):
    __tablename__ = 'professores'

    cpf = Column(String(length=11), primary_key=True)
    nome = Column(String(length=50), nullable=False)
    telefone = Column(String(length=11), nullable=False)
    endereco = Column(String(length=100), nullable=False)
    data_contratacao = Column(DateTime, nullable=False)
    salario = Column(Float, nullable=False)
    ativo = Column(Boolean, nullable=False)
    cod_curso = Column(Integer, ForeignKey('cursos.cod_curso', ondelete='CASCADE'))

    curso = relationship('Curso', back_populates='professores', lazy='joined')
    disciplinas = relationship('Disciplina', back_populates='professor', lazy='joined')

    def __repr__(self) -> str:
        return f'Professor(cpf={self.cpf}, nome={self.nome}, ativo={self.ativo})'
