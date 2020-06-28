from os import environ

from app.service.service import ServiceRequestHandler
from app.config import settings


class ServiceRestCountriesAPI(ServiceRequestHandler):
    _service = settings.REST_COUNTRIES_HOST
    _service_key = None
    _headers = dict()
