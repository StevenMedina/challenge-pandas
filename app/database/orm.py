from .sqlite import SQLite


class ORMManager:
    def __init__(self, statement: str, table_name: str, dict_statement: dict):
        self._statement = statement
        self._table_name = table_name
        self._dict_statement = dict_statement

    def execute(self):
        sql_statement = self._handle_statement()

        sqlite = SQLite(sql_statement=sql_statement)
        connection = sqlite.execute()

        return connection

    def _handle_statement(self):
        return {
            "create": self._create_statement,
            "insert": self._insert_statement,
        }[self._statement]()

    def _create_statement(self):
        sql_statement = "CREATE TABLE IF NOT EXISTS {table_name} ({keys});".format(
            table_name=self._table_name,
            keys=', '.join(self._dict_statement.keys()),
        )

        return sql_statement

    def _insert_statement(self):
        pass
