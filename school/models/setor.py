from sqlalchemy import String, Integer, Column
from ..config.base import Base


class Setor(Base):
    __tablename__ = 'setores'

    cod_setor = Column(Integer, primary_key=True)
    nome = Column(String(length=50), nullable=False)

    def __repr__(self):
        return f'Setor(cod_setor={self.cod_setor}), nome={self.nome}'
