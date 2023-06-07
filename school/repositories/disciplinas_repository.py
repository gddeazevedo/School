from ..config.db_connection_handler import DBConnectionHandler
from ..models import Disciplina


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
    def insert(nome: str, cpf_professor: str) -> None:
        with DBConnectionHandler() as db:
            try:
                new_disciplina = Disciplina(
                    cod_disciplina=None,
                    nome=nome,
                    cpf_professor=cpf_professor
                )
                db.session.add(new_disciplina)
                db.session.commit()
            except Exception as e:
                print(e)
                return None

    @staticmethod
    def update(cod_disciplina: int, **new_values) -> None:
         with DBConnectionHandler() as db:
            try:
                db.session.query(Disciplina)\
                    .filter(Disciplina.cod_disciplina == cod_disciplina)\
                    .update(new_values)
                db.session.commit()
            except Exception as e:
                print(e)
                return None

    @staticmethod
    def delete(cod_disciplina: int) -> None:
        with DBConnectionHandler() as db:
            try:
                db.session.query(Disciplina)\
                    .filter(Disciplina.cod_disciplina == cod_disciplina)\
                    .delete()
                db.session.commit()
            except Exception as e:
                print(e)
                return None
