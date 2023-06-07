from sqlalchemy import Table, Column, ForeignKey, Integer
from ..config.base import Base



class CursoDisciplina(Base):
    __tablename__ = 'cursos_disciplinas'

    cod_curso = Column(
        Integer,
        ForeignKey('cursos.cod_curso', ondelete='CASCADE'),
        primary_key=True
    )
    cod_disciplina = Column(
        Integer,
        ForeignKey('disciplinas.cod_disciplina', ondelete='CASCADE'),
        primary_key=True
    )

    def __repr__(self) -> str:
        return f'CursoDisciplina(cod_curso={self.cod_disciplina}, cod_disciplina={self.cod_disciplina})'
