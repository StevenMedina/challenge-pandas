import sqlite3, logging
from sqlite3 import Error

from app.config import settings


class SQLite:
    _connection = None

    def __init__(self, sql_statement: str):
        self._db_file = settings.DB_FILE
        self._sql_statement = sql_statement

    def execute(self):
        self._connect()

        self._set_cursor()

        self._execute_statement()

        return self._connection

    def _connect(self):
        try:
            self._connection = sqlite3.connect(self._db_file)
        except Error as error:
            logging.warning(error)

        return self._connection

    def _set_cursor(self):
        self._cursor = self._connection.cursor()

    def _execute_statement(self):
        cursor = self._cursor
        cursor.execute(self._sql_statement)
