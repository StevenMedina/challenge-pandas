from os import environ

from app.service.service import ServiceRequestHandler


class ServiceRestCountriesAPI(ServiceRequestHandler):
    service = environ.get("REST_COUNTRIES_HOST")
