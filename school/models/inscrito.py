from sqlalchemy import Integer, String, Float, ForeignKey, Column
from ..config.base import Base


class Inscrito(Base):
    __tablename__ = 'inscritos'

    cod_disciplina = Column(
        Integer,
        ForeignKey('disciplinas.cod_disciplina', ondelete='CASCADE'),
        primary_key=True
    )
    cpf_aluno = Column(
        String(length=11),
        ForeignKey('alunos.cpf', ondelete='CASCADE'),
        primary_key=True
    )
    nota = Column(Float, nullable=True, default=0)
    vez = Column(Integer, nullable=False, default=1)

    def __repr__(self) -> str:
        return f'Inscrito(cod_disciplia={self.cod_disciplina}, cpf_aluno={self.cpf_aluno}, nota={self.nota}, vez={self.vez})'
