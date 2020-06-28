from .service.rapid_api.rapid_api import ServiceRapidAPI
from .service.rest_countries.rest_countries import ServiceRestCountriesAPI


class FactoryProcess:
    def execute(self):
        service_rapid_api = ServiceRapidAPI(request_url="all", method="get")
        request = service_rapid_api.execute()

        print(vars(request))
