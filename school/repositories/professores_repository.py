from ..config.db_connection_handler import DBConnectionHandler
from ..models import Professor
import datetime


class ProfessoresRepository:
    @staticmethod
    def select_all() -> list[Professor]:
        with DBConnectionHandler() as db:
            return db.session.query(Professor).all()

    @staticmethod
    def select_by_cpf(cpf: str) -> Professor | None:
        with DBConnectionHandler() as db:
            try:
                return db.session.query(Professor).filter(Professor.cpf == cpf).first()
            except Exception as e:
                print(e)
                return None

    @staticmethod
    def insert(cpf: str, nome: str, telefone: str, endereco: str, data_contratacao: datetime.datetime, salario: float, ativo: bool, cod_curso: int) -> None:
        with DBConnectionHandler() as db:
            try:
                new_professor = Professor(
                    cpf=cpf,
                    nome=nome,
                    telefone=telefone,
                    endereco=endereco,
                    data_contratacao=data_contratacao, 
                    salario=salario,
                    ativo=ativo,
                    cod_curso=cod_curso
                )
                db.session.add(new_professor)
                db.session.commit()
            except Exception as e:
                print(e)

    @staticmethod
    def update(cpf: str, **new_values) -> None:
        with DBConnectionHandler() as db:
            try:
                db.session.query(Professor)\
                    .filter(Professor.cpf == cpf)\
                    .update(new_values)
                db.session.commit()
            except Exception as e:
                print(e)

    @staticmethod
    def delete(cpf: str):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Professor)\
                    .filter(Professor.cpf == cpf).delete()
                db.session.commit()
            except Exception as e:
                print(e)
