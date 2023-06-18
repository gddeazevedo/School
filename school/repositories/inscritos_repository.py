from ..config.db_connection_handler import DBConnectionHandler
from ..models import Inscrito
import sqlalchemy as sa


class InscritosRepository:
    @staticmethod
    def select_all() -> list[Inscrito]:
        with DBConnectionHandler() as db:
            return db.session.query(Inscrito).all()

    @staticmethod
    def select_by_cpf_aluno_and_cod_disciplina(cpf_aluno: str, cod_disciplina: int) -> Inscrito | None:
        with DBConnectionHandler() as db:
            try:
                return db.session.query(Inscrito)\
                    .filter(sa.and_(Inscrito.cpf_aluno == cpf_aluno, Inscrito.cod_disciplina == cod_disciplina))\
                    .first()
            except Exception as e:
                print(e)
                return None

    @staticmethod
    def insert(cpf_aluno: str, cod_disciplina: int, nota: float, vez: int) -> bool:
        with DBConnectionHandler() as db:
            try:
                new_inscrito = Inscrito(
                    cpf_aluno=cpf_aluno,
                    cod_disciplina=cod_disciplina,
                    nota=nota,
                    vez=vez
                )
                db.session.add(new_inscrito)
                db.session.commit()
                return True
            except Exception as e:
                print(e)
                return False
    
    @staticmethod
    def update(cpf_aluno: str, cod_disciplina: int, **new_values) -> bool:
        with DBConnectionHandler() as db:
            try:
                db.session.query(Inscrito)\
                    .filter(
                        sa.and_(Inscrito.cod_disciplina == cod_disciplina, Inscrito.cpf_aluno == cpf_aluno)
                    )\
                    .update(new_values)
                db.session.commit()
                return True
            except Exception as e:
                print(e)
                return False

    @staticmethod
    def delete(cpf_aluno: str, cod_disciplina: int) -> bool:
        with DBConnectionHandler() as db:
            try:
                db.session.query(Inscrito)\
                    .filter(
                        sa.and_(Inscrito.cod_disciplina == cod_disciplina,Inscrito.cpf_aluno == cpf_aluno)
                    ).delete()
                db.session.commit()
                return True
            except Exception as e:
                print(e)
                return False
