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
    def insert(cpf: str, nome: str, telefone: str, endereco: str, ativo: bool, cod_curso: int) -> bool:
        with DBConnectionHandler() as db:
            try:
                new_aluno = Aluno(cpf=cpf, nome=nome, telefone=telefone, endereco=endereco, ativo=ativo, cod_curso=cod_curso)
                db.session.add(new_aluno)
                db.session.commit()
                return True
            except Exception as e:
                print(e)
                return False

    @staticmethod
    def update(cpf: str, **new_values) -> bool:
         with DBConnectionHandler() as db:
            try:
                db.session.query(Aluno)\
                    .filter(Aluno.cpf == cpf)\
                    .update(new_values)
                db.session.commit()
                return True
            except Exception as e:
                print(e)
                return False

    @staticmethod
    def delete(cpf: str) -> bool:
        with DBConnectionHandler() as db:
            try:
                db.session.query(Aluno)\
                    .filter(Aluno.cpf == cpf)\
                    .delete()
                db.session.commit()
                return True
            except Exception as e:
                print(e)
                return False
