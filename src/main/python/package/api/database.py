import logging
import mysql.connector

from settings import Configuration, MYSQL_ERRORS


class Database:
    def __init__(self):
        self.params: dict = Configuration().getSettings("db_params")

    def insert(self, operation: str, params: tuple) -> bool:
        try:
            with mysql.connector.connect(**self.params) as db:
                with db.cursor() as c:
                    c.execute(operation=operation, params=params)
                db.commit()
                return True
        except MYSQL_ERRORS as e:
            logging.error(f"{type(e)}: {e}")
            raise

    def select(self, table: str, column: str = None, searched_element: str | int = None) -> list[tuple]:
        try:
            if searched_element and column:
                if isinstance(searched_element, int):
                    request = f"SELECT * FROM {table} WHERE {column} = {searched_element}"
                else:
                    request = f"SELECT * FROM {table} WHERE {column} = '{searched_element}'"
            else:
                request = f"SELECT * FROM {table}"
            with mysql.connector.connect(**self.params) as db:
                with db.cursor() as c:
                    c.execute(request)
                    return c.fetchall()
        except MYSQL_ERRORS as e:
            logging.error(f"{type(e)} - {e}")
            raise

    def update(self, table: str, column_to_modify: str, new_value: str | int | bool, reference_column: str,
               reference_value: str | int | bool) -> bool:
        operation = f"UPDATE {table} SET {column_to_modify} = '{new_value}' WHERE {reference_column} = {reference_value}"
        try:
            with mysql.connector.connect(**self.params) as db:
                with db.cursor() as c:
                    c.execute(operation=operation)
                db.commit()
                return True
        except MYSQL_ERRORS as e:
            logging.error(f"{type(e)}: {e}")
            raise
