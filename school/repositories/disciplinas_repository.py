import sqlalchemy as sa
from sqlalchemy.sql import func
from ..config.db_connection_handler import DBConnectionHandler
from ..models import Disciplina, Inscrito
from typing import Optional


class DisciplinasRepository:
    @staticmethod
    def select_all() -> list[Disciplina]:
        with DBConnectionHandler() as db:
            return db.session.query(Disciplina).all()

    @staticmethod
    def select_by_cod_disciplina(cod_disciplina: str) -> Disciplina | None:
        with DBConnectionHandler() as db:
            try:
                return db.session.query(Disciplina).filter(Disciplina.cod_disciplina == cod_disciplina).first()
            except Exception as e:
                print(e)
                return None

    @staticmethod
    def insert(nome: str, cpf_professor: str, cod_disciplina: Optional[int] = None) -> bool:
        with DBConnectionHandler() as db:
            try:
                new_disciplina = Disciplina(
                    cod_disciplina=cod_disciplina,
                    nome=nome,
                    cpf_professor=cpf_professor
                )
                db.session.add(new_disciplina)
                db.session.commit()
                return True
            except Exception as e:
                print(e)
                return False

    @staticmethod
    def update(cod_disciplina: int, **new_values) -> bool:
         with DBConnectionHandler() as db:
            try:
                db.session.query(Disciplina)\
                    .filter(Disciplina.cod_disciplina == cod_disciplina)\
                    .update(new_values)
                db.session.commit()
                return True
            except Exception as e:
                print(e)
                return False

    @staticmethod
    def delete(cod_disciplina: int) -> bool:
        with DBConnectionHandler() as db:
            try:
                db.session.query(Disciplina)\
                    .filter(Disciplina.cod_disciplina == cod_disciplina)\
                    .delete()
                db.session.commit()
                return True
            except Exception as e:
                print(e)
                return False

    @staticmethod
    def get_with_mais_inscritos():
        with DBConnectionHandler() as db:
            try:
                query = sa.select(Disciplina.nome, func.count(Inscrito.cpf_aluno))\
                    .join(Disciplina.inscritos)\
                    .group_by(Disciplina.nome)\
                    .having(func.count(Inscrito.cpf_aluno) >= sa.all_(
                        sa.select(func.count(Inscrito.cpf_aluno))
                            .join(Disciplina.inscritos)\
                            .group_by(Disciplina.nome).scalar_subquery()
                    ))

                return db.session.execute(query)
            except Exception as e:
                print(e)
                return None
