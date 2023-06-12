from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..config.base import Base


class Disciplina(Base):
    __tablename__ = 'disciplinas'

    cod_disciplina = Column(Integer, primary_key=True)
    nome = Column(String(length=50), nullable=False)
    cpf_professor = Column(String(length=11), ForeignKey('professores.cpf', ondelete='CASCADE'))

    professor = relationship('Professor', back_populates='disciplinas', lazy='joined')
    inscritos = relationship('Inscrito', lazy='joined')

    def __repr__(self) -> str:
        return f'Disciplina(cod_disciplina={self.cod_disciplina}, nome={self.nome})'
