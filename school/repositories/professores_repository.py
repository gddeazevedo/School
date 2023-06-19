import datetime
import sqlalchemy as sa
from sqlalchemy.sql import func
from ..config.db_connection_handler import DBConnectionHandler
from ..models import Professor, Disciplina, Inscrito, CursoDisciplina


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
    def insert(cpf: str, nome: str, telefone: str, endereco: str, data_contratacao: datetime.date, salario: float, ativo: bool, cod_curso: int) -> bool:
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
                return True
            except Exception as e:
                print(e)
                return False

    @staticmethod
    def update(cpf: str, **new_values) -> bool:
        with DBConnectionHandler() as db:
            try:
                db.session.query(Professor)\
                    .filter(Professor.cpf == cpf)\
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
                db.session.query(Professor)\
                    .filter(Professor.cpf == cpf).delete()
                db.session.commit()
                return True
            except Exception as e:
                print(e)
                return False

    @staticmethod
    def get_professor_mais_antigo() -> Professor | None:
        with DBConnectionHandler() as db:
            query = sa.select(Professor.cpf, Professor.nome, Professor.data_contratacao)\
                .where(Professor.data_contratacao <= sa.all_(
                    sa.select(Professor.data_contratacao).scalar_subquery()
                ))

            return db.session.execute(query)

    @staticmethod
    def get_media_notas(cpf_professor: str):
        with DBConnectionHandler() as db:
            try:
                subquery = sa.select(Professor.nome, Disciplina.cod_disciplina, Disciplina.nome)\
                    .join(Professor.disciplinas)\
                    .where(Professor.cpf == cpf_professor).subquery()

                query = sa.select(subquery.c.nome,subquery.c.nome_1, func.avg(Inscrito.nota))\
                    .join(Inscrito, subquery.c.cod_disciplina == Inscrito.cod_disciplina)\
                    .group_by(subquery.c.nome, subquery.c.nome_1)

                return db.session.execute(query)
            except Exception as e:
                print(e)
                return None

    @staticmethod
    def get_qtd_cursos_by_professor():
        with DBConnectionHandler() as db:
            query = sa.select(Professor.cpf, Professor.nome, func.count(CursoDisciplina.cod_curso))\
                .join(Professor.disciplinas)\
                .join(CursoDisciplina, CursoDisciplina.cod_disciplina == Disciplina.cod_disciplina)\
                .group_by(Professor.cpf, Professor.nome)\
                .order_by(func.count(CursoDisciplina.cod_curso), Professor.nome)
            return db.session.execute(query)
