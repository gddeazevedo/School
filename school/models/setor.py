from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import relationship
from ..config.base import Base


class Setor(Base):
    __tablename__ = 'setores'

    cod_setor = Column(Integer, primary_key=True)
    nome = Column(String(length=50), nullable=False)

    funcionarios = relationship("Funcionario", back_populates="setor")

    def __repr__(self) -> str:
        return f'Setor(cod_setor={self.cod_setor}), nome={self.nome}'
