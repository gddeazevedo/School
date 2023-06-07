from ..config.db_connection_handler import DBConnectionHandler
from ..models import Curso
import datetime

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
    def insert(nome: str, ano_inicio: datetime.datetime) -> None:
        with DBConnectionHandler() as db:
            try:
                new_curso = Curso(
                    cod_curso=None,
                    nome=nome,
                    ano_inicio=ano_inicio
                )
                db.session.add(new_curso)
                db.session.commit()
            except Exception as e:
                print(e)

    @staticmethod
    def update(cod_curso: int, **new_values) -> None:
        with DBConnectionHandler() as db:
            try:
                db.session.query(Curso)\
                    .filter(Curso.cod_curso == cod_curso)\
                    .update(new_values)
                db.session.commit()
            except Exception as e:
                print(e)

    @staticmethod
    def delete(cod_curso: int) -> None:
        with DBConnectionHandler() as db:
            try:
                db.session.query(Curso)\
                    .filter(Curso.cod_curso == cod_curso).delete()
                db.session.commit()
            except Exception as e:
                print(e)
