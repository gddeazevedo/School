import sqlalchemy as sa
from sqlalchemy.sql import func
from ..config.db_connection_handler import DBConnectionHandler
from ..models import Setor, Funcionario
from typing import Optional



class SetoresRepository:
    @staticmethod
    def select_all() -> list[Setor]:
        with DBConnectionHandler() as db:
            return db.session.query(Setor).all()
  
    @staticmethod
    def select_by_cod_setor(cod_setor: int) -> Setor | None:
        with DBConnectionHandler() as db:
            try:
                return db.session.query(Setor).filter(Setor.cod_setor == cod_setor).first()
            except Exception as e:
                print(e)
                return None

    @staticmethod
    def select_by_nome(nome: str) -> Setor | None:
        with DBConnectionHandler() as db:
            try:
                return db.session.query(Setor).filter(Setor.nome == nome).first()
            except Exception as e:
                print(e)
                return None

    @staticmethod
    def insert(nome: str, cod_setor: Optional[int] = None) -> bool:
        with DBConnectionHandler() as db:
            try:
                new_setor = Setor(cod_setor=cod_setor, nome=nome)
                db.session.add(new_setor)
                db.session.commit()
                return True
            except Exception as e:
                print(e)
                return False

    @staticmethod
    def update(cod_setor: int, **new_values) -> bool:
        with DBConnectionHandler() as db:
            try:
                db.session.query(Setor)\
                    .filter(Setor.cod_setor == cod_setor)\
                    .update(new_values)
                db.session.commit()
                return True
            except Exception as e:
                print(e)
                return False

    @staticmethod
    def delete(cod_setor: int) -> bool:
        with DBConnectionHandler() as db:
            try:
                db.session.query(Setor)\
                    .filter(Setor.cod_setor == cod_setor).delete()
                db.session.commit()
                return True
            except Exception as e:
                print(e)
                return False

    @staticmethod
    def get_folha_pagamento_by_setor() -> tuple[str | int | float]:
        with DBConnectionHandler() as db:
            query = sa.select(Setor.cod_setor, Setor.nome, func.sum(Funcionario.salario))\
                .join(Setor.funcionarios)\
                .group_by(Setor.cod_setor, Setor.nome)\
                .order_by(sa.desc(func.sum(Funcionario.salario)))

            return db.session.execute(query)
