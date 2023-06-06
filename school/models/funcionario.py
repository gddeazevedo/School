from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..config.base import Base


class Funcionario(Base):
    __tablename__ = 'funcionarios'

    cpf = Column(String(length=11), primary_key=True)
    nome = Column(String(length=50), nullable=False)
    endereco = Column(String(100), nullable=False)
    salario = Column(Float, nullable=False)
    cod_setor = Column(Integer, ForeignKey('setores.cod_setor'))

    setor = relationship('Setor', back_populates='funcionarios')

    def __repr__(self) -> str:
        return f'Funcionario(cpf={self.cpf}, nome={self.nome})'
