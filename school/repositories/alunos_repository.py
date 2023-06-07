from ..config.db_connection_handler import DBConnectionHandler
from ..models import Aluno


class AlunosRepository:
    @staticmethod
    def select_all() -> list[Aluno]:
        with DBConnectionHandler() as db:
            return db.session.query(Aluno).all()

    @staticmethod
    def select_by_cpf(cpf: str) -> Aluno | None:
        with DBConnectionHandler() as db:
            try:
                return db.session.query(Aluno).filter(Aluno.cpf == cpf).first()
            except Exception as e:
                print(e)
                return None

    @staticmethod
    def insert(cpf: str, nome: str, telefone: str, endereco: str, ativo: bool) -> None:
        with DBConnectionHandler() as db:
            try:
                new_aluno = Aluno(cpf=cpf, nome=nome, telefone=telefone, endereco=endereco, ativo=ativo)
                db.session.add(new_aluno)
                db.session.commit()
            except Exception as e:
                print(e)
                return None

    @staticmethod
    def update(cpf: str, **new_values) -> None:
         with DBConnectionHandler() as db:
            try:
                db.session.query(Aluno)\
                    .filter(Aluno.cpf == cpf)\
                    .update(new_values)
                db.session.commit()
            except Exception as e:
                print(e)
                return None

    @staticmethod
    def delete(cpf: str) -> None:
        with DBConnectionHandler() as db:
            try:
                db.session.query(Aluno)\
                    .filter(Aluno.cpf == cpf)\
                    .delete()
                db.session.commit()
            except Exception as e:
                print(e)
                return None
