import logging, pandas, random, hashlib, time

from requests import Request

from .database.sqlite import SQLite
from .database.orm import ORMManager
from .service.rapid_api.rapid_api import ServiceRapidAPI
from .service.rest_countries.rest_countries import ServiceRestCountriesAPI


logging.getLogger().setLevel(logging.INFO)


class FactoryProcess:
    def execute(self):
        self._factory_process()

    def _call_rapid_api(self):
        service_rapid_api = ServiceRapidAPI(request_url="all", method="get")
        return service_rapid_api.execute()

    def _call_rest_countries_api(self, region: str):
        service_rapid_api = ServiceRestCountriesAPI(request_url=f"region/{region}", method="get")
        return service_rapid_api.execute()

    def _execute_statement(self, statement: str, dict_statement: dict) -> None:
        ORMManager(statement=statement, dict_statement=dict_statement)

    def _factory_process(self):
        region_list = self._get_region_list()
        region_item = random.choice(region_list)

        country_list = self._get_country_list(region=region_item)

        dataframe = self._generate_dataframe(item_list=country_list)

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

    def _generate_dataframe(self, item_list: list):
        return pandas.DataFrame(item_list)
