import logging

from .database.sqlite import SQLite
from .database.orm import ORMManager
from .service.rapid_api.rapid_api import ServiceRapidAPI
from .service.rest_countries.rest_countries import ServiceRestCountriesAPI


logging.getLogger().setLevel(logging.INFO)


class FactoryProcess:
    def execute(self):
        sql_statement = """
        CREATE TABLE IF NOT EXISTS projects (
            id integer PRIMARY KEY,
            name text NOT NULL,
            begin_date text,
            end_date text
        );
        """

    def _call_rapid_api(self):
        service_rapid_api = ServiceRapidAPI(request_url="all", method="get")
        return service_rapid_api.execute()

    def _call_rest_countries_api(self):
        service_rapid_api = ServiceRestCountriesAPI(request_url="all", method="get")
        return service_rapid_api.execute()

    def _execute_sql_statement(self, dict_statement: dict) -> None:
        orm = ORMManager(statement=dict_statement)

    def _process(self):
        pass
