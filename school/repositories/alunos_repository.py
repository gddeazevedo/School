from ..config.db_connection_handler import DBConnectionHandler
from ..models import Aluno


class AlunosRepository:
    @staticmethod
    def select_all() -> list[Aluno]:
        pass

    @staticmethod
    def select_by_cpf(cpf: str) -> Aluno | None:
        pass

    @staticmethod
    def insert(cpf: str, nome: str, telefone: str, endereco: str, ativo: bool) -> None:
        pass
    
    @staticmethod
    def update(cpf: str, **new_values) -> None:
        pass

    @staticmethod
    def delete(cpf: str) -> None:
        pass
