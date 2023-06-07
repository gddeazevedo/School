from ..config.db_connection_handler import DBConnectionHandler
from ..models import Disciplina


class DisciplinasRepository:
    @staticmethod
    def select_all() -> list[Disciplina]:
        pass

    @staticmethod
    def select_by_cpf(cod_disciplina: int) -> Disciplina | None:
        pass

    @staticmethod
    def insert(cod_disciplina: int, nome: str, cpf_professor: str) -> None:
        pass
    
    @staticmethod
    def update(cod_disciplina: int, **new_values) -> None:
        pass

    @staticmethod
    def delete(cod_disciplina: int) -> None:
        pass
