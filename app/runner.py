import logging, pandas, random, hashlib, time

from requests import Request

from .database.orm import ORMManager
from .service.rapid_api.rapid_api import ServiceRapidAPI
from .service.rest_countries.rest_countries import ServiceRestCountriesAPI


logging.getLogger().setLevel(logging.INFO)


class FactoryProcess:
    def execute(self):
        self._factory_process()

    @classmethod
    def _call_rapid_api(self):
        service_rapid_api = ServiceRapidAPI(request_url="all", method="get")
        return service_rapid_api.execute()

    @classmethod
    def _call_rest_countries_api(self, region: str):
        service_rapid_api = ServiceRestCountriesAPI(request_url=f"region/{region}", method="get")
        return service_rapid_api.execute()

    def _execute_statement(
        self, statement: str, table_name: str, dict_statement: dict
    ) -> ORMManager:
        orm_manager = ORMManager(
            statement=statement, table_name=table_name, dict_statement=dict_statement
        )
        return orm_manager.execute()

    def _factory_process(self):
        logging.info('==============================================================')
        logging.info('Init process')
        logging.info('==============================================================')
        logging.info('Create a table Location')
        self._connection = self._execute_statement(
            "create",
            "Location",
            {
                "id integer PRIMARY KEY": "",
                "region text NOT NULL": "",
                "city_name text NOT NULL": "",
                "language text NOT NULL": "",
                "time text NOT NULL": "",
            }
        )

        logging.info('==============================================================')
        logging.info('Call service to get region list')
        region_list = self._get_region_list()
        region_item = random.choice(region_list)

        logging.info('==============================================================')
        logging.info('Call service to get country list from region random item')
        country_list = self._get_country_list(region=region_item)

        logging.info('==============================================================')
        logging.info('Generate Dataframe')
        dataframe = self._generate_dataframe(item_list=country_list)
        logging.info('==============================================================')
        logging.info(dataframe)
        logging.info('==============================================================')

        logging.info(f'Sum of time: {dataframe["time"].sum()}')
        logging.info(f'Average time: {dataframe["time"].mean()}')
        logging.info(f'Max time: {dataframe["time"].max()}')
        logging.info('==============================================================')

        logging.info('Save SQLite dataframe')
        self._save_sqlite_dataframe(table_name="Location", dataframe=dataframe)
        logging.info('==============================================================')

        logging.info('Save Json dataframe')
        self._save_json_dataframe(dataframe=dataframe)
        logging.info('==============================================================')

    def _get_region_list(self) -> list:
        region_list_response = self._call_rapid_api()
        region_data = region_list_response.json()

        region_list = []
        for region_item in region_data:
            if region_item["region"]:
                region_list.append(region_item["region"])

        return pandas.unique(region_list).tolist()

    def _get_country_list(self, region: str) -> list:
        start_time = time.clock()

        country_list_response = self._call_rest_countries_api(region=region.lower())
        country_data = country_list_response.json()

        country_list = []
        for country_item in country_data:
            languages = ", ".join([
                language["name"] for language in country_item["languages"]
            ])
            country_dict = {
                "region": country_item["region"],
                "city_name": country_item["name"],
                "language": hashlib.sha1(languages.encode('utf-8')).hexdigest(),
                "time": time.clock() - start_time,
            }
            country_list.append(country_dict)

        return country_list

    def _generate_dataframe(self, item_list: list) -> pandas.DataFrame:
        return pandas.DataFrame(item_list)

    def _save_sqlite_dataframe(self, table_name: str, dataframe: pandas.DataFrame):
        dataframe.to_sql(table_name, con=self._connection, if_exists="append", index=False)

    def _save_json_dataframe(self, dataframe: pandas.DataFrame):
        with open('data.json', 'w') as json_file:
            json_file.write(dataframe.to_json(orient='records', lines=True))
