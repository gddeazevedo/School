from ..config.db_connection_handler import DBConnectionHandler
from ..models import Funcionario


class FuncionariosRepository:
    @staticmethod
    def select_all() -> list[Funcionario]:
        with DBConnectionHandler() as db:
            return db.session.query(Funcionario).all()

    @staticmethod
    def select_by_cpf(cpf: str) -> Funcionario | None:
        with DBConnectionHandler() as db:
            try:
               return db.session.query(Funcionario).filter(Funcionario.cpf == cpf).first()
            except Exception as e:
                print(e)
                return None

    @staticmethod
    def insert(cpf: str, nome: str, endereco: str, salario: float, cod_setor: int) -> None:
        with DBConnectionHandler() as db:
            try:
                new_funcionario = Funcionario(
                    cpf=cpf,
                    nome=nome,
                    endereco=endereco,
                    salario=salario,
                    cod_setor=cod_setor
                )
                db.session.add(new_funcionario)
                db.session.commit()
            except Exception as e:
                print(e)

    @staticmethod
    def update(cpf: str, **new_values) -> None:
        with DBConnectionHandler() as db:
            try:
                db.session.query(Funcionario)\
                    .filter(Funcionario.cpf == cpf)\
                    .update(new_values)
                db.session.commit()
            except Exception as e:
                print(e)

    @staticmethod
    def delete(cpf: str) -> None:
        with DBConnectionHandler() as db:
            try:
                db.session.query(Funcionario)\
                    .filter(Funcionario.cpf == cpf)\
                    .delete()
                db.session.commit()
            except Exception as e:
                print(e)
