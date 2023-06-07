from ..config.db_connection_handler import DBConnectionHandler
from ..models import Setor
from typing import Optional


class SetoresRepository:
    @staticmethod
    def select_all() -> list[Setor]:
        with DBConnectionHandler() as db:
            return db.session.query(Setor).all()
  

    @staticmethod
    def select_by_cod_setor(cod_setor: int) -> Setor | list[Setor] | None:
        with DBConnectionHandler() as db:
            try:
                return db.session.query(Setor).filter(Setor.cod_setor == cod_setor).first()
            except Exception as e:
                print(e)
                return None

    @staticmethod
    def insert(nome: str, cod_setor: Optional[int] = None) -> None:
        with DBConnectionHandler() as db:
            try:
                new_setor = Setor(cod_setor=cod_setor, nome=nome)
                db.session.add(new_setor)
                db.session.commit()
            except Exception as e:
                print(e)

    @staticmethod
    def update(cod_setor: int, **new_values) -> None:
        with DBConnectionHandler() as db:
            try:
                db.session.query(Setor)\
                    .filter(Setor.cod_setor == cod_setor)\
                    .update(new_values)
                db.session.commit()
            except Exception as e:
                print(e)

    @staticmethod
    def delete(cod_setor: int):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Setor)\
                    .filter(Setor.cod_setor == cod_setor).delete()
                db.session.commit()
            except Exception as e:
                print(e)
