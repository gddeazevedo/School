from ..config.db_connection_handler import DBConnectionHandler
from ..models import Curso, Professor
import sqlalchemy as sa
from sqlalchemy.sql import func
from typing import Optional


class CursosRepository:
    @staticmethod
    def select_all() -> list[Curso]:
        with DBConnectionHandler() as db:
            return db.session.query(Curso).all()

    @staticmethod
    def select_by_cod_curso(cod_curso: int) -> Curso | None:
        with DBConnectionHandler() as db:
            try:
                return db.session.\
                    query(Curso).filter(Curso.cod_curso == cod_curso).\
                        first()
            except Exception as e:
                print(e)
                return None

    @staticmethod
    def insert(nome: str, ano_inicio: int, cod_curso: Optional[int] = None) -> bool:
        with DBConnectionHandler() as db:
            try:
                new_curso = Curso(
                    cod_curso=cod_curso,
                    nome=nome,
                    ano_inicio=ano_inicio
                )
                db.session.add(new_curso)
                db.session.commit()
                return True
            except Exception as e:
                print(e)
                return False

    @staticmethod
    def update(cod_curso: int, **new_values) -> bool:
        with DBConnectionHandler() as db:
            try:
                db.session.query(Curso)\
                    .filter(Curso.cod_curso == cod_curso)\
                    .update(new_values)
                db.session.commit()
                return True
            except Exception as e:
                print(e)
                return False

    @staticmethod
    def delete(cod_curso: int) -> bool:
        with DBConnectionHandler() as db:
            try:
                db.session.query(Curso)\
                    .filter(Curso.cod_curso == cod_curso).delete()
                db.session.commit()
                return True
            except Exception as e:
                print(e)
                return False

    @staticmethod
    def get_qtd_professores_ativos_by_curso() -> tuple[int | str]:
        with DBConnectionHandler() as db:
            query = sa.select(Curso.cod_curso, Curso.nome, func.count(Professor.cpf))\
                .join(Curso.professores)\
                .where(Professor.ativo == 1).group_by(Curso.cod_curso, Curso.nome)\
                .order_by(func.count(Professor.cpf))

            return db.session.execute(query)

    @staticmethod
    def get_media_salario_by_curso() -> tuple[int | float | str]:
        with DBConnectionHandler() as db:
            query = sa.select(Curso.cod_curso, Curso.nome, func.avg(Professor.salario))\
                .join(Curso.professores)\
                .group_by(Curso.cod_curso, Curso.nome)\
                .order_by(Curso.cod_curso)

            return db.session.execute(query)
